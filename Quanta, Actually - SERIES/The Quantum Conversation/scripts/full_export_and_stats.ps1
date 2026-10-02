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

    # PDF export disabled by docx-only policy; keep the DOCX as the build artifact.
    Write-Host "PDF export disabled; DOCX retained at $DocPath"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
