# 配套论文索引 / Companion papers

> **CCRP DataSet v0.1 现有两篇独立论文，均由春芽数源 / Spring Buds Data Source Inc. 机构署名。** 它们基于同一批 597 题生成–求解闭环，但研究问题与结论互不替代。2026-11-10 新增第二篇，并于同日把中英两版署名统一为数据集机构署名；数据集内容、实验数字、已发布 tag/Release 附件与 Zenodo 归档均未改动。

| # | 论文 | 作者署名 | 语言版本 | 核心问题 |
|---|---|---|---|---|
| 1 | 《汉字字谜能否成为大语言模型的结构探针？》 / *Can Chinese Character Riddles Serve as Structural Probes for Large Language Models?* | 春芽数源 / Spring Buds Data Source Inc.（机构署名，与数据集一致） | 中文原稿 + 英文全译，各 md / HTML / PDF | 六条判据 C1–C6 → 三套探针 → 逐条裁定；结论为「有条件的肯定」：诊断型探针＝能、排名型基准＝不能、训练信号探针＝尚不能判定 |
| 2 | 《盲人摸字：通过汉字字谜探查大模型的一维符号代数与二维空间失明》 / *Blind Men Touching Characters: Probing Symbolic Algebra vs. 2D Spatial Perception in LLMs via Chinese Character Riddles* | 春芽数源 / Spring Buds Data Source Inc.（机构署名，与数据集、Paper 1 一致） | 中文原文 PDF + 英文全译 md / HTML / PDF | 一维符号代数 vs. 二维空间失明、2×2 私有拆字先验、CoT 退化与 RiddlePlay / RLVR 训练框架 |

## 文件清单

**Paper 1 — `riddle-paper*`**（CC BY 4.0）

| 文件 | 说明 |
|---|---|
| `riddle-paper.md` / `.html` / `.pdf` | 中文原稿（HTML 含 4 幅示意图） |
| `riddle-paper-en.md` / `.html` / `.pdf` | 英文全译 |

**Paper 2 — `gmn-paper*`**（权利状态见下节）

| 文件 | 说明 |
|---|---|
| `gmn-paper-zh.pdf` | 中文原文（11 页 PDF）；仅首页作者行于 2026-11-10 改为机构署名，正文与其余 10 页零改动 |
| `gmn-paper-en.md` | 英文全译：7 节 + 摘要 + 参考文献 + 编者注，9 张表、式 (1)–(7)、17 条参考文献，9,802 词 |
| `gmn-paper-en.html` / `.pdf` | 由英文全译排版生成（19 页 A4）；排版脚本是工作区本地工具，未随包发布（与 Paper 1 的 `build_paper.py` 口径一致） |

## 许可与署名（重要）

- `LICENSE-DOCS` 的 **CC BY 4.0 只适用于 Paper 1 与本项目自有文档**。
- **Paper 2 的中文原文未声明论文本身的许可**（首页只标注数据集许可 CC BY-NC-SA 4.0），仓库不代为补充授权。2026-11-10 按发布方要求，把中英两版首页署名统一为机构署名「春芽数源 / Spring Buds Data Source Inc.」，**仅改署名，正文、表格、公式、数字与结论零改动**。两版在此**仅供对照阅读与学术引用**；超出阅读范围的再利用请取得发布方许可。
- 英译忠实原则：所有中文谜面例证保留汉字并附英文释义；所有数值、*p* 值、样本量、GID、模型代号照抄，**不重算、不修正**；参考文献按中文原版照录（其中若干条使用泛化团体署名或 2026 年 arXiv 编号，译者未核实、未补造 URL 或 DOI，引用前请自行核对）。
- 两版均已通过方案 C 合规扫描：**不含 31 条下架网络 UGC 谜面文本、不含任何网页 URL、不含本机绝对路径、不含明文凭据**。
- 中文原版中的 1,050 / 1,050 / 1,023 是**构建期（本地研究树）口径**；公开包按方案 C 下架 31 条后为 1,019 / 1,019。英译**未改动原文任何数字**，差异说明见英文全译末尾的 *Editorial notes* 与 Paper 1 §3.4。
- 本次新增只落在 `main` 分支的文档层：**未打新 tag、未发 v0.1.2 Release、未替换任何已发布附件、未重传 Zenodo 文件、未改动 DOI**。版本 DOI `10.5281/zenodo.24077793` 仍固定指向 v0.1.1 归档快照。
