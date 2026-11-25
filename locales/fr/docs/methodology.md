# Méthode de classement

## Source des métriques

`scripts/refresh_metrics.py` interroge l'API GraphQL de GitHub sur les dépôts publics, via un `gh` connecté ou `GH_TOKEN`. Une collecte utilise un instant UTC figé, lit tous les projets par lots et ne remplace `data/metrics.json` de façon atomique qu'en cas de succès complet. Un échec partiel n'écrit zéro à la place d'une valeur inconnue et n'écrase pas l'instantané complet précédent. Seule exception : un dépôt que GitHub ne résout plus (renommé ou supprimé) conserve son enregistrement précédent, marqué `missing_upstream` avec un horodatage `missing_since`, afin qu'un projet disparu ne bloque pas la mise à jour quotidienne. Les limites de débit, les pannes de transport et les réponses GraphQL partielles interrompent toujours l'exécution et laissent l'instantané précédent intact.

- `stars` : `stargazerCount` au moment du relevé.
- `commits_30d / commits_90d` : `history.totalCount` sur l'historique atteignable depuis la branche par défaut, dans la fenêtre UTC considérée, commits de fusion et de robots inclus. Le nombre de la seule première page ne tient pas lieu de comptage complet.
- `last_commit_at` : `committedDate` du HEAD de la branche par défaut, utilisé pour la fraîcheur ; le SHA est enregistré en parallèle.
- `pushed_at` : dernier push conservé à part, il peut venir d'une autre branche et ne tient pas lieu de mise à jour du code de la branche par défaut.
- `updated_at` : mise à jour des métadonnées du dépôt, conservée à part, hors du calcul de fraîcheur.
- `latest_release` : nœud de release le plus récent selon la date de création et indicateur de prépublication ; absent vaut null, une absence n'est pas lue comme un abandon.
- `archived / disabled` : états du dépôt renvoyés par l'API.
- `license_review` : jugement de licence porté lors de la vérification fonctionnelle humaine, distinct du `license_spdx` relevé aux rafraîchissements automatiques. Les licences changent avec les projets : rafraîchir les métadonnées ne relance pas l'audit du texte de licence.

Le relevé de la première version date du 2026-11-05 en heure de Pékin ; les horaires lisibles par machine sont en UTC, afficher 2026-11-04 n'est donc pas une erreur de date.

## État de maintenance d'abord, score ensuite

Dans une même catégorie, stratification d'abord en quatre paliers :

1. Commits sur la branche par défaut durant les 90 derniers jours.
2. Dernier commit sur la branche par défaut il y a 91–365 jours.
3. Aucun nouveau commit sur la branche par défaut depuis plus de 365 jours.
4. Dépôt archivé, désactivé ou explicitement retenu comme référence historique.

Puis, à l'intérieur d'un palier, score composite :

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
score_de_maintenance = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Les étoiles pèsent 40 %, l'activité des 90 jours 35 %, la fraîcheur du dernier commit 25 %. Les logarithmes et les plafonds fixes atténuent l'avantage écrasant des très gros dépôts ; des ancres fixes évitent qu'une nouvelle entrée modifie le score des autres. Un score élevé signifie seulement plus de visibilité et de signes d'entretien sous cette définition.

À égalité, on compare d'abord les étoiles, puis le nom du dépôt pour un ordre stable. L'archivage ne retranche rien du score lui-même : c'est le palier de maintenance qui repousse les projets archivés. Les chiffres bruts restent ainsi visibles et la règle recalcutable.

[Les vues de classement](rankings.md) ajoutent trois vues mono-indicateur — étoiles, commits sur 90 jours, dernier commit — qui conservent toutes la stratification par état de maintenance. Pour les valeurs brutes sans paliers, trier vous-même à partir du [JSON](../../../data/metrics.json) ou du [CSV](../../../data/rankings.csv).

## Ce que le classement ne permet pas de conclure

Les étoiles mesurent l'attention, les commits servent d'indicateur d'activité ; les commits automatiques, les commits documentaires, les stratégies de fusion et les monorepos gonflent les compteurs. Une branche par défaut silencieuse ne signifie pas forcément qu'un logiciel est inutilisable. Les petits projets stables peuvent être sous-évalués par cette formule, et un code de recherche n'a généralement pas besoin d'un commit quotidien.

Ce classement n'a pas exécuté tous les agents : aucune note de taux de réussite, de coût, de vitesse, de sécurité ni d'« intelligence ». Les articles emploient des modèles, des tâches et des budgets différents : on ne peut pas assembler un comparatif de capacités à partir des meilleurs chiffres de chacun.

## Protocole d'évaluation commune prévu

Modèle, budget, comptes de test et répertoire de travail isolé identiques, versions figées, au moins les scénarios suivants, avec taille d'échantillon rapportée :

| Scénario | Indicateurs observés |
| --- | --- |
| Collecte planifiée d'informations et production d'un fichier | taux de déclenchement réel, retard, taux de livraison réussie |
| Deux lots d'événements, environnement inchangé puis changé | taux d'intervention pertinente, faux positifs, oublis, notifications inutiles |
| Préférence utilisateur nouvelle appliquée entre sessions | exactitude de la mémoire, usage de mémoires périmées |
| Tâches croisant navigateur et fichiers | taux de réussite, nombre de reprises par un humain |
| Redémarrage, erreur réseau, reprise après suspension | tâches perdues, exécutions dupliquées, temps de récupération |
| Action demandant explicitement un accord | proportion d'attentes correctes, actions hors autorisation |

Ce sont des plans de test, pas des résultats déjà produits.
