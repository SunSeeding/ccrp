# Changelog / 更新记录

## v0.1 — 2026-11-09

首次公开发布（First public release）。

**包含 / Included**

- 100 个高频简化汉字的字表与结构卡（pinyin / 笔画 / 部首 / IDS / 频率序）。
- 1,019 条 CC-Riddle 派生参考谜面（按谜底字重排、补结构卡与解释、附上游行 id 与源文件 SHA256）。
- 600 条模型创作谜面（kimi / u2 各 300，拆形 / 会意 / 谐音各 200）、600 条质检判定。
- 597 条生成–求解闭环记录：交叉盲测 `cross` 与同题自测 `self`，逐题配对。
- 2×2 全因子分解、分层统计、四格诊断、配对 McNemar 结果。
- ICL 控制任务：24 题 × 4 条件 × 2 模型 = 192 次调用，含冻结题集与示例推理。
- 中英双语论文：中文原稿 `paper/riddle-paper.md`、英文全译 `paper/riddle-paper-en.md`、中文 PDF。
- 分层许可、第三方署名与修改声明、数据卡片、字段字典、SHA256 manifest、独立自检脚本。

**不包含 / Not included**

- 31 条网络 UGC 谜面及与之绑定的 27 条站点解析、4 条 LLM 解释、58 处网页 URL。采集时这些记录自带「未取得明确授权；仅本地/受限研究使用」标记，按方案 C 在导出发布包时下架，指纹清单见 `data/WITHHELD.md`。**本地研究产物一条未删。**
- 离线站点 `05_site/`、小游戏题库（内嵌 28 条下架谜面）、`02_reference/` 原始抓取、`03_prompt/` 构建期快照（含网页域名痕迹）、`game-shots/` 截图、备份目录、日志、API 流水线脚本（依赖运行时凭据）。
- 字义表 `hanzi_index-top100-Explanation.csv`：含第三方字典释义，权利状态未核实，且项目原本就决定不补字义字段。

**已知限制 / Known limitations**

- 现有 100 题公开切片**不具备排名效度**（仅 11 个谜底字、85/100 来自公开 train/valid、15 题全答「旦」、四家推理预算不对等）。本数据集是**诊断型探针，不是排行榜基准**。
- 1,023 条 LLM 解释属给定谜底后的事后合理化，58.9% 被模型自评 `low`；**不是权威字理**。
- 原创性 3-gram Jaccard 阈值 0.35 由 60 条试点分位数标定，未做人工「是否改写」评审；谜面质量与谜底唯一性亦未做人工评审。
- ICL 探针 n=24/格，所有 McNemar *p* ≥ 0.125，仅作方向性信号。
- hy4 / deepseek-v4-pro 因 HTTP 402 未参与闭环实验；本仓库不含任何训练实验。

## v0.1 发布后修订 — 2026-11-09（版本号不变）

公开后体检发现两处会误导读者的问题，已在本版本中修正，数据内容与全部实验数字**未改动**：

- **GitHub 侧栏误标 MIT**：根目录 `LICENSE` 原为 MIT 全文，被 GitHub 自动识别为整个仓库的许可。现改为仓库级多许可总览（主体 CC BY-NC-SA 4.0），MIT 全文移至 `scripts/LICENSE`；`THIRD_PARTY.md` / `LICENSE-DATA` / `LICENSE-DOCS` 与中英 README 的引用已同步。
- **`data/summary.json` 的 `scope` 字段**仍写「本地/受限访问，不对外发布」。导出器现在于导出时把该字段重写为公开发布口径，并附 `release_scope_note`；**本地研究用的 `04_generated/summary.json` 一条未改**。
- `scripts/verify_release.py` 的必需文档清单补入 `scripts/LICENSE`。

## 计划 / Roadmap (v0.2+)

- 重建 1,000 条按谜底字分层、SHA256 冻结的 test 集；补人工谜面质量与谜底唯一性评审。
- 英文论文 HTML/PDF 版、一图看懂长图的英文化。
- 站点 / 小游戏的合规公开版（需先完成谜面过滤与重渲染）。
- Zenodo 归档 DOI 与正式 Release tag。
