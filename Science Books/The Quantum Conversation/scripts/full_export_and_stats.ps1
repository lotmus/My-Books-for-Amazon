param(
    [string]$DocPath,
    [string]$OutPdfPath
)
$ErrorActionPreference = "Stop"
Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 3

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$true)
try {
    $pages = $doc.ComputeStatistics(2)   # wdStatisticPages
    $words = $doc.ComputeStatistics(0)   # wdStatisticWords
    $chars = $doc.ComputeStatistics(3)   # wdStatisticCharacters
    Write-Host "Pages: $pages"
    Write-Host "Words: $words"
    Write-Host "Characters: $chars"

    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    # wdExportAllDocument = 0 for the Range param -- exports every page
    $doc.ExportAsFixedFormat($OutPdfPath, 17, $false, 0, 0, 0, 0, 0, $true, $true, 0, $true, $true, $false)
    $sw.Stop()
    Write-Host "Full-document PDF export succeeded in $($sw.Elapsed.TotalSeconds) sec: $OutPdfPath"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
