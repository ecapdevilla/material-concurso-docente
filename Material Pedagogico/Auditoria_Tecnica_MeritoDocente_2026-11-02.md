# Auditoría independiente del código — Mérito Docente

**Fecha:** 2 de noviembre de 2026  
**Fuente inspeccionada:** `MeritoDocente_Revision_Completa.zip` (102 entradas, ~1,35 MB descomprimidos).  
**Alcance:** revisión estática del frontend, backend, migraciones, carga de catálogo, pruebas y contenido académico.  
**No realizado:** acceso a Supabase Production, consulta de datos personales, ejecución de SQL contra ningún servidor, pagos, prueba de carga, prueba visual con autenticación real o despliegue.

## Veredicto

**Base funcional prometedora para un piloto controlado, pero NO lista aún para comercialización como tres cursos completos y evaluaciones acreditables.** Hay separación entre práctica, lectura finalizada y evaluación certificable que debe definirse en el backend. El paquete SQL de catálogo está preparado, pero antes de instalarlo deben existir un respaldo restaurable y una decisión editorial sobre publicar contenido introductorio.

## Hallazgos por prioridad

### P0 — Resolver antes de cobrar o certificar

1. **Acceso público al contenido que se quiera vender como premium.** `src/routes/courses.js:49-95` atiende `GET /api/v1/courses/:id` sin autenticación ni autorización, y devuelve `lessons.contenido` y las preguntas. Esto es coherente con un curso gratuito, **pero incompatible con comercializar el mismo material bajo control de suscripción sin añadir autorización en servidor**. Se necesita separar resumen público y lecciones privadas, con verificación real de matrícula y derecho de acceso. No basta ocultar botones en HTML.

2. **Las evaluaciones todavía no prueban dominio para certificación.** `src/routes/quizzes.js:302-342` devuelve `correctOptionId` incluso cuando se respondió mal, y `src/services/lessonQuiz.js:26-65` considera dominada una pregunta si alguna vez se acertó. El frontend permite reintentar inmediatamente (`indexInicial.html:6417-6467`). Adicionalmente, `POST /progress/lesson/:id` permite completar la lección sin dominar el quiz salvo que `LESSON_COMPLETION_REQUIRES_QUIZ=true` (`src/routes/progress.js:26-54`). Esto es adecuado **para práctica formativa guiada**, no como evaluación de suficiencia. Separar actividades formativas con solución y evaluaciones certificables con primer intento, límite de reintentos, porcentaje, versión y auditoría.

3. **Contenido académico insuficiente para tres cursos completos.** `npm run contenido:catalogo` examinó 11 lecciones: 3 en Pedagogía, 2 en Legislación, 6 en IA. Las primeras cinco contienen entre 75 y 95 palabras cada una; las de IA entre 123 y 144 palabras. El criterio automatizado 'completo' de seis lecciones es solo un umbral técnico editorial, **no validación pedagógica, bibliográfica ni normativa**. Todos los 11 cuestionarios tienen una sola pregunta de cuatro opciones con clave B. Datos reproducidos por `scripts/auditar-contenido-catalogo.js` y `docs/catalogo-contenido-auditoria.md`. No anunciar cursos desarrollados integralmente sin ampliar y revisar contenido.

### P1 — Resolver antes de instalación definitiva / piloto de usuarios

4. **Cuestionarios archivados o en borrador aparecen en el detalle y son respondibles.** `src/routes/courses.js:76-87` selecciona `quizzes` sin exigir `estado_revision = 'publicado'`. `src/routes/quizzes.js:225-248` tampoco aplica ese filtro al aceptar respuestas. `src/services/lessonQuiz.js:26-50` cuenta todas las preguntas de la lección, independientemente del estado. Corregir el contrato público, la elegibilidad de respuesta y el cálculo de dominio con el mismo criterio de publicación. Añadir pruebas para preguntas en `borrador`, `revision` y `archivado`.

5. **Progreso y matrículas potencialmente desincronizados.** En `src/routes/quizzes.js:297-323`, cuando se domina una lección, el servidor hace `INSERT/UPDATE user_progress`, pero no recalcula `enrollments.progreso_total` ni concede badges. El endpoint `src/routes/progress.js:135-252` sí lo hace, por otro camino. Una invocación directa al endpoint del cuestionario puede dejar porcentajes y recompensas inconsistentes hasta otra llamada. Crear un servicio transaccional compartido para actualizar avance, matrícula e insignias, y hacerlo idempotente.

6. **Finalización de lección no transaccional.** `src/routes/progress.js:67-252` ejecuta consultas `pool.query` separadas: matrícula, progreso, porcentaje y badges. Un error intermedio o concurrencia puede dejar cambios parciales. Usar un único cliente y transacción de PostgreSQL, y controlar colisiones en creación de badges.

7. **La carga publicaría automáticamente cuestionarios sin validación editorial.** `database/loads/20261101_carga_catalogo_tres_cursos.sql` inserta/rehabilita preguntas con `estado_revision='publicado'`; el frontend y el generador replican el material existente. Su ejecución sería técnicamente reversible por desactivación, pero dejaría disponibles preguntas que requieren revisión. Decidir entre catálogo de demostración, publicación parcial o contenidos finales antes de aplicar el lote.

8. **Respaldo JSON no equivale a respaldo completo restaurable.** `database/loads/20261101_carga_catalogo_tres_cursos_respaldo.sql:13-21` exporta únicamente entidades de los tres cursos por título, no las tablas de usuarios ni historial del piloto. Antes de escribir en Production: respaldo completo apropiado del proyecto y prueba de restauración en staging; retener acta de ejecución y comprobaciones antes/después.

9. **Reversión física destructiva, aunque protegida.** `database/loads/20261101_carga_catalogo_tres_cursos_reversion_fisica.sql` puede eliminar dependencias debido a claves `ON DELETE CASCADE` si la protección no cubre algún futuro vínculo. Usar solo la reversión **segura** por desactivación en Production (`..._reversion.sql`), conservando historiales. Revisar el plan cuando el esquema crezca.

10. **Login de usuarios inactivos.** `src/routes/auth.js:69-93` autentica contraseña y emite token sin comprobar `users.activo`. `src/middleware/auth.js:12-19` sí rechaza tokens de usuarios inactivos en rutas protegidas. Conviene bloquear en login con respuesta genérica, añadir prueba y verificar que el frontend informe el error consistentemente.

### P2 — Ingeniería para crecimiento

11. **Patrón N+1 de consultas por curso.** `src/routes/courses.js:61-90` consulta módulos y luego lecciones y quizzes en bucles; el costo crece con el catálogo. Agregar consultas por lotes/JSON, paginación o caché controlado.

12. **Rate limiting por proceso, no global.** `src/server.js:64-71` usa el almacenamiento en memoria predeterminado de `express-rate-limit`: no sincroniza límites entre instancias serverless. Para protección comercial y consumo de IA: cuota por usuario/organización más almacén compartido, techo de gasto y observabilidad.

13. **CORS demasiado abierto como configuración predeterminada.** `src/server.js:34-38` combina `origin='*'` con `credentials: true`. Si se necesita comunicación entre dominios con credenciales, hay que declarar una lista explícita de orígenes autorizados. No es el principal bloqueo actual mientras se use la misma web y token Bearer.

14. **Contenido todavía acoplado al HTML monolítico.** `scripts/generar-carga-catalogo.js:5-9` extrae `MODULES` de `indexInicial.html` y genera SQL desde ese arreglo. Es útil para migrar el prototipo, pero no será sostenible como flujo editorial de cientos de lecciones: conviene que PostgreSQL sea la fuente de verdad del contenido publicado y usar un editor con versionado, aprobación y bibliografía.

15. **Comercialización aún no implementada.** En el ZIP no hay evidencia de checkout, webhooks de pago, derechos de acceso de pago, facturación, tabla de planes o tutor DeepSeek integrado en el backend. Son trabajos futuros; no deben contarse como funciones existentes.

## Comprobaciones realizadas aquí

- Se verificó la integridad de extracción del ZIP y el árbol de código.
- Se ejecutó `npm run carga:catalogo -- --resumen`: reportó **3 cursos, 9 módulos, 11 lecciones, 11 cuestionarios, 44 opciones**, sin escribir en bases de datos.
- Se ejecutó `npm run contenido:catalogo`: **11 lecciones inspeccionadas; cinco marcadas para revisión; claves de las 11 preguntas en B**.
- `node --check` completó correctamente en `src/server.js`, `src/routes/quizzes.js`, `src/routes/progress.js`, `scripts/generar-carga-catalogo.js` y `scripts/auditar-contenido-catalogo.js`.
- **No** se consiguieron ejecutar las 136 pruebas Jest: la instalación de dependencias del ZIP se detuvo por tiempo de espera en este entorno. Los 136 casos aprobados siguen siendo **evidencia reportada por DeepSeek**, no una reproducción independiente en esta sesión.
- **No** se instalaron la migración ni el catálogo en Production.

## Plan de avance con el mínimo retrabajo

**Lote 1 — Antes de cargar el catálogo:** comprobar respaldo real y restauración; corregir filtro `estado_revision` de `quizzes` en consulta, envío y dominio; definir si los cursos se publican solo como demostración. Auditar columnas existentes de Production con SQL de solo lectura antes de cualquier migración.

**Lote 2 — Consistencia:** unificar actualización de matrícula/progreso/badges en transacción; impedir finalización acreditable sin regla de evaluación; probar usuarios activos/inactivos; validar el nuevo endpoint contra PostgreSQL aislado.

**Lote 3 — Contenido vendible:** desarrollar y validar académicamente al menos un curso integral, con objetivos, casos, bibliografía, secuencia didáctica y banco amplio de preguntas tipo situacional. Variar claves, revisar distractores y diseñar rúbricas reales. Solo entonces ofrecerlo como curso de pago.

**Lote 4 — Comercial:** derechos de acceso en backend, checkout/webhooks verificados, reconciliación de pagos, métricas y soporte; políticas de privacidad y protección de datos; luego tutor IA con presupuesto y cuotas.

## Decisión para el usuario

**No ejecutar todavía `20261101_carga_catalogo_tres_cursos.sql` como publicación comercial definitiva.** Si se desea visualizar la ruta pronto, primero acordar expresamente un **catálogo piloto/no comercial**, garantizar respaldo y corregir el filtro editorial. No habilitar una reversión física en un entorno con usuarios.

Esta auditoría distingue hallazgos verificados en el código del ZIP de los estados reales de Supabase/Vercel, que aquí no fueron consultados.
