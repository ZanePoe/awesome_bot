# Método de búsqueda y registro de cobertura

Esta ronda siguió un proceso de tres pasadas: "proyectos de referencia -> palabras de rasgo -> web y GitHub -> relleno de índices -> verificación en la documentación original". El entregable es la primera versión del catálogo selecto, y la razón de parar es el límite de tres pasadas previsto de antemano, **no la afirmación de haberlo buscado todo**. La tercera pasada aún encontraba fuentes nuevas, así que se puede seguir ampliando.

## Términos de búsqueda derivados de los proyectos de referencia

| Rasgo | Palabras clave en inglés | Palabras clave en chino |
| --- | --- | --- |
| No espera instrucciones nuevas | proactive agent, anticipatory assistant, initiative | 主动式智能体、主动助手、需求预判 |
| Presencia permanente | always-on, persistent agent, sessionless, background agent | 常驻助手、持久 Agent、后台运行 |
| Despertar autónomo | heartbeat, cron, scheduler, event-driven, webhook, routines | 心跳、定时、事件驱动、周期任务 |
| Acción real | computer use, desktop automation, browser agent, MCP | 电脑操作、桌面自动化、浏览器 Agent |
| Comprensión a través del tiempo | long-term memory, user context, personalization, long-horizon | 长期记忆、用户上下文、个性化、长期目标 |
| Adaptar bases existentes | harness, plugin, extension, Pi, Hermes, DeepSeek Harness | Harness 插件、扩展、二次开发 |
| Investigación sobre proactividad | proactive assistance benchmark, intervention timing, abstention | 主动辅助评测、介入时机、保持静默 |

La palabra genérica autonomous agent devuelve con facilidad ejecutores de un solo uso, bots de juego y flujos de trabajo corrientes; por eso se acotó con palabras de mecanismo como heartbeat / routines / persistent y luego se verificó el README. Grok Bot y Muse sirvieron para descubrir la categoría de producto; la condición de código abierto se decide siempre por el repositorio y su licencia.

## Las tres pasadas

| Pasada | Lotes de búsqueda/verificación | Resultados registrados | Fuentes nuevas | Tasa de fuentes nuevas |
| --- | --- | --- | --- | --- |
| 1 | 12 | 228 | 220 | 96.5% |
| 2 | 6 | 53 | 42 | 79.2% |
| 3 | 4 | 171 | 138 | 80.7% |

El registro de búsqueda contiene 22 lotes: un lote de recolección de enlaces de índices, dos grupos de expansión con la búsqueda nativa de repositorios de GitHub y la verificación por lotes de repositorios originales y artículos. No son 22 palabras clave de Internet independientes, ni los 400 registrados son proyectos aptos para su inclusión.

- La primera pasada cubrió ocho ejes de búsqueda: semántica, documentación oficial, índices selectos, repositorios, alternativas, evaluaciones, limitaciones y cambios recientes. El techo de recolección de índices fue de 100 enlaces, y cada grupo de búsqueda web registró habitualmente hasta 20 resultados.
- La segunda pasada añadió, a partir de los resultados, nombres nuevos como rho, murmur, Pulse, PASK, ProAgentBench y PIRA-Bench, y verificó asistentes completos y extensiones de harness.
- La tercera pasada usó la búsqueda nativa de GitHub para cubrir huecos y volvió al README oficial, a las métricas GraphQL de GitHub y a los resúmenes de los artículos de todas las entradas finales. La evidencia de funciones quedó fijada a commits.

La deduplicación se basa sobre todo en la normalización de URL, el canonical repo y el ID de arXiv. Los dominios espejo encontrados en búsquedas web pudieron contarse como fuentes candidatas distintas dentro del recuento de investigación; el catálogo final de proyectos y artículos sí está deduplicado con esas claves de entidad. La tasa de fuentes nuevas es una métrica del proceso de búsqueda, no de relevancia ni de calidad de los proyectos.

Los cinco enlaces de referencia originales quedaron todos cubiertos (5/5). Los ocho ejes de búsqueda obtuvieron pistas relevantes, lo que no significa que cada subcampo esté cubierto por completo. No hubo estudios con usuarios ni pruebas en máquinas reales; las funciones se documentan según lo que reporta cada autor.

## Fábrica de contenido

Se llamó a la búsqueda estructurada por la vía curl de la habilidad `content-factory-search-api`, en el rango **2026-08-05 a 2026-11-05**, con un máximo de 30 resultados por grupo y un máximo de 15 tras la deduplicación.

Las consultas de esta ronda: `主动式 Agent`, `Grok Bot OR nanoMuse OR rakazo OR PilotDeck`, `Hermes Agent OR DeepSeek Harness OR Pi Agent`, `OpenClaw`, `Hermes`. Las cinco peticiones devolvieron JSON correcto, pero los arrays de resultados estuvieron vacíos, así que ningún contenido de la fábrica de soporte sirvió como evidencia de las entradas finales; un resultado vacío no demuestra que esos proyectos no existan en la base ni en Internet. No se consultó el histórico completo. Con cero resultados no hace falta lanzar el cálculo vectorial.

En el repositorio público solo se conservan los términos de búsqueda, el rango de fechas y las estadísticas de resultados; no se publican direcciones de servicios privados, claves ni textos internos.

## Correcciones en fuentes originales y limitaciones

- El [README de LettaBot](https://github.com/letta-ai/lettabot) anuncia explícitamente que deja de mantenerse activamente y dirige la migración a Letta Code. Los metadatos de GitHub muestran además el repositorio archivado.
- El diseño de bots + cron de [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) sigue teniendo valor de referencia, pero la API de esta ronda indica que está archivado, por lo que figura como referencia histórica.
- [Pi](https://github.com/earendil-works/pi) usa la ruta actual del canonical repo; la antigua `badlogic/pi-mono` no se repite.
- [MemoProAgent](https://arxiv.org/abs/2610.22671) es el título de la versión actual del mismo artículo; el nombre anterior ProPerAgent no se lista aparte; su código de investigación usa una licencia con condición no comercial, por lo que no entra en la recomendación de licencias abiertas.
- La página actual de [ProactiveBench](https://arxiv.org/abs/2603.19466) indica ECCV 2026; no se arrastra la etiqueta ICLR 2026 de índices de terceros, y no se lo confunde con el benchmark homónimo de ProactiveAgent.
- La página de Mame declara MIT, pero no se localizó el texto completo de la licencia; en ContextAgent no se encontró LICENSE. Ambos conservan el hueco de verificación: que algo sea públicamente visible no equivale a una licencia completa.

## Sin cubrir y pendiente de avanzar

Las ramas de compañía multimodal, operaciones sectoriales, dispositivos domésticos y aprendizaje proactivo vertical solo dieron pistas y no se incluyeron a fondo en esta primera versión. No se hicieron experimentos de comparación con las funciones de Grok Bot / Muse, cerrados. El mantenimiento en segundo plano en móviles, la fiabilidad entre dispositivos y la compatibilidad de combinaciones concretas de complementos siguen necesitando pruebas reales. No se compararon las mejores cifras de artículos distintos, para evitar falsas clasificaciones por diferencias de modelo, datos y presupuesto.

El resumen y la clasificación de los mecanismos centrales son juicios editoriales. En esta ronda no se hicieron experimentos de ablación; no se puede responder "sin memoria/planificación, quién cae más". Las estrellas y los commits solo sostienen la ordenación de mantenimiento.

## Archivos verificables

- [Registro de búsqueda](../../../research/search-log.json): pasadas, ejes, consultas, fuentes y recuentos de resultados.
- [Decisiones de clasificación y evidencia](../../../research/decisions.json): fronteras de inclusión y fuentes fijadas a commit.
- [Primera instantánea de métricas](../../../research/initial-metrics.json): conserva el resultado de la primera recolección; las actualizaciones diarias posteriores no la sobrescriben.
- [Instantánea actual de métricas](../../../data/metrics.json) y [CSV de ordenación](../../../data/rankings.csv): la clasificación recalculable más reciente.
- [Estado de la investigación](../../../research/status.json) y [verificación de integridad](../../../research/verification.json): sin referencias de evidencia colgantes ni errores de URL normalizadas duplicadas; las cinco consultas con cero resultados se conservan como advertencia conocida.

El texto completo de los resultados de búsqueda y los registros de ejecución de las herramientas locales se guardan en la máquina local y no se copian al repositorio público. Las 99 evidencias/juicios y los 123 registros de métricas del estado de investigación son recuentos de auditoría locales; la versión pública aporta las decisiones enlazadas, las fuentes originales y las instantáneas de métricas.
