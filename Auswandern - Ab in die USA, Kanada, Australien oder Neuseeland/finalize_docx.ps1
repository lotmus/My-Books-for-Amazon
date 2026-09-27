# Opens the built DOCX in Word (hidden), updates the table of contents and all
# fields (so page numbers are real), saves, and exports a print-quality PDF.
# Does NOT kill other Word processes -- it starts its own instance.
#   powershell -File finalize_docx.ps1 -DocPath <docx> -OutPdfPath <pdf>
param(
    [Parameter(Mandatory = $true)][string]$DocPath,
    [Parameter(Mandatory = $true)][string]$OutPdfPath
)
$ErrorActionPreference = "Stop"
$DocPath = (Resolve-Path $DocPath).Path
# Word's COM working directory isn't PowerShell's cwd, so a relative
# -OutPdfPath would resolve against the wrong folder (or fail outright).
# Build an absolute path by hand -- the PDF doesn't exist yet, so
# Resolve-Path (which requires an existing target) can't be used here.
if (-not [System.IO.Path]::IsPathRooted($OutPdfPath)) {
    $OutPdfPath = Join-Path (Get-Location) $OutPdfPath
}
$OutPdfDir = Split-Path $OutPdfPath -Parent
if ($OutPdfDir -and -not (Test-Path $OutPdfDir)) { New-Item -ItemType Directory -Force $OutPdfDir | Out-Null }

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0   # wdAlertsNone: no "update fields?" prompt
$doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$false)
try {
    # Two passes: the first fills the TOC, the second corrects page numbers
    # that shifted because the TOC itself takes space.
    foreach ($pass in 1..2) {
        foreach ($toc in $doc.TablesOfContents) { $toc.Update() }
        [void]$doc.Fields.Update()
    }
    $doc.Save()
    $pages = $doc.ComputeStatistics(2)   # wdStatisticPages
    $words = $doc.ComputeStatistics(0)   # wdStatisticWords
    Write-Host "Pages: $pages"
    Write-Host "Words: $words"
    # wdExportFormatPDF = 17, wdExportOptimizeForPrint = 0, wdExportAllDocument = 0
    $doc.ExportAsFixedFormat($OutPdfPath, 17, $false, 0, 0, 0, 0, 0, $true, $true, 0, $true, $true, $false)
    Write-Host "PDF: $OutPdfPath"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
