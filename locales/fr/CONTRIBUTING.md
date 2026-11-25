# Guide de contribution

Les projets, les articles et les correctifs de preuves sont bienvenus. Un faible nombre d'étoiles n'est pas un motif de refus.

1. Ajouter l'entrée dans `data/projects.json` ou `data/papers.json` ; ne jamais modifier directement les tableaux générés du README.
2. Fournir l'adresse canonique GitHub ou la page primaire de l'article, au moins une source établissant le mécanisme décrit, et la date de vérification.
3. Préciser s'il s'agit d'un assistant complet, d'une extension, d'un harness, d'un composant de contrôle ou de code de recherche ; le déclenchement doit être concret. Une capacité non confirmée s'écrit « à vérifier », et un roadmap ne vaut pas fonction implémentée.
4. Examiner la licence. Sans texte complet de licence, l'entrée peut rester candidate ou de recherche ; un code comportant des restrictions non commerciales ne peut pas être marqué comme licence ouverte vérifiée.
5. En cas de renommage, mettre à jour le dépôt canonique GitHub ; pour un article, dédoublonner par identifiant arXiv, l'ancien nom pouvant rester en note.
6. Exécuter les commandes ci-dessous et livrer les fichiers générés. Un dépôt nouvellement ajouté exige de relancer une collecte complète des métriques.

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests
python scripts/build.py --check
```

Quand une description fonctionnelle est mise à jour, fixer le SHA du commit de preuve ; un rafraîchissement automatique des étoiles ne doit pas faire passer une ancienne conclusion fonctionnelle pour récemment vérifiée. La méthode de classification est dans `docs/taxonomy.md`, celle de classement dans `docs/methodology.md`.

Sont interdits dans ce dépôt : adresses de services de recherche privés, jetons, corps d'articles internes, liens de téléchargement signés et données personnelles.

## Fichiers multilingues

- `data/projects.json` porte la revue canonique en chinois : les faits ne se corrigent qu'à cet endroit.
- Les textes des autres langues viennent de `locales/<lang>/entries.json` (`description`, `trigger`, `boundary`, `license_label`, `license_note`) et de `locales/<lang>/ui.json` ; ceux des articles viennent de `locales/<lang>/papers.json` (`title`, `summary`, `boundary`, `publication_note`) ; `zh` retombe directement sur `data/projects.json`, d'où l'absence de `locales/zh/entries.json`.
- Pour un nouveau projet ou une réécriture de positionnement, de limites ou de conclusion de licence, les quatre locales en/es/hi/fr doivent être complétées dans la même PR, sinon `python scripts/build.py --check` et `python -m unittest discover -s tests -v` échouent.
- Documentation statique : l'anglais est à la racine (`docs/` et `CONTRIBUTING.md`), les autres langues sous le même chemin relatif dans `locales/<lang>/`. Les liens relatifs d'un miroir se résolvent depuis le répertoire du fichier : vers `data/`, `scripts/`, `research/`, `LICENSE` ou `record/` de la racine, écrire `../../../` depuis `locales/<lang>/docs/` et `../../` depuis `locales/<lang>/CONTRIBUTING.md` ; `docs/readme-intro.md` échappe à la règle, il est inséré dans le README et se résout depuis la racine de la langue.
- `record/` et `research/` conservent le texte d'origine au moment où ils ont été écrits, comme piste d'audit, sans traduction automatique.
- Les fichiers générés (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` et leurs homologues dans chaque miroir de langue) ne se modifient pas à la main : `python scripts/build.py` les produit.
