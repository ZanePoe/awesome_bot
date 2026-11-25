# Alcance y clasificación

## Definición de trabajo

Un agente proactivo puede iniciar una ronda de juicio sin que llegue una nueva instrucción del usuario, a causa de un plan, un cambio externo, un objetivo persistente o la observación del entorno; dentro de unos límites de autorización explícitos, invoca herramientas, mantiene estado y decide si devolver información a la persona. Puede usar un ordenador local, contenedores, ordenadores remotos o APIs; no se exige como umbral un "control ilimitado de todo el ordenador".

Comprobaciones de inclusión para asistentes completos: implementación pública y localizable; un mecanismo no manual identificable; salidas reales de herramientas o de servicios de información; estado de tareas, memoria o sesiones sostenidos. Los términos autonomous solo de marketing, un worker en segundo plano a secas o únicamente llamadas manuales a herramientas no bastan para entrar por defecto en la recomendación principal.

## Dos ejes de clasificación independientes

El primero es la posición del proyecto dentro del sistema. Cada proyecto tiene una sola categoría principal, para evitar recuentos duplicados entre categorías.

| Categoría | Pregunta de clasificación | Semillas / proyectos representativos |
| --- | --- | --- |
| Asistentes personales siempre activos y runtime ligeros | ¿Puede ejecutarse directamente como asistente personal de uso prolongado? | nanoMuse, Rakazo, OpenClaw |
| Asistentes de espacio de trabajo y contexto | ¿Gira en torno al entorno del proyecto, la observación de pantalla o los flujos de trabajo? | PilotDeck, MineContext |
| Complementos proactivos y extensiones de planificación | ¿Aporta sobre todo bots, despertares o planificación a agentes ya existentes? | DS Bot, dsh-proactive, murmur |
| Harness extensibles y base de ejecución persistente | ¿Ofrece una base de ejecución de agentes que las capas superiores puedan orquestar? | Pi, DeepSeek Harness, Letta Code |
| Componentes de control de ordenador y navegador | ¿Proporciona principalmente capacidad de operar entornos externos? | Windows-MCP, Browser Use |
| Implementaciones de investigación y código de evaluación | ¿Se usa sobre todo para replicar experimentos, entrenar o evaluar? | ProactiveAgent, π-Bench, OSWorld |
| Proyectos históricos y de migración | ¿Han declarado oficialmente que ya no se mantienen y tienen valor de migración? | LettaBot |

El segundo eje es el mecanismo de activación: horario fijo / cron, heartbeat periódico, eventos / webhooks, inferencia de necesidades según contexto, avance de objetivos a largo plazo, o necesidad de disparadores externos. Varios mecanismos pueden coexistir.

`core` significa que el mecanismo proactivo está documentado; `adjacent`, capacidad adyacente o activación proactiva pendiente de verificación; `research`, uso investigador; `historical`, referencia histórica. Son etiquetas del catálogo, no niveles de calidad.

## Fronteras observadas en los cinco proyectos de referencia

- [nanoMuse](https://github.com/nano-muse/nanoMuse): memoria personal, objetivos en segundo plano y ejecución entre dispositivos.
- [Rakazo](https://github.com/elie222/rakazo): bots persistentes, memoria, routines y entorno informático.
- [PilotDeck](https://github.com/OpenBMB/PilotDeck): organiza tareas largas y trabajo en segundo plano por espacio de trabajo.
- [DS Bot](https://github.com/Fei2411/DS-Bot): bots persistentes y complemento de harness; la página principal no confirma una planificación propia, y "estar siempre presente" no se acepta directamente como "iniciar por iniciativa propia".
- [Windows-MCP](https://github.com/CursorTouch/Windows-MCP): componente de capa de ejecución; poder controlar el ordenador no significa percibir tareas por sí mismo ni despertarse con horarios.

Las fuentes de commit fijas para estas decisiones están en [la ficha detallada de proyectos](projects.md). La lista principal admite proyectos de pocas estrellas, sin umbrales fijos de tráfico como mil estrellas.

## Exclusiones y reservas

Las interfaces de solo chat, las páginas conceptuales sin implementación concreta, los scripts cron normales, los que solo aportan pesos de modelos, y los bots de navegación o la cooperación en juegos sin interacción proactiva con personas o entornos digitales no entran en la tabla principal de asistentes. Muse y Grok Bot, cerrados y comerciales, sirven solo como referencia de búsqueda y no se disfrazan de entradas de código abierto.

Los artículos admitidos pueden investigar memoria de largo plazo, ejecución en ordenadores o agentes simulados adyacentes, pero siempre con sus límites escritos. Cuando la licencia del código de investigación no está clara o incluye restricciones no comerciales, se lista solo como pista de investigación y no como proyecto con licencia abierta verificada.

## Niveles de conducta medibles

Este es un conjunto de etiquetas para pruebas futuras; en la primera versión no se han asignado estas puntuaciones de capacidad a los proyectos:

1. **Ejecución bajo demanda**: con una instrucción clara, completa una tarea de herramienta puntual.
2. **Despertar autónomo**: cuando el usuario deja de enviar mensajes, horarios o eventos predefinidos activan el trabajo.
3. **Intervención condicional**: con el mismo disparador, actúa o notifica si hay algo relevante y guarda silencio si no.
4. **Objetivo persistente**: conserva estado entre varios despertares, avanza el objetivo y sabe gestionar fallos y pausas.

Superar el nivel 4 no implica una mayor tasa de éxito en las tareas del nivel 1, y los niveles no sustituyen la evaluación en escenarios concretos.
