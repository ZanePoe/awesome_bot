# Turning an existing agent into a proactive assistant

Choose the execution base first, then add triggers, persistent state and result delivery. Adding a lone cron solves scheduled starts; it does not automatically grant need inference or standing-goal management.

| Existing base | Path to investigate | Verified mechanism | Current boundary |
| --- | --- | --- | --- |
| Pi | [rho](https://github.com/mikeyobrien/rho) | resident running, persistent memory, heartbeat | An application layer above Pi; check the run platforms and the maintenance snapshot |
| Pi / Claude / Codex CLI | [murmur](https://github.com/t0dorakis/murmur) | periodic CLI wake-ups defined as Markdown tasks | Delivery and business actions are still performed by the invoked agent |
| DeepSeek Harness | [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive) | host-level scheduled wake-ups of cold sessions, silent wrap-up | Match DSH / plugin versions; the host must still be running |
| DeepSeek Harness | [DS Bot](https://github.com/Fei2411/DS-Bot) | persistent named bots, group chat and memory | The homepage does not confirm an independent timer; combinations with other plugins are untested |
| Hermes Agent | [built-in cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | unattended scheduled tasks and channel delivery | Prefer the built-in mechanism first; this directory has not deployed it for users |
| Hermes desktop | [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | bot UI + host cron routines | Archived now; kept for design and code reference only |
| OpenClaw | [Pulse](https://github.com/Hypostas/pulse) | webhook wake-ups driven by sensing and urgency | Depends on the host; does not replace all cron functionality |
| Letta | [Letta Code](https://github.com/letta-ai/letta-code) + [scheduling](https://docs.letta.com/letta-code/scheduling) | persistent agents, remote environments, self-managed schedules | LettaBot is deprecated; prefer the official new path for migration |
| Any MCP-capable host | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | Windows operation tools | Only patches the execution layer; triggers, state and delivery are still needed |

The rows above are combination entry points confirmed by public documentation, not a compatibility integration-test report. For first validation, use "generate one file in an isolated directory at a specified time" as the minimal task, then check whether the assistant stays silent when nothing changed and whether tasks duplicate after a restart.

Evidence, licenses and verification dates for every project are in [project details](projects.md).
