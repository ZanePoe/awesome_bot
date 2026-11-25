# Scope and taxonomy

## Working definition

A proactive agent can start a round of judgement without a new user instruction — because of a plan, an external change, a standing goal or an environment observation; within an explicitly granted scope it calls tools, keeps state, and decides whether to report back to a human. It may use a local computer, a container, a remote computer or an API; holding "unlimited permission over the whole computer" is not an entry requirement.

Inclusion checks for a complete assistant: a publicly locatable implementation; an identifiable non-manual trigger mechanism; real output through tools or information services; persistent task state, memory or sessions. Marketing use of "autonomous" alone, a background worker alone, or manual tool calling alone is not enough to enter the core recommendations automatically.

## Two independent classification axes

The first axis is where the project sits in the system. Each project has exactly one primary category, so cross-category double counting is avoided.

| Category | Deciding question | Representative seeds / projects |
| --- | --- | --- |
| Resident personal assistants and lightweight runtimes | Can it run directly as a long-term personal assistant? | nanoMuse, Rakazo, OpenClaw |
| Workspace and context assistants | Is it centred on project environments, screen observation or workflows? | PilotDeck, MineContext |
| Proactive plugins and scheduling extensions | Does it mainly give existing agents bots, wake-ups or scheduling? | DS Bot, dsh-proactive, murmur |
| Extensible harnesses and persistent runtime bases | Does it provide agent execution infrastructure for upper-layer apps to orchestrate? | Pi, DeepSeek Harness, Letta Code |
| Computer and browser control components | Does it mainly provide external-environment operation? | Windows-MCP, Browser Use |
| Research implementations and evaluation code | Is it mainly for reproducing experiments, training or evaluation? | ProactiveAgent, π-Bench, OSWorld |
| Historical and migration projects | Has the official party announced end of maintenance, with migration value? | LettaBot |

The second axis is the trigger mechanism: fixed time / cron, periodic heartbeat, events / webhooks, contextual need inference, long-horizon goal continuation, or an external trigger being required. Several mechanisms can coexist.

`core` means the proactive mechanism is documented; `adjacent` means adjacent capability or an unverified proactive trigger; `research` means research use; `historical` means historical reference. These are catalogue labels, not quality grades.

## Boundaries learned from the five reference projects

- [nanoMuse](https://github.com/nano-muse/nanoMuse): personal memory, background goals and cross-device execution.
- [Rakazo](https://github.com/elie222/rakazo): persistent bots, memory, routines and a computer environment.
- [PilotDeck](https://github.com/OpenBMB/PilotDeck): organizes long-running tasks and background work per workspace.
- [DS Bot](https://github.com/Fei2411/DS-Bot): persistent bots and a harness plugin; the homepage does not confirm independent scheduling, so "long-lived" is not directly accepted as "proactively initiated".
- [Windows-MCP](https://github.com/CursorTouch/Windows-MCP): an execution-layer component. Being able to control the computer does not mean perceiving tasks or waking up on a schedule by itself.

Pinned-commit sources for these judgements are in [project details](projects.md). The core list allows new projects with low stars; there is no hard traffic threshold such as one thousand stars.

## Exclusions and retentions

Pure chat interfaces, concept pages without concrete implementations, ordinary scheduled scripts, model-weight-only releases, and robot navigation or game co-op unrelated to proactive interaction with a personal/digital environment do not enter the core assistant list. The commercial closed-source Muse and Grok Bot serve only as search references and are not disguised as open-source entries.

Papers on adjacent long-term memory, computer execution and simulated-agent foundations may be included, but their boundaries must be stated. When research source code has an unclear license or non-commercial restrictions, it is a research lead only and is never labelled a project with a verified open license.

## Testable behaviour levels

These are labels for later testing; the first release does not actually score projects on them:

1. **On-demand execution**: given an explicit instruction, completes a single tool task.
2. **Autonomous wake-up**: with no new user messages, a preset time or event can trigger work.
3. **Conditional intervention**: under the same trigger, acts/notifies when there is something to do and stays silent when there is not.
4. **Standing goals**: keeps state across wake-ups, advances a goal, and handles failure and pausing.

Passing level 4 does not mean a higher level-1 task success rate; the levels cannot replace concrete scenario evaluation.
