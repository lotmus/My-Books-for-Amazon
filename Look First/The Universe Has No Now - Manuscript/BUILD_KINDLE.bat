@echo off
setlocal
cd /d "%~dp0"
if not exist export mkdir export

where python >nul 2>&1
if %ERRORLEVEL%==0 (
  python export\assemble_export.py
  if %ERRORLEVEL%==0 goto :done
)

echo Python assembler failed or missing. Concatenating markdown with PowerShell...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0export\concat_markdown.ps1"

where pandoc >nul 2>&1
if %ERRORLEVEL%==0 (
  pandoc "The_Universe_Has_No_Now.md" --from markdown+raw_tex+tex_math_dollars --toc --toc-depth=2 --resource-path=".;Figures\figs" --metadata title="The Universe Has No Now" --metadata author="Lothar J. Musiol" --to docx -o "export\The_Universe_Has_No_Now.docx"
)

:done
echo.
echo Build finished. Look in this folder for The_Universe_Has_No_Now.md
echo and in export\ for the .docx (docx only)
endlocal
