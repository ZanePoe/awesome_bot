"""Render the curated catalogue and transparent metadata rankings without network access."""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'personal': '常驻个人助手与轻量运行时',
    'workspace': '工作空间与上下文助手',
    'extensions': '主动插件与调度扩展',
    'harness': '可扩展 Harness 与持久运行基础',
    'computer-use': '电脑与浏览器控制组件',
    'research': '研究实现与评测代码',
    'historical': '历史与迁移项目',
}
PAPER_CATEGORIES = {
    'foundations': '定义、机制与基础研究',
    'systems': '个人 Agent 系统',
    'memory': '长期记忆与潜在需求',
    'benchmarks': '主动性评测基准',
    'computer-use': '电脑操作与个性化执行',
    'reliability': '长期运行与可靠性研究',
}
SCOPE = {'core':'主动机制已文档化','adjacent':'相邻能力','research':'研究资源','historical':'历史参考'}

def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)

def age_days(metric, as_of):
    return max(0.0, (dt(as_of)-dt(metric['last_commit_at'])).total_seconds()/86400)

def score(metric, as_of):
    popularity = min(1, math.log1p(metric['stars']) / math.log1p(100000))
    activity = min(1, math.log1p(metric['commits_90d']) / math.log1p(500))
    freshness = math.exp(-age_days(metric, as_of)/90)
    return round(100 * (0.40*popularity + 0.35*activity + 0.25*freshness), 2)

def tier(project, metric, as_of):
    if metric['archived'] or metric['disabled'] or project['scope']=='historical': return 3
    age=age_days(metric, as_of)
    return 0 if age<=90 else 1 if age<=365 else 2

def status(project, metric, as_of):
    return ['近90天有提交','91–365天未提交','超过365天未提交','归档 / 历史'][tier(project,metric,as_of)]

def rank(projects, metrics, as_of, mode='balanced'):
    def key(p):
        m=metrics[p['repo']]
        primary={'balanced':-score(m,as_of),'stars':-m['stars'],'activity':-m['commits_90d'],'recent':-dt(m['last_commit_at']).timestamp()}[mode]
        return (tier(p,m,as_of),primary,-m['stars'],p['repo'].lower())
    return sorted(projects,key=key)

def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])

def anchor(repo): return repo.lower().replace('/','--').replace('_','-').replace('.','-')

def validate(projects,papers,snapshot):
    assert snapshot['schema_version']==1
    dt(snapshot['as_of'])
    repos=[p['repo'] for p in projects]
    assert len(repos)==len(set(r.lower() for r in repos)), 'Duplicate repositories'
    assert set(repos)==set(snapshot['repositories']), 'Snapshot/catalogue mismatch'
    for p in projects:
        assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo']), p['repo']
        assert p['category'] in CATEGORIES and p['scope'] in SCOPE
        assert p['description'] and p['boundary'] and p['trigger'] and p['evidence']
        assert all(e['url'].startswith('https://') for e in p['evidence'])
        assert p['license_review']['status'] in {'verified','source_available','unverified'}
        m=snapshot['repositories'][p['repo']]
        assert m['canonical_repo'].lower()==p['repo'].lower(), 'Resolve repository redirect explicitly'
        assert all(isinstance(m[k],int) and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d'])
        assert m['commits_30d']<=m['commits_90d']
        dt(m['last_commit_at'])
        assert re.fullmatch(r'[0-9a-f]{40}',m['head_sha'])
    assert len(papers)==len(set(p['id'] for p in papers)), 'Duplicate papers'
    for p in papers:
        assert p['category'] in PAPER_CATEGORIES and p['url']=='https://arxiv.org/abs/'+p['id']
        assert p['code_repo'] is None or p['code_repo'] in repos
        datetime.strptime(p['published'],'%Y-%m-%d')
    seeds={p['repo'] for p in projects if p.get('seed')}
    assert seeds=={'Fei2411/DS-Bot','CursorTouch/Windows-MCP','elie222/rakazo','OpenBMB/PilotDeck','nano-muse/nanoMuse'}

def render(projects,papers,snapshot):
    metrics=snapshot['repositories']; as_of=snapshot['as_of']
    reviewed_at=max(p['reviewed_at'] for p in projects)
    ordered=rank(projects,metrics,as_of)
    shortlist=[p for p in ordered if p['scope']=='core' and p['license_review']['status']=='verified' and tier(p,metrics[p['repo']],as_of)==0]
    intro=(ROOT/'docs/readme-intro.md').read_text(encoding='utf-8')
    readme=[intro, f'\n## 当前快照\n\n收录 **{len(projects)} 个项目 / 研究代码库、{len(papers)} 篇论文**。指标采集：**{as_of}（UTC）**；功能人工核验：{reviewed_at}。\n\n仅依据公开文档和 GitHub 元数据，尚未开展统一运行测评。类别与功能需人工复核，指标由脚本更新。', '\n## 活跃主动项目速览\n\n以下只从已核验开放许可证、主动机制已文档化、未归档项目中选取，按维护分排序；相邻组件、待核验许可和历史项目不进入此表。']
    def compact(p):
        m=metrics[p['repo']]
        return [f"[{p['name']}](https://github.com/{p['repo']})",p['trigger'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}"]
    readme.append(table(['项目','主动机制','Stars','90天提交','最近提交 UTC','维护分'],[compact(p) for p in shortlist[:10]]))
    readme.append('\n## 分类目录\n\n`★种子` 为用户提供的参考项目。所有分类内部使用相同排序规则，归档项目自动后置。许可显示以人工核验与 GitHub SPDX 识别为依据；未知不会当成零或默认 MIT。')
    detail=['# 项目说明与证据\n\n每项功能均为公开文档核验；没有安装运行或完成统一能力测试。证据尽量固定到核验时的提交，后续指标刷新不自动修改功能判断。\n']
    for category,label in CATEGORIES.items():
        group=[p for p in ordered if p['category']==category]
        readme.append(f'\n### {label}\n')
        rows=[]
        for p in group:
            m=metrics[p['repo']]; licence=p['license_review']['label']; state=status(p,m,as_of)
            tags=(' · ★种子' if p.get('seed') else '')+(' · 归档' if tier(p,m,as_of)==3 else '')
            if p['license_review']['status']!='verified':tags+=' · 许可限制/待核验'
            rows.append([f"[{p['name']}](https://github.com/{p['repo']}){tags}",p['trigger'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}",licence])
            evidence=' · '.join(f"[来源{i+1}]({e['url']})" for i,e in enumerate(p['evidence']))
            detail.extend([f'\n<a id="{anchor(p["repo"])}"></a>\n\n## [{p["name"]}](https://github.com/{p["repo"]})',f"\n{p['description']}\n\n- 分类：{label}；{SCOPE[p['scope']]}。\n- 触发方式：{p['trigger']}。\n- 边界：{p['boundary']}\n- 当前维护状态：{state}；{m['commits_30d']} 次 / 30 天，{m['commits_90d']} 次 / 90 天。\n- 许可：[{licence}]({p['license_review']['source']})；{p['license_review']['note']}。\n- 功能核验：{p['reviewed_at']}；{evidence}。"])
        readme.append(table(['项目','机制 / 定位','Stars','90天提交','最近提交 UTC','维护分','许可'],rows))
    readme.append('\n完整描述、边界与证据见 [项目详表](docs/projects.md)。按 star、活跃度、最新提交分别查看 [排序表](docs/rankings.md)。\n\n## 论文\n\n论文按问题分类，同类按首次提交日期倒序。论文年份、项目 star 与系统能力不是同一种评价，不混合计算。')
    paperdoc=['# 论文目录\n\n依据 arXiv 原始摘要页核验标题和首次提交日期（2026-11-05）。同一 arXiv ID 的版本/更名只计一篇。没有独立核验的会议状态保留为 arXiv。\n']
    for category,label in PAPER_CATEGORIES.items():
        group=sorted([p for p in papers if p['category']==category],key=lambda p:(p['published'],p['id']),reverse=True)
        rows=[]
        for p in group:
            rows.append([p['published'],f"[{p['title']}]({p['url']})",p['summary']])
            code=f"[代码](https://github.com/{p['code_repo']})" if p['code_repo'] else '尚未在本轮核验代码链接'
            paperdoc.extend([f"\n## [{p['title']}]({p['url']})",f"\n- 类别：{label}；首次提交：{p['published']}；{p['publication_note']}。\n- 研究问题：{p['summary']}\n- 阅读边界：{p['boundary']}\n- 资源：{code}。"])
        readme.append(f'\n### {label}\n\n'+table(['首次提交','论文','关注问题'],rows))
    readme.append('\n论文版本、代码关联与适用边界见 [论文详表](docs/papers.md)。\n\n## 维护与贡献\n\n- [定义、纳入标准与分类](docs/taxonomy.md)\n- [排序公式与局限](docs/methodology.md)\n- [检索词、来源与调研覆盖](docs/research.md)\n- [基于现有 Harness 的扩展路线](docs/harness-guide.md)\n- [贡献方式](CONTRIBUTING.md)\n\n```sh\npython scripts/refresh_metrics.py   # 需要 gh 登录或 GH_TOKEN\npython scripts/build.py\npython -m unittest discover -s tests\npython scripts/build.py --check\n```\n\nGitHub Actions 每天更新已收录项目的指标与排序。新增项目、论文和功能分类通过人工核验后合并；自动指标更新不代表功能或许可已重新审计。\n\n## 致谢与许可\n\n检索入口参考 [Awesome Proactive Agents](https://github.com/LowEntropyAI/awesome-proactive-agent) 和 [Awesome Personal Agents](https://github.com/upgundecha/awesome-personal-agents)，条目回到原始仓库及论文核验。\n\n本仓库原创说明、整理数据及维护脚本使用 [MIT](LICENSE)。所链接项目、论文、模型和数据遵循各自许可。')
    ranking=['# 排序视图\n\n全目录元数据排序；组件、研究与助手仅展示维护指标，不表示可以相互替代。所有视图先按维护状态分层，再按该视图指标降序；同分以 star、仓库名稳定排序。\n\n快照：'+as_of+'。公式与字段口径见 [methodology.md](methodology.md)。\n']
    for mode,label in [('stars','Star 优先'),('activity','90 天提交数优先'),('recent','默认分支最近提交优先')]:
        ranking.append('\n## '+label+'\n')
        rows=[]
        for p in rank(projects,metrics,as_of,mode):
            m=metrics[p['repo']]
            rows.append([f"[{p['name']}](https://github.com/{p['repo']})",CATEGORIES[p['category']],status(p,m,as_of),f"{m['stars']:,}",m['commits_90d'],m['last_commit_at'][:10]])
        ranking.append(table(['项目','类别','维护层','Stars','90天提交','最近提交 UTC'],rows))
    output={'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n'.join(detail)+'\n','docs/papers.md':'\n'.join(paperdoc)+'\n','docs/rankings.md':'\n'.join(ranking)+'\n'}
    buf=io.StringIO(newline=''); writer=csv.writer(buf,lineterminator='\n')
    writer.writerow(['repo','category','scope','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_status','score','as_of'])
    for p in ordered:
        m=metrics[p['repo']]
        writer.writerow([p['repo'],p['category'],p['scope'],p['license_review']['label'],p['license_review']['status'],m['stars'],m['commits_30d'],m['commits_90d'],m['last_commit_at'],status(p,m,as_of),score(m,as_of),as_of])
    output['data/rankings.csv']=buf.getvalue()
    return output

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    read=lambda path:json.loads((ROOT/path).read_text(encoding='utf-8'))
    projects,papers,snapshot=read('data/projects.json'),read('data/papers.json'),read('data/metrics.json')
    validate(projects,papers,snapshot)
    files=render(projects,papers,snapshot)
    for name,content in files.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:raise SystemExit(f'Generated file is stale: {name}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print(f'{"Checked" if args.check else "Generated"} {len(files)} files; {len(projects)} projects, {len(papers)} papers')

if __name__=='__main__':main()
