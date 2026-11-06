# 2026-11-06 收录 OpenMausBot

- 项目：<https://github.com/milind-soni/OpenMausBot>
- 分类：常驻个人助手与轻量运行时
- 主动机制：schedules、webhooks、connected-app events
- 核心许可：Apache-2.0；`enterprise/` 目录除外

OpenMausBot 是本地优先的多 Bot 聊天应用。每个 Bot 可以配置自己的模型、线程记忆、电脑与连接应用；Agent 进程由本地 harness 管理，可接入 Claude、Codex、Grok CLI 或兼容模型提供商。触发器支持单次、选定工作日或 5–1440 分钟间隔的 schedules，并支持 webhook 与 connected-app events。

功能判断固定到提交 `083fd7b51405e6d0c01e189b2f65ab0322509b5a` 的 README，未做实机能力测试。仓库主体为 Apache-2.0；README 与 `enterprise/LICENSE` 明确 `enterprise/` 使用独立 source-available 许可，生产启用需要有效许可证密钥，并禁止再分发、转售、白标或向第三方托管，除非取得书面协议。
