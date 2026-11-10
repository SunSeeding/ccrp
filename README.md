# 汉字字谜探针数据集 · CCRP DataSet v0.1

**Chinese Character Riddle Probes Dataset** ｜ 简称 **CCRP DataSet** ｜ 版本 **0.1**（2026-11-09）
发布机构：**春芽数源 / Spring Buds Data Source Inc.**

仓库：<https://github.com/SunSeeding/ccrp>

在线站点：<https://sunseeding.github.io/ccrp/>

Zenodo 归档 DOI：<https://doi.org/10.5281/zenodo.24077793>

> **数据许可：`data/` 为 CC BY-NC-SA 4.0（非商业 · 署名 · 相同方式共享）**；`scripts/` 为 MIT，本项目文档与 `paper/` 中的 Paper 1 为 CC BY 4.0（**Paper 2 例外，见 `paper/README.md`**）。GitHub 侧栏显示 `Other`，是因平台识别库不含 CC-BY-NC-SA-4.0（仅有 CC-BY-4.0 / CC-BY-SA-4.0 / CC0-1.0），**不代表数据可商用、属 MIT 或公有领域**。以根 `LICENSE`（含 CC 官方完整法律文本）与 §4 许可地图为准。

> 面向「汉字字谜作为大语言模型**行为层结构探针**」的研究数据集：100 个高频简化汉字、参考谜面与结构卡、模型创作谜面、生成–求解闭环、2×2 全因子分解与 ICL 控制任务的全部逐题记录。

> ⚠️ **本数据集不是排行榜基准。** 配套论文已裁定：现有公开 100 题切片不具排名效度（仅 11 个谜底字、85/100 来自公开 train/valid、15 题全部答「旦」、四家推理预算不对等）。所有数值仅用于**同一批题、同一判分器下不同条件之间的配对比较**，不得用于跨模型能力排名。详见 `paper/riddle-paper.md` §6.2 与 §6.5。

---

## 1. 一句话概览

| 项目 | 数量 | 说明 |
|---|---|---|
| 目标汉字 | 100 | 现代汉语高频简化字，按频率序 |
| 参考谜面（发布） | 1,019 | 全部来自 CC-Riddle 人工谜面，按谜底字重排并补结构卡 |
| 参考谜面（下架） | 31 | 网络 UGC，采集时标注「仅本地/受限研究使用」，见 `data/WITHHELD.md` |
| 模型创作谜面 | 600 | kimi 300 / u2 300；拆形 200 / 会意 200 / 谐音 200 |
| 质检通过 | 597 | 交叉盲测与同题自测共用这 597 题 |
| 闭环答题记录 | 1,194 | 交叉盲测 597 + 同题自测 597，逐题配对 |
| ICL 控制任务 | 192 次 | 24 题 × 4 条件 × 2 模型，冻结种子 `20261106` |
| 配套论文 | **2 篇** | Paper 1 中英双版；Paper 2 中文原文 + 英文全译；索引见 `paper/README.md` |

**两篇独立论文**（2026-11-10 新增第二篇）：①《汉字字谜能否成为大语言模型的结构探针？》（本机构署名，裁定「字谜作为探针」的有效性）；②《盲人摸字：通过汉字字谜探查大模型的一维符号代数与二维空间失明》（同为春芽数源 / Spring Buds Data Source Inc. 机构署名，英文全译 `paper/gmn-paper-en.md`）。两者基于同一批 597 题闭环，问题与结论互不替代；数据集内容、实验数字、已发布的 tag / Release / Zenodo 归档均未改动。

**核心结论**（引用请照抄，勿重新估算）：交叉盲测 39.03%（233/597）→ 同题自测 44.22%（264/597），逐题配对 McNemar 精确 *p*=0.0144；2×2 全因子分解给出猜题能力差 *β*=+16.26 pp、题源难度差 *α*=+11.36 pp、自我熟悉净效应 *γ*=+5.22 pp。按制谜方分层看到的方向相反（+21.48 pp / −11.04 pp）是 *β* 翻转符号所致，不是「只有一个模型有自我偏好」。

---

## 2. 快速开始

```bash
# 校验发布包完整性（Python 3 标准库，零依赖，不联网）
python scripts/verify_release.py .

# 读取参考谜面
python -c "import json;print(next(json.loads(l) for l in open('data/reference-slice.jsonl',encoding='utf-8')))"

# 复算配对 McNemar 所需的四格数
python -c "import json,collections;print(collections.Counter((r['correct'] for r in map(json.loads,open('data/blind.jsonl',encoding='utf-8')))))"
```

字段字典见 [`data/README.md`](data/README.md)，数据卡片见 [`docs/DATASHEET.md`](docs/DATASHEET.md)，全文件哈希见 `manifest.json`，采集与下架说明见 [`data/WITHHELD.md`](data/WITHHELD.md)。

**判分口径**：答案去空白后与单一汉字**精确匹配**；`correct` 异常记 0（分母不变），另留 `format_bad / error / timed_out` 标记。整合数据里 `split` 统一为 `test`，原公开集划分保留在 `source_split`，**不可删除**（公开集记忆污染诊断的关键协变量）。

---

## 3. 目录结构

```
.
├── README.md / README.en.md        中英说明（本文件与英文版）
├── CHANGELOG.md                    v0.1 变更与已知限制
├── CITATION.cff                    引用格式
├── THIRD_PARTY.md                  上游署名、修改声明、下架说明
├── LICENSE                         CC BY-NC-SA 4.0 官方全文 + 多许可总览
├── LICENSE-DATA                    CC BY-NC-SA 4.0（data/）
├── LICENSE-DOCS                    CC BY 4.0（本项目文档 + Paper 1；Paper 2 例外）
├── manifest.json                   全文件字节数 + SHA256 + 行数口径
├── data/                           数据集本体（CC BY-NC-SA 4.0）
│   ├── README.md                   字段字典
│   ├── WITHHELD.md                 31 条下架记录的指纹清单
│   ├── hanzi_index-top100.csv      100 字表与结构卡
│   ├── pipeline_meta.json          prompt_version 等项目版本真源
│   ├── reference-slice.jsonl       1,019 条参考谜面
│   ├── explanations-llm.jsonl      对应的 LLM 解释
│   ├── provenance-reference.jsonl  参考谜面逐条溯源
│   ├── generated-*.jsonl           600 条模型创作
│   ├── quality.jsonl               600 条质检判定
│   ├── blind*.jsonl                交叉盲测 / 同题自测
│   ├── provenance-generated.jsonl  创作题溯源（含 input_snapshot_sha256）
│   ├── selftest-*.json*            配对统计、2×2 分解、对话指纹
│   ├── icl-probe-*                 ICL 冻结题集 / 示例 / 192 次调用 / 分析
│   └── summary.json                流水线汇总与限制声明
├── paper/                          两篇配套论文（许可见 paper/README.md）
│   ├── README.md                   论文索引：两篇论文的署名、语言版本与许可
│   ├── riddle-paper.md             Paper 1 中文原稿（CC BY 4.0）
│   ├── riddle-paper.html           Paper 1 中文排版 HTML（4 幅示意图）
│   ├── riddle-paper.pdf            Paper 1 中文 PDF
│   ├── riddle-paper-en.md          Paper 1 英文全译
│   ├── riddle-paper-en.html        Paper 1 英文排版 HTML
│   ├── riddle-paper-en.pdf         Paper 1 英文 PDF
│   ├── gmn-paper-zh.pdf            Paper 2 中文原文 PDF（机构署名，未声明论文许可）
│   ├── gmn-paper-en.md             Paper 2 英文全译（9,802 词 / 9 表 / 式 1–7）
│   ├── gmn-paper-en.html           Paper 2 英文排版 HTML
│   └── gmn-paper-en.pdf            Paper 2 英文 PDF（19 页 A4）
├── docs/DATASHEET.md               数据卡片
└── scripts/                        MIT
    ├── build_release.py             从本地研究树导出本发布包
    └── verify_release.py            独立完整性自检
```

---

## 4. 许可地图（分层，按目录生效）

| 路径 | 许可 | 说明 |
|---|---|---|
| `data/` | **CC BY-NC-SA 4.0** | 含 CC-Riddle 派生内容；再分发须同许可 + 署名 + 标修改 |
| `scripts/` | **MIT** | 我们原创的工具代码（全文见 `scripts/LICENSE`） |
| `docs/`、`README*.md`、`THIRD_PARTY.md`、`CHANGELOG.md`、`paper/README.md`、`paper/riddle-paper*` | **CC BY 4.0** | 本项目自有文档与 Paper 1；论文只短引谜面作例证 |
| `paper/gmn-paper-zh.pdf`、`paper/gmn-paper-en.*` | **未声明论文文本许可** | Paper 2 与 Paper 1 同为春芽数源机构署名；中文原文只标了数据集许可、未标论文许可，仓库不代为补充授权；两版仅供对照阅读与学术引用，再利用请先取得发布方许可 |
| 第三方材料 | 见 `THIRD_PARTY.md` | 上游署名与 31 条下架记录 |

- **发布本身不违反 NC**：CC BY-NC-SA 4.0 §1 把「非主要为商业利益或金钱报酬」定义为 NonCommercial，并明确无偿数字文件共享属 NonCommercial；NC 约束的是**下游商业使用**。
- **SA 的边界**：§4(b) 规定把源库全部或实质部分纳入自有数据库时，**该库本身（but not its individual contents）**构成 Adapted Material。因此含 1,019 条 CC-Riddle 谜面的 `data/` 按 BY-NC-SA 发布；原创代码与文档不自动被传染，可分层许可。
- **CC BY-NC-SA 4.0 不是 OSI 认证的开源许可**。请称「按 CC BY-NC-SA 4.0 公开发布」，不要称「开源数据集」。
- **GitHub 侧栏的 `Other` 不是许可判断**：其识别库（choosealicense，47 个许可）不含 CC-BY-NC-SA-4.0，平台无法给出该标签；根 `LICENSE` 已附 CC 官方完整法律文本。**不要为了换取侧栏标签而替换成别的许可文本**。实际适用一律以本表为准。

---

## 5. 溯源规则与方案 C 下架

| 谜面来源 | 给出的出处 |
|---|---|
| CC-Riddle | 论文 arXiv:2206.13778 + 上游仓库 + 行 id + 源文件 SHA256 + 许可（上游数据集**没有逐条 URL**） |
| 网络页面 | 原网页 URL / 标题 / 抓取时间 / 片段哈希 —— **v0.1 全部下架** |
| 模型生成 | `no_url`，只记模型 / prompt 版本 / 时间戳 / 输入快照哈希 |

**绝不伪造 URL**。参考谜面来自 CC-Riddle 时给论文链接而非逐条网页链接；模型生成的解释与创作谜面没有出处链接。

v0.1 采用**方案 C：导出时下架，本地研究与既有产物一条不改**。31 条网络 UGC 在采集时全部带有「未取得明确授权；仅本地/受限研究使用」标记，公开仓库不是受限环境，因此不随包发布；与之绑定的 27 条站点解析、4 条 LLM 解释、58 处网页 URL、28 条游戏题、87 处 prompt 快照域名痕迹一并留在本地。发布包改保留 `question_sha256`、`input_snapshot_sha256` 与条数口径，使溯源在**指纹层面**仍然闭合（论文判据 C6）。离线站点 / 小游戏 / 原始抓取 / API 流水线不在 v0.1 范围内。

---

## 6. 引用

```bibtex
@dataset{ccrp2026,
  title  = {Chinese Character Riddle Probes Dataset (CCRP DataSet)},
  author = {{Spring Buds Data Source Inc.}},
  year   = {2026},
  doi    = {10.5281/zenodo.24077793},
  note   = {Version 0.1. Upstream corpus: CC-Riddle, arXiv:2206.13778,
            licensed CC BY-NC-SA 4.0. Selected, reorganized and augmented.},
  url    = {https://doi.org/10.5281/zenodo.24077793}
}
```

上游必署：Fan Xu, Yunxiang Zhang, Xiaojun Wan（北京大学王选计算机研究所文本挖掘与语言计算组），*CC-Riddle: A Question Answering Dataset of Chinese Character Riddles*, arXiv:2206.13778，CC BY-NC-SA 4.0。**本数据集对其做了选取、重排与补充说明**，完整署名与修改声明见 `THIRD_PARTY.md`（§3(a) 要求，再分发请保留）。

**引用第二篇论文**：*Blind Men Touching Characters: Probing Symbolic Algebra vs. 2D Spatial Perception in LLMs via Chinese Character Riddles*（中文原题《盲人摸字……》），作者「春芽数源 / Spring Buds Data Source Inc.」（机构署名），中文原文 2026-11-06、英文全译 2026-11-10。它与 Paper 1 是**两篇独立论文**，`CITATION.cff` 的 `preferred-citation` 仍指向数据集的 Paper 1，`references` 另列 Paper 2；两篇作者相同，但引用时请勿把两篇的结论互相替换。

机器可读引用见 `CITATION.cff`。**长期归档已完成**：版本 DOI [`10.5281/zenodo.24077793`](https://doi.org/10.5281/zenodo.24077793) 固定指向本次 v0.1 归档；概念 DOI [`10.5281/zenodo.24077792`](https://doi.org/10.5281/zenodo.24077792) 指向该记录的所有版本。**引用具体版本请用版本 DOI**。

归档对象为 `CCRP-DataSet-v0.1.1.zip`（MD5 `8f367d19cc2560cfbe13f2ab1c80cb05`，与 GitHub `v0.1.1` Release 附件逐字节相同）；GitHub 仓库与在线站点是同一版本的分发副本。逐文件 SHA256 见 `manifest.json`，归档步骤与记录元数据核对见 `docs/ZENODO.md`。

---

## 7. 已知限制（对外使用必读）

1. **解释不是权威字理**：1,023 条解释是在「给定谜面 + 谜底」条件下生成的**事后合理化**，58.9% 被模型自评 `low`；自动手法分类也明显偏向会意（594:427:2）。不宜直接当 CoT 监督信号。
2. **质量闸门未经人工验证**：原创性 3-gram Jaccard 阈值 0.35 由 60 条试点分位数标定；谜面质量、谜底唯一性均**未做人工评审**。
3. **ICL 只是方向性信号**：n=24/格，所有 McNemar *p* ≥ 0.125，不构成训练有效性结论。
4. **无训练实验**：论文与数据均为 API 调用层面的零权重修改实验；关于「训练该补什么」的全部表述均为可证伪假设 H1–H3。
5. **模型覆盖有限**：闭环实验仅两个中文商用 API；hy4 / deepseek-v4-pro 因额度耗尽未参与；无开源权重模型、无人类基线、无重复采样。
6. **字义字段不补**：项目决定不引入第三方字典释义，语义类手法受此约束。

完整限制清单见 `paper/riddle-paper.md` §7 与 `docs/DATASHEET.md`。

---

本文件与 `README.en.md` 按 CC BY 4.0 发布。第三方材料与许可细节见 `THIRD_PARTY.md`；该文件不是法律意见。
