Add-Type -AssemblyName System.Drawing
$w = 1650
$h = 2550
$bmp = New-Object System.Drawing.Bitmap $w, $h
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$g.Clear([System.Drawing.Color]::FromArgb(255, 18, 22, 34))
$pink = [System.Drawing.Color]::FromArgb(255, 232, 120, 150)
$cream = [System.Drawing.Color]::FromArgb(255, 245, 236, 228)
$muted = [System.Drawing.Color]::FromArgb(255, 176, 168, 160)
$penOuter = New-Object System.Drawing.Pen $pink, 10
$penInner = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(255, 90, 98, 120)), 3
$g.DrawEllipse($penOuter, 390, 620, 870, 870)
$g.DrawEllipse($penInner, 470, 700, 710, 710)
$sf = New-Object System.Drawing.StringFormat
$sf.Alignment = [System.Drawing.StringAlignment]::Center
$sf.LineAlignment = [System.Drawing.StringAlignment]::Center
$brush = New-Object System.Drawing.SolidBrush $cream
$brushPink = New-Object System.Drawing.SolidBrush $pink
$brushMuted = New-Object System.Drawing.SolidBrush $muted
function Font([single]$size, [System.Drawing.FontStyle]$style) {
  return [System.Drawing.Font]::new("Georgia", $size, $style, [System.Drawing.GraphicsUnit]::Point)
}
$fontSeries = Font 18 ([System.Drawing.FontStyle]::Regular)
$fontTitle = Font 54 ([System.Drawing.FontStyle]::Regular)
$fontSub = Font 16 ([System.Drawing.FontStyle]::Italic)
$fontAuthor = Font 20 ([System.Drawing.FontStyle]::Regular)
$g.DrawString("THE INVASION STORYBOOKS", $fontSeries, $brushPink, (New-Object System.Drawing.RectangleF 120, 280, 1410, 80), $sf)
$g.DrawString("PROTOCOL`nFLAMINGO", $fontTitle, $brush, (New-Object System.Drawing.RectangleF 140, 900, 1370, 280), $sf)
$g.DrawString("Earth. This year. Somebody left the sky unlocked.", $fontSub, $brushMuted, (New-Object System.Drawing.RectangleF 160, 1680, 1330, 140), $sf)
$g.DrawString("GEORGE HERBERT FONTAINE", $fontAuthor, $brush, (New-Object System.Drawing.RectangleF 120, 2140, 1410, 80), $sf)
$out = "C:\Users\lomus\OneDrive\My Books for Amazon\Protocol Flamingo\Protocol_Flamingo_cover_front.jpg"
$enc = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$ep = New-Object System.Drawing.Imaging.EncoderParameters 1
$ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality, [long]92)
$bmp.Save($out, $enc, $ep)
$g.Dispose(); $bmp.Dispose()
Write-Output "saved"
