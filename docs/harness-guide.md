# 把现有 Agent 变成主动助手

先选执行基础，再补触发、持久状态和结果交付。只加一个 cron 能解决定时启动，不能自动获得需求理解与长期目标管理。

| 已有基础 | 可调查的路线 | 已核验机制 | 当前边界 |
| --- | --- | --- | --- |
| Pi | [rho](https://github.com/mikeyobrien/rho) | 常驻运行、持久记忆、heartbeat | Pi 的上层应用；检查运行平台及维护快照 |
| Pi / Claude / Codex CLI | [murmur](https://github.com/t0dorakis/murmur) | 以 Markdown 任务定义周期唤醒 CLI | 交付和业务动作仍由被调用的 Agent 完成 |
| DeepSeek Harness | [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive) | host 级定时唤醒冷会话、静默收尾 | 核对 DSH / 插件版本；宿主仍需运行 |
| DeepSeek Harness | [DS Bot](https://github.com/Fei2411/DS-Bot) | 持久命名 Bot、群聊与记忆 | 首页未证实独立定时机制；与其他插件的组合尚未实测 |
| Hermes Agent | [内置 cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | 无人值守定时任务与渠道交付 | 先用内置机制；本目录没有替用户部署 |
| Hermes 桌面端 | [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | Bot UI + 宿主 cron routines | 当前已归档，仅保留设计和代码参考 |
| OpenClaw | [Pulse](https://github.com/Hypostas/pulse) | 传感与紧急度驱动的 webhook 唤醒 | 依赖宿主；不替代全部 cron 功能 |
| Letta | [Letta Code](https://github.com/letta-ai/letta-code) + [scheduling](https://docs.letta.com/letta-code/scheduling) | 持久 Agent、远程环境、self-managed schedules | LettaBot 已弃用，迁移优先参考官方新路径 |
| 任意支持 MCP 的宿主 | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | Windows 操作工具 | 只补执行层，还需触发、状态与交付 |

以上是公开文档确认的组合入口，不是兼容性集成测试报告。首次验证可使用“到指定时间在隔离目录生成一份文件”作为最小任务，再检查无变化时是否保持静默以及重启后任务是否重复。

所有项目的证据、许可和核验日期见 [项目详表](projects.md)。
