$ErrorActionPreference = 'Stop'
$book = Split-Path -Parent $PSScriptRoot
$qa = Join-Path $book 'bak/review-20261005'
$inputFile = Join-Path $book 'The_Permitted_Options_BOOK_2_REVISION_20261005.docx'
$source = Join-Path $book 'The_Permitted_Options_BOOK_2_DRAFT.docx'
$inputHash = (Get-FileHash -LiteralPath $inputFile -Algorithm SHA256).Hash
$sourceHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    $document = $word.Documents.Open($inputFile,$false,$true,$false)
    $document.Repaginate()
    $pages = $document.ComputeStatistics(2)
    $document.ExportAsFixedFormat((Join-Path $qa 'revision.pdf'),17)
    "Word exported $pages pages from read-only revision."
} finally {
    if ($null -ne $document) { $document.Close(0) }
    if ($null -ne $word) { $word.Quit() }
    if ((Get-FileHash -LiteralPath $inputFile -Algorithm SHA256).Hash -ne $inputHash) { throw 'Revision changed during render.' }
    if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -ne $sourceHash) { throw 'Source changed during render.' }
}
