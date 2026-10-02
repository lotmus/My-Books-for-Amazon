$ErrorActionPreference = "Stop"
$src = Split-Path -Parent $PSScriptRoot
$out = Join-Path $src "The_Universe_Has_No_Now.md"
$figs = Join-Path $src "Figures\figs"

$files = @(
  "00_Front_Matter.md",
  "01_Part_One_No_Now.md",
  "02_Part_Two_Past.md",
  "03_Part_Three_Burst.md",
  "04_Part_Four_Missing.md",
  "05_Part_Five_Horizons.md",
  "06_Part_Six_Getting_There.md",
  "07_Part_Seven_Loops.md",
  "08_Part_Eight_Copies.md",
  "09_Part_Nine_Filter.md",
  "10_Part_Ten_Future.md",
  "11_Appendix.md"
)

$yaml = @"
---
title: The Universe Has No Now
subtitle: Time, Origins, and Whether We Can Get Somewhere Else
author: Lothar J. Musiol
lang: en-US
rights: Copyright © 2026 Lothar J. Musiol. All rights reserved.
---

"@

$sb = New-Object System.Text.StringBuilder
[void]$sb.Append($yaml)

function Resolve-Fig([int]$n) {
  foreach ($name in @(
      ("fig{0:D2}.jpg" -f $n),
      ("fig{0:D2}.jpeg" -f $n),
      ("fig{0:D2}.png" -f $n),
      ("fig{0:D2}_slot.png" -f $n)
    )) {
    $p = Join-Path $figs $name
    if (Test-Path $p) { return "Figures/figs/$name" }
  }
  return ("Figures/figs/fig{0:D2}.png" -f $n)
}

$missing = New-Object System.Collections.Generic.List[int]
foreach ($name in $files) {
  $raw = Get-Content -LiteralPath (Join-Path $src $name) -Raw -Encoding UTF8
  $raw = $raw -replace "%%TOC%%\r?\n\r?\n", "" -replace "%%TOC%%\r?\n", "" -replace "%%TOC%%", ""
  $raw = [regex]::Replace($raw, '!\[(Figure\s+(\d+)[^\]]*)\]\([^)]+\)', {
      param($m)
      $n = [int]$m.Groups[2].Value
      $rel = Resolve-Fig $n
      $full = Join-Path $src ($rel -replace "/", "\")
      if (-not (Test-Path $full)) { $script:missing.Add($n) }
      return "![$($m.Groups[1].Value)]($rel)"
    })
  $lines = $raw -split "`r?`n", 0
  foreach ($line in $lines) {
    if ($line -match '^# PART' -or $line -match '^# APPENDIX' -or $line -match '^## ') {
      [void]$sb.AppendLine("\newpage")
      [void]$sb.AppendLine("")
    }
    [void]$sb.AppendLine($line)
  }
  [void]$sb.AppendLine("")
  [void]$sb.AppendLine("\newpage")
  [void]$sb.AppendLine("")
}

[System.IO.File]::WriteAllText($out, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

$plain = [regex]::Replace($sb.ToString(), '(?s)^---.*?---\s*', '')
$plain = [regex]::Replace($plain, '!\[.*?\]\(.*?\)', ' ')
$plain = $plain -replace '\\newpage', ' '
$words = ([regex]::Matches($plain, "[A-Za-z0-9’']+")).Count
$miss = ($missing | Select-Object -Unique) -join ","
$stamp = @"
$words
missing=$miss
assembled=$out
"@
[System.IO.File]::WriteAllText((Join-Path $PSScriptRoot "WORD_COUNT.txt"), $stamp, [System.Text.UTF8Encoding]::new($false))
Write-Host "assembled $out"
Write-Host "words $words"
Write-Host "missing figure files $miss"
