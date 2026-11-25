# Périmètre et taxonomie

## Définition de travail

Un agent proactif engage une passe de jugement sans nouvelle consigne de l'utilisateur, à partir d'un plan, d'un changement externe, d'un objectif persistant ou d'une observation de l'environnement ; dans un périmètre d'autorisation explicite, il appelle des outils, conserve un état et décide de rendre compte ou non aux personnes. Il peut utiliser un ordinateur local, un conteneur, un ordinateur distant ou une API : détenir des droits illimités sur toute la machine n'est pas un critère d'entrée.

Contrôles d'inclusion pour un assistant complet : implémentation publiquement localisable ; mécanisme de déclenchement non manuel identifiable ; sortie réelle d'outils ou de services d'information ; état de tâche, mémoire ou session durables. Le seul mot « autonomous » dans du marketing, le seul worker d'arrière-plan ou le seul appel d'outil manuel ne suffisent pas à entrer dans la recommandation principale.

## Deux axes de classification indépendants

Le premier est la place du projet dans le système. Chaque projet n'a qu'une catégorie principale, pour éviter les doubles comptages entre catégories.

| Catégorie | Question de classement | Exemples de projets / graines |
| --- | --- | --- |
| Assistants personnels always-on et runtimes légers | Peut-il tourner directement comme assistant personnel de longue durée ? | nanoMuse, Rakazo, OpenClaw |
| Assistants d'espace de travail et de contexte | Tourne-t-il autour de l'environnement projet, de l'observation de l'écran ou des flux de travail ? | PilotDeck, MineContext |
| Plugins proactifs et extensions d'ordonnancement | Fournit-il surtout des bots, des réveils ou de l'ordonnancement à un agent existant ? | DS Bot, dsh-proactive, murmur |
| Harness extensibles et socles d'exécution persistants | Offre-t-il une base d'exécution d'agent que des applications de niveau supérieur peuvent orchestrer ? | Pi, DeepSeek Harness, Letta Code |
| Composants de contrôle ordinateur et navigateur | Fournit-il principalement la capacité d'agir sur un environnement externe ? | Windows-MCP, Browser Use |
| Implémentations de recherche et code d'évaluation | Sert-il surtout à reproduire des expériences, entraîner ou évaluer ? | ProactiveAgent, π-Bench, OSWorld |
| Projets historiques et migrations | La maintenance est-elle officiellement abandonnée, avec une valeur de migration ? | LettaBot |

Le second axe est le mécanisme de déclenchement : heure fixe / cron, heartbeat périodique, événements / webhook, déduction de besoins à partir du contexte, poursuite d'objectifs de long terme, ou nécessité d'un déclencheur externe. Plusieurs mécanismes peuvent coexister.

`core` signifie mécanisme proactif documenté ; `adjacent` désigne des capacités adjacentes ou un déclenchement proactif à vérifier ; `research` un usage de recherche ; `historical` une référence historique. Ce sont des étiquettes de catalogue, pas des niveaux de qualité.

## Limites déduites des cinq projets de référence

- [nanoMuse](https://github.com/nano-muse/nanoMuse) : mémoire personnelle, objectifs d'arrière-plan et exécution multi-appareils.
- [Rakazo](https://github.com/elie222/rakazo) : bots persistants, mémoire, routines et environnement d'ordinateur.
- [PilotDeck](https://github.com/OpenBMB/PilotDeck) : organise les tâches de long terme et le travail d'arrière-plan par espace de travail.
- [DS Bot](https://github.com/Fei2411/DS-Bot) : bot persistant et plugin de harness ; la page d'accueil ne confirme pas d'ordonnanceur autonome, « longtemps présent » n'est donc pas reconnu comme « initiative proactive ».
- [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) : composant de la couche d'exécution. Pouvoir contrôler un ordinateur n'implique pas de percevoir les tâches ni de se réveiller seul.

Les sources à commit figé de ces jugements sont dans [le détail des projets](projects.md). La liste principale admet des projets à faible étoilage : aucun seuil de trafic, par exemple mille étoiles, n'est imposé.

## Exclusions et conservations

Les interfaces de chat seules, les pages de concept sans implémentation concrète, les simples scripts planifiés, les dépôts de poids de modèles uniquement, ainsi que la navigation de robots ou la collaboration en jeu sans rapport avec un environnement personnel ou numérique n'entrent pas dans le classement des assistants principaux. Les produits commerciaux fermés Muse et Grok Bot ne servent que de repères de recherche et ne sont pas présentés comme des entrées open source.

Les articles peuvent couvrir la mémoire de long terme adjacente, l'exécution sur ordinateur et la recherche fondamentale sur les agents simulés, à condition d'écrire les limites. Quand la licence du code de recherche est inconnue ou comporte des restrictions non commerciales, il reste un indice de recherche et n'est pas étiqueté comme projet à licence ouverte vérifiée.

## Niveaux de comportement mesurables

Etiquettes prévues pour des tests ultérieurs : aucune note de capacité n'a encore été attribuée aux projets sur cette échelle.

1. **Exécution à la demande** : avec une consigne claire, achever une tâche unique impliquant des outils.
2. **Réveil autonome** : lorsque l'utilisateur n'envoie plus de message, une heure ou un événement prédéfini déclenche le travail.
3. **Intervention conditionnelle** : à déclencheur égal, agir ou notifier si nécessaire, rester silencieux sinon.
4. **Objectif persistant** : conserver l'état entre plusieurs réveils, faire avancer l'objectif et gérer l'échec comme la suspension.

Réussir le niveau 4 ne signifie pas un meilleur taux de réussite au niveau 1 ; les niveaux ne remplacent pas une évaluation par scénario précis.
