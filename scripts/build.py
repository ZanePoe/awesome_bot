"""Render the curated multilingual catalogue and transparent metadata rankings without network access."""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DEFAULT='en'; MIRRORED=['zh','es','hi','fr']; LOCALES=[DEFAULT,*MIRRORED]
STATIC=['docs/readme-intro.md','docs/taxonomy.md','docs/methodology.md','docs/research.md','docs/harness-guide.md','CONTRIBUTING.md']
KEYWORD_FILES=['docs/research.md']
CJK=re.compile(r'[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]')

def ui(locale):
    return json.loads((ROOT/'locales'/locale/'ui.json').read_text(encoding='utf-8'))

def placeholders(template):
    return set(re.findall(r'(?<!\{)\{(\w+)\}(?!\})',template))

def entries(locale,projects):
    """Per-locale wording; Chinese falls back to the canonical reviewed data."""
    if locale=='zh':
        return {p['repo']:{'name':p['name'],'description':p['description'],'boundary':p['boundary'],'trigger':p['trigger'],'license_label':p['license_review']['label'],'license_note':p['license_review'].get('note','')} for p in projects}
    raw=json.loads((ROOT/'locales'/locale/'entries.json').read_text(encoding='utf-8'))
    out={}
    for p in projects:
        t=raw[p['repo']]
        out[p['repo']]={'name':t.get('name') or p['name'],'description':t['description'],'boundary':t['boundary'],'trigger':t['trigger'],'license_label':t['license_label'],'license_note':t['license_note']}
    return out

def paper_text(locale,papers):
    """Per-locale paper wording; Chinese falls back to the canonical reviewed data."""
    if locale=='zh':
        return {p['id']:{'title':p['title'],'summary':p['summary'],'boundary':p['boundary'],'publication_note':p['publication_note']} for p in papers}
    raw=json.loads((ROOT/'locales'/locale/'papers.json').read_text(encoding='utf-8'))
    return {p['id']:{'title':raw[p['id']]['title'],'summary':raw[p['id']]['summary'],'boundary':raw[p['id']]['boundary'],'publication_note':raw[p['id']]['publication_note']} for p in papers}

def path(locale,name):
    if locale==DEFAULT: return Path(name)
    if name=='README.md': return Path(f'locales/{locale}/README.md')
    return Path(f'locales/{locale}')/name

def prefix(locale,depth=0):
    """`../` count from a generated file to the repository root; depth 0 is the locale root (README.md), depth 1 the locale's docs/. English sits at the root (0 levels) or root docs/ (1 level); a mirror root is two levels down."""
    return ('../'*(2+depth)) if locale!=DEFAULT else ('../'*depth)

def anchor(repo): return repo.lower().replace('/','--').replace('_','-').replace('.','-')

def heading_anchor(title):
    """GitHub's README heading anchor: lowercase, spaces to hyphens, keep letters/digits/marks/_/- (Devanagari matras survive), drop punctuation such as 、 and . (verified against live github.com heading ids)."""
    out=[]
    for ch in title.strip().lower():
        if ch==' ':out.append('-')
        elif ch.isalnum() or ch in '_-' or unicodedata.category(ch) in ('Mn','Mc','Me'):out.append(ch)
    return ''.join(out)

def switcher(langs,locale):
    items=[]
    for code,name in langs:
        if code==locale: items.append(f'**{name}**')
        elif code==DEFAULT: items.append(f'[{name}]({"README.md" if locale==DEFAULT else "../../README.md"})')
        elif locale==DEFAULT: items.append(f'[{name}](locales/{code}/README.md)')
        else: items.append(f'[{name}](../{code}/README.md)')
    return '🌐 '+' · '.join(items)

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

INLINE=['docs/readme-intro.md']
GENERATED={'README.md','docs/projects.md','docs/papers.md','docs/rankings.md'}
def check_links():
    """Prose links resolve from the file's own directory; the inlined readme intro resolves from the locale root."""
    bad=[]
    for locale in LOCALES:
        base=ROOT if locale==DEFAULT else ROOT/'locales'/locale
        pending={(base/name).resolve() for name in GENERATED}
        for rel in STATIC:
            origin=base if rel in INLINE else base/Path(rel).parent
            for href in re.findall(r'\]\((?!https?:|#)([^)#]+?)(?:#[^)]*)?\)',(base/rel).read_text(encoding='utf-8')):
                target=(origin/href).resolve()
                if target in pending or target.exists():continue
                bad.append('%s:%s -> %s' % (locale,rel,href))
    assert not bad,'broken relative links: '+', '.join(bad)

def validate(projects,papers,snapshot):
    u=ui('zh');repos=[p['repo'] for p in projects]
    assert snapshot['schema_version']==1
    dt(snapshot['as_of'])
    assert len(repos)==len(set(r.lower() for r in repos)), 'Duplicate repositories'
    assert set(repos)==set(snapshot['repositories']), 'Snapshot/catalogue mismatch'
    canonical={p['repo']:p['name'] for p in projects}
    for p in projects:
        assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo']), p['repo']
        assert p['category'] in u['categories'] and p['scope'] in u['scopes']
        assert p['description'] and p['boundary'] and p['trigger'] and p['evidence']
        assert all(e['url'].startswith('https://') for e in p['evidence'])
        assert p['license_review']['status'] in u['license_status']
        m=snapshot['repositories'][p['repo']]
        assert m['canonical_repo'].lower()==p['repo'].lower(), 'Resolve repository redirect explicitly'
        assert all(isinstance(m[k],int) and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d'])
        assert m['commits_30d']<=m['commits_90d']
        dt(m['last_commit_at'])
        assert re.fullmatch(r'[0-9a-f]{40}',m['head_sha'])
    assert len(papers)==len(set(p['id'] for p in papers)), 'Duplicate papers'
    for p in papers:
        assert p['category'] in u['paper_categories'] and p['url']=='https://arxiv.org/abs/'+p['id']
        assert p['code_repo'] is None or p['code_repo'] in repos
        datetime.strptime(p['published'],'%Y-%m-%d')
    seeds={p['repo'] for p in projects if p.get('seed')}
    assert seeds=={'Fei2411/DS-Bot','CursorTouch/Windows-MCP','elie222/rakazo','OpenBMB/PilotDeck','nano-muse/nanoMuse'}
    for f in STATIC: assert (ROOT/f).exists(), 'missing English static document: '+f
    def keys(value,base=''):
        if isinstance(value,dict): return sorted(sum([keys(value[k],base+'/'+k) for k in value],[]))
        return [base or '.']
    shape=keys(u['templates'])
    pids={p['id'] for p in papers}
    for locale in MIRRORED:
        if locale=='zh': continue
        other=ui(locale)
        assert set(other)==set(u),'ui.json top-level keys differ for '+locale
        assert other['language']==locale and other['list_separator'].strip()
        assert keys(other['templates'])==shape, 'template keys differ for '+locale
        assert set(other['categories'])==set(u['categories']) and set(other['paper_categories'])==set(u['paper_categories']) and set(other['scopes'])==set(u['scopes']) and set(other['license_status'])==set(u['license_status']) and set(other['modes'])==set(u['modes'])
        assert len(other['tiers'])==4 and set(other['headers'])==set(u['headers']) and set(other['sections'])==set(u['sections']) and set(other['tags'])==set(u['tags'])
        for name,tmpl in other['templates'].items():
            assert placeholders(tmpl)==placeholders(u['templates'][name]),'placeholders differ for %s/%s' % (locale,name)
        assert not CJK.search(json.dumps({k:v for k,v in other.items() if k in ('categories','paper_categories','scopes','license_status','modes','tiers','headers','sections','tags','templates')},ensure_ascii=False)),'untranslated Chinese remains in '+locale+' ui.json'
        raw=json.loads((ROOT/'locales'/locale/'entries.json').read_text(encoding='utf-8'))
        assert set(raw)==set(repos),'entry coverage differs for '+locale
        for repo,t in raw.items():
            assert set(t)>={'description','boundary','trigger','license_label','license_note'} and all(str(t[k]).strip() for k in ('description','boundary','trigger','license_label','license_note')),'incomplete entry: %s %s' % (locale,repo)
            assert not CJK.search(json.dumps(t,ensure_ascii=False)),'untranslated Chinese remains in %s %s' % (locale,repo)
            if CJK.search(canonical[repo]):
                assert t.get('name'),'missing localized display name for %s %s' % (locale,repo)
        pw=json.loads((ROOT/'locales'/locale/'papers.json').read_text(encoding='utf-8'))
        assert set(pw)==pids,'paper coverage differs for '+locale
        for pid,t in pw.items():
            assert set(t)>={'title','summary','boundary','publication_note'} and all(str(t[k]).strip() for k in ('title','summary','boundary','publication_note')),'incomplete paper: %s %s' % (locale,pid)
            assert not CJK.search(json.dumps(t,ensure_ascii=False)),'untranslated Chinese remains in %s paper %s' % (locale,pid)
        for f in STATIC: assert (ROOT/'locales'/locale/f).exists(),'missing %s static document: %s' % (locale,f)
    check_links()

def render(locale,u,words,pws,projects,papers,snapshot):
    metrics=snapshot['repositories']; as_of=snapshot['as_of']
    reviewed_at=max(p['reviewed_at'] for p in projects)
    ordered=rank(projects,metrics,as_of)
    R=prefix(locale)
    cat=u['categories'];pcat=u['paper_categories'];scope=u['scopes'];tags=u['tags'];T=u['templates'];S=u['sections']
    shortlist=[p for p in ordered if p['scope']=='core' and p['license_review']['status']=='verified' and tier(p,metrics[p['repo']],as_of)==0]
    intro=(ROOT/('docs/readme-intro.md' if locale==DEFAULT else f'locales/{locale}/docs/readme-intro.md')).read_text(encoding='utf-8')
    nav='\n## '+S['tags']+'\n\n'+' · '.join(f'[{x}](#{heading_anchor(x)})' for x in cat.values())+'\n\n'+'**'+S['papers']+'** · '+' · '.join(f'[{x}](#{heading_anchor(x)})' for x in pcat.values())
    readme=[intro,nav, f'\n## {S["current"]}\n\n'+T['current'].format(total=len(projects),papers=len(papers),as_of=as_of,reviewed=reviewed_at), f'\n## {S["shortlist"]}\n\n'+T['shortlist_note']]
    def compact(p):
        m=metrics[p['repo']];w=words[p['repo']]
        return [f"[{w['name']}](https://github.com/{p['repo']})",w['trigger'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}"]
    readme.append(table(u['headers']['shortlist'],[compact(p) for p in shortlist[:10]]))
    readme.append(f'\n## {S["toc"]}\n\n'+T['toc_note'])
    detail=[f'# {S["detail_title"]}\n\n'+T['detail_intro']+'\n']
    for category,label in cat.items():
        group=[p for p in ordered if p['category']==category]
        readme.append(f'\n### {label}\n')
        rows=[]
        for p in group:
            m=metrics[p['repo']];w=words[p['repo']];licence=w['license_label'];state=u['tiers'][tier(p,m,as_of)]
            mark=(' · '+tags['seed'] if p.get('seed') else '')+(' · '+tags['archived'] if tier(p,m,as_of)==3 else '')
            if p['license_review']['status']!='verified':mark+=' · '+tags['license']
            rows.append([f"[{w['name']}](https://github.com/{p['repo']}){mark}",w['trigger'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}",licence])
            sources=' · '.join(f"[{T['source_link'].format(index=i+1)}]({e['url']})" for i,e in enumerate(p['evidence']))
            body=T['entry'].format(category=label,scope=scope[p['scope']],trigger=w['trigger'],boundary=w['boundary'],maintenance=state,commits_30d=m['commits_30d'],commits_90d=m['commits_90d'],license=licence,license_source=p['license_review']['source'],license_note=w['license_note'],reviewed_at=p['reviewed_at'],sources=sources)
            detail.extend([f'\n<a id="{anchor(p["repo"])}"></a>\n\n## [{w["name"]}](https://github.com/{p["repo"]})',f"\n{w['description']}\n\n"+body])
        readme.append(table(u['headers']['detail'],rows))
    readme.append('\n'+T['projects_note']+f'\n\n## {S["papers"]}\n\n'+T['papers_note'])
    paperdoc=[f'# {S["papers_title"]}\n\n'+T['papers_intro']+'\n']
    for category,label in pcat.items():
        group=sorted([p for p in papers if p['category']==category],key=lambda p:(p['published'],p['id']),reverse=True)
        rows=[]
        for p in group:
            pw=pws[p['id']]
            rows.append([p['published'],f"[{pw['title']}]({p['url']})",pw['summary']])
            code=T['paper_code_link'].format(url='https://github.com/'+p['code_repo']) if p['code_repo'] else T['paper_code_none']
            paperdoc.extend([f"\n## [{pw['title']}]({p['url']})","\n"+T['paper_entry'].format(category=label,published=p['published'],publication_note=pw['publication_note'],summary=pw['summary'],boundary=pw['boundary'],code=code)])
        readme.append(f'\n### {label}\n\n'+table(u['headers']['papers'],rows))
    readme.append('\n'+T['papers_link']+f'\n\n## {S["data"]}\n\n'+T['data']+f'\n\n## {S["thanks"]}\n\n'+T['thanks'].format(R=R))
    readme.append(T['records_note'].format(R=R))
    ranking=[f'# {S["rankings_title"]}\n\n'+T['rankings_intro'].format(as_of=as_of)+'\n']
    for mode in ['stars','activity','recent']:
        ranking.append('\n## '+u['modes'][mode]+'\n')
        rows=[]
        for p in rank(projects,metrics,as_of,mode):
            m=metrics[p['repo']];w=words[p['repo']]
            rows.append([f"[{w['name']}](https://github.com/{p['repo']})",cat[p['category']],u['tiers'][tier(p,m,as_of)],f"{m['stars']:,}",m['commits_90d'],m['last_commit_at'][:10]])
        ranking.append(table(u['headers']['rankings'],rows))
    return {'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n'.join(detail)+'\n','docs/papers.md':'\n'.join(paperdoc)+'\n','docs/rankings.md':'\n'.join(ranking)+'\n'}

def csv_snapshot(projects,snapshot):
    metrics=snapshot['repositories'];as_of=snapshot['as_of']
    buf=io.StringIO(newline=''); writer=csv.writer(buf,lineterminator='\n')
    writer.writerow(['repo','category','scope','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_tier','score','as_of'])
    for p in rank(projects,metrics,as_of):
        m=metrics[p['repo']]
        writer.writerow([p['repo'],p['category'],p['scope'],p['license_review']['label'],p['license_review']['status'],m['stars'],m['commits_30d'],m['commits_90d'],m['last_commit_at'],tier(p,m,as_of),score(m,as_of),as_of])
    return buf.getvalue()

def render_all(projects,papers,snapshot):
    u={locale:ui(locale) for locale in LOCALES};langs=[(locale,u[locale]['language_name']) for locale in LOCALES];out={}
    for locale in LOCALES:
        files=render(locale,u[locale],entries(locale,projects),paper_text(locale,papers),projects,papers,snapshot)
        for name,content in files.items():
            out[path(locale,name).as_posix()]=content
        readme=path(locale,'README.md').as_posix()
        out[readme]=switcher(langs,locale)+'\n\n'+out[readme]
    out['data/rankings.csv']=csv_snapshot(projects,snapshot)
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    read=lambda path:json.loads((ROOT/path).read_text(encoding='utf-8'))
    projects,papers,snapshot=read('data/projects.json'),read('data/papers.json'),read('data/metrics.json')
    validate(projects,papers,snapshot)
    files=render_all(projects,papers,snapshot)
    for name,content in files.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:raise SystemExit(f'Generated file is stale: {name}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print(f'{"Checked" if args.check else "Generated"} {len(files)} files; {len(projects)} projects, {len(papers)} papers, {len(LOCALES)} locales')

if __name__=='__main__':main()
