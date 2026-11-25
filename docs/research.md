# Search method and coverage log

This round followed a three-pass loop: "reference projects → feature keywords → web-wide and GitHub search → catalogue gap-filling → primary-source verification". The deliverable is a first-release curated directory; the stopping reason is the preset three-pass boundary, **not a claim of having searched exhaustively**. The third pass still surfaced new sources, so the work can keep expanding.

## Search terms distilled from the reference projects

| Trait | English keywords | Chinese keywords |
| --- | --- | --- |
| Does not wait for a new instruction | proactive agent, anticipatory assistant, initiative | 主动式智能体、主动助手、需求预判 |
| Long-lived presence | always-on, persistent agent, sessionless, background agent | 常驻助手、持久 Agent、后台运行 |
| Autonomous wake-up | heartbeat, cron, scheduler, event-driven, webhook, routines | 心跳、定时、事件驱动、周期任务 |
| Real action | computer use, desktop automation, browser agent, MCP | 电脑操作、桌面自动化、浏览器 Agent |
| Understanding across time | long-term memory, user context, personalization, long-horizon | 长期记忆、用户上下文、个性化、长期目标 |
| Retrofitting existing bases | harness, plugin, extension, Pi, Hermes, DeepSeek Harness | Harness 插件、扩展、二次开发 |
| Proactivity research | proactive assistance benchmark, intervention timing, abstention | 主动辅助评测、介入时机、保持静默 |

The generic term autonomous agent easily returns one-shot executors, game bots and ordinary workflows; mechanism words such as heartbeat / routines / persistent narrow the set before READMEs are verified. Grok Bot / Muse were used for product-category discovery; open-source status is always decided by the repository and license.

## The three passes

| Pass | Search/verification batches | Logged results | New sources | New-source rate |
| --- | --- | --- | --- | --- |
| 1 | 12 | 228 | 220 | 96.5% |
| 2 | 6 | 53 | 42 | 79.2% |
| 3 | 4 | 171 | 138 | 80.7% |

The search log holds 22 batches in total: one catalogue-link harvest, two GitHub-native repository-search expansions, plus batch verification of original repositories and papers. They are not 22 independent internet keywords, and not all 400 results were suitable for inclusion.

- Pass one covered eight search axes: semantics, official docs, curated lists, repositories, alternatives, benchmarks, limitations and recent changes. The catalogue harvest capped at 100 links; web search typically recorded up to 20 results per query group.
- Pass two added new names surfaced by the results — rho, murmur, Pulse, PASK, ProAgentBench, PIRA-Bench and others — verifying complete assistants and harness extensions.
- Pass three used GitHub-native search to fill gaps, then returned to the official README, GitHub GraphQL metrics and paper abstract of every final entry. Feature evidence is pinned to commits.

Deduplication keys on normalized URL, canonical repo and arXiv ID. Mirror domains inside web results may still enter the research counts as distinct candidate sources; the final project/paper catalogue is deduplicated on the entity keys above. The new-source rate is a search-process metric; it says nothing about relevance or project quality.

All five original reference links are covered (5/5). Every one of the eight search axes produced relevant leads, but that does not mean each subfield is fully covered. There was no independent user study and no hardware run-through; features are reported as the authors document them.

## Content factory

Structured search was called through the curl path of the `content-factory-search-api` skill, scoped to **2026-08-05 to 2026-11-05**, taking at most 30 items per group and at most 15 after deduplication.

This round's queries: `主动式 Agent`, `Grok Bot OR nanoMuse OR rakazo OR PilotDeck`, `Hermes Agent OR DeepSeek Harness OR Pi Agent`, `OpenClaw`, `Hermes`. All five requests returned valid JSON, but every result array was empty, so no content-factory material was used as evidence for the final entries; empty results do not prove these projects are absent from the library or the internet. No full-history query was run. Empty results require no vector-computation follow-up.

The public repository keeps only the search terms, date ranges and result statistics; private service addresses, keys and internal article text are not published.

## Primary-source corrections and limits

- The [LettaBot README](https://github.com/letta-ai/lettabot) explicitly announces it is no longer actively maintained, pointing to Letta Code for migration. GitHub metadata also shows the repository archived.
- [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) and its bot + cron design remain instructive, but the API showed it archived this round, so it stays as a historical reference.
- [Pi](https://github.com/earendil-works/pi) uses the current canonical repository address; the old address `badlogic/pi-mono` is not listed a second time.
- [MemoProAgent](https://arxiv.org/abs/2610.22671) is the current version's title for the same paper; the old name ProPerAgent is not listed separately. Its research code carries a non-commercial license condition, so it is excluded from the open-license recommendations.
- The current [ProactiveBench](https://arxiv.org/abs/2603.19466) paper page notes ECCV 2026; the ICLR 2026 tag carried by curated lists is not repeated, and it is not confused with the identically named benchmark of ProactiveAgent.
- Mame's homepage declares MIT, but the full license text could not be located; ContextAgent has no LICENSE found. Both keep their verification gap: public visibility is not equated with license completeness.

## Not covered and next steps

Branches such as multimodal companions, industrial operations, home devices and vertical proactive learning yielded only leads and are not fully included in this first release. No comparison experiments were run against the closed-source Grok Bot / Muse features. Phone background keep-alive, cross-device reliability and specific plugin-combination compatibility still need hands-on testing. Best results across different papers were not compared, avoiding pseudo-rankings caused by different models, data and budgets.

The summary and classification of core mechanisms are editorial judgement. No ablation studies were run this round; "who degrades most if memory or scheduling is removed" cannot be answered. Stars and commit volume can support only a maintenance ranking.

## Verifiable files

- [Search log](../research/search-log.json): passes, search axes, queries, sources and result counts.
- [Classification and evidence decisions](../research/decisions.json): inclusion boundaries and pinned commit sources.
- [First metrics snapshot](../research/initial-metrics.json): preserved from the first collection; later daily updates do not overwrite it.
- [Current metrics snapshot](../data/metrics.json) and [ranking CSV](../data/rankings.csv): the latest recomputable rankings.
- [Research status](../research/status.json) and [completeness verification](../research/verification.json): no dangling evidence references or duplicate normalized-URL errors; the five zero-result queries are kept as known notices.

The full search-result text and local tool run logs stay on the machine and are not copied into the public repository. The 99 evidence/judgement records and 123 metric records in the research status are local audit counts; the public edition ships the linked decisions, original source URLs and metrics snapshots.
