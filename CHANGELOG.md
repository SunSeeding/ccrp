# Changelog / 更新记录

## 2026-11-10（后续修订）— 两篇论文署名统一（main 文档增补，**未打 tag**）

- 按发布方要求，把 Paper 2 中文原文 PDF 首页与英文全译的署名统一为 **春芽数源 / Spring Buds Data Source Inc.（机构署名）**，与数据集、Paper 1 一致；中文原文最初以课题组名义流传，此次仅改首页作者行。
- `paper/gmn-paper-zh.pdf`：仅首页作者行修订，正文与其余 10 页逐字未改；`paper/gmn-paper-en.md` / `.html` / `.pdf`：署名行与文末 *Editorial notes* 同步，正文数字、表格、公式、参考文献与结论零改动。
- `paper/README.md`、中英 `README*`、`CITATION.cff`、`LICENSE-DOCS`、`THIRD_PARTY.md`、`docs/DATASHEET.md` 与站点公开版说明中的「另一课题组 / 不同作者」表述全部改为统一机构署名。**许可口径不变**：中文原文只标数据集许可、未声明论文文本许可，仓库不代为补充授权，Paper 2 仍不适用 `LICENSE-DOCS`。
- 数据集内容、实验数字、Paper 1 六个产物、已发布 tag / Release 附件、Zenodo 归档与 DOI 均未改动。

## 2026-11-10 — 新增第二篇配套论文（main 文档增补，**未打 tag**）

**数据集内容版本仍为 `0.1`；本次只增补 `paper/` 与文档层，数据、实验数字、已发布 tag / Release 附件、Zenodo 归档与 DOI 全部零改动。**

- **新增论文 2**：《盲人摸字：通过汉字字谜探查大模型的一维符号代数与二维空间失明》/ *Blind Men Touching Characters: Probing Symbolic Algebra vs. 2D Spatial Perception in LLMs via Chinese Character Riddles*，机构署名「春芽数源 / Spring Buds Data Source Inc.」（**与数据集、Paper 1 一致**），中文原文 2026-11-06。
  - `paper/gmn-paper-zh.pdf`：中文原文 PDF（11 页）；2026-11-10 修订首页署名，正文与其余 10 页零改动。
  - `paper/gmn-paper-en.md` / `.html` / `.pdf`：**英文全译**，9,802 词 / 9 张表 / 式 (1)–(7) / 17 条参考文献 / 19 页 A4；由工作区本地排版脚本从同一份 Markdown 生成（脚本未随包发布，与 Paper 1 一致；复用 `build_paper.py` 的 CSS 与渲染器，只读；`build_paper.py` 与 Paper 1 的六个产物字节级不变）。
- 新增 `paper/README.md` 论文索引：两篇论文的作者、语言版本、许可状态与口径差异。中英 `README*`、`LICENSE-DOCS`、`THIRD_PARTY.md`、`docs/DATASHEET.md`、`CITATION.cff`（`preferred-citation` 仍指向 Paper 1，新增 `references` 列 Paper 2）、导出器 `COPY_FILES` 与自检器必需文档清单同步。
- **许可例外**：中文原文只标注了数据集许可 CC BY-NC-SA 4.0，未声明论文本身许可，仓库不代为补充授权；因此 `paper/gmn-paper-zh.pdf` 与 `gmn-paper-en.*` **不适用仓库的 `paper/` CC BY 4.0**，两版仅供对照阅读与学术引用，再利用需发布方许可。`LICENSE-DOCS` 适用范围为本项目文档 + Paper 1。
- **翻译口径**：中文谜面例证保留汉字并附英文释义；所有数值、*p* 值、GID、模型代号照抄，不重算不修正；参考文献按中文原版照录（其中若干条为泛化团体署名或 2026 年 arXiv 编号，未核实、未补造 URL / DOI）；论文中 1,050 / 1,023 为构建期口径，公开包为 1,019，差异只在英文全译末尾 *Editorial notes* 与 Paper 1 §3.4 说明，**不改正文数字**。
- **合规扫描**：两个版本均不含 31 条下架网络 UGC 谜面文本、网页 URL、本机绝对路径与明文凭据；`build_release.py` 的泄露扫描与 `verify_release.py` 自检均 PASS，`manifest.json` 已重算。
- **未做的事**：未打 `v0.1.2` tag、未发新 Release、未替换任何已发布附件、未重传 Zenodo 文件、未改动版本 DOI `10.5281/zenodo.24077793`。该 DOI 仍固定指向 `CCRP-DataSet-v0.1.1.zip`（3,035,750 B / MD5 `8f367d19cc2560cfbe13f2ab1c80cb05`）；本次新增只存在于 `main` 分支与在线站点的分发副本。

## v0.1.1 — 2026-11-09（文档补丁 / documentation patch）

**数据集内容与 v0.1.0 完全一致**：所有 `data/` 文件、论文、脚本、实验数字零改动。数据集版本号仍为 **0.1**；`v0.1.1` 只是本仓库的补丁发布号（tag / GitHub Release），符合「已发布版本不改写、修复走新版本」的语义化版本惯例。

- 中英 README 首屏把「仓库」与「在线站点」两个裸 URL 从同一行拆为各自独立一行，改用 GFM 尖括号显式链接 `<https://…>`。此前渲染器会因全角空格 + `｜` 把两者粘连成一个超链；**URL 本身从未写错**。
- 清理 Roadmap 中 4 条本版本已完成却仍列为「计划」的条目；ZENODO 指引补充「多个 Release 时以最新补丁版归档」的说明。
- 与 `v0.1.0` 相比，仅 `README.md` / `README.en.md` / `CHANGELOG.md` / `docs/ZENODO.md` / `CITATION.cff` / `manifest.json` 发生变化，其余文件逐字节相同；完整性可用包内 `scripts/verify_release.py` 与 `manifest.json` 复算。
- **（16:35 main 后续修订，未打新 tag）Zenodo 元数据与归档指引校正**：核实 Zenodo 新版（InvenioRDM）后，`.zenodo.json` 的 `license` 改为词汇表 id `cc-by-nc-sa-4.0`、关系标识改为 `isderivedfrom` / `issupplementto`；`docs/ZENODO.md` 重写为新版流程（Sync now 不归档、启用前的 Release 不回溯、自动集成立即发布无草稿），并补表单速查表。仅文档与元数据，数据 / 论文 / 脚本零改动；`v0.1.1` tag 与 Release 附件仍是发布时快照。
- **（v0.1.1 发布后 main 后续修订，未打新 tag）Zenodo 归档完成与 DOI 回填**：手动上传 `CCRP-DataSet-v0.1.1.zip` 为 **Dataset** 记录，`status=published`；版本 DOI **`10.5281/zenodo.24077793`**，概念 DOI `10.5281/zenodo.24077792`。`CITATION.cff`、中英 README 首屏与引用段、本文件、`docs/ZENODO.md`、`docs/DATASHEET.md` 与 GitHub `v0.1.0` / `v0.1.1` Release 正文已回填；`.zenodo.json` **故意不写 `doi` 字段**（GitHub 自动集成会读该文件，写入已存在的 DOI 会与新归档冲突）。归档包与 `v0.1.1` Release 附件逐字节相同（3,035,750 B / MD5 `8f367d19cc2560cfbe13f2ab1c80cb05`），**未改写已发布 tag、未替换 Release 附件**；数据 / 论文 / 脚本零改动，仅文档与 `manifest.json` 变化。

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

## v0.1.0 发布当日修订（数据内容不变）

公开后体检发现两处会误导读者的问题，已修正，数据内容与全部实验数字**未改动**：

- **GitHub 侧栏误标 MIT**：根目录 `LICENSE` 原为 MIT 全文，被 GitHub 自动识别为整个仓库的许可。现改为仓库级多许可总览（主体 CC BY-NC-SA 4.0），MIT 全文移至 `scripts/LICENSE`；`THIRD_PARTY.md` / `LICENSE-DATA` / `LICENSE-DOCS` 与中英 README 的引用已同步。
- **`data/summary.json` 的 `scope` 字段**仍写「本地/受限访问，不对外发布」。导出器现在于导出时把该字段重写为公开发布口径，并附 `release_scope_note`；**本地研究用的 `04_generated/summary.json` 一条未改**。
- `scripts/verify_release.py` 的必需文档清单补入 `scripts/LICENSE`。
- **（15:30 补充）明确显示 CC BY-NC-SA 4.0**：查证 GitHub 的 licensee 识别库（choosealicense，47 个许可）**不含 CC-BY-NC-SA-4.0**，侧栏标签在平台上无法获得；因此**不**用错误许可文本换取标签。根 `LICENSE` 改为「多许可总览 + CC 官方 `legalcode.txt` 全文（原文未改动）」，中英 README 首页顶部加醒目许可横幅并解释侧栏 `Other` 的成因；目录树与许可地图的说明同步。
- **（15:40 补充）英文论文 HTML/PDF**：`paper/build_paper.py` 增加 `--lang en`，中文默认输出经 SHA256 验证**字节级不变**；新增 `riddle-paper-en.html`（14 节 / 21 表 / 4 图）与 `riddle-paper-en.pdf`，中文排版 HTML 也一并纳入发布包。中英 README 目录树与引用说明同步。
- **（15:45 补充）站点合规公开版 + 论文联动**：论文中英两版 §7 与附录 A 的「站点不对外发布」改为「合规公开版发布于 GitHub Pages」；重生成中英 HTML/PDF、重跑 `verify_paper.py`（PASS）、重跑 `publish_site.py`、同步重生成「一图看懂」长图。新增 `build_pages.py` 导出 gh-pages 分支内容：下架 31 条 UGC 谜面文本 / 26 处网页 URL / 28 条游戏题，`data.json` 参考集 1,019 条、题库 1,541 条，残留扫描 0。本地研究树一条未删。
- **（15:50 补充）Zenodo 归档准备**：新增 `.zenodo.json`（机构署名、CC-BY-NC-SA-4.0、上游关联标识、关键词）与 `docs/ZENODO.md`（归档与 DOI 回填步骤）。**当时 DOI 尚未产生，未编造**；`CITATION.cff` 与中英 README 预留了回填位置（**该条为发布当日 15:50 的历史状态；归档已于当日完成，见上方 v0.1.1 节**）。
- **（15:50 补充）v0.1.0 tag 与 GitHub Release**：整包 zip + 中英 PDF 作为附件；Release 与 About 描述、topics、Pages 通过 GitHub API 设置。
- **（16:05 补充）README 首屏链接拆分**：此修复已作为 **v0.1.1 补丁**正式发布，详见本文件顶部 v0.1.1 节。

## 计划 / Roadmap (v0.2+)

- 重建 1,000 条按谜底字分层、SHA256 冻结的 test 集；补人工谜面质量与谜底唯一性评审。
- 一图看懂长图与站点界面的英文化。
