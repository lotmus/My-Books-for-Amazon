import io
f = r"C:\Users\lomus\wt-dt4\NOVELS\The Digital  Twin\notes\REVIEW_REV4_2026-10-15.md"
t = io.open(f, encoding="utf-8", newline="").read()
a = t.index("After (REV4):"); b = t.index("## What is not done")
t = t[:a] + 'After (REV4): "It has been noted," he said, "that on Friday morning Securishred destroyed a box file at this address to a satisfactory standard. It has also been noted that it contained council tax." The passive is his whole personality and pays off the new Ch 22 scene.\n\n' + t[b:]
t = t.replace("Plants: Ch 4 (instructed in advance, peppermint), Ch 15 (peppermint tin), Ch 16/22/24 (hen, lanyard), Ch 27.", "Plants: Ch 4 (instructed in advance, peppermint), Ch 15 (peppermint tin), Ch 24 (hen with lanyard), Ch 30 (peppermint, 'Gareth. Whatever you have.').")
t = t.replace("Ch 28/29 hints.", "Ch 34 echo after the reveal.")
io.open(f, "w", encoding="utf-8", newline="").write(t)
print("ok")