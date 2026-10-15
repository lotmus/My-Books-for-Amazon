$ErrorActionPreference = 'Stop'
$repo = 'D:\My Books for Amazon'
$series = "Lolly Wren's Curious Science Adventures - SERIES"
$book = "$series/Book 2 - The Permitted Options"
Set-Location -LiteralPath $repo
function Invoke-SeriesGit {
    param([string[]]$Arguments)
    $result = & git @Arguments
    if ($LASTEXITCODE -ne 0) { throw "Git failed: $($Arguments -join ' ')" }
    return $result
}
$branch = Invoke-SeriesGit @('branch','--show-current')
if ($branch -ne 'book-2-lectures-after-qed') { throw 'Current branch changed; inspect again.' }
$base = Invoke-SeriesGit @('rev-parse','HEAD')
$upstream = Invoke-SeriesGit @('rev-parse',"origin/$branch")
if ($base -ne $upstream) { throw 'Branch and upstream diverged; inspect before committing.' }
$remote = Invoke-SeriesGit @('ls-remote','origin',"refs/heads/$branch")
if (($remote -split '\s+')[0] -ne $base) { throw 'Remote branch changed; fetch and inspect.' }
$paths = @(
    "$series/Book 1 - Schrodingers Paperwork/Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx",
    "$series/Book 1 - Schrodingers Paperwork/notes/MANUSCRIPT_GUIDE.md",
    "$book/The_Permitted_Options_BOOK_2_DRAFT.docx",
    "$book/notes/MANUSCRIPT_GUIDE.md",
    "$book/The_Permitted_Options_BOOK_2_REVISION_20261005.docx",
    "$book/notes/REVISION_20261005.md",
    "$book/scripts/review_20261005.py",
    "$book/scripts/revise_20261005.py",
    "$book/scripts/render_word_20261005.ps1",
    "$book/scripts/sync_series_20261005.ps1"
)
$outsideBefore = @(Invoke-SeriesGit @('ls-files','--stage','--','.',":(exclude)$series/**")) -join "`n"
$b1Path = Join-Path $repo $paths[0]
$b1Hash = (Get-FileHash -LiteralPath $b1Path -Algorithm SHA256).Hash
$originalAlternateIndex = $env:GIT_INDEX_FILE
try {
    $env:GIT_INDEX_FILE = Join-Path $repo "$book/bak/review-20261005/git-series.index"
    if (Test-Path -LiteralPath $env:GIT_INDEX_FILE) { throw 'Alternate index exists; will not overwrite it.' }
    Invoke-SeriesGit @('read-tree',$base) | Out-Null
    Invoke-SeriesGit (@('add','--') + $paths) | Out-Null
    $changed = @(Invoke-SeriesGit @('diff','--cached','--name-only',$base))
    foreach ($path in $changed) {
        if (-not $path.StartsWith($series+'/') -or $path -match '/(bak|\.claude)/') { throw "Excluded path in commit: $path" }
    }
    Invoke-SeriesGit @('diff','--cached','--stat',$base)
    $tree = Invoke-SeriesGit @('write-tree')
    $commit = Invoke-SeriesGit @('commit-tree',$tree,'-p',$base,'-m','Lolly Wren: preserve unique recap labels and add separate Book 2 editorial revision')
    $env:GIT_INDEX_FILE = $originalAlternateIndex
    if ((Invoke-SeriesGit @('rev-parse','HEAD')) -ne $base) { throw 'Local HEAD changed concurrently.' }
    Invoke-SeriesGit @('update-ref',"refs/heads/$branch",$commit,$base) | Out-Null
    # Reset only the explicitly committed paths in the real index. No worktree changes.
    Invoke-SeriesGit (@('reset','--quiet',$commit,'--') + $paths) | Out-Null
    $outsideAfter = @(Invoke-SeriesGit @('ls-files','--stage','--','.',":(exclude)$series/**")) -join "`n"
    if ($outsideBefore -ne $outsideAfter) { throw 'Unrelated index entries changed.' }
    if ((Get-FileHash -LiteralPath $b1Path -Algorithm SHA256).Hash -ne $b1Hash) { throw 'Book 1 file changed during sync.' }
    Invoke-SeriesGit @('push','origin',"${branch}:refs/heads/$branch")
    $verified = Invoke-SeriesGit @('ls-remote','origin',"refs/heads/$branch")
    if (($verified -split '\s+')[0] -ne $commit) { throw 'Remote branch verification failed.' }
    "SYNCED branch=$branch commit=$commit"
    'Verified unrelated staged entries and Book 1 working file unchanged. No force push or branch switch.'
} finally {
    $env:GIT_INDEX_FILE = $originalAlternateIndex
}
