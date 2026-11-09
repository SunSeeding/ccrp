# Third-Party Material and Attribution / 第三方材料与署名

This file is part of the attribution required by CC BY-NC-SA 4.0 §3(a).
**Retain it in any redistribution of `data/`.**

> 本文件是 CC BY-NC-SA 4.0 §3(a) 要求的署名材料之一，再分发 `data/` 时请一并保留。

---

## 1. CC-Riddle (upstream dataset)

A subset of this dataset is derived from **CC-Riddle: A Question Answering
Dataset of Chinese Character Riddles**.

| Item | Value |
|---|---|
| Authors | Fan Xu, Yunxiang Zhang, Xiaojun Wan |
| Institution | Text Mining and Linguistic Computing Group, Wangxuan Institute of Computer Technology, Peking University |
| Paper | arXiv:2206.13778 — https://arxiv.org/abs/2206.13778 |
| Repository | https://github.com/pku0xff/CC-Riddle |
| Upstream license | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) |
| Upstream license text | https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode |
| Upstream statement | "This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0) International License. We allow the dataset to be used for non-commercial purposes only." |

**Modifications made by us (required notice under §3(a)(1)(B)):**

1. Selected 1,019 human-authored riddles from the 27,517-item upstream corpus,
   covering 100 high-frequency simplified Chinese characters, rather than
   redistributing the corpus in full or in its original order.
2. Reorganized the selection by target character and attached a character
   structure card (pinyin, stroke count, radical, IDS sequence, frequency rank).
3. Added one explanation per riddle. Explanations are either model-generated
   post-hoc rationalisations or site-provided hints; **they are not
   authoritative character etymology**.
4. Stored for each riddle the upstream row id and the SHA256 of the upstream
   source file, in `data/provenance-reference.jsonl`.
5. Built derived artifacts on top: 600 model-authored riddles, quality-control
   verdicts, two blind-test conditions, a same-item self-test and an ICL probe.

**Attribution statement to reuse in derivative works:**

> Contains material derived from *CC-Riddle: A Question Answering Dataset of
> Chinese Character Riddles* by Fan Xu, Yunxiang Zhang and Xiaojun Wan
> (Peking University), arXiv:2206.13778, licensed under CC BY-NC-SA 4.0.
> Selected, reorganized and augmented with explanations by Spring Buds Data
> Source Inc. for CCRP DataSet v0.1.

The upstream authors' copyright notices, the license notice and the warranty
disclaimer are retained here by reference. We do not claim endorsement by,
or affiliation with, the CC-Riddle authors or Peking University (§2(a)(6)).

---

## 2. Withheld web UGC material (NOT included in this package)

During collection on 2026-11-05, 31 riddles were gathered from public web
pages to fill gaps for 14 high-frequency characters. **All 31 records were
tagged at collection time** in `source_ref.license_note` as web UGC reposts
with no clear authorisation and a "local / restricted research use only"
scope. Because a public repository is not a restricted environment, these
records are **withheld** from CCRP DataSet v0.1.

Withheld together with them: their 27 site-provided explanations, 4
model-generated explanations keyed to them, 58 page-URL references in the
research site, 28 items in the offline game bank, and the prompt-snapshot
references in `03_prompt/`.

**No clue text and no source URL from this batch appears anywhere in this
package.** `data/WITHHELD.md` lists only SHA256 fingerprints, answer characters
and internal row ids, so the provenance chain remains checkable at the
fingerprint level. The 600 model-authored riddles were verified to contain
zero text from this batch; their `input_snapshot_sha256` values are preserved
in `data/provenance-generated.jsonl`.

The offline site (`05_site/`), the game bank and the raw prompt snapshots are
**not part of v0.1** and remain in the local, restricted research
environment. Their own "local / restricted access, not publicly released"
notice is therefore still accurate for those artifacts.

If you hold rights to any withheld record and would like it removed from the
local research set as well, please open an issue in this repository.

---

## 3. Model-generated content — no source URLs

Riddles authored by the models, and explanations generated from
(clue, answer) pairs, have **no external source URL**. For each we record only
the generating model, the prompt version, a timestamp and an input-snapshot
hash, and mark `no_url`. **No URL is fabricated for any record.**

Link policy used throughout the project:

| Origin of a clue | Link given |
|---|---|
| CC-Riddle | arXiv paper link + upstream repository + row id + source-file SHA256 + license (the upstream dataset has no per-item URLs) |
| A public web page | that page's URL, title, capture date and snippet hash — **withheld in v0.1**, see §2 |
| Model-generated | `no_url`; model / prompt version / timestamp / input hash only |

---

## 4. Scope of licenses

| Path | License |
|---|---|
| `data/` | CC BY-NC-SA 4.0 — `LICENSE-DATA` |
| `scripts/` | MIT — `LICENSE` |
| `paper/`, `docs/`, `README*.md`, this file | CC BY 4.0 — `LICENSE-DOCS` |

CC BY-NC-SA 4.0 is not an OSI-approved open-source license. Publishing this
repository free of charge is itself a NonCommercial act under §1 of the
license; the restriction applies to downstream commercial use.

This document is provided for information and is **not legal advice**.
