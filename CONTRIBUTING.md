# 贡献指南

欢迎补充项目、论文和证据更正。低 star 不是拒绝理由。

1. 在 `data/projects.json` 或 `data/papers.json` 增加条目；不要直接改生成的 README 表格。
2. 提供 canonical GitHub 地址或论文原始页面，至少一个能证明所述机制的来源，以及核验日期。
3. 说明是完整助手、扩展、Harness、控制组件或研究代码；触发方式必须具体。未确认的能力写“待核验”，roadmap 不能当成已实现功能。
4. 检查许可证。缺少许可证全文可先进入候选/研究项；含非商业限制的源码不得标为已核验开放许可证。
5. 重命名按 GitHub canonical repo 更新；同一论文按 arXiv ID 去重，旧名字可以写入备注。
6. 运行下面的命令并提交生成结果。新增仓库时需要重新获取完整指标快照。

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests
python scripts/build.py --check
```

更新功能说明时固定证据提交 SHA；自动更新 star 不应顺带把旧功能判断标成刚核验。分类方法见 `docs/taxonomy.md`，排序方法见 `docs/methodology.md`。

禁止把私有搜索服务地址、令牌、内部文章正文、签名下载链接或个人数据提交到本仓库。
