# Transformer un agent existant en assistant proactif

Choisir d'abord le socle d'exécution, puis ajouter le déclenchement, l'état persistant et la livraison des résultats. Un simple cron règle le démarrage à heure fixe, sans donner gratuitement la compréhension des besoins ni la gestion d'objectifs de long terme.

| Base existante | Voie à explorer | Mécanisme vérifié | Limites actuelles |
| --- | --- | --- | --- |
| Pi | [rho](https://github.com/mikeyobrien/rho) | fonctionnement permanent, mémoire persistante, heartbeat | application de niveau supérieur pour Pi ; vérifier la plateforme d'exécution et l'instantané de maintenance |
| Pi / Claude / Codex CLI | [murmur](https://github.com/t0dorakis/murmur) | réveil périodique des CLI via des tâches définies en Markdown | la livraison et les actions métier restent à la charge de l'agent appelé |
| DeepSeek Harness | [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive) | réveil planifié au niveau de l'hôte sur session refroidie, clôture silencieuse | vérifier les versions DSH / plugin ; l'hôte doit tourner |
| DeepSeek Harness | [DS Bot](https://github.com/Fei2411/DS-Bot) | bots nommés persistants, discussions de groupe et mémoire | aucun mécanisme planifié autonome prouvé par la page d'accueil ; les combinaisons avec d'autres plugins ne sont pas testées |
| Hermes Agent | [cron intégré](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | tâches planifiées sans surveillance et livraison par canal | utiliser d'abord le mécanisme intégré ; ce catalogue ne déploie rien à la place de l'utilisateur |
| Hermes desktop | [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | interface bot + routines cron de l'hôte | archivé actuellement, conservé comme référence de design et de code |
| OpenClaw | [Pulse](https://github.com/Hypostas/pulse) | réveils webhook pilotés par capteurs et urgence | dépend de l'hôte ; ne remplace pas toutes les fonctions de cron |
| Letta | [Letta Code](https://github.com/letta-ai/letta-code) + [scheduling](https://docs.letta.com/letta-code/scheduling) | agents persistants, environnements distants, self-managed schedules | LettaBot est abandonné, la migration suit d'abord la nouvelle voie officielle |
| Tout hôte compatible MCP | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | outils de contrôle de Windows | comble seulement la couche d'exécution ; déclenchement, état et livraison restent à ajouter |

Ces combinaisons proviennent de documentation publique confirmée, ce n'est pas un rapport de test d'intégration de compatibilité. Pour une première validation, on peut prendre comme tâche minimale « générer un fichier dans un répertoire isolé à une heure donnée », puis vérifier le silence en l'absence de changement et l'absence de doublons après redémarrage.

Preuves, licences et dates de vérification de tous les projets dans [le détail des projets](projects.md).
