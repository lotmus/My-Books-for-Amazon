$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$pandoc = (Get-Command pandoc -ErrorAction Stop).Source
$css = Join-Path $PSScriptRoot 'kindle-reflowable.css'
$books = @(
    @{
        Source = 'Book 1 - The Murder That Hadnt Happened Yet\FINAL_REV14_The_Murder_That_Hadnt_Happened_Yet_KINDLE_READY.docx'
        Cover = 'Book 1 - The Murder That Hadnt Happened Yet\Kindle Front Cover.jpg'
        Output = 'Book 1 - The Murder That Hadnt Happened Yet\The_Murder_That_Hadnt_Happened_Yet_REV14_Kindle_Reflowable.epub'
        Title = "The Murder That Hadn't Happened Yet"
    },
    @{
        Source = 'Book 2 - The Warning That Was Sent Too Late\The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV04.docx'
        Cover = 'Book 2 - The Warning That Was Sent Too Late\Kindle Front Cover.jpg'
        Output = 'Book 2 - The Warning That Was Sent Too Late\The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV04_Kindle_Reflowable.epub'
        Title = 'The Warning That Was Sent Too Late'
    }
)
foreach ($book in $books) {
    $source = Join-Path $root $book.Source
    $cover = Join-Path $root $book.Cover
    $output = Join-Path $root $book.Output
    & $pandoc $source --output $output --to epub3 --standalone --toc --toc-depth=2 --split-level=1 --css $css --epub-cover-image=$cover --metadata-file (Join-Path $PSScriptRoot 'kindle-metadata.yaml') --metadata "title=$($book.Title)"
    if ($LASTEXITCODE -ne 0) { throw "EPUB export failed for $($book.Title) with exit code $LASTEXITCODE" }
    Write-Output "Wrote $output"
}
