# Chinese Character Riddle Probes Dataset (CCRP DataSet) v0.1

**汉字字谜探针数据集** ｜ short name **CCRP DataSet** ｜ version **0.1** (2026-11-09)
Publisher: **Spring Buds Data Source Inc. / 春芽数源**

Repository: <https://github.com/SunSeeding/ccrp>

Live site: <https://sunseeding.github.io/ccrp/>

> **Data license: `data/` is CC BY-NC-SA 4.0 (NonCommercial · Attribution · ShareAlike)**; `scripts/` is MIT, `paper/` and docs are CC BY 4.0. The GitHub sidebar shows `Other` because the platform's detector does not include CC-BY-NC-SA-4.0 (only CC-BY-4.0 / CC-BY-SA-4.0 / CC0-1.0). This does **not** mean the data is commercially usable, MIT, or public domain. See the root `LICENSE` (official CC legal code) and the §5 license map.

> A research dataset for studying Chinese character riddles as a **behavioral
> structural probe** for large language models: 100 high-frequency simplified
> characters, reference clues with structure cards, model-authored riddles, a
> generation–solving closed loop, a 2×2 factorial decomposition, and an ICL
> control task, with complete per-item records.

> ⚠️ **This is not a ranking benchmark.** The accompanying paper finds that the
> off-the-shelf 100-item public slice has no ranking validity (only 11 answer
> characters, 85/100 items drawn from public train/valid, all 15 test items
> answering 「旦」 *dàn*, and unequal reasoning budgets across vendors). All
> numbers here support **paired, within-item, between-condition comparisons
> under one scorer** — never cross-model ability rankings. See
> `paper/riddle-paper-en.md` §6.2 and §6.5.

---

## 1. What a riddle looks like

A Chinese character riddle gives a natural-language clue whose answer is
**exactly one Chinese character**. Solving requires treating the character as
a decomposable, recombinable object of components, strokes, sound and sense.

> 「叉去一点，添上一寸」 → **对** (*duì*, "correct / right")
> Literally: "remove one dot from 叉 (*chā*, 'fork') and add an inch 寸
> (*cùn*)". 叉 minus 丶 yields 又; juxtaposing 又 with 寸 gives 对.

**Riddle texts are kept verbatim in Chinese throughout this repository.**
They are untranslatable: the clue operates on glyph shape, meaning or tone.
Where English text is needed we add a literal gloss and a structural
annotation, as above. The three techniques are **graphemic decomposition
(DECOMP / 拆形)**, **semantic reinterpretation (SEM / 会意)** and
**homophonic pun (HOMO / 谐音)**.

---

## 2. Contents at a glance

| Item | Count | Note |
|---|---|---|
| Target characters | 100 | high-frequency simplified Chinese, in frequency order |
| Reference clues (published) | 1,019 | all CC-Riddle human-authored, reorganized by answer character |
| Reference clues (withheld) | 31 | web UGC tagged "local / restricted research use only"; see `data/WITHHELD.md` |
| Model-authored riddles | 600 | kimi 300 / u2 300; DECOMP 200 / SEM 200 / HOMO 200 |
| Passed quality control | 597 | shared by both blind-test conditions |
| Closed-loop answers | 1,194 | cross blind test 597 + same-item self-test 597, item-level paired |
| ICL control task | 192 calls | 24 items × 4 conditions × 2 models, frozen seed `20261106` |
| Papers | 2 | Chinese original + full English translation + Chinese PDF |

**Headline result** (quote verbatim; do not recompute): cross blind test
39.03% (233/597) → same-item self-test 44.22% (264/597), item-level paired
exact McNemar *p* = 0.0144. A 2×2 additive decomposition gives a
solver-ability gap *β* = +16.26 pp, an item-source difficulty gap
*α* = +11.36 pp and a net self-familiarity effect *γ* = +5.22 pp. The
opposite-signed differences seen when stratifying by maker (+21.48 pp /
−11.04 pp) are *β* flipping the sign — not evidence that only one model has
a self-preference.

---

## 3. Quick start

```bash
# Verify package integrity — Python 3 standard library only, offline
python scripts/verify_release.py .

# Inspect a reference clue
python -c "import json;print(next(json.loads(l) for l in open('data/reference-slice.jsonl',encoding='utf-8')))"

# Count outcomes in the cross blind test
python -c "import json,collections;print(collections.Counter(r['correct'] for r in map(json.loads,open('data/blind.jsonl',encoding='utf-8'))))"
```

Field dictionary: [`data/README.md`](data/README.md). Dataset datasheet:
[`docs/DATASHEET.md`](docs/DATASHEET.md). Per-file SHA256: `manifest.json`.
Withheld-record ledger: [`data/WITHHELD.md`](data/WITHHELD.md).

**Scoring convention**: exact single-character match after whitespace removal.
Anomalies are recorded as `correct = 0` with the denominator unchanged, plus
`format_bad / error / timed_out` flags. In integrated records `split` is
uniformly `test`; the original public split is preserved in `source_split`
and **must not be dropped** — it is the key covariate for diagnosing
public-corpus memorization contamination.

---

## 4. Repository layout

```
.
├── README.md / README.en.md        Chinese / English guides
├── CHANGELOG.md                    v0.1 changes and known limitations
├── CITATION.cff                    citation metadata
├── THIRD_PARTY.md                  upstream attribution, modification notice, withheld material
├── LICENSE                         official CC BY-NC-SA 4.0 legal code + multi-license notice
├── LICENSE-DATA                    CC BY-NC-SA 4.0 (data/)
├── LICENSE-DOCS                    CC BY 4.0 (paper/, docs/, README)
├── manifest.json                   byte sizes + SHA256 + row-count conventions
├── data/                           the dataset (CC BY-NC-SA 4.0)
│   ├── README.md                   field dictionary
│   ├── WITHHELD.md                 fingerprint ledger for 31 withheld clues
│   ├── hanzi_index-top100.csv      character list + structure cards
│   ├── pipeline_meta.json          prompt_version and project metadata
│   ├── reference-slice.jsonl       1,019 reference clues
│   ├── explanations-llm.jsonl      corresponding LLM explanations
│   ├── provenance-reference.jsonl  per-clue provenance
│   ├── generated-*.jsonl           600 model-authored riddles
│   ├── quality.jsonl               600 quality verdicts
│   ├── blind*.jsonl                cross blind test / same-item self-test
│   ├── provenance-generated.jsonl  generation-side input_snapshot_sha256
│   ├── selftest-*.json*            paired statistics, 2×2, conversation hashes
│   ├── icl-probe-*                 frozen items / exemplars / 192 calls / analysis
│   └── summary.json                pipeline summary and limitations
├── paper/                          Chinese + English papers (CC BY 4.0)
│   ├── riddle-paper.md             Chinese original
│   ├── riddle-paper.html           typeset Chinese HTML (4 figures)
│   ├── riddle-paper.pdf            Chinese PDF
│   ├── riddle-paper-en.md          full English translation
│   ├── riddle-paper-en.html        typeset English HTML
│   └── riddle-paper-en.pdf         English PDF
├── docs/DATASHEET.md               datasheet
└── scripts/                        MIT
    ├── build_release.py             export this package from the local research tree
    └── verify_release.py            standalone integrity check
```

---

## 5. License map (per-directory)

| Path | License | Reason |
|---|---|---|
| `data/` | **CC BY-NC-SA 4.0** | contains CC-Riddle-derived material; redistribution requires the same license, attribution and a modification notice |
| `scripts/` | **MIT** | our original tooling (full text: `scripts/LICENSE`) |
| `paper/`, `docs/`, `README*.md`, `THIRD_PARTY.md`, `CHANGELOG.md` | **CC BY 4.0** | documentation; the papers quote only short clue examples |
| Third-party material | see `THIRD_PARTY.md` | upstream attribution + withheld records |

- **Publishing does not violate NonCommercial.** CC BY-NC-SA 4.0 §1 defines
  NonCommercial as "not primarily intended for or directed towards commercial
  advantage or monetary compensation", and expressly treats unpaid digital
  file sharing as NonCommercial. NC restricts **downstream commercial use**.
- **Scope of ShareAlike.** §4(b) provides that incorporating all or a
  substantial part of a database's contents into a database of your own makes
  *that database* Adapted Material — "but not its individual contents".
- **The GitHub sidebar `Other` label is not a licensing judgement.** Its
  detector (choosealicense, 47 licenses) does not include CC-BY-NC-SA-4.0,
  so no sidebar label is possible for this license. The root `LICENSE`
  reproduces the official CC legal code verbatim. **Do not substitute a
  different license text merely to obtain a label.** Always consult the
  table above and the per-directory license files.
  `data/` therefore ships under BY-NC-SA; our original code and documents are
  not automatically covered and are licensed separately.
- **CC BY-NC-SA 4.0 is not an OSI-approved open-source license.** Please say
  "publicly released under CC BY-NC-SA 4.0", not "open source dataset".

---

## 6. Provenance rules and the Scheme-C withhold

| Origin of a clue | Link provided |
|---|---|
| CC-Riddle | arXiv:2206.13778 paper link + upstream repository + row id + source-file SHA256 + license (**the upstream dataset has no per-item URLs**) |
| A public web page | page URL / title / capture date / snippet hash — **all withheld in v0.1** |
| Model-generated | `no_url`; model / prompt version / timestamp / input hash only |

**No URL is ever fabricated.** CC-Riddle clues point to the paper and
repository, never to invented per-item pages; model-generated clues and
explanations have no source link at all.

v0.1 applies **Scheme C: withhold at export time; the local research tree and
all existing artifacts are left byte-for-byte untouched.** All 31 web UGC
clues were tagged at collection time as having no clear authorisation and a
"local / restricted research use only" scope, and a public repository is not
a restricted environment. They are therefore not shipped, together with
their 27 site-provided explanations, 4 LLM explanations, 58 page-URL
references, 28 game-bank items and 87 prompt-snapshot domain traces. The
package retains `question_sha256`, `input_snapshot_sha256` and row counts, so
provenance stays auditable at the **fingerprint level** (paper criterion C6).
The offline site, the game, raw crawls and the API-driven pipeline are out of
scope for v0.1.

---

## 7. Citation

```bibtex
@dataset{ccrp2026,
  title  = {Chinese Character Riddle Probes Dataset (CCRP DataSet)},
  author = {{Spring Buds Data Source Inc.}},
  year   = {2026},
  note   = {Version 0.1. Upstream corpus: CC-Riddle, arXiv:2206.13778,
            licensed CC BY-NC-SA 4.0. Selected, reorganized and augmented.},
  url    = {https://github.com/SunSeeding/ccrp}
}
```

Required upstream attribution: Fan Xu, Yunxiang Zhang, Xiaojun Wan (Text
Mining and Linguistic Computing Group, Wangxuan Institute of Computer
Technology, Peking University), *CC-Riddle: A Question Answering Dataset of
Chinese Character Riddles*, arXiv:2206.13778, CC BY-NC-SA 4.0. We selected,
reorganized and augmented their corpus. The full attribution and
modification notice is in `THIRD_PARTY.md`; retain it when redistributing
(CC BY-NC-SA 4.0 §3(a)).

Machine-readable citation: `CITATION.cff`; its `repository-code` / `url`
fields point to this repository. A **Zenodo DOI will be backfilled after the
deposition is published** (metadata pre-filled in `.zenodo.json`; procedure in
`docs/ZENODO.md`). No DOI is invented before it exists.

---

## 8. Known limitations (read before use)

1. **Explanations are not authoritative character etymology.** The 1,023
   explanations are post-hoc rationalisations produced *given clue + answer*;
   58.9% were self-rated `low`, and automatic technique labels skew heavily
   toward SEM (594:427:2). They should not be used directly as CoT supervision.
2. **Quality gates were not human-validated.** The 3-gram Jaccard originality
   threshold of 0.35 was calibrated on 60 pilot items; clue quality and
   answer uniqueness received **no human review**.
3. **The ICL probe is directional only.** n = 24 per cell, all McNemar
   *p* ≥ 0.125; it does not establish training effectiveness.
4. **No training experiments.** Paper and data are API-level, zero-weight-
   modification experiments. Everything about "what training should supply"
   is stated as falsifiable hypotheses H1–H3.
5. **Limited model coverage.** Only two Chinese commercial APIs took part in
   the closed loop; hy4 and deepseek-v4-pro were excluded by quota exhaustion.
   No open-weight model, no human baseline, no repeated sampling.
6. **No character-meaning field.** Third-party dictionary glosses were
   deliberately not introduced, which constrains SEM items.

Full limitations: `paper/riddle-paper-en.md` §7 and `docs/DATASHEET.md`.

---

This file and `README.md` are licensed CC BY 4.0. Third-party notices and
license details are in `THIRD_PARTY.md`; that document is not legal advice.
