# Opens the built DOCX in Word (hidden), updates the table of contents and all
# fields (so page numbers are real), and saves.
# Does NOT kill other Word processes -- it starts its own instance.
#   powershell -File finalize_docx.ps1 -DocPath <docx>
param(
    [Parameter(Mandatory = $true)][string]$DocPath
)
$ErrorActionPreference = "Stop"
$DocPath = (Resolve-Path $DocPath).Path

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
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
