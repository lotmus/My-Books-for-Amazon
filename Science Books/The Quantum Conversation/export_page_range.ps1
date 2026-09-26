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
    $doc.ExportAsFixedFormat($OutPdfPath, 17, $false, 0, 3, $FromPage, $ToPage, 0, $true, $true, 0, $true, $true, $false)
    Write-Host "Exported pages $FromPage-$ToPage to $OutPdfPath"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
