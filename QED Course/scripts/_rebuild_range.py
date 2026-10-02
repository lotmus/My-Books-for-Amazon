# -*- coding: utf-8 -*-
"""Rebuild selected lessons into standalone docx files and the complete book."""
import glob
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lesson as bl

ROOT = bl.ROOT
nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else (
    list(range(2, 88))
)
failed = []
for n in nums:
    matches = glob.glob(os.path.join(HERE, "lesson%02d.txt" % n))
    if not matches:
        failed.append(("missing", n))
        continue
    src = matches[0]
    last_err = None
    for attempt in range(5):
        try:
            meta, blocks = bl.parse(src)
            out = os.path.join(bl.CHAPTERS, "Lesson %02d %s.docx" % (int(meta["NUM"]), meta["TITLE"]))
            bl.build_standalone(meta, blocks, out)
            bl.splice_into_complete(meta, blocks)
            print("OK", os.path.basename(out), "blocks", len(blocks))
            last_err = None
            break
        except Exception as e:
            last_err = e
            print("RETRY", n, attempt + 1, e)
            time.sleep(2 + attempt)
    if last_err is not None:
        failed.append((n, repr(last_err)))
        print("FAIL", n, last_err)

if failed:
    print("FAILED", failed)
    sys.exit(1)
print("done", len(nums))
