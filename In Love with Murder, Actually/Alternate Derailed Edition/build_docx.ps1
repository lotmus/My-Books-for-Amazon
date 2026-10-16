$ErrorActionPreference = 'Stop'
$md = Join-Path $PSScriptRoot 'In_Love_with_Murder_Actually_Derailed_Edition.md'
$out = Join-Path $PSScriptRoot 'In_Love_with_Murder_Actually_Derailed_Edition.docx'
$book = Split-Path $PSScriptRoot -Parent
$reference = Join-Path $book 'In_Love_with_Murder_Actually.docx'
$Pandoc = (Get-Command pandoc -ErrorAction Stop).Source
& $Pandoc $md '--from=markdown+smart' '--standalone' "--reference-doc=$reference" "--output=$out"
if ($LASTEXITCODE -ne 0) { throw "Pandoc failed with exit code $LASTEXITCODE" }
Write-Output "Built $out"
