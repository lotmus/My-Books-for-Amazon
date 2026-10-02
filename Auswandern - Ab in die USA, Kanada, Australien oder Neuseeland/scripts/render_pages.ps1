# Renders selected pages of a DOCX to PNG images through Word itself (no extra
# software needed) -- used for visual QA of the layout.
#   powershell -File render_pages.ps1 -DocPath <docx> -OutDir <dir> -From 1 -To 8 [-Scale 1.6]
param(
    [Parameter(Mandatory = $true)][string]$DocPath,
    [Parameter(Mandatory = $true)][string]$OutDir,
    [int]$From = 1,
    [int]$To = 4,
    [double]$Scale = 1.6
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing
$DocPath = (Resolve-Path $DocPath).Path
New-Item -ItemType Directory -Force $OutDir | Out-Null

$word = New-Object -ComObject Word.Application
$word.Visible = $true          # page rendering needs a window
$word.DisplayAlerts = 0
$doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$true)
try {
    $doc.ActiveWindow.View.Type = 3    # wdPrintView
    $pane = $doc.ActiveWindow.ActivePane
    $count = $pane.Pages.Count
    if ($To -gt $count) { $To = $count }
    Write-Host "Document has $count pages; rendering $From-$To"
    for ($i = $From; $i -le $To; $i++) {
        $bytes = $pane.Pages.Item($i).EnhMetaFileBits
        $ms = New-Object System.IO.MemoryStream(, $bytes)
        $img = [System.Drawing.Image]::FromStream($ms)
        $w = [int]($img.Width * $Scale); $h = [int]($img.Height * $Scale)
        $bmp = New-Object System.Drawing.Bitmap($w, $h)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.Clear([System.Drawing.Color]::White)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.DrawImage($img, 0, 0, $w, $h)
        $file = Join-Path $OutDir ("page_{0:D3}.png" -f $i)
        $bmp.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)
        $g.Dispose(); $bmp.Dispose(); $img.Dispose(); $ms.Dispose()
    }
    Write-Host "Done: $OutDir"
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
