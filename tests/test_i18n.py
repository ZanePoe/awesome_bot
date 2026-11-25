import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build

SURFACES = ('README.md', 'docs/projects.md', 'docs/papers.md', 'docs/rankings.md')

def readme_headings(text):
    return {build.heading_anchor(h) for h in re.findall(r'^#{1,6}\s+(.*)$', text, re.M)}

class LocaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        read = lambda p: json.loads((ROOT / p).read_text(encoding='utf-8'))
        cls.projects = read('data/projects.json')
        cls.papers = read('data/papers.json')
        cls.snapshot = read('data/metrics.json')
        cls.out = build.render_all(cls.projects, cls.papers, cls.snapshot)

    def test_every_locale_renders_all_surfaces(self):
        for locale in build.LOCALES:
            for name in SURFACES:
                target = build.path(locale, name).as_posix()
                self.assertIn(target, self.out, target)
                self.assertGreater(len(self.out[target]), 1000, target)

    def test_switcher_links_resolve(self):
        for locale in build.LOCALES:
            text = self.out[build.path(locale, 'README.md').as_posix()]
            line = text.splitlines()[0]
            self.assertTrue(line.startswith('🌐'), line)
            for other in build.LOCALES:
                self.assertIn(build.ui(other)['language_name'], line)
            self.assertEqual(line.count('**'), 2, 'current language is bold, others link')
            for href in re.findall(r'\]\(([^)#]+?/README\.md)\)', line):
                base = ROOT if locale == build.DEFAULT else ROOT / 'locales' / locale
                self.assertTrue((base / href).resolve().exists(), f'{locale} -> {href}')

    def test_in_page_anchors_exist(self):
        for locale in build.LOCALES:
            name = build.path(locale, 'README.md').as_posix()
            text = self.out[name]
            headings = readme_headings(text)
            for anchor in re.findall(r'\]\(#([^)]+)\)', text):
                self.assertIn(anchor, headings, f'{name} anchor #{anchor}')

    def test_project_anchor_ids_are_language_invariant(self):
        for locale in build.LOCALES:
            text = self.out[build.path(locale, 'docs/projects.md').as_posix()]
            for p in self.projects:
                self.assertIn(f'<a id="{build.anchor(p["repo"])}"></a>', text, f'{locale} {p["repo"]}')

    def test_paper_entries_cover_every_locale(self):
        for locale in build.LOCALES:
            text = self.out[build.path(locale, 'docs/papers.md').as_posix()]
            for p in self.papers:
                self.assertIn(p['url'], text, f'{locale} paper {p["id"]} missing from docs/papers.md')

    def test_relative_links_exist_on_disk(self):
        for locale in build.LOCALES:
            base = ROOT if locale == build.DEFAULT else ROOT / 'locales' / locale
            for name in SURFACES:
                origin = base if name == 'README.md' else base / 'docs'
                text = self.out[build.path(locale, name).as_posix()]
                for href in re.findall(r'\]\((?!https?:)([^)#]+?)(?:#[^)]*)?\)', text):
                    target = (origin / href).resolve()
                    self.assertTrue(target.exists() or (base / href).resolve().exists(), f'{name} -> {href}')

    def test_generated_output_is_cjk_free_outside_zh(self):
        """Display names, wording and labels come from the locale; only the switcher line may quote another language's name."""
        for locale in build.LOCALES:
            if locale == 'zh':
                continue
            for name in SURFACES:
                body = self.out[build.path(locale, name).as_posix()]
                if name == 'README.md':
                    body = '\n'.join(body.splitlines()[1:])
                self.assertIsNone(build.CJK.search(body), f'{locale} {name} still contains Chinese')

    def test_canonical_display_names_need_no_localization(self):
        """awesome_bot ships no Chinese project names, so entries.json may omit `name`; validate() enforces it as soon as one appears."""
        cjk = [p['repo'] for p in self.projects if build.CJK.search(p['name'])]
        self.assertEqual(cjk, [], 'Chinese canonical names now exist; non-zh locales must provide `name`')
        words = build.entries('zh', self.projects)
        for p in self.projects:
            self.assertEqual(words[p['repo']]['name'], p['name'])

    def test_zh_mirror_uses_canonical_review_data(self):
        sample = next(p for p in self.projects if p['category'] == 'personal')
        readme = self.out[build.path('zh', 'README.md').as_posix()]
        details = self.out[build.path('zh', 'docs/projects.md').as_posix()]
        self.assertIn(sample['trigger'], readme)
        self.assertIn(sample['description'], details)

    def test_static_prose_present_for_every_locale(self):
        for locale in build.LOCALES:
            for rel in build.STATIC:
                target = ROOT / rel if locale == build.DEFAULT else ROOT / 'locales' / locale / rel
                self.assertTrue(target.exists(), str(target))
                if locale == build.DEFAULT:
                    continue
                body = target.read_text(encoding='utf-8')
                if locale == 'zh':
                    continue
                if rel in build.KEYWORD_FILES:
                    for line in body.splitlines():
                        if build.CJK.search(line) and not line.lstrip().startswith('|'):
                            self.assertIsNone(build.CJK.search(re.sub(r'`[^`]*`', ' ', line)),
                                              f'{locale} {rel} prose line still Chinese: {line[:60]}')
                else:
                    self.assertIsNone(build.CJK.search(body), f'{locale} {rel} still Chinese')

    def test_csv_is_language_neutral(self):
        header = self.out['data/rankings.csv'].splitlines()[0].split(',')
        self.assertEqual(header[header.index('maintenance_tier')], 'maintenance_tier')
        self.assertNotIn('maintenance_status', header)
        tier = header.index('maintenance_tier')
        rows = self.out['data/rankings.csv'].splitlines()[1:]
        self.assertTrue(all(row.split(',')[tier] in {'0', '1', '2', '3'} for row in rows))

    def test_missing_locale_entry_is_rejected(self):
        projects = [dict(p) for p in self.projects]
        path = ROOT / 'locales' / 'es' / 'entries.json'
        original = path.read_text(encoding='utf-8')
        raw = json.loads(original)
        repo = projects[0]['repo']
        raw.pop(repo)
        path.write_text(json.dumps(raw, ensure_ascii=False), encoding='utf-8')
        try:
            with self.assertRaises(AssertionError):
                build.validate(projects, self.papers, self.snapshot)
        finally:
            path.write_text(original, encoding='utf-8')

    def test_missing_locale_paper_is_rejected(self):
        papers = [dict(p) for p in self.papers]
        path = ROOT / 'locales' / 'es' / 'papers.json'
        original = path.read_text(encoding='utf-8')
        raw = json.loads(original)
        raw.pop(papers[0]['id'])
        path.write_text(json.dumps(raw, ensure_ascii=False), encoding='utf-8')
        try:
            with self.assertRaises(AssertionError):
                build.validate(self.projects, papers, self.snapshot)
        finally:
            path.write_text(original, encoding='utf-8')

    def test_untranslated_trigger_is_rejected(self):
        path = ROOT / 'locales' / 'es' / 'entries.json'
        original = path.read_text(encoding='utf-8')
        raw = json.loads(original)
        repo = self.projects[0]['repo']
        raw[repo].pop('trigger')
        path.write_text(json.dumps(raw, ensure_ascii=False), encoding='utf-8')
        try:
            with self.assertRaises(AssertionError):
                build.validate(self.projects, self.papers, self.snapshot)
        finally:
            path.write_text(original, encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
