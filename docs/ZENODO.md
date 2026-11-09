# Zenodo 归档与 DOI（v0.1）

本文件说明如何为 CCRP DataSet v0.1 取得长期归档 DOI。**DOI 目前尚不存在，仓库中任何位置都没有编造 DOI**；拿到真实 DOI 后再回填 `CITATION.cff` 与 README。

元数据已预置在仓库根目录 `.zenodo.json`；若走 GitHub 集成，Zenodo 只使用该文件（`CITATION.cff` 会被忽略）。本文件按 **Zenodo 新版（InvenioRDM）** 行为编写，2026-11-09 核实。

## 关键事实：启用集成 ≠ 已归档

| 事实 | 依据 / 实测 |
|---|---|
| 仓库打开 `On` 只是**安装 webhook** | 实测 `SunSeeding/ccrp` 的 hook 指向 `zenodo.org/api/hooks/receivers/github/events/`，`active=true`；最近投递只有 1 次 `ping`（202），**无任何 `release` 事件** |
| **Sync now 只刷新仓库列表**，不产生归档 | Zenodo 官方《Enable a repository》：Sync now 是「找到要启用的仓库」这一步 |
| **不会回溯**启用前已发布的 Release | Zenodo 官方 FAQ：「Only the repositories which were enabled before a release was made will be archived automatically」；本仓库 `v0.1.0` / `v0.1.1` 均在启用前发布，因此不会被归档 |
| 自动集成**立即发布记录并分配 DOI，没有草稿可审** | 官方《Archive a release from GitHub》：等 release 处理完即可「click the record DOI」；发布后元数据不可改，只能发新版本 |
| 集成创建的是 **Software 记录**（送往 Software Heritage） | 官方该节标题明确为「create a **Software** record」；`.zenodo.json` 的 `upload_type: dataset` 可能被覆盖 |
| 已发布记录检索 | 实测 Zenodo 精确标题检索返回 0 条，配合 webhook 只有 ping，确认尚无归档记录 |

Zenodo 官方对「启用集成前的旧 Release」给出的办法是：**下载该 Release 的 ZIP，通过网页手动上传为常规记录**。

## 推荐路径：手动上传 `v0.1.1` 整包

理由：不制造内容零变化的新版本号；能选 **Dataset**（而非 Software）资源类型；能先 **Save draft** 逐项核对再 Publish，避免不可撤回的元数据错误。

1. 登录 <https://zenodo.org> → `+` → **New upload**。
2. 上传 `CCRP-DataSet-v0.1.1.zip`（文件位置：工作区根目录，也是 GitHub `v0.1.1` Release 的首个附件；43 文件 / 2.90 MB，逐文件 SHA256 见包内 `manifest.json`）。记录里**只放这一个 ZIP**。
3. **Resource type 选 `Dataset`**（不要选 Software）。
4. 按下方速查表填元数据 → **Save draft** → 逐项核对 → **Publish**。
5. 复制 DOI `10.5281/zenodo.<数字>`，交给维护者执行回填。

### 表单速查表

| 字段 | 值 |
|---|---|
| Title | 汉字字谜探针数据集 / Chinese Character Riddle Probes Dataset (CCRP DataSet) v0.1 |
| Resource type | **Dataset** |
| Version | `0.1`（数据版本；仓库补丁号 `v0.1.1` 不作数据版本） |
| Publication date | 2026-11-09 |
| Creators | `Spring Buds Data Source Inc.`（机构署名；affiliation 可填「春芽数源」） |
| License | `CC BY-NC-SA 4.0`（界面标识符 `cc-by-nc-sa-4.0`）；在 Description / Notes 中说明 `scripts/` MIT、论文与文档 CC BY 4.0 |
| Language | Chinese / `zho`（界面若无中文选项可选 English） |
| Access right | Open |
| Keywords | Chinese character riddles; structural probe; large language models; behavioural probe; control task; generation-solving closed loop; in-context learning; dataset; CC-Riddle; 字谜 |
| Description / Notes | 直接复制 `.zenodo.json` 的 `description` 与 `notes` 字段（含「不是排行榜基准」「31 条 UGC 下架」「上游 CC-Riddle 署名与修改声明」） |
| Related identifiers | `https://arxiv.org/abs/2206.13778` → Is derived from / Dataset；`https://github.com/pku0xff/CC-Riddle` → Is derived from / Software；`https://github.com/SunSeeding/ccrp` → Is supplement to / Software |

## 备选路径：发 `v0.1.2` 触发自动集成

只在希望「以后每次 GitHub Release 都自动归档」时选。启用集成后**必须 publish 一个新的 Release** 才会触发 webhook；`v0.1.2` 内容可与 `v0.1.1` 完全相同。代价：

- 无草稿、立即铸 DOI，元数据若错只能再发新版本修正；
- 记录类型很可能是 Software 而非 Dataset；
- 多出一个内容零变化的版本号。

若走此路，`.zenodo.json` 已按新版词汇表校正：`license: cc-by-nc-sa-4.0`、`relation: isderivedfrom / issupplementto`（旧值 `CC-BY-NC-SA-4.0`、`isDerivedFrom`、`isSupplementTo` 不在新版词汇表中）。发布后到 Zenodo 的 GitHub 页面查看该 Release 的处理状态；若失败，展开条目看 **Errors**，修元数据后重新 Release。

## 回填清单（拿到 DOI 后）

| 文件 | 改动 |
|---|---|
| `CITATION.cff` | 取消注释并填 `doi: "10.5281/zenodo.<数字>"` |
| `README.md` / `README.en.md` | 引用段把「Zenodo DOI 待归档」替换为 DOI 链接 `https://doi.org/10.5281/zenodo.<数字>` |
| `CHANGELOG.md` | 记一行归档日期与 DOI |
| `.zenodo.json` | 可加 `doi` 字段（Zenodo 也支持 `prereserve_doi`） |
| GitHub Release 正文 | 追加 DOI 徽章或链接 |

回填后需重跑 `python -u build_release.py` 与 `python -u scripts/verify_release.py .`，再提交并推送；**不改写已发布 tag**，把 DOI 作为后续补丁提交即可。

## 注意事项

- **不要编造 DOI 或 URL**。这是本项目溯源约定的硬规则。
- `cc-by-nc-sa-4.0` 不是 OSI 开源许可；README 中不要称本数据集为「开源数据集」。
- Zenodo 归档的是**长期快照**；GitHub Release 附件是同一版本的分发副本，两者 SHA256 可通过 `manifest.json` 核对。
- 手动上传产生的记录与 GitHub 集成不自动联动：以后若有新版本，需在 Zenodo 记录上点 **New version** 手动上传，或改用自动集成路径。
