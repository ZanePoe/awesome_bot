# Guía de contribución

Se agradecen proyectos y artículos nuevos y correcciones de evidencia. Tener pocas estrellas no es motivo de rechazo.

1. Añade la entrada en `data/projects.json` o `data/papers.json`; no edites directamente las tablas generadas del README.
2. Aporta la dirección canónica de GitHub o la página original del artículo, al menos una fuente que demuestre el mecanismo descrito, y la fecha de verificación.
3. Indica si es un asistente completo, una extensión, un harness, un componente de control o código de investigación; el modo de activación debe ser concreto. Las capacidades sin confirmar se marcan "pendiente de verificación", y un roadmap no puede presentarse como función ya implementada.
4. Revisa la licencia. Si falta el texto completo de la licencia puede entrar como candidato/ítem de investigación; el código con restricciones no comerciales no puede etiquetarse como licencia abierta verificada.
5. Los cambios de nombre siguen el canonical repo de GitHub; los artículos se deduplican por ID de arXiv, y el nombre anterior puede quedar en las notas.
6. Ejecuta los comandos siguientes y entrega los resultados generados. Al añadir repositorios hay que volver a obtener la instantánea completa de métricas.

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests
python scripts/build.py --check
```

Al actualizar la descripción de funciones, fija la evidencia al SHA del commit; la actualización automática de estrellas no debe reetiquetar como recién verificados juicios de funciones antiguos. El método de clasificación está en `docs/taxonomy.md` y el de ordenación en `docs/methodology.md`.

Está prohibido enviar a este repositorio direcciones de servicios privados de búsqueda, tokens, el cuerpo de artículos internos, enlaces de descarga firmados o datos personales.

## Archivos multilingües

- `data/projects.json` son los datos canónicos de revisión en chino: los hechos solo se cambian una vez, aquí.
- Los textos de los demás idiomas proceden de `locales/<lang>/entries.json` (`description`, `trigger`, `boundary`, `license_label`, `license_note`) y `locales/<lang>/ui.json`; los de los artículos proceden de `locales/<lang>/papers.json` (`title`, `summary`, `boundary`, `publication_note`); `zh` cae directamente en `data/projects.json`, por lo que no existe `locales/zh/entries.json`.
- Al añadir un proyecto o reescribir su propósito, límites o conclusión de licencia, completa en el mismo PR los cuatro locales en/es/hi/fr; si no, fallarán `python scripts/build.py --check` y `python -m unittest discover -s tests -v`.
- Documentación estática: el inglés está en `docs/` y `CONTRIBUTING.md` de la raíz; los demás idiomas, en la misma ruta relativa bajo `locales/<lang>/`. Los enlaces relativos de un espejo se resuelven desde el directorio de cada archivo: desde `locales/<lang>/docs/` los que apuntan a `data/`, `scripts/`, `research/`, `LICENSE` o `record/` de la raíz se escriben `../../../`, y desde `locales/<lang>/CONTRIBUTING.md`, `../../`; `docs/readme-intro.md` es la excepción: se inserta en el README y sus enlaces se resuelven desde la raíz del idioma.
- `record/` y `research/` conservan el texto original con el que se escribieron, como rastro de auditoría, y no se traducen automáticamente.
- Los artefactos generados (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` y sus copias homónimas en los espejos de cada idioma) no se editan a mano: los produce `python scripts/build.py`.
