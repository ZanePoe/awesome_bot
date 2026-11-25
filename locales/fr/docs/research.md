# Méthode de recherche et journal de couverture

Cette passe a suivi trois tours : « projets de référence → termes distinctifs → web et GitHub → compléments depuis des index → vérification sur les documents primaires ». La livraison est un catalogue sélectif de première version, arrêté par la limite de trois tours fixée à l'avance, **sans revendiquer une recherche exhaustive**. Le troisième tour a encore apporté des sources nouvelles, le catalogue peut donc continuer à s'étendre.

## Termes de recherche déduits des projets de référence

| Caractéristique | Mots-clés anglais | Mots-clés chinois |
| --- | --- | --- |
| N'attend pas de nouvelle consigne | proactive agent, anticipatory assistant, initiative | 主动式智能体、主动助手、需求预判 |
| Présence durable | always-on, persistent agent, sessionless, background agent | 常驻助手、持久 Agent、后台运行 |
| Réveil autonome | heartbeat, cron, scheduler, event-driven, webhook, routines | 心跳、定时、事件驱动、周期任务 |
| Action réelle | computer use, desktop automation, browser agent, MCP | 电脑操作、桌面自动化、浏览器 Agent |
| Compréhension dans la durée | long-term memory, user context, personalization, long-horizon | 长期记忆、用户上下文、个性化、长期目标 |
| Transformer une base existante | harness, plugin, extension, Pi, Hermes, DeepSeek Harness | Harness 插件、扩展、二次开发 |
| Recherche sur la proactivité | proactive assistance benchmark, intervention timing, abstention | 主动辅助评测、介入时机、保持静默 |

Le terme générique autonomous agent fait remonter des exécuteurs à usage unique, des bots de jeu et des flux de travail ordinaires ; les mots de mécanisme heartbeat / routines / persistent resserrent la recherche, puis le README est vérifié. Grok Bot et Muse ont servi à découvrir des catégories de produits ; le statut open source reste jugé sur le dépôt et la licence.

## Déroulement en trois tours

| Tour | Lots de recherche/vérification | Résultats consignés | Sources nouvelles | Taux de sources nouvelles |
| --- | --- | --- | --- | --- |
| 1 | 12 | 228 | 220 | 96.5% |
| 2 | 6 | 53 | 42 | 79.2% |
| 3 | 4 | 171 | 138 | 80.7% |

Le journal de recherche compte 22 lots : un lot de collecte de liens d'index, deux lots d'élargissement par recherche native GitHub et des vérifications en lot des dépôts et articles primaires. Il ne s'agit pas de 22 mots-clés internet indépendants, ni de 400 projets tous candidats à l'inclusion.

- Le premier tour a couvert huit axes : sémantique, documentation officielle, index sélectifs, dépôts, alternatives, évaluations, limites et changements récents. La collecte depuis un index était plafonnée à 100 liens, et les lots de recherche web enregistraient d'ordinaire 20 résultats au maximum.
- Le deuxième tour a ajouté, au fil des résultats, des noms nouveaux comme rho, murmur, Pulse, PASK, ProAgentBench et PIRA-Bench, et a vérifié assistants complets et extensions de harness.
- Le troisième tour a comblé les manques par la recherche native GitHub, puis est revenu aux README officiels, aux métriques GitHub GraphQL et aux résumés d'articles de toutes les entrées finales. Les preuves fonctionnelles sont figées au commit.

La déduplication repose surtout sur l'URL normalisée, le dépôt canonique et l'identifiant arXiv. Des domaines miroirs rencontrés dans la recherche web peuvent encore compter comme sources candidates distinctes dans les statistiques de recherche ; le catalogue final des projets et articles est dédoublonné selon ces clés d'entité. Le taux de sources nouvelles est un indicateur de processus de recherche, pas de pertinence ni de qualité.

Les cinq liens de référence initiaux sont tous couverts (5/5). Les huit axes de recherche ont tous produit des pistes pertinentes, ce qui ne vaut pas couverture suffisante de chaque sous-domaine. Aucune étude utilisateur ni test sur machine indépendant : les fonctions sont rapportées d'après la documentation des auteurs.

## Content factory

Recherche structurée appelée par la voie curl du skill `content-factory-search-api`, sur la plage **2026-08-05 au 2026-11-05**, au plus 30 résultats par lot et 15 après déduplication.

Requêtes de cette passe : `主动式 Agent`, `Grok Bot OR nanoMuse OR rakazo OR PilotDeck`, `Hermes Agent OR DeepSeek Harness OR Pi Agent`, `OpenClaw`, `Hermes`. Les cinq requêtes ont renvoyé un JSON valide mais des tableaux de résultats vides : rien n'a donc servi de preuve pour une entrée finale. Un résultat vide ne prouve pas que ces projets soient absents de la base ou d'internet ; aucune requête sur tout l'historique n'a été lancée. En l'absence de résultats, aucun calcul vectoriel n'était nécessaire.

Le dépôt public ne conserve que les termes de recherche, la plage de dates et les statistiques de résultats, sans adresses de service privé, jetons ni textes internes.

## Corrections sur les sources primaires et limites

- Le [README de LettaBot](https://github.com/letta-ai/lettabot) annonce l'abandon de la maintenance active et oriente vers Letta Code. Les métadonnées GitHub indiquent aussi un dépôt archivé.
- La conception Bot + cron de [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) garde une valeur de référence, mais l'API de cette passe la montre archivée : elle reste donc en référence historique.
- [Pi](https://github.com/earendil-works/pi) est listé sous son adresse canonique actuelle ; l'ancienne adresse `badlogic/pi-mono` n'est pas listée une seconde fois.
- [MemoProAgent](https://arxiv.org/abs/2610.22671) est le titre de la version courante du même article ; l'ancien nom ProPerAgent n'apparaît pas deux fois. Son code de recherche utilise une licence à condition non commerciale, il figure donc hors des recommandations sous licence ouverte.
- La page actuelle de [ProactiveBench](https://arxiv.org/abs/2603.19466) indique ECCV 2026 : l'étiquette ICLR 2026 reprise des index sélectifs n'est pas conservée, et le benchmark ne doit pas être confondu avec l'homonyme utilisé par ProactiveAgent.
- Mame déclare MIT sur sa page d'accueil sans texte de licence localisé ; aucun LICENSE trouvé pour ContextAgent. Ces lacunes de vérification sont conservées : visibilité publique ne vaut pas licence complète.

## Non couvert et suites possibles

Les branches compagnon multimodal, exploitation sectorielle, appareils domestiques et apprentissage proactif vertical n'ont donné que des pistes, sans inclusion complète dans cette première version. Les produits fermés Grok Bot et Muse n'ont fait l'objet d'aucune expérience de comparaison. Le maintien en arrière-plan sur mobile, la fiabilité multi-appareils et la compatibilité de combinaisons de plugins concrètes restent à mesurer. Aucun comparatif des meilleurs résultats entre articles n'a été établi, pour éviter un faux classement provoqué par des modèles, des données et des budgets différents.

La synthèse des mécanismes centraux et la classification sont des choix éditoriaux. Cette passe ne comporte pas d'ablation : impossible de dire « qui perd le plus sans mémoire ou sans ordonnancement ». Étoiles et volumes de commits ne soutiennent qu'un classement de maintenance.

## Fichiers vérifiables

- [Journal de recherche](../../../research/search-log.json) : tours, axes, requêtes, sources et nombres de résultats.
- [Décisions de classification et de preuve](../../../research/decisions.json) : périmètres d'inclusion et sources à commit figé.
- [Premier instantané de métriques](../../../research/initial-metrics.json) : conserve le relevé de la première version, que les mises à jour quotidiennes n'écrasent pas.
- [Instantané courant des métriques](../../../data/metrics.json) et [CSV de classement](../../../data/rankings.csv) : dernier classement recalcutable.
- [État de la recherche](../../../research/status.json) et [contrôle d'intégrité](../../../research/verification.json) : aucune référence de preuve orpheline ni d'URL normalisée dupliquée ; les cinq requêtes à résultat vide restent signalées.

Les textes complets des résultats de recherche et les journaux d'exécution des outils locaux restent en local et ne sont pas copiés dans le dépôt public. Les 99 preuves/jugements et les 123 relevés de métriques de l'état de recherche sont des comptages d'audit locaux ; la version publique fournit les décisions reliées, les liens vers les sources primaires et les instantanés de métriques.
