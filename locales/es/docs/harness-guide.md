# Convertir un agente existente en asistente proactivo

Primero elige la base de ejecución; después añade disparadores, estado persistente y entrega de resultados. Añadir solo un cron resuelve el arranque programado, pero no otorga por sí mismo comprensión de necesidades ni gestión de objetivos a largo plazo.

| Base existente | Ruta investigable | Mecanismo verificado | Frontera actual |
| --- | --- | --- | --- |
| Pi | [rho](https://github.com/mikeyobrien/rho) | Ejecución siempre activa, memoria persistente, heartbeat | Aplicación de nivel superior sobre Pi; revisa las plataformas de ejecución y la instantánea de mantenimiento |
| Pi / Claude / Codex CLI | [murmur](https://github.com/t0dorakis/murmur) | Despierta CLIs periódicamente según tareas definidas en Markdown | La entrega y las acciones de negocio las sigue realizando el agente invocado |
| DeepSeek Harness | [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive) | Despertar programado a nivel de host de sesiones enfriadas, con cierre silencioso | Verifica las versiones de DSH y del complemento; el anfitrión debe seguir en ejecución |
| DeepSeek Harness | [DS Bot](https://github.com/Fei2411/DS-Bot) | Bots persistentes con nombre, chats grupales y memoria | La página principal no confirma un mecanismo propio de temporización; las combinaciones con otros complementos no se han probado |
| Hermes Agent | [cron integrado](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | Tareas programadas sin supervisión y entrega por canales | Usa primero el mecanismo integrado; este catálogo no ha desplegado nada por los usuarios |
| Hermes de escritorio | [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | Interfaz de bots + routines cron del anfitrión | Archivado actualmente; solo se conserva como referencia de diseño y código |
| OpenClaw | [Pulse](https://github.com/Hypostas/pulse) | Despertar por webhook según sensores y urgencia | Depende del anfitrión; no sustituye a todas las funciones de cron |
| Letta | [Letta Code](https://github.com/letta-ai/letta-code) + [scheduling](https://docs.letta.com/letta-code/scheduling) | Agentes persistentes, entornos remotos y self-managed schedules | LettaBot está retirado; la referencia prioritaria de migración es la ruta oficial nueva |
| Cualquier host compatible con MCP | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | Herramientas de operación de Windows | Solo completa la capa de ejecución; faltan disparadores, estado y entrega |

Lo anterior son combinaciones cuya entrada confirma la documentación pública; no es un informe de pruebas de integración de compatibilidad. Para la primera validación puede usarse como tarea mínima "generar un archivo en un directorio aislado a la hora indicada", y después comprobar si guarda silencio cuando no hay cambios y si las tareas se duplican tras un reinicio.

Las evidencias, licencias y fechas de verificación de todos los proyectos están en [la ficha detallada de proyectos](projects.md).
