# Withheld third-party clues / 未随包发布的第三方谜面

> **No clue text and no source URL is included in this file.** Only SHA256 fingerprints,
> answer characters and internal row ids are listed, so the provenance chain stays
> auditable without redistributing the original material.

## Why

During collection on 2026-11-05, all 31 of these records were tagged in
`source_ref.license_note` as *web UGC reposts, no clear authorisation, local /
restricted research use only*. A public GitHub repository is not a restricted
environment, so these records are withheld from CCRP DataSet v0.1.

## What was withheld with them

| Item | Count | Note |
|---|---|---|
| Web UGC clue texts | 31 | covering 14 answer characters: 不 之 事 他 到 后 在 她 己 所 把 然 的 第 |
| Page URLs in the research site | 58 (27 distinct) | not copied; the site is not part of v0.1 |
| Site-provided explanations | 27 | a subset of the withheld clues |
| LLM explanations keyed to withheld clues | 4 | removed from `explanations-llm.jsonl` |
| Game-bank items | 28 | the offline game is not part of v0.1 |
| Prompt-snapshot references | 87 domain hits | `03_prompt/` stays local; `input_snapshot_sha256` is retained in `provenance-generated.jsonl` |

The 600 model-authored riddles, 597 quality-controlled items, both blind-test
conditions and the ICL probe were checked to contain **zero** withheld clue text
and **zero** non-CC URLs. Their `input_snapshot_sha256` values are retained, so a
reader can verify that the published artifacts match the generation-time inputs
without needing access to the withheld text.

## Fingerprint list

| # | answer char | rid | question_sha256 |
|---|---|---|---|
| 1 | 不 | `0eb2b85a7088` | `409d1e6a5cdbd64b57132bfec17472a80336d402509bc1e95ebd5a495d193cc4` |
| 2 | 不 | `1871a135368c` | `7de3cc2dcf0a8f2226f8d4a2b91bcd3a24b4017471f590641d06ab54a9c69718` |
| 3 | 不 | `2abddafabf4a` | `35da687a81f4634cd50ab6706b59663c0b924814e7a84b68253467806c23f3aa` |
| 4 | 不 | `a13a06335e33` | `d8f2bc6bfa51b2f35f23b669d7edafc776783cedf3531e36b2aaac54f17bd4c7` |
| 5 | 不 | `debd5a2a2b0e` | `70c1e03c3c36e8ca1e6dda423b2c9c6bc9ed87f6e7721a2a8dd0a95e30467916` |
| 6 | 之 | `a2fdbc3e0644` | `8afa778d99e030fd7dd02608b43ebc58aafe10012730c97f5bb328f3d447cede` |
| 7 | 事 | `629945b94973` | `0cfca2a5c66168230921e37ff9db0abfbd78f44dd655f241b18f276b1c06a73c` |
| 8 | 他 | `8e2f2c1ca51a` | `c84f9cab19df5fd3c5cacced006a73529e747313f306b56df76c85c5f360e7c7` |
| 9 | 他 | `a3bdc8efcff6` | `d96bcd177d48d84dbe9716b69e051c6d80de8eab7750c05f1a181a4367f0ad5e` |
| 10 | 到 | `469345b8015b` | `2d2227c483fffbce4a7e8d19a4f71393aabf33e42c1da10db0beaac70f3ce201` |
| 11 | 后 | `388365651e4c` | `07be7286516f9a3dcfda8ab51461ee9a0ad60f28d31a87fa0ade5286cbf5819d` |
| 12 | 后 | `3d7dfa087feb` | `7e93a0bca4226e318e3b839c0867ca14428ea07304fee769dafa910d8d168b87` |
| 13 | 在 | `61191fc3163e` | `695e00bf7e0e559103a7bb426b2290fde9466b21f6e6707cd674d21d9dbae1ae` |
| 14 | 在 | `d4faa332c3cd` | `7a69b234b5abe46fd31834fbf79086186dda38d377e84c7e2129b465eb57c37d` |
| 15 | 她 | `34b8af906595` | `adc441cb0bd39437edd36c901f8e095f34fd9defc2d8d4cb6eeba0bb1a2aeb86` |
| 16 | 她 | `e28a3d1d0089` | `fd8bbd5b0822a4a93135a69b4a1ada41152ef3001030d91ba85683f7c6feeb76` |
| 17 | 己 | `8142da1e3d50` | `533d46d9543715edebc3f5b5f1c209073cfb96a9fb41c7f525b2ca4022ce37fd` |
| 18 | 己 | `a248d0de1cd4` | `2ede53da3001c237048fc7745032cff4d9e69500f721515d6d171b6544575165` |
| 19 | 所 | `47607c175dc7` | `07fb81f4407a4b3efacd352a7c64472670c2ce067450621fa6540eda9c3c1d28` |
| 20 | 所 | `ac40ab5d9bb9` | `d763aaaf35d9d4f78d04244b0251818242c731e47bec5d2ac25d15f14544cddb` |
| 21 | 把 | `198ee8d60482` | `89393d7ebb764c0fdc8915169a362479b699c1c611c5a21a16894c3fed53b9dd` |
| 22 | 把 | `52b2ac53ca2c` | `14226af04d5d23f5e9b0565333b358fd8a294e45ee5abfef67d47952bc9c8f16` |
| 23 | 然 | `2e62ad980c24` | `50ee0c5dfc2a845823882ec1b47ab4440e99922dcc20c6a25f7326d535d196c6` |
| 24 | 然 | `de1b641bbcc2` | `f410c2a4bd934b1009ef4acf02e4de87ba51a84c552c0a64079bbc930fb7606b` |
| 25 | 的 | `46a0858c4a6b` | `a7be5cfbbdc9fcc376a68124b949da202a210a16a9785156e051024ca77b7e35` |
| 26 | 的 | `582194f71611` | `b853b00f6113b1f99aacb1b0c1387698a7f18387f5a3fda3b6de5266841bd75c` |
| 27 | 的 | `7dbd5c45fc76` | `4df9058f8477aa7dfd028ede5004f4f50573a87a4eca9ea95c91237875372b82` |
| 28 | 的 | `83b7c4466829` | `7f2097e41da8e8ab296308a10f715638b78e2a85ac7f0d7f3b996c05373bee39` |
| 29 | 第 | `1261a20be70e` | `3cf200fbaa06323dd8ecc018f8db70dd6f951149db753e17300df22ef3d6751d` |
| 30 | 第 | `cfdea0af9684` | `060db477fdf9b0c7398f9a041800632911be196a4a3215e629849c774c79424e` |
| 31 | 第 | `f8f926e7c3b5` | `6941813226ae3f387678d9b6fa8e26dd17e9cdf31714b721df9db63496095513` |

Requests regarding these records: please open an issue in this repository.

See also `THIRD_PARTY.md` for the CC-Riddle attribution and modification notice.
