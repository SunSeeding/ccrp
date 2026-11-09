# Zenodo 归档与 DOI（v0.1）

本文件说明如何为 CCRP DataSet v0.1 取得长期归档 DOI。**DOI 目前尚不存在，仓库中任何位置都没有编造 DOI**；拿到真实 DOI 后再回填 `CITATION.cff` 与 README。

元数据已预置在仓库根目录 `.zenodo.json`，Zenodo 的 GitHub 集成会在创建 deposition 时自动读取。

## 需要账号操作的步骤（我无法代做）

1. 用 GitHub 账号登录 <https://zenodo.org>（如无 Zenodo 账号，先完成 OAuth 授权）。
2. 打开 <https://zenodo.org/account/settings/github/>，在仓库列表里启用 **`SunSeeding/ccrp`**。
3. 在 GitHub 发布一个 Release（本版本已打 `v0.1.0` tag 并创建 Release）。启用集成后，Zenodo 会自动为该 Release 创建一个 deposition；也可以手动点 **Deposit new upload → Import from GitHub**。
4. 检查 deposition 表单：标题、机构署名、许可 `CC BY-NC-SA-4.0`、关键词、上游 CC-Riddle 关联标识应从 `.zenodo.json` 自动载入。**确认许可字段正确**（多许可仓库以数据主体许可为准）。
5. 点 **Publish**。发布后 Zenodo 分配 DOI，形如 `10.5281/zenodo.<数字>`。
6. 把 DOI 交给维护者（或在本仓库提 issue），执行回填。

## 回填清单（拿到 DOI 后）

| 文件 | 改动 |
|---|---|
| `CITATION.cff` | 取消注释并填 `doi: "10.5281/zenodo.<数字>"` |
| `README.md` / `README.en.md` | 引用段把「Zenodo DOI 待归档」替换为 DOI 链接 `https://doi.org/10.5281/zenodo.<数字>` |
| `CHANGELOG.md` | 记一行归档日期与 DOI |
| `.zenodo.json` | 可加 `doi` 字段（Zenodo 也支持 `prereserve_doi`） |
| GitHub Release 正文 | 追加 DOI 徽章或链接 |

回填后需重跑 `python -u build_release.py` 与 `python -u scripts/verify_release.py .`，再提交并推送；若已发布 tag，建议把 DOI 作为新补丁提交而非改写历史。

## 注意事项

- **不要编造 DOI 或 URL**。这是本项目溯源约定的硬规则。
- Zenodo 的 `CC-BY-NC-SA-4.0` 是许可标识符，不是 OSI 开源许可；README 中不要称本数据集为「开源数据集」。
- Zenodo 归档的是**长期快照**；GitHub Release 附件是同一版本的分发副本，两者 SHA256 可通过 `manifest.json` 核对。
