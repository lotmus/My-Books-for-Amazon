# EE series deploy helper (seven-book layout, 2026-10-01).
# Usage: ee_deploy.ps1 -Book BookN -Name <master basename without .docx> -Md5 <current MD5> -Tag <tag> -Key <key>
# Expects $env:TEMP\<key>_new.docx and $env:TEMP\<key>_src.tgz (front.txt + src/).
# Backs up the master to bak\deploy\, moves chapters\<Book> to bak\chapters\, installs the new sources and master.
param($Book,$Name,$Md5,$Tag,$Key)
$B='D:\My Books for Amazon'
$R=(Get-ChildItem $B -Directory | ? { $_.Name -like 'EE - Series*' -or $_.Name -like 'EE - SERIES*' } | Select-Object -First 1).FullName
if(-not $R){ "ABORT series folder not found"; exit 1 }
$s=Get-Date -Format 'yyyyMMdd-HHmm'; $f="$R\$Name.docx"; $t=$env:TEMP
$h=(Get-FileHash $f -Algorithm MD5).Hash
if($h -ne $Md5){ "ABORT md5 $h"; exit 1 }
New-Item -ItemType Directory -Force "$R\bak\deploy","$R\bak\chapters" | Out-Null
Copy-Item $f "$R\bak\deploy\$Name.before-$Tag-$s.docx"
if(Test-Path "$R\chapters\$Book"){ Move-Item "$R\chapters\$Book" "$R\bak\chapters\$Book-before-$Tag-$s" }
New-Item -ItemType Directory -Force "$R\chapters\$Book" | Out-Null
tar -xzf "$t\${Key}_src.tgz" -C "$R\chapters\$Book"
$tpl="$R\bak\chapters\$Book-before-$Tag-$s\template_stub.docx"; if(Test-Path $tpl){ Copy-Item $tpl "$R\chapters\$Book\" }
Copy-Item "$t\${Key}_new.docx" $f -Force
Remove-Item "$t\${Key}_new.docx","$t\${Key}_src.tgz"
"OK $s $R"; (Get-FileHash $f -Algorithm MD5).Hash
