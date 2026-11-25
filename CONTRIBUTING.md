# Contributing

Additions of projects, papers and evidence corrections are welcome. A low star count is not a reason to reject.

1. Add the entry in `data/projects.json` or `data/papers.json`; never edit the generated README tables directly.
2. Provide the canonical GitHub URL or the paper's original page, at least one source proving the stated mechanism, and the verification date.
3. Say whether it is a complete assistant, an extension, a harness, a control component or research code; the trigger must be concrete. Write "pending verification" for unconfirmed capabilities, and never present a roadmap as an implemented feature.
4. Check the license. Missing full license text may still enter as a candidate/research entry; source code with non-commercial restrictions must not be labelled as a verified open license.
5. On renames, update to the GitHub canonical repository; deduplicate the same paper by arXiv ID, and old names can go in notes.
6. Run the commands below and commit the generated results. A newly added repository requires a fresh full metrics snapshot.

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests
python scripts/build.py --check
```

When updating feature descriptions, pin the evidence commit SHA; an automatic star refresh must not relabel old feature judgements as freshly verified. Classification is documented in `docs/taxonomy.md` and ranking in `docs/methodology.md`.

Never commit private search-service addresses, tokens, internal article text, signed download links or personal data to this repository.

## Localisation files

- `data/projects.json` is the canonical Chinese review data: facts are changed here once and only here.
- Wording in the other languages comes from `locales/<lang>/entries.json` (`description`, `trigger`, `boundary`, `license_label`, `license_note`) and `locales/<lang>/ui.json`; `zh` falls back directly to `data/projects.json`, so there is no `locales/zh/entries.json`.
- When adding a project or rewriting its positioning, boundary or license conclusion, complete the en/es/hi/fr locales in the same PR, otherwise `python scripts/build.py --check` and `python -m unittest discover -s tests -v` fail.
- Static documents: English lives in the root `docs/` and `CONTRIBUTING.md`; other languages use the same relative paths under `locales/<lang>/`. Relative links inside a mirror resolve from that file's own directory, so from `locales/<lang>/docs/` a link to repository-root `data/`, `scripts/`, `research/`, `LICENSE` or `record/` is written as `../../../`, while from `locales/<lang>/CONTRIBUTING.md` it is `../../`; `docs/readme-intro.md` is the exception — it is inlined into the README and resolves from the language root.
- `record/` and `research/` keep the original wording used at writing time as an audit trail; they are not machine translated.
- Generated files (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv`, and the same-named files in each language mirror) are never hand-edited; they are produced by `python scripts/build.py`.
