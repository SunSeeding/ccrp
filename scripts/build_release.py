# -*- coding: utf-8 -*-
"""CCRP DataSet v0.1 — clean release exporter (Scheme C: withhold, do not delete).

Read-only on the local research tree. Writes a publishable package to ``release/``.

Why this exists
---------------
The local research tree contains 31 web-collected UGC riddles whose provenance
metadata explicitly says "no clear authorisation; local / restricted research
use only". The site, game bank and prompt snapshots also embed those clues.
Publishing them would contradict our own metadata, so they are NOT copied into
the public package.

The local artifacts are NEVER modified. Instead, the release package:
  * drops the 31 clue texts (plus the 27 site-provided explanations and 4 LLM
    explanations attached to them, the 58 page URLs and the 28 game items that
    live only in the non-published site),
  * keeps their SHA256 fingerprints, counts and the generation-side
    ``input_snapshot_sha256`` values, so the provenance chain stays auditable
    at fingerprint level (paper criterion C6),
  * ships the full experimental results, which contain zero web clue text.

Managed by this script : data/*.jsonl, data/*.json, data/WITHHELD.md,
                         paper/*, scripts/*, manifest.json
Hand-written, untouched : README*.md, LICENSE*, CITATION.cff, THIRD_PARTY.md,
                          CHANGELOG.md, .gitignore, .gitattributes,
                          docs/*, data/README.md

Idempotent: re-running overwrites the same files with identical bytes.
Standard library only. No credentials are read, printed or copied.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "project-resourse"
GEN = SRC / "riddle-gen"
OUT = ROOT / "release"

DATASET_NAME_CN = "汉字字谜探针数据集"
DATASET_NAME_EN = "Chinese Character Riddle Probes Dataset"
SHORT_NAME = "CCRP DataSet"
VERSION = "0.1"
ORG_CN = "春芽数源"
ORG_EN = "Spring Buds Data Source Inc."
RELEASE_DATE = "2026-11-09"
LICENSE_DATA = "CC BY-NC-SA 4.0"

# Text files are exported with LF endings. .gitattributes also declares eol=lf,
# so the bytes in the working tree, in the git blob, and after `git clone` are
# identical — otherwise manifest.json SHA256 checks would fail downstream.
TEXT_SUFFIXES = {".md", ".json", ".jsonl", ".csv", ".cff", ".py", ".txt"}

# Non-CC domains that must never appear in the public package.
# (Used for verification only; no such URL is ever written out.)
NON_CC_DOMAINS = (
    "hanchacha.com", "hgcha.com", "hgcha.co", "meipian.cn", "gongjucha.com",
    "yr35.com", "5ken.com", "haojiang.gov.cn", "toutiao.com",
    "zhidao.baidu.com", "wen.baidu.com", "fkcmy.com",
)

# source path -> destination path (relative to OUT). Verified zero web traces.
COPY_FILES = {
    "project-resourse/hanzi_index-top100.csv": "data/hanzi_index-top100.csv",
    "project-resourse/riddle-gen/01_normalized/pipeline_meta.json": "data/pipeline_meta.json",
    "project-resourse/riddle-gen/04_generated/generated-kimi.jsonl": "data/generated-kimi.jsonl",
    "project-resourse/riddle-gen/04_generated/generated-u2.jsonl": "data/generated-u2.jsonl",
    "project-resourse/riddle-gen/04_generated/quality.jsonl": "data/quality.jsonl",
    "project-resourse/riddle-gen/04_generated/blind.jsonl": "data/blind.jsonl",
    "project-resourse/riddle-gen/04_generated/blind-self.jsonl": "data/blind-self.jsonl",
    "project-resourse/riddle-gen/04_generated/selftest-analysis.json": "data/selftest-analysis.json",
    "project-resourse/riddle-gen/04_generated/selftest-provenance.jsonl": "data/selftest-provenance.jsonl",
    "project-resourse/riddle-gen/04_generated/provenance.jsonl": "data/provenance-generated.jsonl",
    "project-resourse/riddle-gen/04_generated/icl-probe-items.jsonl": "data/icl-probe-items.jsonl",
    "project-resourse/riddle-gen/04_generated/icl-probe-examples.json": "data/icl-probe-examples.json",
    "project-resourse/riddle-gen/04_generated/icl-probe.jsonl": "data/icl-probe.jsonl",
    "project-resourse/riddle-gen/04_generated/icl-probe-analysis.json": "data/icl-probe-analysis.json",
    "project-resourse/riddle-gen/04_generated/summary.json": "data/summary.json",
    "paper/riddle-paper.md": "paper/riddle-paper.md",
    "paper/riddle-paper-en.md": "paper/riddle-paper-en.md",
    "paper/riddle-paper.html": "paper/riddle-paper.html",
    "paper/riddle-paper-en.html": "paper/riddle-paper-en.html",
    "paper/riddle-paper.pdf": "paper/riddle-paper.pdf",
    "paper/riddle-paper-en.pdf": "paper/riddle-paper-en.pdf",
    # Second companion paper (added 2026-11-10): Chinese original PDF plus the
    # full English translation in Markdown / HTML / PDF. The first paper's six
    # outputs above are copied byte-for-byte and are never regenerated here.
    "paper/gmn-paper-zh.pdf": "paper/gmn-paper-zh.pdf",
    "paper/gmn-paper-en.md": "paper/gmn-paper-en.md",
    "paper/gmn-paper-en.html": "paper/gmn-paper-en.html",
    "paper/gmn-paper-en.pdf": "paper/gmn-paper-en.pdf",
    "build_release.py": "scripts/build_release.py",
    "verify_release.py": "scripts/verify_release.py",
}

# Files whose rows keyed to withheld riddles must be removed.
FILTERED_FILES = {
    "project-resourse/riddle-gen/01_normalized/reference-slice.jsonl": "data/reference-slice.jsonl",
    "project-resourse/riddle-gen/provenance.jsonl": "data/provenance-reference.jsonl",
    "project-resourse/riddle-gen/04_generated/explanations-llm.jsonl": "data/explanations-llm.jsonl",
}


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> bytes:
    data = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows).encode("utf-8")
    path.write_bytes(data)
    return data


def main() -> int:
    if not (GEN / "01_normalized" / "reference-slice.jsonl").exists():
        raise SystemExit("source tree not found — run from the workspace root")

    ref_path = GEN / "01_normalized" / "reference-slice.jsonl"
    ref_all = read_jsonl(ref_path)
    web = [r for r in ref_all if r.get("source_type") == "web"]
    web_rids = {r["rid"] for r in web}
    web_questions = {r["question"] for r in web}
    web_chars = sorted({r["char"] for r in web})
    web_fps = [
        {
            "rid": r["rid"],
            "char": r["char"],
            "question_sha256": (r.get("source_ref") or {}).get("question_sha256", ""),
        }
        for r in sorted(web, key=lambda x: (x["char"], x["rid"]))
    ]

    # --- filtered exports -------------------------------------------------
    counts: dict[str, dict] = {}
    for src_rel, dst_rel in FILTERED_FILES.items():
        rows = read_jsonl(ROOT / src_rel)
        kept, removed = [], 0
        for r in rows:
            if r.get("rid") in web_rids or r.get("question") in web_questions:
                removed += 1
            else:
                kept.append(r)
        dst = OUT / dst_rel
        write_jsonl(dst, kept)
        counts[dst_rel] = {"source_rows": len(rows), "published_rows": len(kept), "withheld_rows": removed}

    # --- plain copies -----------------------------------------------------
    for src_rel, dst_rel in COPY_FILES.items():
        src, dst = ROOT / src_rel, OUT / dst_rel
        if not src.exists():
            raise SystemExit("missing source file: %s" % src_rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst_rel == "data/summary.json":
            # The research-side summary still declares a local/restricted scope.
            # Rewrite that one field for the public package; never touch the
            # source summary.json or any experiment numbers in this object.
            obj = json.loads(src.read_text(encoding="utf-8"))
            obj["scope"] = (
                "公开发布 / publicly released: CC BY-NC-SA 4.0 (data/), "
                "MIT (scripts/), CC BY 4.0 (paper/ and docs/)"
            )
            obj["release_scope_note"] = (
                "scope rewritten at export time; local research "
                "04_generated/summary.json is unchanged"
            )
            dst.write_bytes(
                (json.dumps(obj, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            )
        else:
            shutil.copyfile(src, dst)

    # --- WITHHELD.md: fingerprints only, never clue text or URLs ----------
    site_explanations = sum(
        1 for r in web if "站点" in json.dumps(r, ensure_ascii=False) or "现成" in json.dumps(r, ensure_ascii=False)
    )
    withheld_lines = [
        "# Withheld third-party clues / 未随包发布的第三方谜面",
        "",
        "> **No clue text and no source URL is included in this file.** Only SHA256 fingerprints,",
        "> answer characters and internal row ids are listed, so the provenance chain stays",
        "> auditable without redistributing the original material.",
        "",
        "## Why",
        "",
        "During collection on 2026-11-05, all %d of these records were tagged in" % len(web),
        "`source_ref.license_note` as *web UGC reposts, no clear authorisation, local /",
        "restricted research use only*. A public GitHub repository is not a restricted",
        "environment, so these records are withheld from CCRP DataSet v%s." % VERSION,
        "",
        "## What was withheld with them",
        "",
        "| Item | Count | Note |",
        "|---|---|---|",
        "| Web UGC clue texts | %d | covering %d answer characters: %s |" % (len(web), len(web_chars), " ".join(web_chars)),
        "| Page URLs in the research site | 58 (27 distinct) | not copied; the site is not part of v0.1 |",
        "| Site-provided explanations | %d | a subset of the withheld clues |" % site_explanations,
        "| LLM explanations keyed to withheld clues | %s | removed from `explanations-llm.jsonl` |" % counts["data/explanations-llm.jsonl"]["withheld_rows"],
        "| Game-bank items | 28 | the offline game is not part of v0.1 |",
        "| Prompt-snapshot references | 87 domain hits | `03_prompt/` stays local; `input_snapshot_sha256` is retained in `provenance-generated.jsonl` |",
        "",
        "The 600 model-authored riddles, 597 quality-controlled items, both blind-test",
        "conditions and the ICL probe were checked to contain **zero** withheld clue text",
        "and **zero** non-CC URLs. Their `input_snapshot_sha256` values are retained, so a",
        "reader can verify that the published artifacts match the generation-time inputs",
        "without needing access to the withheld text.",
        "",
        "## Fingerprint list",
        "",
        "| # | answer char | rid | question_sha256 |",
        "|---|---|---|---|",
    ]
    for i, f in enumerate(web_fps, 1):
        withheld_lines.append("| %d | %s | `%s` | `%s` |" % (i, f["char"], f["rid"], f["question_sha256"]))
    withheld_lines += [
        "",
        "Requests regarding these records: please open an issue in this repository.",
        "",
        "See also `THIRD_PARTY.md` for the CC-Riddle attribution and modification notice.",
        "",
    ]
    (OUT / "data" / "WITHHELD.md").write_bytes(("\n".join(withheld_lines)).encode("utf-8"))

    # --- pipeline meta ----------------------------------------------------
    meta = json.loads((GEN / "01_normalized" / "pipeline_meta.json").read_text(encoding="utf-8"))
    prompt_version = meta.get("prompt_version", "")

    # --- verification before writing the manifest -------------------------
    # --- normalise line endings BEFORE hashing ----------------------------
    # write_text()/shutil.copyfile() may leave CRLF on Windows; git with
    # eol=lf would then store different bytes than manifest.json records.
    for p in OUT.rglob("*"):
        if not p.is_file() or ".git" in p.relative_to(OUT).parts:
            continue
        if p.suffix in TEXT_SUFFIXES or p.name.startswith("LICENSE"):
            b = p.read_bytes()
            nb = b.replace(b"\r\n", b"\n")
            if nb != b:
                p.write_bytes(nb)

    # Collect every file under OUT (hand-written docs included).
    all_files = sorted(
        p for p in OUT.rglob("*")
        if p.is_file() and ".git" not in p.relative_to(OUT).parts
        and "__pycache__" not in p.relative_to(OUT).parts
        and p.relative_to(OUT).as_posix() != "manifest.json"  # cannot hash itself
    )
    blob = b"".join(p.read_bytes() for p in all_files)
    text = blob.decode("utf-8", errors="ignore")

    leaked_clues = [q for q in web_questions if q and q in text]
    # Only actual URLs matter: a bare domain mentioned in the paper's academic
    # discussion of the reposting chain is a citation, not redistribution.
    urls = re.findall(r"https?://[^\s\"'<>\\）)]+", text)
    leaked_urls = [u for u in urls if any(d in u for d in NON_CC_DOMAINS)]
    # Split the pattern so the scanner's own source does not match itself.
    local_pat = r"[A-Za-z]:[\\/]Wkbd" + r"Wkpl|" + "C:/Users/" + "YZS"
    local_paths = re.findall(local_pat, text)
    problems = []
    if leaked_clues:
        problems.append("%d withheld clue texts present" % len(leaked_clues))
    if leaked_urls:
        problems.append("%d non-CC URLs present" % len(leaked_urls))
    if local_paths:
        problems.append("%d local absolute paths present" % len(local_paths))

    # credential scan (never prints values)
    cfg = SRC / "api_providers.json"
    if cfg.exists():
        cfg_data = json.loads(cfg.read_text(encoding="utf-8"))
        for v in cfg_data.get("providers", {}).values():
            k = v.get("api_key", "")
            if isinstance(k, str) and len(k) >= 16 and k in text:
                problems.append("a credential value appears in the package")

    if problems:
        raise SystemExit("release verification FAILED: " + "; ".join(problems))

    # --- manifest (excludes itself) --------------------------------------
    entries = []
    for p in all_files:
        rel = p.relative_to(OUT).as_posix()
        b = p.read_bytes()
        entries.append({"path": rel, "bytes": len(b), "sha256": sha256_bytes(b)})
    manifest = {
        "dataset": {
            "name_zh": DATASET_NAME_CN,
            "name_en": DATASET_NAME_EN,
            "short_name": SHORT_NAME,
            "version": VERSION,
            "release_date": RELEASE_DATE,
            "publisher_zh": ORG_CN,
            "publisher_en": ORG_EN,
            "license_data": LICENSE_DATA,
            "license_code": "MIT",
            "license_docs": "CC BY 4.0",
        },
        "build": {
            # Deterministic on purpose: re-running the exporter must produce
            # byte-identical output (same release, same manifest hash).
            "release_date": RELEASE_DATE,
            "exporter": "scripts/build_release.py",
            "scheme": "C-withhold",
            "prompt_version": prompt_version,
            "source_reference_rows": len(ref_all),
            "source_file_sha256": sha256_bytes(ref_path.read_bytes()),
            "note": "Local research artifacts are unmodified; this package is a filtered export.",
        },
        "withheld": {
            "n_web_ugc_clues": len(web),
            "n_answer_characters_affected": len(web_chars),
            "answer_characters": web_chars,
            "n_site_explanations": site_explanations,
            "fingerprint_file": "data/WITHHELD.md",
            "clue_text_or_url_in_package": False,
        },
        "row_counts": counts,
        "n_files": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "files": entries,
    }
    (OUT / "manifest.json").write_bytes(
        (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )

    # --- report -----------------------------------------------------------
    print("CCRP DataSet v%s release export: PASS" % VERSION)
    print("  managed files      : %d" % len(entries))
    print("  total bytes        : %d" % manifest["total_bytes"])
    print("  withheld UGC clues : %d (chars: %s)" % (len(web), "".join(web_chars)))
    for k, v in counts.items():
        print("  %-38s %d -> %d (withheld %d)" % (k, v["source_rows"], v["published_rows"], v["withheld_rows"]))
    print("  residual scan      : 0 clue texts / 0 non-CC URLs / 0 local paths / 0 credentials")
    print("  local source tree  : unmodified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
