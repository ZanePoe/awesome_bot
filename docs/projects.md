# Project notes and evidence

Every documented feature was verified against public documentation; nothing was installed, run, or put through a unified capability test. Evidence is pinned to the commit verified at review time, and later metric refreshes do not change feature judgements.


<a id="openclaw--openclaw"></a>

## [OpenClaw](https://github.com/openclaw/openclaw)

Resident personal assistant that connects messaging channels, memory and tools.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled / heartbeat / events.
- Boundary: Background execution depends on the gateway; permissions for each platform and tool must be configured separately.
- Current maintenance status: Commits within the last 90 days; 11646 commits / 30 days, 48572 commits / 90 days.
- License: [MIT](https://api.github.com/repos/openclaw/openclaw/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/openclaw/openclaw/blob/8cb658e39b6dbe1bbe03746bf2a468a898c15da2/README.md#L18) · [Source 2](https://docs.openclaw.ai/gateway/heartbeat) · [Source 3](https://docs.openclaw.ai/gateway/heartbeat).

<a id="nousresearch--hermes-agent"></a>

## [Hermes Agent](https://github.com/NousResearch/hermes-agent)

Personal agent with persistent memory, skill accumulation and scheduled delivery across channels.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled / session heartbeat.
- Boundary: Features are documented by the official docs; no hands-on testing was done for this list.
- Current maintenance status: Commits within the last 90 days; 17323 commits / 30 days, 50744 commits / 90 days.
- License: [MIT](https://api.github.com/repos/NousResearch/hermes-agent/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/NousResearch/hermes-agent/blob/cad0aaaf0d77ffa4899ebf0d3db8bae7a6b5147f/README.md#L27).

<a id="hkuds--nanobot"></a>

## [nanobot](https://github.com/HKUDS/nanobot)

Lightweight Python personal agent supporting files, memory, MCP and long-term goals.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled / local triggers.
- Boundary: After a restart the background service does not replay missed scheduled tasks; see the official recovery notes.
- Current maintenance status: Commits within the last 90 days; 311 commits / 30 days, 1220 commits / 90 days.
- License: [MIT](https://api.github.com/repos/HKUDS/nanobot/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/HKUDS/nanobot/blob/ce3aa50e70f6550d7be19f73f2cfa2ba6fb66880/README.md#L63).

<a id="zeroclaw-labs--zeroclaw"></a>

## [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

Rust agent runtime supporting background services, tools and event-triggered flows.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: cron / webhook / MQTT.
- Boundary: The scope of computer control depends on the configured tools and execution environment.
- Current maintenance status: Commits within the last 90 days; 293 commits / 30 days, 1073 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/zeroclaw-labs/zeroclaw/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/zeroclaw-labs/zeroclaw/blob/683d10139bc200ab8db768fcb4515f79404846ac/README.md#L83).

<a id="milind-soni--openmausbot"></a>

## [OpenMausBot](https://github.com/milind-soni/OpenMausBot)

Local-first multi-bot chat app where each bot can use its own model, thread memory, computer and connected apps.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: schedules / webhooks / app events.
- Boundary: Bots depend on local CLIs such as Claude, Codex or Grok, or compatible model providers; the cloud desktop, Composio and enterprise features carry separate service or license boundaries.
- Current maintenance status: Commits within the last 90 days; 6899 commits / 30 days, 12973 commits / 90 days.
- License: [Apache-2.0 (except enterprise/)](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519); Apache-2.0 open-source edition once enterprise/ is removed; enterprise/ is separately source-available, production use requires a license key, and redistribution or hosting for third parties is prohibited.
- Feature verified: 2026-11-06; [Source 1](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L73) · [Source 2](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L413) · [Source 3](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519).

<a id="nanocoai--nanoclaw"></a>

## [NanoClaw](https://github.com/nanocoai/nanoclaw)

Assistant operated through messaging channels; runs agents inside containers and executes periodic tasks.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled / script gates.
- Boundary: The execution environment is a container, which does not establish arbitrary host-desktop control.
- Current maintenance status: Commits within the last 90 days; 152 commits / 30 days, 525 commits / 90 days.
- License: [MIT](https://api.github.com/repos/nanocoai/nanoclaw/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/nanocoai/nanoclaw/blob/f7440e85f8b2a75b17fc9a08f0cc6aacf723a1e2/README.md#L65).

<a id="elie222--rakazo"></a>

## [Rakazo](https://github.com/elie222/rakazo)

Self-hostable persistent bot and team computer workspace with user-chosen models and sandboxes.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: routines.
- Boundary: Private computer, team computer and container capabilities differ by configuration.
- Current maintenance status: Commits within the last 90 days; 3063 commits / 30 days, 4666 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/elie222/rakazo/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/elie222/rakazo/blob/ed67158935a95b6153aad6c9cd874c6cc8d2413d/README.md#L24).

<a id="nano-muse--nanomuse"></a>

## [nanoMuse](https://github.com/nano-muse/nanoMuse)

Personal agent across phone and computer, combining memory, background goals and device operation.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: goal checks / routines.
- Boundary: Device capabilities and background-run conditions vary by platform; the paper and the software are listed as separate entries.
- Current maintenance status: Commits within the last 90 days; 846 commits / 30 days, 2767 commits / 90 days.
- License: [GPL-3.0](https://api.github.com/repos/nano-muse/nanoMuse/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/nano-muse/nanoMuse/blob/57f5c5abed2d66fa19ab8fc39fd52eb365e4f14d/README.md#L80).

<a id="moltis-org--moltis"></a>

## [Moltis](https://github.com/moltis-org/moltis)

Personal agent service integrating memory, voice, messaging, browser and scheduling.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: cron.
- Boundary: Models and the needed integrations must be configured by the user.
- Current maintenance status: Commits within the last 90 days; 0 commits / 30 days, 49 commits / 90 days.
- License: [MIT](https://api.github.com/repos/moltis-org/moltis/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md#L28).

<a id="nearai--ironclaw"></a>

## [IronClaw](https://github.com/nearai/ironclaw)

Rust personal assistant that runs background tasks through routines and heartbeat.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled / events / heartbeat.
- Boundary: Tool isolation is a design feature, not a claim that this list has audited its security.
- Current maintenance status: Commits within the last 90 days; 0 commits / 30 days, 44 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/nearai/ironclaw/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md#L95).

<a id="afk-surf--comma"></a>

## [Comma](https://github.com/AFK-surf/Comma)

Combines persistent task state with cross-device work, waking the agent through a monitoring loop.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: routines / event loops.
- Boundary: The cloud runtime environment and local device connections are separate components.
- Current maintenance status: Commits within the last 90 days; 2 commits / 30 days, 10 commits / 90 days.
- License: [AGPL-3.0](https://api.github.com/repos/AFK-surf/Comma/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/AFK-surf/Comma/blob/66ab3dc92475005aea9afd123df36a28e4ef86ab/README.md#L64).

<a id="sipeed--picoclaw"></a>

## [PicoClaw](https://github.com/sipeed/picoclaw)

Go personal assistant for low-resource devices, with file, execution and scheduling tools.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled.
- Boundary: A low-resource runtime does not mean the invoked models or browser are equally low-cost.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/sipeed/picoclaw/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md#L632).

<a id="khoj-ai--khoj"></a>

## [Khoj](https://github.com/khoj-ai/khoj)

Personal knowledge assistant with document and web research plus scheduled automations.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: scheduled automations.
- Boundary: Focused on knowledge and information work, not a general desktop controller.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [AGPL-3.0](https://api.github.com/repos/khoj-ai/khoj/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md#L50) · [Source 2](https://docs.khoj.dev/features/automations) · [Source 3](https://docs.khoj.dev/features/automations).

<a id="mikeyobrien--rho"></a>

## [rho](https://github.com/mikeyobrien/rho)

Pi-based resident personal operations assistant with persistent memory and periodic proactive checks.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: heartbeat.
- Boundary: It is an application layer above Pi; Android and desktop run it differently.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/mikeyobrien/rho/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/mikeyobrien/rho/blob/073a3ee8a5dc0efd5dd32d773a760575ed38abc7/README.md#L34).

<a id="maikunari--mame"></a>

## [Mame](https://github.com/maikunari/mame)

Lightweight resident assistant with persistent memory and messaging channels that can orchestrate coding agents.

- Category: Resident personal assistants and lightweight runtimes; proactive mechanism documented.
- Trigger: cron / heartbeat.
- Boundary: Best treated as a small implementation reference; the maintenance score does not indicate maturity.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [README declares MIT](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md); License full text not found; kept as a candidate and excluded from the open-license shortlist.
- Feature verified: 2026-11-05; [Source 1](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md#L300).

<a id="copilotkit--openbot"></a>

## [OpenBot](https://github.com/CopilotKit/OpenBot)

Self-hosted AI coworker platform giving AG-UI agents a dedicated browser, file workspace, tool permissions, audit logs and scheduled tasks.

- Category: Workspace and context assistants; proactive mechanism documented.
- Trigger: scheduled routines / user-initiated.
- Boundary: OpenBot handles the computer environment, policy, auditing and scheduling; agent capability comes from the connected AG-UI endpoint, and persistent sessions and memory depend on CopilotKit Intelligence.
- Current maintenance status: Commits within the last 90 days; 1044 commits / 30 days, 1449 commits / 90 days.
- License: [MIT](https://api.github.com/repos/CopilotKit/OpenBot/license); Identified via GitHub licenseInfo; deployment and license terms of CopilotKit Intelligence count separately.
- Feature verified: 2026-11-05; [Source 1](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L251) · [Source 2](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L52).

<a id="agent0ai--agent-zero"></a>

## [Agent Zero](https://github.com/agent0ai/agent-zero)

Agent that runs tools, projects and periodic monitoring tasks inside a computer execution environment.

- Category: Workspace and context assistants; proactive mechanism documented.
- Trigger: scheduled operations.
- Boundary: Bounded by the configured execution environment; it does not control all host resources by default.
- Current maintenance status: Commits within the last 90 days; 108 commits / 30 days, 438 commits / 90 days.
- License: [MIT](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE); Root LICENSE file verified manually.
- Feature verified: 2026-11-05; [Source 1](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md#L259).

<a id="anil-matcha--suparagent"></a>

## [Suparagent](https://github.com/Anil-matcha/suparagent)

Desktop and self-hosted workspace centralizing named AI coworkers, team delegation, conversations, memory, routines, tasks and approvals.

- Category: Workspace and context assistants; proactive mechanism documented.
- Trigger: scheduled / webhook / manual routines.
- Boundary: The project is still in early development; self-hosted services and computer/browser capabilities are experimental; the hosted version is a separate product; models and accounts must be provided by the user; some integrations support only Claude or Codex.
- Current maintenance status: Commits within the last 90 days; 446 commits / 30 days, 817 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/Anil-matcha/suparagent/license); Identified via GitHub licenseInfo; the hosted service, third-party engines, Composio and model providers follow their own terms.
- Feature verified: 2026-11-11; [Source 1](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L3) · [Source 2](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L71) · [Source 3](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L183).

<a id="openbmb--pilotdeck"></a>

## [PilotDeck](https://github.com/OpenBMB/PilotDeck)

Isolates files, memory and skills per workspace, with background task discovery and file delivery.

- Category: Workspace and context assistants; proactive mechanism documented.
- Trigger: always-on task discovery.
- Boundary: The benchmarks in the README are author-reported; this repository does not fold them into cross-project capability rankings.
- Current maintenance status: Commits within the last 90 days; 468 commits / 30 days, 960 commits / 90 days.
- License: [AGPL-3.0](https://api.github.com/repos/OpenBMB/PilotDeck/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/OpenBMB/PilotDeck/blob/2865f05b1722c7473ea8a9dda317a92fb8c92dd8/README.md#L97).

<a id="copilotkit--openfuse"></a>

## [OpenFuse](https://github.com/CopilotKit/openfuse)

Open-source app with a personal agent interface, browser and workspace.

- Category: Workspace and context assistants; adjacent capability.
- Trigger: background task worker; autonomous triggering unverified.
- Boundary: A background worker is not autonomous initiation; some connectors and actions are still on the roadmap.
- Current maintenance status: Commits within the last 90 days; 3 commits / 30 days, 147 commits / 90 days.
- License: [MIT](https://api.github.com/repos/CopilotKit/openfuse/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/CopilotKit/openfuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md#L43).

<a id="copilotkit--openduet"></a>

## [OpenDuet](https://github.com/CopilotKit/OpenDuet)

Open-source app template for building proactive work assistants.

- Category: Workspace and context assistants; proactive mechanism documented.
- Trigger: routines / background suggestions.
- Boundary: The template needs its dependencies and models configured; it is not a deployed hosted service.
- Current maintenance status: Commits within the last 90 days; 24 commits / 30 days, 92 commits / 90 days.
- License: [MIT](https://api.github.com/repos/CopilotKit/OpenDuet/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/CopilotKit/OpenDuet/blob/f52288fff5ccdbd3de428d573d9f026fce5ff480/README.md#L5).

<a id="volcengine--minecontext"></a>

## [MineContext](https://github.com/volcengine/MineContext)

Proactive information assistant that turns screen context into insights, to-dos and daily/weekly summaries.

- Category: Workspace and context assistants; adjacent capability.
- Trigger: context observation / proactive push.
- Boundary: Proactive suggestions are documented; that does not establish autonomous operation of all apps.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/volcengine/MineContext/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/README.md#L9).

<a id="fei-craft--ds-bot"></a>

## [DS Bot](https://github.com/Fei-Craft/DS-Bot)

Extends DeepSeek Harness into a desktop app and plugin with memory, group chat and bot collaboration.

- Category: Proactive plugins and scheduling extensions; adjacent capability.
- Trigger: persistent bot / group chat; autonomous wake-up unverified.
- Boundary: The homepage does not confirm an independent scheduling mechanism; long-lived sessions must not be equated with proactive initiation.
- Current maintenance status: Commits within the last 90 days; 2844 commits / 30 days, 3858 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/Fei-Craft/DS-Bot/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/Fei-Craft/DS-Bot/blob/71d344bf193f3f18185f25de3d8e5c483046910a/README.md#L41).

<a id="john-walks-slow--dsh-proactive"></a>

## [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive)

Adds proactive wake-ups to DeepSeek Harness that can still fire after a session cools down.

- Category: Proactive plugins and scheduling extensions; proactive mechanism documented.
- Trigger: host-level once / interval / cron.
- Boundary: Depends on the host running and on version compatibility; includes do-not-disturb and notification-budget settings.
- Current maintenance status: Commits within the last 90 days; 0 commits / 30 days, 97 commits / 90 days.
- License: [MIT](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/packages/dsh-proactive/LICENSE); Plugin subdirectory LICENSE verified manually.
- Feature verified: 2026-11-05; [Source 1](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/README.md#L1).

<a id="t0dorakis--murmur"></a>

## [murmur](https://github.com/t0dorakis/murmur)

Lightweight scheduling daemon that periodically starts CLI sessions such as Claude, Codex and Pi.

- Category: Proactive plugins and scheduling extensions; proactive mechanism documented.
- Trigger: cron / interval.
- Boundary: Message delivery and business actions are performed by the prompt and the invoked agent.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/t0dorakis/murmur/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/t0dorakis/murmur/blob/d666df4c749c28ecb775613ecec8b12954b387e7/README.md#L10).

<a id="hypostas--pulse"></a>

## [Pulse](https://github.com/Hypostas/pulse)

Extension daemon that wakes OpenClaw based on changes, goals and urgency.

- Category: Proactive plugins and scheduling extensions; proactive mechanism documented.
- Trigger: sensing / urgency-triggered.
- Boundary: Depends on the OpenClaw webhook; the author's autonomy claims are not conclusions tested by this repository.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/Hypostas/pulse/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/Hypostas/pulse/blob/4bebd1e23bff218dde1cd0b693f901493d45f972/README.md#L5).

<a id="nousresearch--hermes-bot-mode"></a>

## [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode)

Adds named bots, separate conversations and a periodic-task panel to the Hermes desktop app.

- Category: Proactive plugins and scheduling extensions; historical reference.
- Trigger: host cron routines.
- Boundary: Archived on GitHub; kept as a reference for the Hermes bot UI and cron integration, not recommended as an active plugin.
- Current maintenance status: Archived / historical; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/NousResearch/Hermes-Bot-Mode/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/NousResearch/Hermes-Bot-Mode/blob/80fee22582b871b9765a65e2992b8b5a8211c9f8/README.md#L23).

<a id="earendil-works--pi"></a>

## [Pi](https://github.com/earendil-works/pi)

Extensible agent harness for building resident assistants via SDK, RPC and plugins.

- Category: Extensible harnesses and persistent runtime bases; adjacent capability.
- Trigger: needs upstream scheduling / extensions.
- Boundary: The old address badlogic/pi-mono now redirects; can be paired with rho or murmur.
- Current maintenance status: Commits within the last 90 days; 1378 commits / 30 days, 2364 commits / 90 days.
- License: [MIT](https://api.github.com/repos/earendil-works/pi/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/earendil-works/pi/blob/fcebc099565d8f30c15b321ff6a1af5f34d89400/README.md#L15).

<a id="deepseek-ai--deepseek-harness"></a>

## [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

Agent execution base with a plugin architecture, suited to attaching bots and proactive wake-up plugins.

- Category: Extensible harnesses and persistent runtime bases; adjacent capability.
- Trigger: needs host plugins to provide the proactive mechanism.
- Boundary: Developer preview; plugin compatibility needs verification.
- Current maintenance status: Commits within the last 90 days; 3743 commits / 30 days, 14426 commits / 90 days.
- License: [MIT](https://api.github.com/repos/deepseek-ai/deepseek-harness/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/README.md#L7).

<a id="letta-ai--letta-code"></a>

## [Letta Code](https://github.com/letta-ai/letta-code)

Agents with persistent memory that form a resident assistant through remote environments and channels.

- Category: Extensible harnesses and persistent runtime bases; proactive mechanism documented.
- Trigger: remote environments / cron.
- Boundary: Official migration target for LettaBot; needs remote environments plus scheduling configuration.
- Current maintenance status: Commits within the last 90 days; 362 commits / 30 days, 978 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/letta-ai/letta-code/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/letta-ai/letta-code/blob/e6d6cc27ef1111da80e919dc1cef179613894b66/README.md#L29) · [Source 2](https://docs.letta.com/letta-code/scheduling) · [Source 3](https://docs.letta.com/letta-code/scheduling).

<a id="browser-use--browser-use"></a>

## [Browser Use](https://github.com/browser-use/browser-use)

Gives agents web-page understanding and browser execution.

- Category: Computer and browser control components; adjacent capability.
- Trigger: on-demand browser tasks.
- Boundary: Primarily browser-scoped; does not establish proactive scheduling or full desktop control.
- Current maintenance status: Commits within the last 90 days; 639 commits / 30 days, 954 commits / 90 days.
- License: [MIT](https://api.github.com/repos/browser-use/browser-use/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md#L1).

<a id="cursortouch--windows-mcp"></a>

## [Windows-MCP](https://github.com/CursorTouch/Windows-MCP)

MCP service exposing Windows computer-operation capabilities to agents.

- Category: Computer and browser control components; adjacent capability.
- Trigger: invoked by the host.
- Boundary: The control component is not itself a resident personal assistant; models, memory and triggers must be attached externally.
- Current maintenance status: Commits within the last 90 days; 110 commits / 30 days, 180 commits / 90 days.
- License: [MIT](https://api.github.com/repos/CursorTouch/Windows-MCP/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/CursorTouch/Windows-MCP/blob/9ab92bca2772dfb53ae3ed4feb98dac22c5b3dea/README.md#L25).

<a id="alibaba--page-agent"></a>

## [Page Agent](https://github.com/alibaba/page-agent)

JavaScript agent that controls the interface in natural language inside a web page.

- Category: Computer and browser control components; adjacent capability.
- Trigger: invoked by the page or host.
- Boundary: A page-control layer; it has no full resident-assistant lifecycle.
- Current maintenance status: Commits within the last 90 days; 22 commits / 30 days, 40 commits / 90 days.
- License: [MIT](https://api.github.com/repos/alibaba/page-agent/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/alibaba/page-agent/blob/9eb6b6646500264d9034dd466a4270cb9fc1ef1e/README.md#L35).

<a id="bytedance--ui-tars-desktop"></a>

## [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop)

Agent applications and related tooling for GUI and browser operation.

- Category: Computer and browser control components; adjacent capability.
- Trigger: on-demand computer / browser tasks.
- Boundary: Automated computer-task execution and unprompted proactive initiation are two different dimensions.
- Current maintenance status: Archived / historical; 0 commits / 30 days, 8 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/bytedance/UI-TARS-desktop/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md#L13).

<a id="xlang-ai--osworld"></a>

## [OSWorld](https://github.com/xlang-ai/OSWorld)

Evaluates multimodal agent execution in real computer environments.

- Category: Research implementations and evaluation code; research resource.
- Trigger: real-computer task evaluation.
- Boundary: Measures task execution; on its own it does not measure proactive initiation or interruption timing.
- Current maintenance status: Commits within the last 90 days; 70 commits / 30 days, 213 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/xlang-ai/OSWorld/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/xlang-ai/OSWorld/blob/8903ebeb0efdf74331bd7dc37ed91ccbbff22317/README.md#L294).

<a id="zju-real--knowu-bench"></a>

## [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)

Evaluates mobile agents on eliciting preferences, proactive intervention and asking for consent.

- Category: Research implementations and evaluation code; research resource.
- Trigger: interactive personalized mobile evaluation.
- Boundary: Focused on mobile GUI and personal preferences, not an all-platform runtime.
- Current maintenance status: Commits within the last 90 days; 1 commits / 30 days, 1 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/ZJU-REAL/KnowU-Bench/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/ZJU-REAL/KnowU-Bench/blob/c03a825991ede13add6631f2ed19b90755930dc6/README.md#L4).

<a id="facebookresearch--memo-pro-agent"></a>

## [MemoProAgent](https://github.com/facebookresearch/Memo-Pro-Agent)

Research on deciding whether to intervene proactively by retrieving evidence from long-term personal memory.

- Category: Research implementations and evaluation code; research resource.
- Trigger: memory-driven intervention evaluation.
- Boundary: Early paper name was ProPerAgent; deduplicated under the same arXiv ID.
- Current maintenance status: Commits within the last 90 days; 0 commits / 30 days, 6 commits / 90 days.
- License: [CC-BY-NC-4.0](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/LICENSE); Non-commercial license; listed as research source code only.
- Feature verified: 2026-11-05; [Source 1](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/README.md#L3).

<a id="simplified-reasoning--pi-bench"></a>

## [π-Bench](https://github.com/Simplified-Reasoning/Pi-Bench)

Evaluates hidden-need recognition and proactive assistance in long multi-turn workflows.

- Category: Research implementations and evaluation code; research resource.
- Trigger: proactivity evaluation.
- Boundary: This is a benchmark; unrelated to the Pi harness.
- Current maintenance status: Commits within the last 90 days; 0 commits / 30 days, 1 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/Simplified-Reasoning/Pi-Bench/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/Simplified-Reasoning/Pi-Bench/blob/4f545be5d289b28ff022d2904d455007358ed3b7/README.md#L1).

<a id="thunlp--proactiveagent"></a>

## [ProactiveAgent](https://github.com/thunlp/ProactiveAgent)

Proactive task-prediction method with its dataset and evaluation code.

- Category: Research implementations and evaluation code; research resource.
- Trigger: event observation / task prediction.
- Boundary: A research implementation, not an out-of-the-box general personal assistant.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/thunlp/ProactiveAgent/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/thunlp/ProactiveAgent/blob/3fcf9beebe256b86871659fbb12541c41c9381b9/README.md#L2).

<a id="xzf-thu--pask"></a>

## [PASK](https://github.com/xzf-thu/Pask)

Research on proactive assistance combining long-term memory, continuous context and latency constraints.

- Category: Research implementations and evaluation code; research resource.
- Trigger: latent need detection / staying silent.
- Boundary: A technical report with research code; practical maturity needs separate validation.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/xzf-thu/Pask/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/xzf-thu/Pask/blob/d54646c52b1555232ce4ab39103768d7f65b8267/README.md#L30).

<a id="deepakn97--pare"></a>

## [PARE](https://github.com/deepakn97/pare)

Evaluates proactive assistants by simulating active users and a stateful digital environment.

- Category: Research implementations and evaluation code; research resource.
- Trigger: proactive assistant / user-simulation evaluation.
- Boundary: Simulated users do not equal long-term results with real users.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/deepakn97/pare/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/deepakn97/pare/blob/261149914a9e9dcacb12de620575c691d50e3c2e/README.md#L3).

<a id="tdemin16--proactivebench"></a>

## [ProactiveBench (MLLM)](https://github.com/tdemin16/proactivebench)

Research benchmark evaluating how multimodal models proactively gather useful information.

- Category: Research implementations and evaluation code; research resource.
- Trigger: multimodal proactivity evaluation.
- Boundary: Distinct from the identically named benchmark used by ProactiveAgent; the official paper page notes ECCV 2026.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [MIT](https://api.github.com/repos/tdemin16/proactivebench/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/tdemin16/proactivebench/blob/428885c9224418b544dfbdbde5307bccc58018d5/README.md#L2).

<a id="openaiotlab--contextagent"></a>

## [ContextAgent](https://github.com/openaiotlab/ContextAgent)

Research on judging proactive service and tool invocation from open-world sensory perception.

- Category: Research implementations and evaluation code; research resource.
- Trigger: sensory context / service prediction.
- Boundary: Research data and tool scenarios cannot be generalized directly to arbitrary desktops.
- Current maintenance status: No commits for 91–365 days; 0 commits / 30 days, 0 commits / 90 days.
- License: [Pending verification](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md); LICENSE not found; listed as a research resource only, no grant inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md#L3).

<a id="letta-ai--lettabot"></a>

## [LettaBot](https://github.com/letta-ai/lettabot)

Formerly provided messaging channels, memory, heartbeat and scheduled tasks as a personal assistant.

- Category: Historical and migration projects; historical reference.
- Trigger: heartbeat / cron.
- Boundary: The official README announces it is no longer actively maintained and recommends migrating to Letta Code.
- Current maintenance status: Archived / historical; 0 commits / 30 days, 0 commits / 90 days.
- License: [Apache-2.0](https://api.github.com/repos/letta-ai/lettabot/license); Identified via GitHub licenseInfo; licenses of attached data or model weights are not inferred.
- Feature verified: 2026-11-05; [Source 1](https://github.com/letta-ai/lettabot/blob/99c3b5dd73550fe0a4eac2ee31b1c3229ca9e550/README.md#L8).
