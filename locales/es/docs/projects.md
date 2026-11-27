# Descripciones de proyectos y evidencia

Cada función se verificó en documentación pública; no se instaló ni ejecutó nada, y no se han completado pruebas de capacidad uniformes. La evidencia se fija, en lo posible, al commit vigente en el momento de la verificación; las actualizaciones posteriores de métricas no modifican automáticamente los juicios sobre las funciones.


<a id="openclaw--openclaw"></a>

## [OpenClaw](https://github.com/openclaw/openclaw)

Asistente personal siempre activo que conecta canales de mensajería, memoria y herramientas.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación / heartbeat / eventos.
- Límites: La ejecución en segundo plano depende de la gateway; los permisos de cada plataforma y herramienta deben configurarse por separado.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 11407 commits / 30 días, 48489 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/openclaw/openclaw/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/openclaw/openclaw/blob/8cb658e39b6dbe1bbe03746bf2a468a898c15da2/README.md#L18) · [Fuente 2](https://docs.openclaw.ai/gateway/heartbeat) · [Fuente 3](https://docs.openclaw.ai/gateway/heartbeat).

<a id="nousresearch--hermes-agent"></a>

## [Hermes Agent](https://github.com/NousResearch/hermes-agent)

Agente personal con memoria persistente, acumulación de habilidades y entrega programada a través de canales.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación / heartbeat de sesión.
- Límites: Las funciones se documentan según la documentación oficial; no se han evaluado en ejecución real en este catálogo.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 17193 commits / 30 días, 50910 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/NousResearch/hermes-agent/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/NousResearch/hermes-agent/blob/cad0aaaf0d77ffa4899ebf0d3db8bae7a6b5147f/README.md#L27).

<a id="hkuds--nanobot"></a>

## [nanobot](https://github.com/HKUDS/nanobot)

Agente personal ligero en Python con archivos, memoria, MCP y objetivos a largo plazo.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación / disparadores locales.
- Límites: Al reiniciar el servicio en segundo plano no se recuperan las tareas programadas perdidas; consulta la nota oficial de recuperación.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 291 commits / 30 días, 1224 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/HKUDS/nanobot/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/HKUDS/nanobot/blob/ce3aa50e70f6550d7be19f73f2cfa2ba6fb66880/README.md#L63).

<a id="zeroclaw-labs--zeroclaw"></a>

## [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

Runtime de agentes en Rust con servicios en segundo plano, herramientas y flujos activados por eventos.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: cron / webhook / MQTT.
- Límites: El alcance del control del ordenador depende de las herramientas y del entorno de ejecución configurados.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 303 commits / 30 días, 1061 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/zeroclaw-labs/zeroclaw/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/zeroclaw-labs/zeroclaw/blob/683d10139bc200ab8db768fcb4515f79404846ac/README.md#L83).

<a id="nanocoai--nanoclaw"></a>

## [NanoClaw](https://github.com/nanocoai/nanoclaw)

Asistente operado desde canales de mensajería que ejecuta agentes en contenedores y tareas periódicas.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación / script gates.
- Límites: El entorno de ejecución es un contenedor; de ahí no puede concluirse ninguna capacidad general de operar el escritorio del anfitrión.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 157 commits / 30 días, 527 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/nanocoai/nanoclaw/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/nanocoai/nanoclaw/blob/f7440e85f8b2a75b17fc9a08f0cc6aacf723a1e2/README.md#L65).

<a id="milind-soni--openmausbot"></a>

## [OpenMausBot](https://github.com/milind-soni/OpenMausBot)

Aplicación de chat local-first con múltiples bots, donde cada bot puede usar modelo propio, memoria por hilo, ordenador y aplicaciones conectadas.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: schedules / webhooks / app events.
- Límites: Los bots dependen de CLIs locales como Claude, Codex o Grok, o de proveedores de modelos compatibles; el escritorio en la nube, Composio y las funciones enterprise tienen límites propios de servicio o de licencia.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 6718 commits / 30 días, 13062 commits / 90 días.
- Licencia: [Apache-2.0 (excepto enterprise/)](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519); Sin enterprise/ es la versión de código abierto Apache-2.0; enterprise/ tiene una licencia source-available aparte, requiere clave de licencia para producción y prohíbe redistribuir o alojar en servicios de terceros.
- Verificación de funciones: 2026-11-06; [Fuente 1](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L73) · [Fuente 2](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L413) · [Fuente 3](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519).

<a id="elie222--rakazo"></a>

## [Rakazo](https://github.com/elie222/rakazo)

Bots persistentes y espacio de trabajo informático de equipo, autoalojable, con modelos a elección y sandbox.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: routines.
- Límites: Las capacidades del ordenador privado, del ordenador de equipo y del contenedor se distinguen según la configuración.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 3061 commits / 30 días, 4709 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/elie222/rakazo/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/elie222/rakazo/blob/ed67158935a95b6153aad6c9cd874c6cc8d2413d/README.md#L24).

<a id="nano-muse--nanomuse"></a>

## [nanoMuse](https://github.com/nano-muse/nanoMuse)

Agente personal entre móvil y ordenador que combina memoria, objetivos en segundo plano y operación del dispositivo.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: revisión de objetivos / routines.
- Límites: Las capacidades del dispositivo y las condiciones de ejecución en segundo plano varían según la plataforma; el artículo y el software se listan por separado.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 826 commits / 30 días, 2799 commits / 90 días.
- Licencia: [GPL-3.0](https://api.github.com/repos/nano-muse/nanoMuse/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/nano-muse/nanoMuse/blob/57f5c5abed2d66fa19ab8fc39fd52eb365e4f14d/README.md#L80).

<a id="moltis-org--moltis"></a>

## [Moltis](https://github.com/moltis-org/moltis)

Servicio de agente personal que integra memoria, voz, mensajería, navegador y planificación.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: cron.
- Límites: Requiere configurar por tu cuenta los modelos y las integraciones necesarias.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 0 commits / 30 días, 49 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/moltis-org/moltis/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md#L28).

<a id="nearai--ironclaw"></a>

## [IronClaw](https://github.com/nearai/ironclaw)

Asistente personal en Rust que ejecuta tareas en segundo plano mediante routines y heartbeat.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación / eventos / heartbeat.
- Límites: El aislamiento de herramientas es un rasgo de diseño y no equivale a que este catálogo haya auditado su seguridad.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 0 commits / 30 días, 32 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/nearai/ironclaw/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md#L95).

<a id="afk-surf--comma"></a>

## [Comma](https://github.com/AFK-surf/Comma)

Combina estado de tareas continuo y trabajo entre dispositivos, y despierta al agente mediante bucles de supervisión.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: routines / event loops.
- Límites: El entorno de ejecución en la nube y la conexión a los dispositivos locales son componentes distintos.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 2 commits / 30 días, 10 commits / 90 días.
- Licencia: [AGPL-3.0](https://api.github.com/repos/AFK-surf/Comma/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/AFK-surf/Comma/blob/66ab3dc92475005aea9afd123df36a28e4ef86ab/README.md#L64).

<a id="sipeed--picoclaw"></a>

## [PicoClaw](https://github.com/sipeed/picoclaw)

Asistente personal en Go para dispositivos con recursos limitados, con herramientas de archivos, ejecución y planificación.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: programación.
- Límites: Un runtime de bajos recursos no implica que los modelos invocados ni el navegador sean igual de económicos.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/sipeed/picoclaw/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md#L632).

<a id="khoj-ai--khoj"></a>

## [Khoj](https://github.com/khoj-ai/khoj)

Asistente de conocimiento personal con investigación en documentos y web, y automatizaciones programadas.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: scheduled automations.
- Límites: Se centra en el trabajo con conocimiento e información; no es un controlador de escritorio de propósito general.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [AGPL-3.0](https://api.github.com/repos/khoj-ai/khoj/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md#L50) · [Fuente 2](https://docs.khoj.dev/features/automations) · [Fuente 3](https://docs.khoj.dev/features/automations).

<a id="mikeyobrien--rho"></a>

## [rho](https://github.com/mikeyobrien/rho)

Asistente personal operativo siempre activo basado en Pi, con memoria persistente y comprobaciones proactivas periódicas.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: heartbeat.
- Límites: Es una aplicación de nivel superior sobre Pi; la forma de ejecutarse difiere entre Android y escritorio.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/mikeyobrien/rho/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/mikeyobrien/rho/blob/073a3ee8a5dc0efd5dd32d773a760575ed38abc7/README.md#L34).

<a id="maikunari--mame"></a>

## [Mame](https://github.com/maikunari/mame)

Asistente ligero siempre activo con memoria persistente y canales de mensajería; puede orquestar agentes de programación.

- Categoría: Asistentes personales siempre activos y runtime ligeros; Mecanismo proactivo documentado.
- Modo de activación: cron / heartbeat.
- Límites: Sirve como referencia de implementación pequeña; la puntuación de mantenimiento del proyecto no representa madurez.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT declarada en el README](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md); No se encontró el texto completo de la licencia; candidato, no entra en la lista de recomendación de código abierto.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md#L300).

<a id="copilotkit--openbot"></a>

## [OpenBot](https://github.com/CopilotKit/OpenBot)

Plataforma autoalojada de colegas de IA que aporta a los agentes AG-UI navegador independiente, espacio de archivos, permisos de herramientas, registro de auditoría y tareas programadas.

- Categoría: Asistentes de espacio de trabajo y contexto; Mecanismo proactivo documentado.
- Modo de activación: routines programadas / inicio manual.
- Límites: OpenBot gestiona el entorno informático, las políticas, la auditoría y la planificación; la capacidad del agente la proporciona el endpoint AG-UI conectado, y las sesiones persistentes y la memoria dependen de CopilotKit Intelligence.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 1093 commits / 30 días, 1501 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/CopilotKit/OpenBot/license); Identificada por GitHub licenseInfo; las condiciones de despliegue y licencia de CopilotKit Intelligence se cuentan aparte.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L251) · [Fuente 2](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L52).

<a id="agent0ai--agent-zero"></a>

## [Agent Zero](https://github.com/agent0ai/agent-zero)

Agente que ejecuta herramientas, proyectos y tareas de supervisión periódica en un entorno informático propio.

- Categoría: Asistentes de espacio de trabajo y contexto; Mecanismo proactivo documentado.
- Modo de activación: scheduled operations.
- Límites: Su límite es el entorno de ejecución configurado; no controla todos los recursos del anfitrión de forma predeterminada.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 97 commits / 30 días, 438 commits / 90 días.
- Licencia: [MIT](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE); LICENSE de la raíz verificada manualmente.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md#L259).

<a id="anil-matcha--suparagent"></a>

## [Suparagent](https://github.com/Anil-matcha/suparagent)

Escritorio y espacio de trabajo autoalojado para administrar de forma centralizada colegas de IA con nombre, delegación en equipo, conversaciones, memoria, routines, tareas y aprobaciones.

- Categoría: Asistentes de espacio de trabajo y contexto; Mecanismo proactivo documentado.
- Modo de activación: scheduled / webhook / manual routines.
- Límites: El proyecto sigue en desarrollo temprano; el servicio autoalojado y las capacidades de ordenador y navegador son experimentales; la versión gestionada es un producto aparte; el usuario aporta modelos y cuentas, y algunas integraciones solo admiten Claude o Codex.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 462 commits / 30 días, 878 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/Anil-matcha/suparagent/license); Identificada por GitHub licenseInfo; el servicio gestionado, los motores de terceros, Composio y los proveedores de modelos siguen sus propios términos.
- Verificación de funciones: 2026-11-11; [Fuente 1](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L3) · [Fuente 2](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L71) · [Fuente 3](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L183).

<a id="openbmb--pilotdeck"></a>

## [PilotDeck](https://github.com/OpenBMB/PilotDeck)

Aísla archivos, memoria y habilidades por espacio de trabajo; descubre tareas en segundo plano y entrega archivos.

- Categoría: Asistentes de espacio de trabajo y contexto; Mecanismo proactivo documentado.
- Modo de activación: descubrimiento always-on de tareas.
- Límites: Los benchmarks del README son autoinformados por los autores; este repositorio no los incluye en clasificaciones de capacidad entre proyectos.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 453 commits / 30 días, 960 commits / 90 días.
- Licencia: [AGPL-3.0](https://api.github.com/repos/OpenBMB/PilotDeck/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/OpenBMB/PilotDeck/blob/2865f05b1722c7473ea8a9dda317a92fb8c92dd8/README.md#L97).

<a id="copilotkit--openfuse"></a>

## [OpenFuse](https://github.com/CopilotKit/openfuse)

Aplicación de código abierto que ofrece interfaz de agente personal, navegador y espacio de trabajo.

- Categoría: Asistentes de espacio de trabajo y contexto; Capacidad adyacente.
- Modo de activación: workers de tareas en segundo plano; activación autónoma pendiente de verificación.
- Límites: Un worker en segundo plano no equivale a iniciar por sí solo; parte de los conectores y acciones siguen en el roadmap.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 3 commits / 30 días, 147 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/CopilotKit/openfuse/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/CopilotKit/openfuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md#L43).

<a id="copilotkit--openduet"></a>

## [OpenDuet](https://github.com/CopilotKit/OpenDuet)

Plantilla de aplicación de código abierto para construir asistentes proactivos de trabajo.

- Categoría: Asistentes de espacio de trabajo y contexto; Mecanismo proactivo documentado.
- Modo de activación: routines / sugerencias en segundo plano.
- Límites: La plantilla requiere configurar dependencias y modelos; no es un servicio gestionado ya desplegado.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 22 commits / 30 días, 92 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/CopilotKit/OpenDuet/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/CopilotKit/OpenDuet/blob/f52288fff5ccdbd3de428d573d9f026fce5ff480/README.md#L5).

<a id="volcengine--minecontext"></a>

## [MineContext](https://github.com/volcengine/MineContext)

Asistente informativo proactivo que genera ideas, tareas pendientes y resúmenes diarios y semanales a partir del contexto de pantalla.

- Categoría: Asistentes de espacio de trabajo y contexto; Capacidad adyacente.
- Modo de activación: observación de contexto / envío proactivo.
- Límites: Las sugerencias proactivas están documentadas; de ahí no se sigue que pueda operar todas las aplicaciones de forma autónoma.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/volcengine/MineContext/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/README.md#L9).

<a id="fei-craft--ds-bot"></a>

## [DS Bot](https://github.com/Fei-Craft/DS-Bot)

Aplicación de escritorio y complementos que amplían DeepSeek Harness con memoria, chats grupales y colaboración entre bots.

- Categoría: Complementos proactivos y extensiones de planificación; Capacidad adyacente.
- Modo de activación: bots persistentes / chats grupales; despertar autónomo pendiente de verificación.
- Límites: La página principal no confirma un mecanismo propio de temporización; no se puede equiparar directamente una sesión prolongada con ejecución proactiva.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 4046 commits / 30 días, 5173 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/Fei-Craft/DS-Bot/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/Fei-Craft/DS-Bot/blob/71d344bf193f3f18185f25de3d8e5c483046910a/README.md#L41).

<a id="john-walks-slow--dsh-proactive"></a>

## [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive)

Añade a DeepSeek Harness despertares proactivos que pueden seguir disparándose después del enfriamiento de la sesión.

- Categoría: Complementos proactivos y extensiones de planificación; Mecanismo proactivo documentado.
- Modo de activación: once / interval / cron a nivel del anfitrión.
- Límites: Depende de la ejecución del anfitrión y de la compatibilidad de versiones; incluye configuración de no molestar y de presupuesto de notificaciones.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 0 commits / 30 días, 97 commits / 90 días.
- Licencia: [MIT](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/packages/dsh-proactive/LICENSE); LICENSE del subdirectorio del complemento verificada manualmente.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/README.md#L1).

<a id="t0dorakis--murmur"></a>

## [murmur](https://github.com/t0dorakis/murmur)

Demonio de planificación ligero que inicia periódicamente sesiones de CLIs como Claude, Codex o Pi.

- Categoría: Complementos proactivos y extensiones de planificación; Mecanismo proactivo documentado.
- Modo de activación: cron / interval.
- Límites: La entrega de mensajes y las operaciones de negocio las realizan las indicaciones proporcionadas y el agente invocado.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/t0dorakis/murmur/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/t0dorakis/murmur/blob/d666df4c749c28ecb775613ecec8b12954b387e7/README.md#L10).

<a id="hypostas--pulse"></a>

## [Pulse](https://github.com/Hypostas/pulse)

Demonio de extensión para OpenClaw que despierta según cambios, objetivos y urgencia.

- Categoría: Complementos proactivos y extensiones de planificación; Mecanismo proactivo documentado.
- Modo de activación: sensores / disparo por urgencia.
- Límites: Depende del webhook de OpenClaw; las afirmaciones de autonomía del autor no son conclusiones medidas por este repositorio.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/Hypostas/pulse/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/Hypostas/pulse/blob/4bebd1e23bff218dde1cd0b693f901493d45f972/README.md#L5).

<a id="nousresearch--hermes-bot-mode"></a>

## [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode)

Añade a Hermes de escritorio bots con nombre, conversaciones independientes y un panel de tareas periódicas.

- Categoría: Complementos proactivos y extensiones de planificación; Referencia histórica.
- Modo de activación: routines cron del anfitrión.
- Límites: Archivado en GitHub; se conserva como referencia de la interfaz de bots de Hermes y de su integración con cron, no como complemento activo recomendado.
- Estado de mantenimiento actual: Archivado / histórico; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/NousResearch/Hermes-Bot-Mode/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/NousResearch/Hermes-Bot-Mode/blob/80fee22582b871b9765a65e2992b8b5a8211c9f8/README.md#L23).

<a id="earendil-works--pi"></a>

## [Pi](https://github.com/earendil-works/pi)

Harness de agentes extensible con el que construir asistentes siempre activos mediante SDK, RPC y complementos.

- Categoría: Harness extensibles y base de ejecución persistente; Capacidad adyacente.
- Modo de activación: requiere planificación de nivel superior / extensiones.
- Límites: La antigua ruta badlogic/pi-mono ya redirige; puede combinarse con rho o murmur.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 1798 commits / 30 días, 2798 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/earendil-works/pi/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/earendil-works/pi/blob/fcebc099565d8f30c15b321ff6a1af5f34d89400/README.md#L15).

<a id="deepseek-ai--deepseek-harness"></a>

## [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

Base de ejecución de agentes con arquitectura de complementos, adecuada para conectar bots y complementos de despertar proactivo.

- Categoría: Harness extensibles y base de ejecución persistente; Capacidad adyacente.
- Modo de activación: el mecanismo proactivo lo debe aportar un complemento del anfitrión.
- Límites: developer preview; hay que verificar la compatibilidad de los complementos.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 3604 commits / 30 días, 14321 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/deepseek-ai/deepseek-harness/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/README.md#L7).

<a id="letta-ai--letta-code"></a>

## [Letta Code](https://github.com/letta-ai/letta-code)

Agente con memoria persistente que, mediante entornos remotos y channels, puede formar un asistente siempre activo.

- Categoría: Harness extensibles y base de ejecución persistente; Mecanismo proactivo documentado.
- Modo de activación: remote environments / cron.
- Límites: Destino oficial de migración de LettaBot; requiere combinar entornos remotos con configuración de planificación.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 346 commits / 30 días, 966 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/letta-ai/letta-code/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/letta-ai/letta-code/blob/e6d6cc27ef1111da80e919dc1cef179613894b66/README.md#L29) · [Fuente 2](https://docs.letta.com/letta-code/scheduling) · [Fuente 3](https://docs.letta.com/letta-code/scheduling).

<a id="browser-use--browser-use"></a>

## [Browser Use](https://github.com/browser-use/browser-use)

Aporta a los agentes comprensión de páginas web y ejecución en el navegador.

- Categoría: Componentes de control de ordenador y navegador; Capacidad adyacente.
- Modo de activación: tareas de navegador bajo demanda.
- Límites: Actúa principalmente en el navegador; no demuestra planificación proactiva ni control de todo el escritorio.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 661 commits / 30 días, 954 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/browser-use/browser-use/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md#L1).

<a id="cursortouch--windows-mcp"></a>

## [Windows-MCP](https://github.com/CursorTouch/Windows-MCP)

Servicio MCP que expone a los agentes capacidades de operar un Windows.

- Categoría: Componentes de control de ordenador y navegador; Capacidad adyacente.
- Modo de activación: invocado por el anfitrión.
- Límites: El componente de control no es en sí un asistente personal siempre activo; necesita modelos, memoria y disparadores externos.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 115 commits / 30 días, 184 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/CursorTouch/Windows-MCP/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/CursorTouch/Windows-MCP/blob/9ab92bca2772dfb53ae3ed4feb98dac22c5b3dea/README.md#L25).

<a id="alibaba--page-agent"></a>

## [Page Agent](https://github.com/alibaba/page-agent)

Agente JavaScript que controla la interfaz en lenguaje natural desde dentro de la página web.

- Categoría: Componentes de control de ordenador y navegador; Capacidad adyacente.
- Modo de activación: invocado por la página o el anfitrión.
- Límites: Es una capa de control dentro de la web; no dispone del ciclo de vida completo de un asistente siempre activo.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 22 commits / 30 días, 40 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/alibaba/page-agent/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/alibaba/page-agent/blob/9eb6b6646500264d9034dd466a4270cb9fc1ef1e/README.md#L35).

<a id="bytedance--ui-tars-desktop"></a>

## [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop)

Aplicación de agente y herramientas relacionadas para operar GUIs y navegadores.

- Categoría: Componentes de control de ordenador y navegador; Capacidad adyacente.
- Modo de activación: tareas de ordenador / navegador bajo demanda.
- Límites: Automatizar tareas de ordenador e iniciar trabajo sin indicación humana son dos dimensiones distintas.
- Estado de mantenimiento actual: Archivado / histórico; 0 commits / 30 días, 8 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/bytedance/UI-TARS-desktop/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md#L13).

<a id="xlang-ai--osworld"></a>

## [OSWorld](https://github.com/xlang-ai/OSWorld)

Evalúa la capacidad de ejecución de agentes multimodales en entornos informáticos reales.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación con tareas reales de ordenador.
- Límites: Mide la ejecución de tareas; por sí sola no mide la iniciativa espontánea ni el momento de interrumpir.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 69 commits / 30 días, 213 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/xlang-ai/OSWorld/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/xlang-ai/OSWorld/blob/8903ebeb0efdf74331bd7dc37ed91ccbbff22317/README.md#L294).

<a id="zju-real--knowu-bench"></a>

## [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)

Evalúa en agentes móviles la obtención de preferencias, la intervención proactiva y la solicitud de consentimiento.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación móvil interactiva y personalizada.
- Límites: Se centra en GUIs móviles y preferencias personales; no es un runtime para todas las plataformas.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 1 commits / 30 días, 1 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/ZJU-REAL/KnowU-Bench/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/ZJU-REAL/KnowU-Bench/blob/c03a825991ede13add6631f2ed19b90755930dc6/README.md#L4).

<a id="facebookresearch--memo-pro-agent"></a>

## [MemoProAgent](https://github.com/facebookresearch/Memo-Pro-Agent)

Investiga cómo buscar evidencia en la memoria personal de largo plazo para decidir si intervenir de forma proactiva.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación de intervención guiada por memoria.
- Límites: Nombre inicial del artículo: ProPerAgent; deduplicado por el mismo ID de arXiv.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 0 commits / 30 días, 6 commits / 90 días.
- Licencia: [CC-BY-NC-4.0](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/LICENSE); Licencia no comercial; listado solo como código de investigación.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/README.md#L3).

<a id="simplified-reasoning--pi-bench"></a>

## [π-Bench](https://github.com/Simplified-Reasoning/Pi-Bench)

Evalúa la identificación de necesidades ocultas y la asistencia proactiva en flujos de trabajo largos y de múltiples turnos.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación de proactividad.
- Límites: Es un benchmark; no guarda relación con el harness Pi.
- Estado de mantenimiento actual: Con commits en los últimos 90 días; 0 commits / 30 días, 1 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/Simplified-Reasoning/Pi-Bench/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/Simplified-Reasoning/Pi-Bench/blob/4f545be5d289b28ff022d2904d455007358ed3b7/README.md#L1).

<a id="thunlp--proactiveagent"></a>

## [ProactiveAgent](https://github.com/thunlp/ProactiveAgent)

Método de predicción proactiva de tareas, junto con sus datos y su código de evaluación.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: observación de eventos / anticipación de tareas.
- Límites: Es una implementación de investigación, no un asistente personal general listo para usar.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/thunlp/ProactiveAgent/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/thunlp/ProactiveAgent/blob/3fcf9beebe256b86871659fbb12541c41c9381b9/README.md#L2).

<a id="xzf-thu--pask"></a>

## [PASK](https://github.com/xzf-thu/Pask)

Investiga la asistencia proactiva que combina memoria a largo plazo, contexto continuo y restricciones de latencia.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: detección de necesidades latentes / mantenerse en silencio.
- Límites: Informe técnico y código de investigación; la madurez práctica debe verificarse aparte.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/xzf-thu/Pask/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/xzf-thu/Pask/blob/d54646c52b1555232ce4ab39103768d7f65b8267/README.md#L30).

<a id="deepakn97--pare"></a>

## [PARE](https://github.com/deepakn97/pare)

Evalúa asistentes proactivos simulando usuarios activos y entornos digitales con estado.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación de asistente proactivo / usuario simulado.
- Límites: Los usuarios simulados no equivalen al resultado del uso prolongado por usuarios reales.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/deepakn97/pare/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/deepakn97/pare/blob/261149914a9e9dcacb12de620575c691d50e3c2e/README.md#L3).

<a id="tdemin16--proactivebench"></a>

## [ProactiveBench (MLLM)](https://github.com/tdemin16/proactivebench)

Benchmark de investigación que evalúa cómo los modelos multimodales obtienen proactivamente información útil.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: evaluación de proactividad multimodal.
- Límites: Distinguirlo del benchmark homónimo utilizado por ProactiveAgent; la página oficial del artículo indica ECCV 2026.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [MIT](https://api.github.com/repos/tdemin16/proactivebench/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/tdemin16/proactivebench/blob/428885c9224418b544dfbdbde5307bccc58018d5/README.md#L2).

<a id="openaiotlab--contextagent"></a>

## [ContextAgent](https://github.com/openaiotlab/ContextAgent)

Investiga cómo usar información de percepción de mundo abierto para decidir el servicio proactivo y la invocación de herramientas.

- Categoría: Implementaciones de investigación y código de evaluación; Recurso de investigación.
- Modo de activación: percepción de contexto / predicción de servicio.
- Límites: Los datos de investigación y los escenarios de herramientas no se pueden generalizar directamente a cualquier escritorio.
- Estado de mantenimiento actual: Sin commits desde hace 91–365 días; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [Pendiente de verificación](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md); No se encontró LICENSE; solo como recurso de investigación, sin inferir autorización.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md#L3).

<a id="letta-ai--lettabot"></a>

## [LettaBot](https://github.com/letta-ai/lettabot)

Asistente personal que ofrecía canales de mensajería, memoria, heartbeat y tareas programadas.

- Categoría: Proyectos históricos y de migración; Referencia histórica.
- Modo de activación: heartbeat / cron.
- Límites: El README oficial anuncia que ya no se mantiene activamente y recomienda migrar a Letta Code.
- Estado de mantenimiento actual: Archivado / histórico; 0 commits / 30 días, 0 commits / 90 días.
- Licencia: [Apache-2.0](https://api.github.com/repos/letta-ai/lettabot/license); Identificada por GitHub licenseInfo; no se infiere la licencia de los datos adjuntos ni de los pesos de los modelos.
- Verificación de funciones: 2026-11-05; [Fuente 1](https://github.com/letta-ai/lettabot/blob/99c3b5dd73550fe0a4eac2ee31b1c3229ca9e550/README.md#L8).
