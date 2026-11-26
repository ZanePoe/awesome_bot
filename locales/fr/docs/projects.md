# Fiches projets et preuves

Chaque fonction provient d'une documentation publique vérifiée ; rien n'a été installé ni soumis à un test de capacités commun dans ce dépôt. Les preuves sont figées autant que possible au commit de la vérification, et un rafraîchissement des métriques ne modifie pas les conclusions fonctionnelles.


<a id="openclaw--openclaw"></a>

## [OpenClaw](https://github.com/openclaw/openclaw)

Assistant personnel always-on reliant canaux de messagerie, mémoire et outils.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié / heartbeat / événements.
- Limites : L'exécution en arrière-plan dépend de la passerelle ; les permissions de chaque plateforme et de chaque outil se configurent séparément.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 11646 commits sur 30 jours, 48572 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/openclaw/openclaw/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/openclaw/openclaw/blob/8cb658e39b6dbe1bbe03746bf2a468a898c15da2/README.md#L18) · [Source2](https://docs.openclaw.ai/gateway/heartbeat) · [Source3](https://docs.openclaw.ai/gateway/heartbeat).

<a id="nousresearch--hermes-agent"></a>

## [Hermes Agent](https://github.com/NousResearch/hermes-agent)

Agent personnel avec mémoire persistante, accumulation de compétences et livraisons planifiées sur plusieurs canaux.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié / heartbeat de session.
- Limites : Fonctions documentées d'après la documentation officielle ; aucun test sur machine réalisé dans ce catalogue.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 17323 commits sur 30 jours, 50744 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/NousResearch/hermes-agent/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/NousResearch/hermes-agent/blob/cad0aaaf0d77ffa4899ebf0d3db8bae7a6b5147f/README.md#L27).

<a id="hkuds--nanobot"></a>

## [nanobot](https://github.com/HKUDS/nanobot)

Agent personnel Python léger prenant en charge fichiers, mémoire, MCP et objectifs de long terme.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié / déclencheurs locaux.
- Limites : Après un redémarrage du service d'arrière-plan, les tâches planifiées manquées ne sont pas rejouées ; voir la note de récupération officielle.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 311 commits sur 30 jours, 1220 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/HKUDS/nanobot/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/HKUDS/nanobot/blob/ce3aa50e70f6550d7be19f73f2cfa2ba6fb66880/README.md#L63).

<a id="zeroclaw-labs--zeroclaw"></a>

## [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

Runtime d'agent en Rust avec services d'arrière-plan, outils et flux déclenchés par événements.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : cron / webhook / MQTT.
- Limites : Le périmètre du contrôle de l'ordinateur dépend des outils configurés et de l'environnement d'exécution.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 293 commits sur 30 jours, 1073 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/zeroclaw-labs/zeroclaw/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/zeroclaw-labs/zeroclaw/blob/683d10139bc200ab8db768fcb4515f79404846ac/README.md#L83).

<a id="milind-soni--openmausbot"></a>

## [OpenMausBot](https://github.com/milind-soni/OpenMausBot)

Application de chat multi-bots locale-first où chaque bot peut disposer de son modèle, de sa mémoire par fil, de son ordinateur et de ses applications connectées.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : schedules / webhooks / app events.
- Limites : L'exécution des bots dépend de CLI installés sur la machine (Claude, Codex, Grok, etc.) ou de fournisseurs de modèles compatibles ; le bureau cloud, Composio et les fonctions enterprise ont des limites de service ou de licence propres.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 6899 commits sur 30 jours, 12973 commits sur 90 jours.
- Licence : [Apache-2.0 (hors enterprise/)](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519) ; Sous Apache-2.0 une fois enterprise/ retiré ; enterprise/ relève d'une licence source-available distincte, exige une clé de licence en production et interdit la redistribution ou l'hébergement chez un tiers.
- Vérification fonctionnelle : 2026-11-06 ; [Source1](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L73) · [Source2](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L413) · [Source3](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519).

<a id="nanocoai--nanoclaw"></a>

## [NanoClaw](https://github.com/nanocoai/nanoclaw)

Assistant piloté par canaux de messagerie, qui fait tourner l'agent dans un conteneur et exécute des tâches périodiques.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié / script gates.
- Limites : L'environnement d'exécution est un conteneur ; on ne peut pas en déduire une capacité d'agir sur le bureau de n'importe quel hôte.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 152 commits sur 30 jours, 525 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/nanocoai/nanoclaw/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/nanocoai/nanoclaw/blob/f7440e85f8b2a75b17fc9a08f0cc6aacf723a1e2/README.md#L65).

<a id="elie222--rakazo"></a>

## [Rakazo](https://github.com/elie222/rakazo)

Bots persistants et espace de travail d'ordinateur d'équipe auto-hébergeables, avec modèles au choix et bacs à sable.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : routines.
- Limites : Les capacités sur ordinateur personnel, ordinateur d'équipe et conteneur dépendent de la configuration.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 3063 commits sur 30 jours, 4666 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/elie222/rakazo/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/elie222/rakazo/blob/ed67158935a95b6153aad6c9cd874c6cc8d2413d/README.md#L24).

<a id="nano-muse--nanomuse"></a>

## [nanoMuse](https://github.com/nano-muse/nanoMuse)

Agent personnel reliant téléphone et ordinateur, combinant mémoire, objectifs d'arrière-plan et actions sur l'appareil.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Surveillance d'objectifs / routines.
- Limites : Les capacités des appareils et les conditions d'exécution en arrière-plan varient selon la plateforme ; l'article et le logiciel sont listés séparément.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 846 commits sur 30 jours, 2767 commits sur 90 jours.
- Licence : [GPL-3.0](https://api.github.com/repos/nano-muse/nanoMuse/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/nano-muse/nanoMuse/blob/57f5c5abed2d66fa19ab8fc39fd52eb365e4f14d/README.md#L80).

<a id="moltis-org--moltis"></a>

## [Moltis](https://github.com/moltis-org/moltis)

Service d'agent personnel intégrant mémoire, voix, messagerie, navigateur et ordonnancement.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : cron.
- Limites : Les modèles et les intégrations nécessaires doivent être configurés par l'utilisateur.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 0 commits sur 30 jours, 49 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/moltis-org/moltis/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md#L28).

<a id="nearai--ironclaw"></a>

## [IronClaw](https://github.com/nearai/ironclaw)

Assistant personnel en Rust qui exécute des tâches d'arrière-plan via routines et heartbeats.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié / événements / heartbeat.
- Limites : L'isolation des outils est un choix de conception, pas la preuve d'un audit de sécurité mené par ce catalogue.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 0 commits sur 30 jours, 44 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/nearai/ironclaw/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md#L95).

<a id="afk-surf--comma"></a>

## [Comma](https://github.com/AFK-surf/Comma)

Combine un état de tâche persistant et un travail multi-appareils, en réveillant l'agent par des boucles de surveillance.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : routines / event loops.
- Limites : L'environnement d'exécution dans le cloud et la connexion aux appareils locaux sont des composants distincts.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 2 commits sur 30 jours, 10 commits sur 90 jours.
- Licence : [AGPL-3.0](https://api.github.com/repos/AFK-surf/Comma/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/AFK-surf/Comma/blob/66ab3dc92475005aea9afd123df36a28e4ef86ab/README.md#L64).

<a id="sipeed--picoclaw"></a>

## [PicoClaw](https://github.com/sipeed/picoclaw)

Assistant personnel en Go pour appareils à faibles ressources, avec outils de fichiers, d'exécution et d'ordonnancement.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : Planifié.
- Limites : Un runtime à faibles ressources n'implique pas que les modèles ou le navigateur appelés coûtent peu.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/sipeed/picoclaw/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md#L632).

<a id="khoj-ai--khoj"></a>

## [Khoj](https://github.com/khoj-ai/khoj)

Assistant de connaissance personnelle : recherche sur documents et sur le web, automatisations planifiées.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : scheduled automations.
- Limites : Centré sur le travail de connaissance et d'information, ce n'est pas un contrôleur de bureau universel.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [AGPL-3.0](https://api.github.com/repos/khoj-ai/khoj/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md#L50) · [Source2](https://docs.khoj.dev/features/automations) · [Source3](https://docs.khoj.dev/features/automations).

<a id="mikeyobrien--rho"></a>

## [rho](https://github.com/mikeyobrien/rho)

Assistant opérationnel personnel always-on construit sur Pi, avec mémoire persistante et vérifications proactives périodiques.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : heartbeat.
- Limites : C'est une application de niveau supérieur pour Pi ; le fonctionnement diffère entre Android et le bureau.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/mikeyobrien/rho/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/mikeyobrien/rho/blob/073a3ee8a5dc0efd5dd32d773a760575ed38abc7/README.md#L34).

<a id="maikunari--mame"></a>

## [Mame](https://github.com/maikunari/mame)

Assistant léger always-on avec mémoire persistante et canaux de messagerie, capable d'orchestrer des agents de codage.

- Catégorie : Assistants personnels always-on et runtimes légers ; Mécanisme proactif documenté.
- Déclenchement : cron / heartbeat.
- Limites : Utile comme référence de petite implémentation ; le score de maintenance ne mesure pas la maturité du projet.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT déclaré dans le README](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md) ; Texte complet de la licence introuvable ; candidat, absent du classement des recommandations open source.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md#L300).

<a id="copilotkit--openbot"></a>

## [OpenBot](https://github.com/CopilotKit/OpenBot)

Plateforme auto-hébergée de coworkers IA offrant à des agents AG-UI un navigateur dédié, un espace de fichiers, des permissions d'outils, un journal d'audit et des tâches planifiées.

- Catégorie : Assistants d'espace de travail et de contexte ; Mécanisme proactif documenté.
- Déclenchement : Routines planifiées / déclenchement humain.
- Limites : OpenBot gère l'environnement d'ordinateur, les politiques, l'audit et l'ordonnancement ; les capacités d'agent viennent du point de terminaison AG-UI connecté, et les sessions persistantes avec mémoire dépendent de CopilotKit Intelligence.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 1044 commits sur 30 jours, 1449 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/CopilotKit/OpenBot/license) ; Identifiée via GitHub licenseInfo ; le déploiement et les conditions de licence de CopilotKit Intelligence relèvent d'un cadre distinct.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L251) · [Source2](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L52).

<a id="agent0ai--agent-zero"></a>

## [Agent Zero](https://github.com/agent0ai/agent-zero)

Agent exécutant outils, projets et tâches de surveillance périodiques dans un environnement d'exécution sur ordinateur.

- Catégorie : Assistants d'espace de travail et de contexte ; Mécanisme proactif documenté.
- Déclenchement : scheduled operations.
- Limites : Borné par l'environnement d'exécution configuré ; il ne prend pas par défaut le contrôle de toutes les ressources de l'hôte.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 108 commits sur 30 jours, 438 commits sur 90 jours.
- Licence : [MIT](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE) ; Fichier LICENSE racine vérifié manuellement.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md#L259).

<a id="anil-matcha--suparagent"></a>

## [Suparagent](https://github.com/Anil-matcha/suparagent)

Espace de travail desktop et auto-hébergé qui centralise coworkers IA nommés, délégation d'équipe, conversations, mémoire, routines, tâches et validations.

- Catégorie : Assistants d'espace de travail et de contexte ; Mécanisme proactif documenté.
- Déclenchement : scheduled / webhook / manual routines.
- Limites : Le projet est encore en développement précoce ; le service auto-hébergé et les capacités ordinateur/navigateur sont expérimentaux ; la version hébergée est un produit distinct, les modèles et comptes restent à la charge de l'utilisateur, et certaines intégrations ne prennent en charge que Claude ou Codex.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 446 commits sur 30 jours, 817 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/Anil-matcha/suparagent/license) ; Identifiée via GitHub licenseInfo ; le service hébergé, les moteurs tiers, Composio et les fournisseurs de modèles suivent leurs propres conditions.
- Vérification fonctionnelle : 2026-11-11 ; [Source1](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L3) · [Source2](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L71) · [Source3](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L183).

<a id="openbmb--pilotdeck"></a>

## [PilotDeck](https://github.com/OpenBMB/PilotDeck)

Isole fichiers, mémoire et compétences par espace de travail, découvre des tâches en arrière-plan et livre des fichiers.

- Catégorie : Assistants d'espace de travail et de contexte ; Mécanisme proactif documenté.
- Déclenchement : Découverte de tâches always-on.
- Limites : Le benchmark du README est auto-déclaré par les auteurs ; ce dépôt ne l'inclut pas dans un classement de capacités transverse.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 468 commits sur 30 jours, 960 commits sur 90 jours.
- Licence : [AGPL-3.0](https://api.github.com/repos/OpenBMB/PilotDeck/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/OpenBMB/PilotDeck/blob/2865f05b1722c7473ea8a9dda317a92fb8c92dd8/README.md#L97).

<a id="copilotkit--openfuse"></a>

## [OpenFuse](https://github.com/CopilotKit/openfuse)

Application open source offrant une interface d'agent personnel, un navigateur et un espace de travail.

- Catégorie : Assistants d'espace de travail et de contexte ; Capacités adjacentes.
- Déclenchement : Workers de tâches d'arrière-plan ; déclenchement autonome à vérifier.
- Limites : Un worker d'arrière-plan ne vaut pas prise d'initiative autonome ; certains connecteurs et actions restent au roadmap.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 3 commits sur 30 jours, 147 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/CopilotKit/openfuse/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/CopilotKit/openfuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md#L43).

<a id="copilotkit--openduet"></a>

## [OpenDuet](https://github.com/CopilotKit/OpenDuet)

Modèle d'application open source pour construire un assistant de travail proactif.

- Catégorie : Assistants d'espace de travail et de contexte ; Mécanisme proactif documenté.
- Déclenchement : routines / suggestions d'arrière-plan.
- Limites : Le modèle demande de configurer dépendances et modèles ; ce n'est pas un service hébergé déjà déployé.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 24 commits sur 30 jours, 92 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/CopilotKit/OpenDuet/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/CopilotKit/OpenDuet/blob/f52288fff5ccdbd3de428d573d9f026fce5ff480/README.md#L5).

<a id="volcengine--minecontext"></a>

## [MineContext](https://github.com/volcengine/MineContext)

Assistant d'information proactif qui tire du contexte à l'écran des enseignements, des tâches à faire et des synthèses quotidiennes et hebdomadaires.

- Catégorie : Assistants d'espace de travail et de contexte ; Capacités adjacentes.
- Déclenchement : Observation du contexte / notifications proactives.
- Limites : Les suggestions proactives sont documentées ; on ne peut pas en déduire qu'il pilote de façon autonome toutes les applications.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/volcengine/MineContext/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/README.md#L9).

<a id="fei-craft--ds-bot"></a>

## [DS Bot](https://github.com/Fei-Craft/DS-Bot)

Étend DeepSeek Harness en application desktop et plugins avec mémoire, discussions de groupe et collaboration entre bots.

- Catégorie : Plugins proactifs et extensions d'ordonnancement ; Capacités adjacentes.
- Déclenchement : Bots persistants / discussions de groupe ; réveil autonome à vérifier.
- Limites : La page d'accueil ne confirme pas de mécanisme planifié autonome ; une session de longue durée n'équivaut pas à un fonctionnement proactif.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 2844 commits sur 30 jours, 3858 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/Fei-Craft/DS-Bot/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/Fei-Craft/DS-Bot/blob/71d344bf193f3f18185f25de3d8e5c483046910a/README.md#L41).

<a id="john-walks-slow--dsh-proactive"></a>

## [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive)

Ajoute à DeepSeek Harness des réveils proactifs capables de se déclencher même après refroidissement de la session.

- Catégorie : Plugins proactifs et extensions d'ordonnancement ; Mécanisme proactif documenté.
- Déclenchement : once / interval / cron au niveau de l'hôte.
- Limites : Dépend du fonctionnement de l'hôte et de la compatibilité des versions ; prévoit des réglages de silence et de budget de notifications.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 0 commits sur 30 jours, 97 commits sur 90 jours.
- Licence : [MIT](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/packages/dsh-proactive/LICENSE) ; Fichier LICENSE du sous-répertoire du plugin vérifié manuellement.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/README.md#L1).

<a id="t0dorakis--murmur"></a>

## [murmur](https://github.com/t0dorakis/murmur)

Démon d'ordonnancement léger qui lance périodiquement des sessions CLI telles que Claude, Codex ou Pi.

- Catégorie : Plugins proactifs et extensions d'ordonnancement ; Mécanisme proactif documenté.
- Déclenchement : cron / interval.
- Limites : La livraison des messages et les actions métier incombent au prompt et à l'agent appelé.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/t0dorakis/murmur/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/t0dorakis/murmur/blob/d666df4c749c28ecb775613ecec8b12954b387e7/README.md#L10).

<a id="hypostas--pulse"></a>

## [Pulse](https://github.com/Hypostas/pulse)

Démon d'extension pour OpenClaw qui réveille l'agent selon les changements, les objectifs et l'urgence.

- Catégorie : Plugins proactifs et extensions d'ordonnancement ; Mécanisme proactif documenté.
- Déclenchement : Capteurs / déclenchement par urgence.
- Limites : Repose sur le webhook d'OpenClaw ; les affirmations d'autonomie de l'auteur ne sont pas des conclusions mesurées par ce dépôt.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/Hypostas/pulse/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/Hypostas/pulse/blob/4bebd1e23bff218dde1cd0b693f901493d45f972/README.md#L5).

<a id="nousresearch--hermes-bot-mode"></a>

## [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode)

Ajoute à Hermes desktop des bots nommés, des conversations distinctes et un panneau de tâches périodiques.

- Catégorie : Plugins proactifs et extensions d'ordonnancement ; Référence historique.
- Déclenchement : Routines cron de l'hôte.
- Limites : Dépôt archivé sur GitHub ; conservé comme référence d'interface bot et d'intégration cron pour Hermes, sans être recommandé comme plugin actif.
- État de maintenance actuel : Archivé / historique ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/NousResearch/Hermes-Bot-Mode/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/NousResearch/Hermes-Bot-Mode/blob/80fee22582b871b9765a65e2992b8b5a8211c9f8/README.md#L23).

<a id="earendil-works--pi"></a>

## [Pi](https://github.com/earendil-works/pi)

Harness d'agent extensible permettant de construire des assistants always-on via SDK, RPC et plugins.

- Catégorie : Harness extensibles et socles d'exécution persistants ; Capacités adjacentes.
- Déclenchement : Ordonnancement externe requis / extensions.
- Limites : L'ancienne adresse badlogic/pi-mono redirige ; se combine avec rho ou murmur.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 1378 commits sur 30 jours, 2364 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/earendil-works/pi/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/earendil-works/pi/blob/fcebc099565d8f30c15b321ff6a1af5f34d89400/README.md#L15).

<a id="deepseek-ai--deepseek-harness"></a>

## [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

Socle d'exécution d'agent reposant sur une architecture de plugins, adapté aux bots et aux plugins de réveil proactif.

- Catégorie : Harness extensibles et socles d'exécution persistants ; Capacités adjacentes.
- Déclenchement : Mécanisme proactif fourni par un plugin de l'hôte.
- Limites : Developer preview ; la compatibilité des plugins doit être vérifiée.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 3743 commits sur 30 jours, 14426 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/deepseek-ai/deepseek-harness/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/README.md#L7).

<a id="letta-ai--letta-code"></a>

## [Letta Code](https://github.com/letta-ai/letta-code)

Agent à mémoire persistante qui devient un assistant always-on via des environnements distants et des channels.

- Catégorie : Harness extensibles et socles d'exécution persistants ; Mécanisme proactif documenté.
- Déclenchement : remote environments / cron.
- Limites : Destination de migration officielle de LettaBot ; nécessite de combiner environnement distant et configuration d'ordonnancement.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 362 commits sur 30 jours, 978 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/letta-ai/letta-code/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/letta-ai/letta-code/blob/e6d6cc27ef1111da80e919dc1cef179613894b66/README.md#L29) · [Source2](https://docs.letta.com/letta-code/scheduling) · [Source3](https://docs.letta.com/letta-code/scheduling).

<a id="browser-use--browser-use"></a>

## [Browser Use](https://github.com/browser-use/browser-use)

Donne à un agent la compréhension des pages web et l'exécution dans le navigateur.

- Catégorie : Composants de contrôle ordinateur et navigateur ; Capacités adjacentes.
- Déclenchement : Tâches de navigateur à la demande.
- Limites : Agit surtout dans le navigateur ; ne prouve ni ordonnancement proactif ni contrôle du bureau entier.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 639 commits sur 30 jours, 954 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/browser-use/browser-use/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md#L1).

<a id="cursortouch--windows-mcp"></a>

## [Windows-MCP](https://github.com/CursorTouch/Windows-MCP)

Service MCP exposant à un agent les capacités de contrôle de l'ordinateur sous Windows.

- Catégorie : Composants de contrôle ordinateur et navigateur ; Capacités adjacentes.
- Déclenchement : Appelé par l'hôte.
- Limites : Ce composant de contrôle n'est pas un assistant personnel always-on ; modèles, mémoire et déclencheurs doivent être ajoutés.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 110 commits sur 30 jours, 180 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/CursorTouch/Windows-MCP/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/CursorTouch/Windows-MCP/blob/9ab92bca2772dfb53ae3ed4feb98dac22c5b3dea/README.md#L25).

<a id="alibaba--page-agent"></a>

## [Page Agent](https://github.com/alibaba/page-agent)

Agent JavaScript qui pilote l'interface d'une page web en langage naturel.

- Catégorie : Composants de contrôle ordinateur et navigateur ; Capacités adjacentes.
- Déclenchement : Appelé par la page ou par l'hôte.
- Limites : Couche de contrôle de page ; ne couvre pas le cycle de vie complet d'un assistant always-on.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 22 commits sur 30 jours, 40 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/alibaba/page-agent/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/alibaba/page-agent/blob/9eb6b6646500264d9034dd466a4270cb9fc1ef1e/README.md#L35).

<a id="bytedance--ui-tars-desktop"></a>

## [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop)

Application d'agent et outils associés pour l'action sur les interfaces graphiques et dans le navigateur.

- Catégorie : Composants de contrôle ordinateur et navigateur ; Capacités adjacentes.
- Déclenchement : Tâches ordinateur / navigateur à la demande.
- Limites : Exécuter automatiquement des tâches d'ordinateur et prendre l'initiative sans consigne sont deux dimensions distinctes.
- État de maintenance actuel : Archivé / historique ; 0 commits sur 30 jours, 8 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/bytedance/UI-TARS-desktop/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md#L13).

<a id="xlang-ai--osworld"></a>

## [OSWorld](https://github.com/xlang-ai/OSWorld)

Évalue l'exécution d'agents multimodaux dans de véritables environnements informatiques.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Évaluation de tâches sur ordinateur réel.
- Limites : Mesure l'exécution des tâches, pas en soi la prise d'initiative ni le moment d'une interruption.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 70 commits sur 30 jours, 213 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/xlang-ai/OSWorld/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/xlang-ai/OSWorld/blob/8903ebeb0efdf74331bd7dc37ed91ccbbff22317/README.md#L294).

<a id="zju-real--knowu-bench"></a>

## [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)

Évalue la capacité d'un agent mobile à recueillir les préférences, à intervenir de sa propre initiative et à demander l'accord.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Évaluation mobile personnalisée interactive.
- Limites : Ciblé sur l'interface mobile et les préférences personnelles, pas sur un runtime multiplateforme.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 1 commits sur 30 jours, 1 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/ZJU-REAL/KnowU-Bench/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/ZJU-REAL/KnowU-Bench/blob/c03a825991ede13add6631f2ed19b90755930dc6/README.md#L4).

<a id="facebookresearch--memo-pro-agent"></a>

## [MemoProAgent](https://github.com/facebookresearch/Memo-Pro-Agent)

Recherche qui puise dans la mémoire personnelle de long terme les éléments justifiant ou non une intervention proactive.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Évaluation d'interventions pilotées par la mémoire.
- Limites : Nom initial de l'article : ProPerAgent ; dédoublonné sous le même identifiant arXiv.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 0 commits sur 30 jours, 6 commits sur 90 jours.
- Licence : [CC-BY-NC-4.0](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/LICENSE) ; Licence non commerciale ; listé uniquement comme code de recherche.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/README.md#L3).

<a id="simplified-reasoning--pi-bench"></a>

## [π-Bench](https://github.com/Simplified-Reasoning/Pi-Bench)

Évalue l'identification de besoins cachés et l'assistance proactive dans des flux de travail multi-tours de long terme.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Évaluation de la proactivité.
- Limites : C'est un benchmark ; sans lien avec le harness Pi.
- État de maintenance actuel : Commits sur les 90 derniers jours ; 0 commits sur 30 jours, 1 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/Simplified-Reasoning/Pi-Bench/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/Simplified-Reasoning/Pi-Bench/blob/4f545be5d289b28ff022d2904d455007358ed3b7/README.md#L1).

<a id="thunlp--proactiveagent"></a>

## [ProactiveAgent](https://github.com/thunlp/ProactiveAgent)

Méthode de prédiction proactive de tâches, avec ses données et son code d'évaluation.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Observation d'événements / anticipation de tâches.
- Limites : Implémentation de recherche, pas un assistant personnel généraliste prêt à l'emploi.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/thunlp/ProactiveAgent/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/thunlp/ProactiveAgent/blob/3fcf9beebe256b86871659fbb12541c41c9381b9/README.md#L2).

<a id="xzf-thu--pask"></a>

## [PASK](https://github.com/xzf-thu/Pask)

Recherche sur l'assistance proactive combinant mémoire de long terme, contexte continu et contraintes de latence.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Détection de besoins latents / rester silencieux.
- Limites : Rapport technique et code de recherche ; la maturité d'usage doit être validée séparément.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/xzf-thu/Pask/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/xzf-thu/Pask/blob/d54646c52b1555232ce4ab39103768d7f65b8267/README.md#L30).

<a id="deepakn97--pare"></a>

## [PARE](https://github.com/deepakn97/pare)

Évalue les assistants proactifs en simulant des utilisateurs actifs et des environnements numériques à état.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Assistants proactifs / évaluation par simulation d'utilisateurs.
- Limites : Des utilisateurs simulés ne remplacent pas l'effet d'un usage prolongé par de vrais utilisateurs.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/deepakn97/pare/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/deepakn97/pare/blob/261149914a9e9dcacb12de620575c691d50e3c2e/README.md#L3).

<a id="tdemin16--proactivebench"></a>

## [ProactiveBench (MLLM)](https://github.com/tdemin16/proactivebench)

Benchmark de recherche évaluant la capacité des modèles multimodaux à obtenir d'eux-mêmes des informations utiles.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Évaluation proactive multimodale.
- Limites : À distinguer du benchmark homonyme utilisé par ProactiveAgent ; la page officielle de l'article indique ECCV 2026.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [MIT](https://api.github.com/repos/tdemin16/proactivebench/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/tdemin16/proactivebench/blob/428885c9224418b544dfbdbde5307bccc58018d5/README.md#L2).

<a id="openaiotlab--contextagent"></a>

## [ContextAgent](https://github.com/openaiotlab/ContextAgent)

Recherche sur l'usage des perceptions du monde ouvert pour décider d'un service proactif et des appels d'outils.

- Catégorie : Implémentations de recherche et code d'évaluation ; Ressource de recherche.
- Déclenchement : Contexte perceptif / prédiction de service.
- Limites : Les données et les scénarios d'outils de l'étude ne se généralisent pas directement à n'importe quel bureau.
- État de maintenance actuel : Aucun commit depuis 91–365 jours ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [À vérifier](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md) ; Aucun fichier LICENSE trouvé ; simple ressource de recherche, aucune autorisation présumée.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md#L3).

<a id="letta-ai--lettabot"></a>

## [LettaBot](https://github.com/letta-ai/lettabot)

Assistant personnel qui proposait canaux de messagerie, mémoire, heartbeat et tâches planifiées.

- Catégorie : Projets historiques et migrations ; Référence historique.
- Déclenchement : heartbeat / cron.
- Limites : Le README officiel annonce l'abandon de la maintenance active et recommande la migration vers Letta Code.
- État de maintenance actuel : Archivé / historique ; 0 commits sur 30 jours, 0 commits sur 90 jours.
- Licence : [Apache-2.0](https://api.github.com/repos/letta-ai/lettabot/license) ; Identifiée via GitHub licenseInfo ; aucune déduction sur la licence des données ou des poids de modèles associés.
- Vérification fonctionnelle : 2026-11-05 ; [Source1](https://github.com/letta-ai/lettabot/blob/99c3b5dd73550fe0a4eac2ee31b1c3229ca9e550/README.md#L8).
