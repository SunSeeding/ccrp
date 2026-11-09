# 数据文件与字段字典 / Data files and field dictionary

UTF-8 / LF。所有 `.jsonl` 为**每行一个 JSON 对象**；空行不计入行数。所有百分比、*p* 值与计数均为逐题原始记录的重算结果，不做二次舍入。

> 说明：文件名在本地研究树中与本发布包中略有不同（为消除歧义做了重命名），字段内容与顺序完全未改。对照见 `manifest.json::row_counts`。

---

## 1. 字表与项目元数据

| 文件 | 行数 | 说明 |
|---|---|---|
| `hanzi_index-top100.csv` | 100 + 表头 | 目标字表 |
| `pipeline_meta.json` | — | 项目版本真源 |

`hanzi_index-top100.csv` 字段：`char, unicode, block, tgscc_level, in_gb2312, gb2312_quwei, pinyin, strokes, radical, ids, top100_rank`。
`ids` 为表意文字描述序列；含占位符或不可拆的字**不作为权威字理依据**。`pinyin` 为无声调/带调混合的字典值，不保证统一格式。

`pipeline_meta.json` 关键键：`prompt_version`（当前 `riddle-gen-skill-v0.2-full100`）、`n_chars`、`chars`（100 字，顺序即频率序）、`dataset_url`、`paper`、`paper_url`、`link_rule`。**改提示词模板必须同步升 `prompt_version`**，否则破坏 `skill_sha256` 溯源。

---

## 2. 参考谜面（1,019 条，CC-Riddle 派生）

| 文件 | 行数 | 字段 |
|---|---|---|
| `reference-slice.jsonl` | 1,019 | `rid, char, answer, question, explanation, char_card, source_type, source_ref, split_role, quality` |
| `explanations-llm.jsonl` | 1,019 | `rid, char, question, explanation, technique, confidence, status, generation` |
| `provenance-reference.jsonl` | 1,019 | `rid, char, question, question_sha256, question_source, explanation_source, explanation_ref, char_card_source, prompt_version` |

- `source_type` 在发布包中**恒为 `ccriddle_human`**；`source_ref` 含上游行 id、源文件 SHA256 与许可信息。
- `question_source` 指向 arXiv:2206.13778 与上游仓库，**数据集本身不含逐条 URL**，不得据此伪造链接。
- `explanation` / `explanations-llm.jsonl` 是给定谜面+谜底后生成的**事后解释**，不是权威字理；`confidence='low'` 的占 58.9%。
- 原参考集为 1,050 条（1,019 CC-Riddle + 31 网络 UGC）。31 条按方案 C 下架，指纹见 `WITHHELD.md`；`explanations-llm.jsonl` 中与之关联的 4 条解释同步移除，故 1,023 − 4 = **1,019**。

---

## 3. 模型创作与质检（600 条）

| 文件 | 行数 | 关键字段 |
|---|---|---|
| `generated-kimi.jsonl` / `generated-u2.jsonl` | 300 + 300 | `gid, char, answer, question, reasoning, technique, technique_requested, model, model_label, status, attempt, self_check, generation` |
| `quality.jsonl` | 600 | `gid, char, question, model, verdict, flags, originality, legality, glyph_consistency, thresholds` |
| `provenance-generated.jsonl` | 600 | `gid, char, question, question_sha256, question_source, explanation_source, explanation_ref, quality_verdict, blind_correct` |

`question_source.type = llm_generated`，含 `model / prompt_version / timestamp / input_snapshot_sha256` 并标 `no_url`。`input_snapshot_sha256` 是生成期输入的指纹，**本地研究树中的 31 条下架谜面文本不随包发布，但该指纹仍可校验生成条件**（论文判据 C6）。

`originality` 为 3-gram Jaccard 相似度，`thresholds` 含 0.35 阈值；该阈值由 60 条试点分位数标定，**未经人工验证**。`verdict` 通过者 597 条进入闭环。

---

## 4. 生成–求解闭环（597 × 2 = 1,194 条逐题记录）

| 文件 | 行数 | 说明 |
|---|---|---|
| `blind.jsonl` | 597 | 交叉盲测 `cross`：A 制谜 → B 作答 |
| `blind-self.jsonl` | 597 | 同题自测 `self`：A 制谜 → A 在**隔天全新单轮对话**作答 |
| `selftest-provenance.jsonl` | 597 | 对话指纹与 `no_url` 标记 |
| `selftest-analysis.json` | — | 配对统计、四格、分层、2×2 分解 |
| `summary.json` | — | 流水线汇总、许可、限制声明 |

共同字段：`gid, char, question, maker, guesser, guesser_label, predicted_answer, correct, reasoning, prompt_version, timestamp, elapsed_s, usage, format_bad, error`。
`blind-self.jsonl` 额外有 `mode`（恒 `self`）与 `conversation`（`fresh_single_turn`、`history_messages=0` 等约定字段）。
`selftest-provenance.jsonl` 字段：`gid, char, question, question_sha256, maker, guesser, mode, predicted_answer, prompt_version, timestamp, conversation_sha256, no_url, note`。

**判分**：`predicted_answer` 去空白后与单一汉字精确匹配。异常记 `correct=0`，分母不变，另留 `format_bad / error / timed_out`。`correct` 是 0/1 整数，不是布尔字符串。

`selftest-analysis.json` 顶层键：`experiment, overall, paired, conditional, answer_agreement, by_maker, by_technique, by_maker_x_technique, by_char, factorial_2x2, quality, limitations, n_pairs, n_complete_pairs, generated_at`。

> ⚠️ 口径提醒：`selftest-analysis.json` 与离线站点采用「各率四舍五入到 4 位后再运算」（*β*=0.16255）；论文采用**原始计数之比**（*β*=+16.26 pp）。两者最多差 0.01 pp，不改变任何结论，论文附录 B 已说明。引用请以论文为准。

---

## 5. ICL 控制任务

| 文件 | 行数 | 说明 |
|---|---|---|
| `icl-probe-items.jsonl` | 24 | 冻结题集，字段 `gid, char, question, answer, maker, technique` |
| `icl-probe-examples.json` | — | 4 条示例谜面 × 4 条件的 `assistant.reasoning` 内容 |
| `icl-probe.jsonl` | 192 | 逐次调用记录 |
| `icl-probe-analysis.json` | — | 主表、分层、关键对比、设计元数据 |

`icl-probe.jsonl` 字段：`gid, char, question, answer, condition, k, model, maker, technique, predicted_answer, correct, reasoning, timestamp, elapsed_s, usage, format_bad, error`。

四条件：`zero`（k=0，无示例）/ `answer`（k=4，只给谜面→谜底）/ `program`（k=4，人写可执行拆解步骤）/ `self`（k=4，模型自己的事后解释）。后三者**共用同一批 4 条谜面与答案**，唯一变量是 `assistant.reasoning` 的来源。示例字 {对, 但, 和, 学} 与 24 题测试字严格隔离，种子 `20261106`，题集 SHA256 见 `icl-probe-analysis.json::design`。

`icl-probe-analysis.json` 顶层键：`design, main, by_technique, key_contrasts, program_minus_answer_by_technique, example_reasonings, predictions, zero_vs_selftest_1106, avg_prompt_tokens_by_condition, complete, quality, limitations, generated_at`。

---

## 6. 溯源与完整性

| 文件 | 说明 |
|---|---|
| `WITHHELD.md` | 31 条下架记录的 `rid` / 谜底字 / `question_sha256`，**不含谜面文本与网页 URL** |
| `manifest.json`（仓库根） | 每个文件的字节数与 SHA256、行数口径、下架统计、项目版本 |
| `THIRD_PARTY.md` | 上游署名、修改声明、许可分层 |

```bash
python ../scripts/verify_release.py ..   # 在 data/ 目录下
# 或仓库根
python scripts/verify_release.py .
```

---

字段字典按 CC BY 4.0 发布（文档）；`data/` 下的数据文件按 CC BY-NC-SA 4.0 发布，见 `LICENSE-DATA`。
