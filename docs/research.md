# 检索方法与覆盖记录

本轮采用“参考项目 → 特征词 → 全网与 GitHub → 目录补漏 → 原始文档核验”的三轮流程。交付是首版精选目录，停止原因是预设的三轮边界，**不是声称已经搜索穷尽**。第三轮仍有新来源，后续可继续扩展。

## 参考项目归纳出的检索词

| 特征 | 英文关键词 | 中文关键词 |
| --- | --- | --- |
| 不等待新指令 | proactive agent, anticipatory assistant, initiative | 主动式智能体、主动助手、需求预判 |
| 长期存在 | always-on, persistent agent, sessionless, background agent | 常驻助手、持久 Agent、后台运行 |
| 自主唤醒 | heartbeat, cron, scheduler, event-driven, webhook, routines | 心跳、定时、事件驱动、周期任务 |
| 真实行动 | computer use, desktop automation, browser agent, MCP | 电脑操作、桌面自动化、浏览器 Agent |
| 跨时间理解 | long-term memory, user context, personalization, long-horizon | 长期记忆、用户上下文、个性化、长期目标 |
| 改造现有基础 | harness, plugin, extension, Pi, Hermes, DeepSeek Harness | Harness 插件、扩展、二次开发 |
| 主动性研究 | proactive assistance benchmark, intervention timing, abstention | 主动辅助评测、介入时机、保持静默 |

泛词 autonomous agent 容易检出一次性执行器、游戏机器人和普通工作流；使用 heartbeat / routines / persistent 等机制词缩小范围，再核验 README。Grok Bot / Muse 用于产品类别发现，开源身份仍以仓库与许可证为准。

## 三轮过程

| 轮次 | 检索/核验批次 | 记录结果 | 新增来源 | 新增来源率 |
| --- | --- | --- | --- | --- |
| 1 | 12 | 228 | 220 | 96.5% |
| 2 | 6 | 53 | 42 | 79.2% |
| 3 | 4 | 171 | 138 | 80.7% |

检索日志共 22 个批次，含一个目录链接采集批次、两组 GitHub 原生仓库搜索扩展以及原始仓库/论文的批量核验。不是 22 个独立互联网关键词，也不是 400 个都适合收录的项目。

- 第一轮覆盖语义、官方文档、精选目录、仓库、替代方案、评测、局限、近期变化八个检索轴。目录采集上限为 100 个链接，网页检索每组记录上限通常为 20 条。
- 第二轮依据结果补入 rho、murmur、Pulse、PASK、ProAgentBench、PIRA-Bench 等新名词，核验完整助手与 harness 扩展。
- 第三轮使用 GitHub 原生搜索补漏，回到所有最终条目的官方 README、GitHub GraphQL 指标和论文摘要。功能证据固定到提交。

去重以 URL 规范化、canonical repo 和 arXiv ID 为主。网页搜索中的镜像域名仍可能作为不同候选来源进入调研计数，最终项目/论文目录已按上述实体键去重。新来源率是检索过程指标，不代表相关性或项目质量。

原始五个参考链接全部覆盖（5/5）。八个检索轴都获得过相关线索，但不意味着每一个细分领域均覆盖充分。没有独立用户研究或实机测评；功能按作者文档报告。

## 内容工厂

通过 `content-factory-search-api` 技能的 curl 路径调用结构化搜索，范围为 **2026-08-05 至 2026-11-05**，每组最多取 30 条、去重后最多 15 条。

本轮查询：`主动式 Agent`、`Grok Bot OR nanoMuse OR rakazo OR PilotDeck`、`Hermes Agent OR DeepSeek Harness OR Pi Agent`、`OpenClaw`、`Hermes`。五组请求都返回成功 JSON，但结果数组均为空，因此没有把内容工厂内容作为最终条目的证据；空结果不证明库中或互联网上不存在这些项目。没有进行全历史查询。没有结果时无须发起向量计算。

公开仓库仅保留检索词、日期范围和结果统计，不发布私有服务地址、密钥或内部正文。

## 原始来源纠错与限制

- [LettaBot README](https://github.com/letta-ai/lettabot) 明确宣布不再积极维护，迁移指向 Letta Code。GitHub 元数据也显示该仓库已归档。
- [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) 的 Bot + cron 设计仍有参考价值，但本轮 API 显示它已归档，故作为历史参考。
- [Pi](https://github.com/earendil-works/pi) 采用当前 canonical 仓库地址；旧地址 `badlogic/pi-mono` 不重复收录。
- [MemoProAgent](https://arxiv.org/abs/2610.22671) 是同一论文当前版本的标题，旧名 ProPerAgent 不再单列；其研究代码使用带非商业条件的许可，未列入开放许可证推荐。
- [ProactiveBench](https://arxiv.org/abs/2603.19466) 当前论文页注明 ECCV 2026；不沿用精选目录中的 ICLR 2026 标签，也不与 ProactiveAgent 的同名基准混淆。
- Mame 首页声明 MIT，但未定位到许可全文；ContextAgent 未找到 LICENSE。均保留核验缺口，不把公开可见等同许可完备。

## 未覆盖和待推进

多模态陪伴、行业运维、家庭设备、垂直主动学习等分支只获得线索，未全面纳入首版。闭源 Grok Bot / Muse 的功能未做对照实验。手机后台保活、跨设备可靠性和具体插件组合兼容性尚需实测。没有比较不同论文中的最好成绩，避免模型、数据、预算不同导致的伪排名。

核心机制的概括与分类是编辑判断。此轮不开展消融实验；无法回答“去掉记忆/调度后谁下降最多”。星数和提交量只能支持维护排序。

## 可核验文件

- [检索日志](../research/search-log.json)：轮次、检索轴、query、来源与结果数。
- [分类与证据决策](../research/decisions.json)：纳入边界和固定提交来源。
- [首次指标快照](../research/initial-metrics.json)：保留首版采集结果，后续每日更新不会覆盖。
- [当前指标快照](../data/metrics.json) 与 [排序 CSV](../data/rankings.csv)：最新可复算排名。
- [调研状态](../research/status.json) 与 [完整性核验](../research/verification.json)：无悬空证据引用或重复规范化 URL 错误；五个零结果查询作为已知提示保留。

完整检索结果文本和本机工具运行日志保留在本地，不复制到公开仓库。研究状态中的 99 条证据/判断与 123 条指标记录为本机审计计数；公开版提供关联决策、原始来源链接及指标快照。
