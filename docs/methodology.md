# Ranking methodology

## Metric sources

`scripts/refresh_metrics.py` uses the GitHub GraphQL API through a logged-in `gh` or `GH_TOKEN` against public repositories. One collection uses a fixed UTC moment, reads all projects in batches, and only atomically replaces `data/metrics.json` when every batch succeeds. A partial failure never writes unknown values as zero and never overwrites the previous complete snapshot.

- `stars`: the `stargazerCount` at collection time.
- `commits_30d / commits_90d`: `history.totalCount` over the default-branch reachable history inside the matching UTC window, including merge and bot commits. First-page counts are never passed off as complete totals.
- `last_commit_at`: the `committedDate` of the default-branch HEAD, used for freshness; the SHA is stored alongside.
- `pushed_at`: the most recent push is stored separately and may come from other branches; it is never used to masquerade as default-branch code updates.
- `updated_at`: the repository-metadata update time is stored separately and does not enter the freshness score.
- `latest_release`: the most recently created release node and its pre-release flag; missing means null, and a missing release is never read as abandonment.
- `archived / disabled`: repository status returned by the API.
- `license_review`: the license judgement made during manual feature verification, kept separate from `license_spdx` collected at refresh time. Licenses change with the project, so a metadata refresh does not re-audit license texts.

The first collection day was 2026-11-05 Beijing time; machine-readable times use UTC, so the displayed 2026-11-04 is not a date error.

## Maintenance status first, then the composite score

Within the same category, projects are first split into four tiers:

1. Default-branch commits within the last 90 days.
2. 91–365 days since the last default-branch commit.
3. Over 365 days without a new default-branch commit.
4. Archived, disabled, or explicitly historical-reference projects.

Within a tier, the composite ordering is:

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
maintenance score = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Stars weigh 40%, 90-day development activity 35%, and last-commit freshness 25%. Logarithms with fixed caps soften the dominance of very large repositories; fixed anchors mean a new entry never changes the scores of existing ones. A higher score means stronger popularity and maintenance signals under this definition.

Ties compare stars first, then sort by repository name for a stable order. The score itself deducts nothing for archival; the maintenance tier pushes archived projects to the end instead. This keeps the raw numbers visible and the rule recomputable.

The [ranking views](rankings.md) additionally provide three single-metric views — stars, 90-day commits and latest commit — all keeping the maintenance-status tiers. For raw untiered values, sort the [JSON](../data/metrics.json) or [CSV](../data/rankings.csv) yourself.

## What must not be inferred from this

Stars measure attention and commits proxy activity; automated commits, documentation commits, merge strategy and monorepos inflate the counts. A quiet default branch does not necessarily mean the software is unusable. Small, stable projects may be underestimated by this formula, and research code usually need not update daily.

This list did not run every agent and provides no success-rate, cost, speed, safety or "smartest" score. Different papers use different models, tasks and budgets; their best reported numbers cannot be stitched into a cross-system capability leaderboard.

## Planned unified evaluation design

Choose the same model, budget, test accounts and isolated working directories, pin versions, and cover at least the following scenarios, reporting sample sizes:

| Scenario | Observed metrics |
| --- | --- |
| Fetch information on a schedule and generate a file | actual trigger rate, lateness, delivery success rate |
| Two event groups: environment unchanged vs changed | correct-intervention rate, false-positive rate, missed-event rate, useless notifications |
| A new user preference takes effect across sessions | memory accuracy, stale-memory usage rate |
| Tasks spanning browser and files | success rate, count of required human takeovers |
| Restart, network errors and pause/resume | lost tasks, duplicate executions, recovery time |
| Actions that explicitly require asking consent | correct-wait ratio, out-of-authority action count |

These are test plans, not results already obtained.
