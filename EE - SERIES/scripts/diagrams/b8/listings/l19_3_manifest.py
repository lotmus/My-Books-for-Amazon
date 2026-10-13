"""Write and check an update manifest: version, size, and SHA-256 of the firmware image."""
import hashlib
import json
import sys
from pathlib import Path

def sha256_file(path, chunk=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while block := f.read(chunk):
            h.update(block)
    return h.hexdigest()

def make_manifest(image, version):
    p = Path(image)
    return {"version": version, "file": p.name, "size": p.stat().st_size, "sha256": sha256_file(p)}

def check(image, manifest):
    p = Path(image)
    if p.stat().st_size != manifest["size"]:
        return "size mismatch"
    if sha256_file(p) != manifest["sha256"]:
        return "hash mismatch"
    return "ok"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: l19_3_manifest.py firmware.bin 1.4.2")
    m = make_manifest(sys.argv[1], sys.argv[2])
    Path(sys.argv[1]).with_suffix(".json").write_text(json.dumps(m, indent=2))
    print(json.dumps(m, indent=2))
    print("check:", check(sys.argv[1], m))
