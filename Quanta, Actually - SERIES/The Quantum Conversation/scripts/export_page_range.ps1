param(
    [string]$DocPath,
    [int]$FromPage,
    [int]$ToPage,
    [string]$OutPdfPath
)
$ErrorActionPreference = "Stop"
Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$true)
try {
    # wdExportFromTo = 3, wdExportOptimizeForPrint = 0, wdExportDocumentContent = 0
    # PDF export disabled by docx-only policy; keep the DOCX as the build artifact.
    Write-Host "PDF export disabled; DOCX retained at $DocPath"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
