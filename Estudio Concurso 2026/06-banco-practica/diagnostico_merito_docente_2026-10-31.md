# Diagnóstico preliminar de Mérito Docente — 31 de octubre de 2026

## Alcance y seguridad
Análisis estático del archivo `mooc-docente.zip` facilitado por el propietario y de la rama pública de GitHub `ecapdevilla/mooc-docente`. **No se ejecutó el servidor, no se conectó ninguna base de datos, no se corrieron pruebas con efectos en datos, no se hizo `git pull`, merge, push, reset ni despliegue.** No se reproducen secretos.

## Resultados confirmados del ZIP

| Elemento | Resultado |
| --- | --- |
| Rama local | `main`, commit `90d5e8a` (5 oct. 2026) |
| Referencia `origin/main` incluida en el ZIP | `5e0c2e0` (9 oct. 2026) |
| Divergencia | 10 commits exclusivamente locales y 5 exclusivos en `origin/main` (respecto a la referencia guardada en el ZIP) |
| Estado de fusión | No hay rutas sin fusionar (`git ls-files -u` sin resultados) |
| Archivos marcados como modificados | 39, pero todos equivalen al commit local después de normalizar `CRLF`/`LF` |
| Archivos sin seguimiento | `docs/formulacion-proyecto.md`, `tmp_check.js` |
| Puntos de recuperación de agentes | Presentes en `.git`, incluidos hasta el 24 oct.; los más recientes agregan documentación/script auxiliar |
| Conexión de desarrollo (`.env`) | `DATABASE_URL` apunta a `localhost` (NO al proyecto Supabase compartido) |
| Vercel | `.vercel/project.json` indica `projectName: mooc-docente`; no se validaron las variables de producción |
| Verificación de sintaxis | `node --check` pasó para archivos JS principales inspeccionados |

La rama local conserva `api/index.js`, `vercel.json`, `src/routes/quizzes.js` y varios archivos de pruebas. La referencia `origin/main` del ZIP no tiene esos archivos. Por otra parte, `origin/main` incluye los commits del 9 de octubre que agregan el curso de **Inteligencia Artificial para Docentes**, con seis lecciones y cuestionarios, que no están en la rama local.

### Riesgos y aclaraciones
1. **No existe un conflicto de merge actualmente activo** en la copia archivada. Hay divergencia de historial que podría producir conflictos al intentar integrarlo.
2. Los 39 archivos marcados `M` son diferencias de final de línea; no deben tratarse como 39 cambios funcionales.
3. La desaparición de `vercel.json` y `api/index.js` en la referencia remota es relevante para el despliegue/API, pero todavía no se ha verificado cuál deployment está en producción.
4. Los tests existentes pueden **registrar y borrar usuarios en la base configurada**. No ejecutar `npm test` o `npm run seed` sin una base aislada y permiso expreso.
5. El ZIP incluye `.env` y `.git`; **no publicar ni reenviar esa copia íntegra** sin limpiar credenciales. Las claves no se muestran aquí.
6. El proyecto Supabase facilitado por el usuario es `uzxiyzkqtsxpdlagcwmj`, pero todavía no se ha contrastado con las variables privadas de Vercel.

## Ruta recomendada
1. Preservar la carpeta original y el ZIP sin modificar.
2. En VS Code, confirmar que la carpeta abierta es la misma de la copia y obtener una nueva lectura de Git en modo solo lectura.
3. Comparar el trabajo local, `origin/main` y los checkpoints de agentes. Registrar lista de funciones que aporta cada rama.
4. Preparar una rama de integración o segundo worktree **solo con autorización posterior**. Conservar funcionalidades locales de backend y pruebas e incorporar el módulo de IA remoto; resolver conflictos archivo por archivo.
5. Verificar sintaxis y ejecutar pruebas solamente en un entorno aislado, nunca en la BD actual.
6. Revisar el despliegue de Vercel y las variables de entorno sin divulgar valores secretos.
7. Publicar solamente después de validación funcional y copia de respaldo.

## Prompt para el asistente de VS Code

Actúa como ingeniero senior de Git, Node.js, Express, PostgreSQL y Vercel. Estás dentro de la carpeta de trabajo de **Mérito Docente**. Tu tarea es hacer una **auditoría de solo lectura** y preparar un plan de integración sin perder funcionalidad.

### Hechos detectados en un ZIP de este proyecto
- `main` local: `90d5e8a` (5-oct-2026).
- `origin/main` guardado en el ZIP: `5e0c2e0` (9-oct-2026).
- Divergencia detectada: 10 commits locales frente a 5 remotos.
- No había un merge activo.
- 39 archivos marcados como modificados eran únicamente diferencias CRLF/LF; dos archivos sin seguimiento: `docs/formulacion-proyecto.md` y `tmp_check.js`.
- La rama local posee `api/index.js`, `vercel.json`, rutas de quizzes y pruebas que faltan en la referencia remota.
- La rama remota posee el curso de IA para docentes con seis lecciones y cuestionarios que falta en la rama local.
- `.env` de esa copia apuntaba a PostgreSQL local. La base Supabase de producción NO está autorizada para ser consultada.

### Tareas permitidas
1. Verifica ruta de trabajo, rama, remotos y estado: `git rev-parse --show-toplevel`, `git status -sb`, `git remote -v`, `git branch -avv`, `git log --all --graph --oneline --decorate -30`, `git ls-files -u`.
2. Verifica `git rev-list --left-right --count main...origin/main` y el merge-base (sin actualizar refs).
3. Distingue diferencias CRLF/LF de cambios de contenido usando `git diff --ignore-space-at-eol`.
4. Compara módulos, rutas, UI, curso de IA y configuración Vercel entre ramas usando `git show`, `git diff` y lectura de archivos.
5. Examina los checkpoints `refs/agents/*` y `refs/cline/*` sin reescribir nada.
6. Identifica cuáles módulos son más completos en cada versión y qué conflictos reales podría producir una fusión futura.
7. Entrega (a) diagnóstico, (b) tabla de funcionalidades por versión, (c) plan seguro y ordenado de integración y (d) lista de riesgos y autorizaciones necesarias.

### Restricciones absolutas
- No ejecutes `git pull`, `git fetch`, `git merge`, `git rebase`, `git reset`, `git clean`, `git stash`, `git push` ni despliegues hasta que lo autorice.
- No instales dependencias ni cambies ningún archivo.
- No ejecutes `npm test`, `npm run seed`, migraciones SQL ni scripts auxiliares sin revisar sus efectos: los tests actuales pueden crear/borrar usuarios.
- No contactes Supabase ni Vercel con credenciales, ni leas/imprimas claves de `.env`, ni consultes información real de alumnos/docentes.
- No des por hecho que la última fecha significa la versión más completa.
- Antes de cualquier cambio, presenta el plan y espera mi autorización.
