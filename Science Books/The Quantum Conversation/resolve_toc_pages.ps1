param(
    [string]$DocPath,
    [string]$EntriesJsonPath,
    [string]$OutJsonPath
)

$ErrorActionPreference = "Stop"
$entries = Get-Content $EntriesJsonPath -Raw | ConvertFrom-Json

function Kill-Word {
    Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 3
}

$succeeded = $false
for ($outerAttempt = 1; $outerAttempt -le 6; $outerAttempt++) {
    Kill-Word
    $word = $null
    $doc = $null
    try {
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $word.DisplayAlerts = 0
        $doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$true)

        $r = $doc.Content.Duplicate
        $r.Find.ClearFormatting()
        $r.Find.Text = "Table of Contents"
        $r.Find.Forward = $true
        $r.Find.Wrap = 0
        if (-not $r.Find.Execute()) { throw "Could not find 'Table of Contents' heading" }

        $lastEntryTitle = $entries[$entries.Count - 1].title
        $cursor = $doc.Range($r.End, $doc.Content.End)
        $cursor.Find.ClearFormatting()
        $cursor.Find.Text = $lastEntryTitle
        $cursor.Find.Forward = $true
        $cursor.Find.Wrap = 0
        if (-not $cursor.Find.Execute()) { throw "Could not find TOC's own last entry '$lastEntryTitle'" }

        $searchStart = $cursor.End
        $results = @{}
        $notFound = @()

        for ($idx = 0; $idx -lt $entries.Count; $idx++) {
            $title = $entries[$idx].title
            $searchRange = $doc.Range($searchStart, $doc.Content.End)
            $searchRange.Find.ClearFormatting()
            $searchRange.Find.Text = $title
            $searchRange.Find.Forward = $true
            $searchRange.Find.Wrap = 0
            $found = $searchRange.Find.Execute()
            if ($found) {
                $page = $searchRange.Information(3)
                $results[[string]$idx] = $page
                $searchStart = $searchRange.End
            } else {
                $notFound += "$idx`: $title"
                $results[[string]$idx] = $null
            }
            $results | ConvertTo-Json | Set-Content -Path $OutJsonPath -Encoding UTF8
        }

        if ($notFound.Count -gt 0) {
            Write-Host "NOT FOUND:"
            $notFound | ForEach-Object { Write-Host "  $_" }
        } else {
            Write-Host "All $($entries.Count) entries resolved on outer attempt $outerAttempt."
        }
        $succeeded = $true
    } catch {
        Write-Host "[outer $outerAttempt] failed: $($_.Exception.Message)"
    }
    try { if ($doc) { $doc.Close([ref]$false) } } catch {}
    try { if ($word) { $word.Quit() } } catch {}
    if ($succeeded) { break }
    Start-Sleep -Seconds (5 * $outerAttempt)
}

if (-not $succeeded) { throw "Failed to resolve TOC pages after 6 outer attempts" }
