# Método de ordenación

## Origen de las métricas

`scripts/refresh_metrics.py` usa la API GraphQL de GitHub a través de un `gh` autenticado o de `GH_TOKEN` para leer repositorios públicos. Cada recolección fija un instante UTC y lee todos los proyectos por lotes; solo si todos tienen éxito se reemplaza de forma atómica `data/metrics.json`. Un fallo parcial no escribe ceros donde hay valores desconocidos ni sobrescribe la instantánea completa anterior. La única excepción es un repositorio que GitHub ya no resuelve (renombrado o borrado): su registro anterior se conserva y se marca con `missing_upstream` y una marca de tiempo `missing_since`, de modo que un proyecto desaparecido no rompe la actualización diaria. Los límites de tasa, los fallos de transporte y las respuestas parciales de GraphQL siguen interrumpiendo la ejecución y manteniendo intacta la instantánea previa.

- `stars`: el `stargazerCount` en el momento de la recolección.
- `commits_30d / commits_90d`: el `history.totalCount` del historial alcanzable de la rama por defecto dentro de la ventana UTC correspondiente, incluidos commits de merge y de bots. No se usa el recuento de la primera página como si fuera el total.
- `last_commit_at`: el `committedDate` del HEAD de la rama por defecto, usado para la frescura; se guarda también el SHA.
- `pushed_at`: se guarda aparte el último push, que puede proceder de otras ramas; no se usa como si fuera la actualización de código de la rama por defecto.
- `updated_at`: se guarda aparte la actualización de metadatos del repositorio; no interviene en la puntuación de frescura.
- `latest_release`: se guarda el nodo de release más reciente por fecha de creación y si es prerelease; la ausencia se registra como null y no se interpreta como abandono.
- `archived / disabled`: el estado del repositorio devuelto por la API.
- `license_review`: el juicio de licencia hecho durante la verificación manual de funciones, separado del `license_spdx` de la actualización automática. Las licencias cambian con los proyectos; actualizar metadatos no vuelve a auditar el texto de la licencia.

La recolección de la primera versión se hizo el 2026-11-05 en hora de Pekín; las fechas legibles por máquina usan UTC, de modo que ver 2026-11-04 no es un error de fecha.

## Primero el estado de mantenimiento, luego la puntuación

Dentro de cada categoría se separan cuatro capas:

1. Con commits en la rama por defecto en los últimos 90 días.
2. Entre 91 y 365 días desde el último commit de la rama por defecto.
3. Más de 365 días sin commits nuevos en la rama por defecto.
4. Proyectos archivados, disabled o declarados referencia histórica.

Ordenación combinada dentro de cada capa:

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
Puntuacion_de_mantenimiento = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Las estrellas pesan un 40%, la actividad de desarrollo a 90 días un 35% y la frescura del último commit un 25%. Los logaritmos y los topes fijos reducen la ventaja aplastante de los repositorios enormes; los anclajes fijos hacen que añadir entradas no cambie la puntuación de las demás. Una puntuación más alta significa solo más atención y señales de mantenimiento bajo estos criterios.

En caso de empate se comparan primero las estrellas y luego se ordena de forma estable por nombre de repositorio. La puntuación no descuenta nada por el archivado; es la capa de mantenimiento la que coloca los proyectos archivados al final. Así los números crudos quedan visibles y la regla es recalculable.

[Vistas de ordenación](rankings.md) ofrece además tres vistas de métrica única por estrellas, commits de 90 días y último commit; todas conservan la estratificación por estado de mantenimiento. Si necesitas los valores crudos sin capas, ordena tú mismo el [JSON](../../../data/metrics.json) o el [CSV](../../../data/rankings.csv).

## Qué no se puede inferir de esto

Las estrellas miden atención y los commits son un sustituto de la actividad; los commits automáticos, los commits de documentación, las estrategias de merge y los monorepos inflan los recuentos. El silencio en la rama por defecto no implica necesariamente que el software no sea utilizable. Los proyectos pequeños y estables pueden quedar subestimados por esta fórmula, y el código de investigación normalmente no necesita actualizaciones diarias.

Esta lista no ha ejecutado todos los agentes y no ofrece puntuaciones de tasa de éxito, coste, velocidad, seguridad ni "el más inteligente". Artículos distintos usan modelos, tareas y presupuestos diferentes, y sus mejores cifras no pueden combinarse en una tabla comparativa de capacidades.

## Diseño previsto para evaluaciones uniformes futuras

Elegir el mismo modelo, presupuesto, cuentas de prueba y directorios de trabajo aislados, fijar las versiones y cubrir al menos los siguientes escenarios reportando el tamaño de muestra:

| Escenario | Métricas observadas |
| --- | --- |
| Obtener información a una hora fijada y generar un archivo | tasa de disparo real, retardo, tasa de entrega exitosa |
| Dos grupos de eventos: entorno sin cambios / con cambios | tasa de intervención correcta, falsos positivos, falsos negativos, notificaciones inútiles |
| Preferencias nuevas del usuario efectivas entre sesiones | precisión de la memoria, uso de memorias obsoletas |
| Tareas entre navegador y archivos | tasa de éxito, veces que hace falta intervención humana |
| Reinicio, errores de red y reanudación tras pausa | tareas perdidas, ejecuciones duplicadas y tiempo de recuperación |
| Acciones que exigen pedir consentimiento expresamente | proporción de esperas correctas, acciones fuera de autorización |

Estos son planes de prueba, no resultados ya obtenidos.
