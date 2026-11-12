# 项目说明与证据

每项功能均为公开文档核验；没有安装运行或完成统一能力测试。证据尽量固定到核验时的提交，后续指标刷新不自动修改功能判断。


<a id="openclaw--openclaw"></a>

## [OpenClaw](https://github.com/openclaw/openclaw)

连接消息渠道、记忆与工具的常驻个人助手。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时 / heartbeat / 事件。
- 边界：后台执行依赖 gateway；各平台和工具权限需单独配置。
- 当前维护状态：近90天有提交；18523 次 / 30 天，48713 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/openclaw/openclaw/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/openclaw/openclaw/blob/8cb658e39b6dbe1bbe03746bf2a468a898c15da2/README.md#L18) · [来源2](https://docs.openclaw.ai/gateway/heartbeat) · [来源3](https://docs.openclaw.ai/gateway/heartbeat)。

<a id="nousresearch--hermes-agent"></a>

## [Hermes Agent](https://github.com/NousResearch/hermes-agent)

带持久记忆、技能积累和跨渠道定时交付的个人 Agent。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时 / 会话 heartbeat。
- 边界：功能依据官方文档，未在本清单中实机测评。
- 当前维护状态：近90天有提交；15084 次 / 30 天，46437 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/NousResearch/hermes-agent/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/NousResearch/hermes-agent/blob/cad0aaaf0d77ffa4899ebf0d3db8bae7a6b5147f/README.md#L27)。

<a id="hkuds--nanobot"></a>

## [nanobot](https://github.com/HKUDS/nanobot)

轻量 Python 个人 Agent，支持文件、记忆、MCP 和长期目标。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时 / 本地触发器。
- 边界：后台服务重启后不补跑错过的定时任务，见官方恢复说明。
- 当前维护状态：近90天有提交；418 次 / 30 天，1329 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/HKUDS/nanobot/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/HKUDS/nanobot/blob/ce3aa50e70f6550d7be19f73f2cfa2ba6fb66880/README.md#L63)。

<a id="zeroclaw-labs--zeroclaw"></a>

## [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

Rust Agent 运行时，支持后台服务、工具及事件触发流程。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：cron / webhook / MQTT。
- 边界：电脑操作范围取决于已配置的工具与执行环境。
- 当前维护状态：近90天有提交；267 次 / 30 天，1072 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/zeroclaw-labs/zeroclaw/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/zeroclaw-labs/zeroclaw/blob/683d10139bc200ab8db768fcb4515f79404846ac/README.md#L83)。

<a id="nanocoai--nanoclaw"></a>

## [NanoClaw](https://github.com/nanocoai/nanoclaw)

通过消息渠道操作的助手，使用容器运行 Agent 并执行周期任务。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时 / script gates。
- 边界：执行环境为容器，不能据此声称拥有任意宿主桌面操作能力。
- 当前维护状态：近90天有提交；138 次 / 30 天，702 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/nanocoai/nanoclaw/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/nanocoai/nanoclaw/blob/f7440e85f8b2a75b17fc9a08f0cc6aacf723a1e2/README.md#L65)。

<a id="milind-soni--openmausbot"></a>

## [OpenMausBot](https://github.com/milind-soni/OpenMausBot)

本地优先的多 Bot 聊天应用，每个 Bot 可使用独立模型、线程记忆、电脑和连接应用。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：schedules / webhooks / app events。
- 边界：Bot 运行依赖本机的 Claude、Codex、Grok 等 CLI 或兼容模型提供商；云桌面、Composio 和 enterprise 功能具有独立服务或许可边界。
- 当前维护状态：近90天有提交；5450 次 / 30 天，9712 次 / 90 天。
- 许可：[Apache-2.0（enterprise/ 除外）](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519)；删除 enterprise/ 后为 Apache-2.0 开源版；enterprise/ 为独立 source-available 许可，生产启用需许可证密钥且禁止再分发或向第三方托管。
- 功能核验：2026-11-06；[来源1](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L73) · [来源2](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L413) · [来源3](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519)。

<a id="elie222--rakazo"></a>

## [Rakazo](https://github.com/elie222/rakazo)

可自托管的持久 Bot 与团队电脑工作空间，支持自选模型和沙箱。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：routines。
- 边界：私有电脑、团队电脑与容器能力按配置区分。
- 当前维护状态：近90天有提交；2206 次 / 30 天，3384 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/elie222/rakazo/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/elie222/rakazo/blob/ed67158935a95b6153aad6c9cd874c6cc8d2413d/README.md#L24)。

<a id="nano-muse--nanomuse"></a>

## [nanoMuse](https://github.com/nano-muse/nanoMuse)

跨手机与电脑的个人 Agent，结合记忆、后台目标与设备操作。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：目标巡检 / routines。
- 边界：设备能力和后台运行条件因平台而异；论文与软件各列一项。
- 当前维护状态：近90天有提交；1239 次 / 30 天，2660 次 / 90 天。
- 许可：[GPL-3.0](https://api.github.com/repos/nano-muse/nanoMuse/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/nano-muse/nanoMuse/blob/57f5c5abed2d66fa19ab8fc39fd52eb365e4f14d/README.md#L80)。

<a id="moltis-org--moltis"></a>

## [Moltis](https://github.com/moltis-org/moltis)

集成记忆、语音、消息、浏览器和调度的个人 Agent 服务。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：cron。
- 边界：需自行配置模型和所需集成。
- 当前维护状态：近90天有提交；16 次 / 30 天，156 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/moltis-org/moltis/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md#L28)。

<a id="nearai--ironclaw"></a>

## [IronClaw](https://github.com/nearai/ironclaw)

Rust 个人助手，通过 routines 与 heartbeat 执行后台任务。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时 / 事件 / heartbeat。
- 边界：工具隔离是设计特征，不等于本清单已审计安全性。
- 当前维护状态：近90天有提交；0 次 / 30 天，170 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/nearai/ironclaw/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md#L95)。

<a id="afk-surf--comma"></a>

## [Comma](https://github.com/AFK-surf/Comma)

持续任务状态与跨设备工作结合，通过监控循环唤醒 Agent。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：routines / event loops。
- 边界：云端运行环境和本地设备连接是不同组件。
- 当前维护状态：近90天有提交；3 次 / 30 天，8 次 / 90 天。
- 许可：[AGPL-3.0](https://api.github.com/repos/AFK-surf/Comma/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/AFK-surf/Comma/blob/66ab3dc92475005aea9afd123df36a28e4ef86ab/README.md#L64)。

<a id="sipeed--picoclaw"></a>

## [PicoClaw](https://github.com/sipeed/picoclaw)

面向低资源设备的 Go 个人助手，包含文件、执行和调度工具。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：定时。
- 边界：低资源运行时不代表所调用模型或浏览器同样低成本。
- 当前维护状态：近90天有提交；0 次 / 30 天，1 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/sipeed/picoclaw/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md#L632)。

<a id="maikunari--mame"></a>

## [Mame](https://github.com/maikunari/mame)

带持久记忆和消息渠道的轻量常驻助手，可编排编码 Agent。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：cron / heartbeat。
- 边界：适合作为小型实现参考，项目维护分不代表成熟度。
- 当前维护状态：近90天有提交；0 次 / 30 天，28 次 / 90 天。
- 许可：[README 声明 MIT](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md)；未找到许可证全文；候选，不进入开源推荐榜。
- 功能核验：2026-11-05；[来源1](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md#L300)。

<a id="khoj-ai--khoj"></a>

## [Khoj](https://github.com/khoj-ai/khoj)

个人知识助手，支持文档与网络研究及定时自动化。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：scheduled automations。
- 边界：以知识与信息工作为主，不是通用桌面控制器。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[AGPL-3.0](https://api.github.com/repos/khoj-ai/khoj/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md#L50) · [来源2](https://docs.khoj.dev/features/automations) · [来源3](https://docs.khoj.dev/features/automations)。

<a id="mikeyobrien--rho"></a>

## [rho](https://github.com/mikeyobrien/rho)

基于 Pi 的常驻个人操作助手，提供持久记忆和定期主动检查。

- 分类：常驻个人助手与轻量运行时；主动机制已文档化。
- 触发方式：heartbeat。
- 边界：是 Pi 的上层应用；Android 与桌面的运行方式不同。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/mikeyobrien/rho/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/mikeyobrien/rho/blob/073a3ee8a5dc0efd5dd32d773a760575ed38abc7/README.md#L34)。

<a id="copilotkit--openbot"></a>

## [OpenBot](https://github.com/CopilotKit/OpenBot)

为 AG-UI Agent 提供独立浏览器、文件工作区、工具权限、审计记录和定时任务的自托管 AI coworker 平台。

- 分类：工作空间与上下文助手；主动机制已文档化。
- 触发方式：定时 routines / 人工发起。
- 边界：OpenBot 负责电脑环境、策略、审计和调度；Agent 能力由接入的 AG-UI endpoint 提供，持久会话与记忆依赖 CopilotKit Intelligence。
- 当前维护状态：近90天有提交；552 次 / 30 天，1086 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/CopilotKit/OpenBot/license)；GitHub licenseInfo 识别；CopilotKit Intelligence 的部署与许可证条件另计。
- 功能核验：2026-11-05；[来源1](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L251) · [来源2](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L52)。

<a id="agent0ai--agent-zero"></a>

## [Agent Zero](https://github.com/agent0ai/agent-zero)

在电脑执行环境中运行工具、项目和周期监控任务的 Agent。

- 分类：工作空间与上下文助手；主动机制已文档化。
- 触发方式：scheduled operations。
- 边界：以所配置的执行环境为边界，并非默认控制宿主所有资源。
- 当前维护状态：近90天有提交；137 次 / 30 天，485 次 / 90 天。
- 许可：[MIT](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE)；根目录 LICENSE 人工核验。
- 功能核验：2026-11-05；[来源1](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md#L259)。

<a id="anil-matcha--suparagent"></a>

## [Suparagent](https://github.com/Anil-matcha/suparagent)

集中管理命名 AI coworkers、团队委派、对话、记忆、routines、任务与审批的桌面及自托管工作区。

- 分类：工作空间与上下文助手；主动机制已文档化。
- 触发方式：scheduled / webhook / manual routines。
- 边界：项目仍处于早期开发，自托管服务和电脑/浏览器能力为实验性；托管版是独立产品，模型及账号需用户自备，部分集成仅支持 Claude 或 Codex。
- 当前维护状态：近90天有提交；652 次 / 30 天，691 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/Anil-matcha/suparagent/license)；GitHub licenseInfo 识别；托管服务、第三方引擎、Composio 与模型提供商遵循各自条款。
- 功能核验：2026-11-11；[来源1](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L3) · [来源2](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L71) · [来源3](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L183)。

<a id="openbmb--pilotdeck"></a>

## [PilotDeck](https://github.com/OpenBMB/PilotDeck)

按工作空间隔离文件、记忆与技能，支持后台发现任务并交付文件。

- 分类：工作空间与上下文助手；主动机制已文档化。
- 触发方式：always-on 任务发现。
- 边界：README 的 benchmark 属作者自报，本仓库不将其纳入跨项目能力排名。
- 当前维护状态：近90天有提交；488 次 / 30 天，1082 次 / 90 天。
- 许可：[AGPL-3.0](https://api.github.com/repos/OpenBMB/PilotDeck/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/OpenBMB/PilotDeck/blob/2865f05b1722c7473ea8a9dda317a92fb8c92dd8/README.md#L97)。

<a id="copilotkit--openmuse"></a>

## [OpenMuse](https://github.com/CopilotKit/openmuse)

提供个人 Agent 界面、浏览器与工作空间的开源应用。

- 分类：工作空间与上下文助手；相邻能力。
- 触发方式：后台任务 worker；自主触发待核验。
- 边界：后台 worker 不等于自主发起；部分连接器和动作仍在 roadmap。
- 当前维护状态：近90天有提交；19 次 / 30 天，144 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/CopilotKit/openmuse/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/CopilotKit/openmuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md#L43)。

<a id="copilotkit--openduet"></a>

## [OpenDuet](https://github.com/CopilotKit/OpenDuet)

用于构建主动工作助手的开源应用模板。

- 分类：工作空间与上下文助手；主动机制已文档化。
- 触发方式：routines / 后台建议。
- 边界：模板需配置依赖和模型；不是已部署的托管服务。
- 当前维护状态：近90天有提交；83 次 / 30 天，83 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/CopilotKit/OpenDuet/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/CopilotKit/OpenDuet/blob/f52288fff5ccdbd3de428d573d9f026fce5ff480/README.md#L5)。

<a id="volcengine--minecontext"></a>

## [MineContext](https://github.com/volcengine/MineContext)

从屏幕上下文生成洞察、待办和日周总结的主动信息助手。

- 分类：工作空间与上下文助手；相邻能力。
- 触发方式：上下文观察 / 主动推送。
- 边界：主动建议有据；不据此认定它能自主操作全部应用。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/volcengine/MineContext/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/README.md#L9)。

<a id="fei2411--ds-bot"></a>

## [DS Bot](https://github.com/Fei2411/DS-Bot)

把 DeepSeek Harness 扩展为有记忆、群聊和 Bot 协作的桌面应用及插件。

- 分类：主动插件与调度扩展；相邻能力。
- 触发方式：持久 Bot / 群聊；自主唤醒待核验。
- 边界：首页未确认独立定时机制；不可把长期会话直接等同主动运行。
- 当前维护状态：近90天有提交；2130 次 / 30 天，2306 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/Fei2411/DS-Bot/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/Fei2411/DS-Bot/blob/71d344bf193f3f18185f25de3d8e5c483046910a/README.md#L41)。

<a id="john-walks-slow--dsh-proactive"></a>

## [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive)

为 DeepSeek Harness 增加会话冷却后仍可触发的主动唤醒。

- 分类：主动插件与调度扩展；主动机制已文档化。
- 触发方式：host 级 once / interval / cron。
- 边界：依赖宿主运行与版本兼容；包含免打扰和通知预算配置。
- 当前维护状态：近90天有提交；8 次 / 30 天，97 次 / 90 天。
- 许可：[MIT](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/packages/dsh-proactive/LICENSE)；插件子目录 LICENSE 人工核验。
- 功能核验：2026-11-05；[来源1](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/README.md#L1)。

<a id="t0dorakis--murmur"></a>

## [murmur](https://github.com/t0dorakis/murmur)

定期启动 Claude、Codex、Pi 等 CLI 会话的轻量调度守护进程。

- 分类：主动插件与调度扩展；主动机制已文档化。
- 触发方式：cron / interval。
- 边界：消息投递和业务操作由提示词与被调用 Agent 实现。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/t0dorakis/murmur/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/t0dorakis/murmur/blob/d666df4c749c28ecb775613ecec8b12954b387e7/README.md#L10)。

<a id="hypostas--pulse"></a>

## [Pulse](https://github.com/Hypostas/pulse)

为 OpenClaw 提供按变化、目标和紧急度唤醒的扩展守护进程。

- 分类：主动插件与调度扩展；主动机制已文档化。
- 触发方式：传感 / 紧急度触发。
- 边界：依赖 OpenClaw webhook；作者的自主性表述不是本仓库的实测结论。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/Hypostas/pulse/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/Hypostas/pulse/blob/4bebd1e23bff218dde1cd0b693f901493d45f972/README.md#L5)。

<a id="nousresearch--hermes-bot-mode"></a>

## [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode)

为 Hermes 桌面端增加命名 Bot、独立对话和周期任务面板。

- 分类：主动插件与调度扩展；历史参考。
- 触发方式：宿主 cron routines。
- 边界：GitHub 已归档；保留为 Hermes Bot UI 与 cron 集成参考，不作为活跃插件推荐。
- 当前维护状态：归档 / 历史；0 次 / 30 天，68 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/NousResearch/Hermes-Bot-Mode/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/NousResearch/Hermes-Bot-Mode/blob/80fee22582b871b9765a65e2992b8b5a8211c9f8/README.md#L23)。

<a id="earendil-works--pi"></a>

## [Pi](https://github.com/earendil-works/pi)

可扩展 Agent harness，可通过 SDK、RPC 和插件构建常驻助手。

- 分类：可扩展 Harness 与持久运行基础；相邻能力。
- 触发方式：需上层调度 / 扩展。
- 边界：旧地址 badlogic/pi-mono 已重定向；可结合 rho 或 murmur。
- 当前维护状态：近90天有提交；945 次 / 30 天，2110 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/earendil-works/pi/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/earendil-works/pi/blob/fcebc099565d8f30c15b321ff6a1af5f34d89400/README.md#L15)。

<a id="deepseek-ai--deepseek-harness"></a>

## [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

以插件架构提供 Agent 运行基础，适合接入 Bot 与主动唤醒插件。

- 分类：可扩展 Harness 与持久运行基础；相邻能力。
- 触发方式：需宿主插件提供主动机制。
- 边界：developer preview；插件兼容性需要核验。
- 当前维护状态：近90天有提交；4402 次 / 30 天，14257 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/deepseek-ai/deepseek-harness/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/README.md#L7)。

<a id="letta-ai--letta-code"></a>

## [Letta Code](https://github.com/letta-ai/letta-code)

带持久记忆的 Agent，可通过远程环境和 channels 构成常驻助手。

- 分类：可扩展 Harness 与持久运行基础；主动机制已文档化。
- 触发方式：remote environments / cron。
- 边界：LettaBot 官方迁移目标；需要结合远程环境与调度配置。
- 当前维护状态：近90天有提交；364 次 / 30 天，1023 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/letta-ai/letta-code/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/letta-ai/letta-code/blob/e6d6cc27ef1111da80e919dc1cef179613894b66/README.md#L29) · [来源2](https://docs.letta.com/letta-code/scheduling) · [来源3](https://docs.letta.com/letta-code/scheduling)。

<a id="browser-use--browser-use"></a>

## [Browser Use](https://github.com/browser-use/browser-use)

为 Agent 提供网页理解和浏览器执行能力。

- 分类：电脑与浏览器控制组件；相邻能力。
- 触发方式：按需浏览器任务。
- 边界：主要作用于浏览器；不证明具备主动调度或整个桌面控制。
- 当前维护状态：近90天有提交；640 次 / 30 天，940 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/browser-use/browser-use/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md#L1)。

<a id="cursortouch--windows-mcp"></a>

## [Windows-MCP](https://github.com/CursorTouch/Windows-MCP)

向 Agent 暴露 Windows 电脑操作能力的 MCP 服务。

- 分类：电脑与浏览器控制组件；相邻能力。
- 触发方式：由宿主调用。
- 边界：控制组件本身不是常驻个人助手，需外接模型、记忆与触发器。
- 当前维护状态：近90天有提交；101 次 / 30 天，149 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/CursorTouch/Windows-MCP/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/CursorTouch/Windows-MCP/blob/9ab92bca2772dfb53ae3ed4feb98dac22c5b3dea/README.md#L25)。

<a id="alibaba--page-agent"></a>

## [Page Agent](https://github.com/alibaba/page-agent)

在网页内用自然语言控制界面的 JavaScript Agent。

- 分类：电脑与浏览器控制组件；相邻能力。
- 触发方式：由网页或宿主调用。
- 边界：网页控制层；不具备完整常驻助手生命周期。
- 当前维护状态：近90天有提交；0 次 / 30 天，18 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/alibaba/page-agent/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/alibaba/page-agent/blob/9eb6b6646500264d9034dd466a4270cb9fc1ef1e/README.md#L35)。

<a id="bytedance--ui-tars-desktop"></a>

## [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop)

提供 GUI 与浏览器操作的 Agent 应用和相关工具。

- 分类：电脑与浏览器控制组件；相邻能力。
- 触发方式：按需电脑 / 浏览器任务。
- 边界：电脑任务自动执行与无人提示的主动发起是两个维度。
- 当前维护状态：归档 / 历史；0 次 / 30 天，8 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/bytedance/UI-TARS-desktop/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md#L13)。

<a id="xlang-ai--osworld"></a>

## [OSWorld](https://github.com/xlang-ai/OSWorld)

在真实电脑环境中评测多模态 Agent 的执行能力。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：真实电脑任务评测。
- 边界：衡量任务执行，不能单独衡量主动发起与打扰时机。
- 当前维护状态：近90天有提交；168 次 / 30 天，190 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/xlang-ai/OSWorld/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/xlang-ai/OSWorld/blob/8903ebeb0efdf74331bd7dc37ed91ccbbff22317/README.md#L294)。

<a id="facebookresearch--memo-pro-agent"></a>

## [MemoProAgent](https://github.com/facebookresearch/Memo-Pro-Agent)

研究从长期个人记忆中寻找证据来决定是否主动介入。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：记忆驱动介入评测。
- 边界：论文早期名称 ProPerAgent；按同一 arXiv ID 去重。
- 当前维护状态：近90天有提交；6 次 / 30 天，6 次 / 90 天。
- 许可：[CC-BY-NC-4.0](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/LICENSE)；非商业许可；仅作为研究源码列出。
- 功能核验：2026-11-05；[来源1](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/README.md#L3)。

<a id="simplified-reasoning--pi-bench"></a>

## [π-Bench](https://github.com/Simplified-Reasoning/Pi-Bench)

评测长期多轮工作流中隐藏需求识别与主动协助。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：主动性评测。
- 边界：这是 benchmark；与 Pi harness 无关。
- 当前维护状态：近90天有提交；1 次 / 30 天，1 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/Simplified-Reasoning/Pi-Bench/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/Simplified-Reasoning/Pi-Bench/blob/4f545be5d289b28ff022d2904d455007358ed3b7/README.md#L1)。

<a id="thunlp--proactiveagent"></a>

## [ProactiveAgent](https://github.com/thunlp/ProactiveAgent)

主动任务预测方法及其数据与评测代码。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：事件观察 / 任务预判。
- 边界：研究实现，不等同开箱即用的通用个人助手。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/thunlp/ProactiveAgent/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/thunlp/ProactiveAgent/blob/3fcf9beebe256b86871659fbb12541c41c9381b9/README.md#L2)。

<a id="xzf-thu--pask"></a>

## [PASK](https://github.com/xzf-thu/Pask)

研究结合长期记忆、持续上下文与延迟约束的主动辅助。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：潜在需求检测 / 保持静默。
- 边界：技术报告与研究代码；实用成熟度需另行验证。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/xzf-thu/Pask/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/xzf-thu/Pask/blob/d54646c52b1555232ce4ab39103768d7f65b8267/README.md#L30)。

<a id="zju-real--knowu-bench"></a>

## [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)

评测移动 Agent 获取偏好、主动介入与征求同意的能力。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：交互式个性化移动评测。
- 边界：聚焦移动 GUI 与个人偏好，不是全平台运行时。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/ZJU-REAL/KnowU-Bench/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/ZJU-REAL/KnowU-Bench/blob/c03a825991ede13add6631f2ed19b90755930dc6/README.md#L4)。

<a id="tdemin16--proactivebench"></a>

## [ProactiveBench (MLLM)](https://github.com/tdemin16/proactivebench)

评测多模态模型主动获取有用信息的研究基准。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：多模态主动性评测。
- 边界：与 ProactiveAgent 使用的同名基准区分；官方论文页标注 ECCV 2026。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/tdemin16/proactivebench/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/tdemin16/proactivebench/blob/428885c9224418b544dfbdbde5307bccc58018d5/README.md#L2)。

<a id="deepakn97--pare"></a>

## [PARE](https://github.com/deepakn97/pare)

通过主动用户与有状态数字环境模拟评估主动助手。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：主动助手 / 用户模拟评测。
- 边界：模拟用户不等同真实用户长期使用效果。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[MIT](https://api.github.com/repos/deepakn97/pare/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/deepakn97/pare/blob/261149914a9e9dcacb12de620575c691d50e3c2e/README.md#L3)。

<a id="openaiotlab--contextagent"></a>

## [ContextAgent](https://github.com/openaiotlab/ContextAgent)

研究如何用开放世界感知信息判断主动服务及工具调用。

- 分类：研究实现与评测代码；研究资源。
- 触发方式：感知上下文 / 服务预测。
- 边界：研究数据和工具场景不能直接泛化为任意桌面。
- 当前维护状态：91–365天未提交；0 次 / 30 天，0 次 / 90 天。
- 许可：[待核验](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md)；未找到 LICENSE；仅作研究资源，不推断授权。
- 功能核验：2026-11-05；[来源1](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md#L3)。

<a id="letta-ai--lettabot"></a>

## [LettaBot](https://github.com/letta-ai/lettabot)

曾提供消息渠道、记忆、heartbeat 和定时任务的个人助手。

- 分类：历史与迁移项目；历史参考。
- 触发方式：heartbeat / cron。
- 边界：官方 README 已宣布不再积极维护，建议迁往 Letta Code。
- 当前维护状态：归档 / 历史；0 次 / 30 天，0 次 / 90 天。
- 许可：[Apache-2.0](https://api.github.com/repos/letta-ai/lettabot/license)；GitHub licenseInfo 识别；不推断附属数据或模型权重许可。
- 功能核验：2026-11-05；[来源1](https://github.com/letta-ai/lettabot/blob/99c3b5dd73550fe0a4eac2ee31b1c3229ca9e550/README.md#L8)。
