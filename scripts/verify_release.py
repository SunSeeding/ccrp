# -*- coding: utf-8 -*-
"""CCRP DataSet — standalone integrity check for a published package.

Run from anywhere:  python verify_release.py [path/to/release]

Self-contained: standard library only, no access to the original research tree,
no credentials, no network. Verifies the manifest hashes, row counts, the
withheld-fingerprint ledger and the absence of redistributed third-party URLs.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

NON_CC_DOMAINS = (
    "hanchacha.com", "hgcha.com", "hgcha.co", "meipian.cn", "gongjucha.com",
    "yr35.com", "5ken.com", "haojiang.gov.cn", "toutiao.com",
    "zhidao.baidu.com", "wen.baidu.com", "fkcmy.com",
)
# Split so this checker's own source does not match its own pattern.
LOCAL_PATH_PAT = re.compile(r"[A-Za-z]:[\\/]Wkbd" + r"Wkpl|" + "C:/Users/" + "YZS")
URL_PAT = re.compile(r"https?://[^\s\"'<>\\）)]+")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main(root: Path) -> int:
    problems: list[str] = []
    notes: list[str] = []

    mf = root / "manifest.json"
    if not mf.exists():
        print("FAIL: manifest.json missing")
        return 1
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    ds = manifest.get("dataset", {})
    print("Dataset : %s (%s) v%s" % (ds.get("name_en"), ds.get("short_name"), ds.get("version")))
    print("Publisher: %s / %s" % (ds.get("publisher_zh"), ds.get("publisher_en")))

    # 1. hashes
    listed = manifest.get("files", [])
    bad = []
    for e in listed:
        p = root / e["path"]
        if not p.exists():
            bad.append(e["path"] + " (missing)")
            continue
        b = p.read_bytes()
        if len(b) != e["bytes"] or sha256_bytes(b) != e["sha256"]:
            bad.append(e["path"] + " (hash/size mismatch)")
    if bad:
        problems.append("manifest mismatch: " + ", ".join(bad[:8]))
    else:
        notes.append("%d/%d files match manifest SHA256" % (len(listed), len(listed)))

    # 2. unlisted stray files (excluding git internals)
    actual = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and ".git" not in p.relative_to(root).parts
        and "__pycache__" not in p.relative_to(root).parts
    }
    # manifest.json cannot list its own hash (circular), so it is exempt.
    declared = {e["path"] for e in listed} | {"manifest.json"}
    stray = sorted(actual - declared)
    if stray:
        problems.append("unlisted files: " + ", ".join(stray[:8]))

    # 3. row counts
    for rel, c in manifest.get("row_counts", {}).items():
        p = root / rel
        if not p.exists():
            problems.append("missing filtered file: " + rel)
            continue
        n = sum(1 for line in p.read_text(encoding="utf-8").splitlines() if line.strip())
        if n != c["published_rows"]:
            problems.append("%s rows %d != expected %d" % (rel, n, c["published_rows"]))
        else:
            notes.append("%s: %d rows (withheld %d)" % (rel, n, c["withheld_rows"]))

    # 4. no web clues survived in the reference slice
    ref = root / "data" / "reference-slice.jsonl"
    if ref.exists():
        bad_sources = set()
        for line in ref.read_text(encoding="utf-8").splitlines():
            if line.strip():
                t = json.loads(line).get("source_type")
                if t != "ccriddle_human":
                    bad_sources.add(str(t))
        if bad_sources:
            problems.append("unexpected source_type in reference slice: %s" % ", ".join(sorted(bad_sources)))
        else:
            notes.append("reference slice contains only ccriddle_human rows")

    # 5. fingerprint ledger
    led = root / "data" / "WITHHELD.md"
    if not led.exists():
        problems.append("data/WITHHELD.md missing")
    else:
        n_fp = len(re.findall(r"^\| \d+ \| .+ \| `[0-9a-f]{12,}` \| `[0-9a-f]{64}` \|$",
                              led.read_text(encoding="utf-8"), re.M))
        expected = manifest.get("withheld", {}).get("n_web_ugc_clues")
        if n_fp != expected:
            problems.append("WITHHELD.md has %d fingerprints, expected %s" % (n_fp, expected))
        else:
            notes.append("withheld fingerprint ledger: %d entries, no clue text / URLs" % n_fp)

    # 6. residual scan across the whole package
    blob = b"".join((root / rel).read_bytes() for rel in sorted(actual))
    text = blob.decode("utf-8", errors="ignore")
    third_party_urls = [u for u in URL_PAT.findall(text) if any(d in u for d in NON_CC_DOMAINS)]
    local_paths = LOCAL_PATH_PAT.findall(text)
    if third_party_urls:
        problems.append("%d non-CC URLs present" % len(third_party_urls))
    if local_paths:
        problems.append("%d local absolute paths present" % len(local_paths))
    # credential-shaped strings (values are never printed)
    key_shaped = re.findall(r"\bsk-[A-Za-z0-9_\-]{16,}\b|\bBearer\s+[A-Za-z0-9_\-\.]{16,}\b", text)
    if key_shaped:
        problems.append("%d credential-shaped strings present" % len(key_shaped))
    if not (third_party_urls or local_paths or key_shaped):
        notes.append("residual scan: 0 non-CC URLs / 0 local paths / 0 credential-shaped strings")

    # 7. required documents
    for rel in ("README.md", "README.en.md", "LICENSE", "LICENSE-DATA", "LICENSE-DOCS",
                "scripts/LICENSE", "THIRD_PARTY.md", "CITATION.cff",
                "data/README.md", "docs/DATASHEET.md"):
        if not (root / rel).exists():
            problems.append("missing required document: " + rel)

    print("\nChecks:")
    for n in notes:
        print("  OK   " + n)
    if problems:
        print("\nFAIL:")
        for p in problems:
            print("  -    " + p)
        return 1
    print("\nRESULT: PASS — package is clean and matches its manifest.")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
    raise SystemExit(main(target))
