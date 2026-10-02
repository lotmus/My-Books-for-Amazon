param(
    [string]$DocPath,
    [string]$EntriesJsonPath,
    [string]$ExpectedJsonPath
)

$ErrorActionPreference = "Stop"
$entries = Get-Content $EntriesJsonPath -Raw | ConvertFrom-Json
$expected = Get-Content $ExpectedJsonPath -Raw | ConvertFrom-Json

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

        $totalPages = $doc.ComputeStatistics(2)
        Write-Host "Total pages in document: $totalPages"

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
        $mismatches = @()

        for ($idx = 0; $idx -lt $entries.Count; $idx++) {
            $title = $entries[$idx].title
            $expectedPage = $expected.($idx.ToString())
            $searchRange = $doc.Range($searchStart, $doc.Content.End)
            $searchRange.Find.ClearFormatting()
            $searchRange.Find.Text = $title
            $searchRange.Find.Forward = $true
            $searchRange.Find.Wrap = 0
            $found = $searchRange.Find.Execute()
            if (-not $found) {
                $mismatches += "$idx`: '$title' NOT FOUND"
                continue
            }
            $actualPage = $searchRange.Information(3)
            $searchStart = $searchRange.End
            if ($actualPage -ne $expectedPage) {
                $mismatches += "$idx`: '$title' expected page $expectedPage but found on page $actualPage"
            }
        }

        if ($mismatches.Count -gt 0) {
            Write-Host "MISMATCHES:"
            $mismatches | ForEach-Object { Write-Host "  $_" }
        } else {
            Write-Host "VERIFY OK: all $($entries.Count) entries match."
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

if (-not $succeeded) { throw "Failed to verify TOC pages after 6 outer attempts" }
