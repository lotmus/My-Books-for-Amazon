param([string]$DocPath, [string[]]$Phrases)
$ErrorActionPreference = "Stop"
Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($DocPath, [ref]$false, [ref]$true)
try {
    foreach ($p in $Phrases) {
        $r = $doc.Content.Duplicate
        $r.Find.ClearFormatting()
        $r.Find.Text = $p
        $r.Find.Forward = $true
        $r.Find.Wrap = 0
        if ($r.Find.Execute()) {
            Write-Host "'$p' -> page $($r.Information(3))"
        } else {
            Write-Host "'$p' -> NOT FOUND"
        }
    }
} finally {
    $doc.Close([ref]$false)
    $word.Quit()
}
