# Zenodo 归档与 DOI（v0.1）— 已归档

> **状态：已发布（2026-11-09）。** 下列 DOI、记录 ID 与校验值均来自 Zenodo API 实时查询，**没有编造任何 DOI 或 URL**。

| 项目 | 值 |
|---|---|
| 记录页 | <https://zenodo.org/records/24077793> |
| **版本 DOI**（引用具体版本用这个） | [`10.5281/zenodo.24077793`](https://doi.org/10.5281/zenodo.24077793) |
| 概念 DOI（指向该记录的全部版本） | [`10.5281/zenodo.24077792`](https://doi.org/10.5281/zenodo.24077792) |
| 记录 ID / 概念记录 ID | `24077793` / `24077792` |
| 资源类型 / 访问权 | `Dataset` / `open` |
| 状态 | `status=published`、`state=done`（非草稿） |
| 发布日期 | 2026-11-09 |
| 归档文件 | `CCRP-DataSet-v0.1.1.zip`（记录中唯一文件） |
| 归档文件体积 / 指纹 | 3,035,750 B；MD5 `8f367d19cc2560cfbe13f2ab1c80cb05`（与 Zenodo API `files[].checksum` 一致） |

## 1. 归档对象与一致性

- 归档 ZIP 就是 GitHub `v0.1.1` Release 的首个附件，**逐字节相同**；内含 **43 个文件**、解压后 10,477,142 B，逐文件 SHA256 见包内 `manifest.json`。
- 离线复算：`cd CCRP-DataSet-v0.1.1 && python scripts/verify_release.py .`（零依赖、不联网）；ZIP 指纹可用 `md5sum CCRP-DataSet-v0.1.1.zip` 核对。
- Zenodo **已发布记录的文件不可修改**（换文件必须 New version，会产生新的版本 DOI）。因此 DOI 回填**只改仓库文档与 Release 正文**：不重建 ZIP、不替换 Release 附件、不改写已发布 tag。`main` 上的文档是后续补丁，`v0.1.1` tag / Release 附件 / Zenodo 记录三者仍是同一份字节快照。

## 2. 引用口径

- 版本 DOI `10.5281/zenodo.24077793` 固定指向本次 v0.1 归档；论文、BibTeX、`CITATION.cff` **一律用它**。
- 概念 DOI `10.5281/zenodo.24077792` 解析到该记录的最新版本，只适合「引用这个数据集、不限版本」的场合。
- GitHub 仓库、Release 附件与在线站点是**同一版本的分发副本**，不是第二个归档对象；引用中不要并列两个 DOI。

## 3. 回填清单（已完成）

| 文件 / 位置 | 改动 |
|---|---|
| `CITATION.cff` | 顶层 `doi: "10.5281/zenodo.24077793"`，`url` 改为 DOI 解析页，`repository-code` 仍指仓库；注释记录概念 DOI |
| `README.md` / `README.en.md` | 首屏新增归档 DOI 行；BibTeX 加 `doi` 并改用 DOI `url`；引用章节说明版本 DOI / 概念 DOI 与归档 ZIP 指纹 |
| `CHANGELOG.md` | `v0.1.1` 节补记归档与回填（main 后续修订、未打新 tag），Roadmap 删除已完成的 Zenodo 待办 |
| `docs/DATASHEET.md` | 维护章节写入两个 DOI，v0.2 计划移除已完成的英文 HTML/PDF、合规站点版、Zenodo DOI |
| `docs/ZENODO.md` | 本文件：由「待归档指引」改写为「已归档事实 + 元数据核对 + 后续版本流程」 |
| GitHub `v0.1.0` / `v0.1.1` Release 正文 | 追加 DOI 徽章与链接、更正「待回填」措辞；**tag 与 4 个附件零改动** |
| `.zenodo.json` | **故意不写 `doi` 字段**：该文件仅供 GitHub 自动集成读取，写入已存在的 DOI 会与未来自动归档冲突；本次走手动上传，不读它 |

回填后执行 `python -u build_release.py`（统一 LF 后重算 `manifest.json`）与 `python scripts/verify_release.py .`；提交只推 `main`。

## 4. 记录元数据核对 —— 维护者待修正

Zenodo API 返回的记录只带最小元数据，与仓库口径有偏差：

| 字段 | 记录现值 | 应有值 / 依据 | 影响 |
|---|---|---|---|
| `title` | `CCRP-DataSet-v0.1.1`（上传文件名） | `.zenodo.json` 的正式中英标题 | 引用展示不佳 |
| `creators` | `Spring Buds Data Source` | `Spring Buds Data Source Inc.`（机构署名，affiliation 可填「春芽数源」） | 署名不一致 |
| **`license`** | **`cc-by-4.0`** | **`cc-by-nc-sa-4.0`**（`data/`）；`scripts/` MIT、论文/文档 CC BY 4.0 写进 Description / Notes | **实质冲突**：记录页会显示可商用的 CC BY 4.0，与包内许可相反 |
| `description` / `notes` / `keywords` / `related_identifiers` / `version` / `language` | 缺失 | 直接复制 `.zenodo.json` 对应字段 | 可发现性、上游署名、分层许可说明缺失 |
| `resource_type` / `access_right` | `Dataset` / `open` ✅ | 保持不变 | 正确 |

**修正方式**（Zenodo 官方 Help《Manage records》《About records》）：已发布记录的**元数据可随时编辑**，在记录页点 **Edit** → 改完点 Publish 即可，**DOI 不变、不需要新版本、附件不动**；只有**文件与 DOI 不可改**。因此这里不需要重新上传 ZIP、也不应发 `v0.1.2`。修正前，任何许可判断**一律以包内根 `LICENSE`（CC 官方完整法律文本）、`LICENSE-DATA` 与 README 许可地图为准**；Zenodo 页面上的 `CC BY 4.0` 是建表时的默认选项，不是授权声明。

> 早前本文件写的「发布后元数据不可改，只能发新版本」并不准确（该说法只适用于文件）。已按官方说明更正，特此留痕。

## 5. 为什么走手动上传（历史决策，供复查）

| 事实 | 依据 / 实测 |
|---|---|
| `Sync now` 只刷新仓库列表，不产生归档 | Zenodo 官方《Enable a repository》 |
| 启用集成**前**已发布的 Release 不回溯 | 官方 FAQ；本仓库 `v0.1.0` / `v0.1.1` 均在打开 On 之前发布 |
| 自动集成立即发布、无草稿可审，且记录多为 **Software** | 官方《Archive a release from GitHub》；送往 Software Heritage |
| webhook `active=true`，最近投递只有 1 次 `ping`（202），无 `release` 事件 | GitHub API 实测 |
| 手动上传可选 **Dataset**、可先 Save draft 逐项核对 | 本次采用，归档 `v0.1.1` 整包 |

若当初改走自动集成，需 publish 一个新的 `v0.1.2` Release 才会触发；代价是无草稿、记录类型很可能是 Software、多出一个内容零变化的版本号。`.zenodo.json` 已按新版词汇表校正（`license: cc-by-nc-sa-4.0`、`isderivedfrom` / `issupplementto`），但该路径**未执行**。

## 6. 后续版本与 GitHub 集成风险

- GitHub 集成目前仍是 **On**。今后只要 publish 新 Release，Zenodo 会**自动另建一条记录**（多为 Software）并铸新 DOI，它**不会**成为本记录的 v2，从而出现两套互不关联的 DOI。二选一：
  - **继续手动归档（推荐保持现状）**：在 Zenodo 的 GitHub 设置里把 `ccrp` 的 On 关掉；以后在记录页点 **New version** 上传新 ZIP（概念 DOI 不变、生成新版本 DOI），再回填 `CITATION.cff` / 中英 README / `CHANGELOG.md`。
  - **改用自动集成**：接受无草稿与 Software 类型，并在文档中说明两条记录链的关系。
- 纯文档修订（不打新 tag）：只提交 `main`，不替换 Release 附件、不动 Zenodo 记录文件，如本次 DOI 回填。

## 7. 注意事项

- **不编造 DOI 或 URL**；本项目溯源约定的硬规则。
- `cc-by-nc-sa-4.0` 不是 OSI 认证的开源许可；README 中不称本数据集为「开源数据集」。
- Zenodo 归档是**长期快照**；GitHub Release 附件是同一版本的分发副本，两者可用 `manifest.json` 逐文件核对。
- 记录元数据修正不需要通知下游引用者（DOI 不变）；若更换归档文件则必然产生新版本 DOI，需重新走回填。
