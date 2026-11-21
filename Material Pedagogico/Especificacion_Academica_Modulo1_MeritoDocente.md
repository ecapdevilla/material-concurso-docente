# Mérito Docente — Especificación académica y técnica del módulo 1

**Fecha:** 2 de noviembre de 2026  
**Curso:** Fundamentos de Pedagogía y Didáctica  
**Módulo existente:** Fundamentos de Pedagogía  
**Estado editorial:** propuesta v1.0, **NO PUBLICADA**, sujeta a revisión disciplinar y de redacción.  
**Finalidad:** preparar a docentes aspirantes mediante comprensión conceptual y toma de decisiones ante casos de aula. Los ejercicios que se diseñen son **originales de Mérito Docente**; no son preguntas oficiales ni reproducen un examen de la CNSC.

## 1. Decisión de producto

- **Base de datos PostgreSQL/Supabase:** fuente de verdad del contenido publicado y versionado, de preguntas, opciones, matrículas, acceso y progreso.
- **Backend Express:** autentica y autoriza, expone el contenido publicado correspondiente al plan del estudiante, califica en servidor y mantiene historial. Nunca incluye `es_correcta`, explicaciones de claves ni material premium en la respuesta pública previa a contestar.
- **Repositorio:** originales editoriales en Markdown/JSON para control de versiones, comparación, revisión y restauración. El pipeline de publicación valida antes de insertar en PostgreSQL.
- **Supabase Storage u otro almacén de objetos:** archivos multimedia y PDF descargables; las rutas privadas deben ser firmadas o estar protegidas por el backend.
- **PDF:** material complementario y exportable, no fuente de verdad de una lección interactiva.
- **DeepSeek:** motor de ayuda opcional con contexto académico autorizado por el backend; no base de datos, no fuente autónoma de calificaciones, no reemplaza revisión editorial.

### Modelo de publicación recomendado

Conservar `courses`, `modules`, `lessons`, `quizzes` y `quiz_options` sin borrarlas. Introducir mediante migración aditiva versionado del contenido de lecciones (p. ej. `lesson_content_versions`: `lesson_id`, `version`, `estado` [borrador/revision/publicado/archivado], `titulo`, `objetivo`, `resultados`, `contenido_bloques JSONB`, `referencias JSONB`, `autor_editorial`, `revisado_por`, `fecha_revision`, `fecha_publicacion`, `creado_en`). Una versión publicada por lección como máximo; publicaciones mediante transacción y auditoría. Acceso por API: catálogo público de títulos y resumen, contenido completo con autorización servidor. Si se requiere una transición, el campo `lessons.contenido` actual se conserva de respaldo y compatibilidad, pero deja de ser la fuente editorial al activar las nuevas vistas.

Las preguntas de práctica y las pruebas sumativas se distinguen por modalidad; sus intentos se registran de forma separable y el resultado final se calcula solo sobre evaluaciones sumativas con reglas explícitas. Los cambios de contenido no sobrescriben intentos ni sus snapshots.

## 2. Competencia y resultados de aprendizaje

**Competencia del módulo:** Analizar situaciones de aula y justificar decisiones didácticas coherentes con los fines educativos, las características de los estudiantes, los aprendizajes previstos y la evidencia de desempeño, considerando la diversidad y el contexto colombiano.

Al concluir el módulo, el aspirante podrá:

1. Diferenciar educación, pedagogía, didáctica, currículo, enseñanza, aprendizaje y evaluación usando ejemplos de aula.
2. Reconocer cómo el conocimiento previo, la interacción, la práctica y la diversidad influyen en decisiones de enseñanza sin reducir las teorías a eslóganes.
3. Elegir y argumentar estrategias didácticas según objetivo, contexto, recursos y evidencia de aprendizaje.
4. Elaborar una microsecuencia de clase que alinee resultado esperado, actividad, evaluación formativa y retroalimentación.

**Producto integrador:** una microsecuencia de clase para un contexto colombiano (objetivo observable, actividad contextualizada, alternativa accesible de participación, evidencia, criterio y ajuste de enseñanza). **Evidencia mínima:** la microsecuencia y una explicación breve de por qué las decisiones son coherentes.

**Duración orientativa propuesta, no medida en la aplicación:** 4 lecciones de 30–45 min de trabajo con lectura y práctica, más 30–45 min para el caso integrador y la evaluación: alrededor de 3–4 horas. Ajustar por pilotaje real.

## 3. Estructura y conservación de registros

| Orden propuesto | Lección | Tipo de cambio | Foco |
|---|---|---|---|
| 1 | ¿Qué es la Pedagogía? | Ampliar lección existente, conservar ID | Diferenciación conceptual y decisiones educativas |
| 2 | Aprendizaje, saberes previos y diversidad | Crear nueva lección | Conocimientos previos, mediación, DUA, barreras |
| 3 | Estrategias didácticas para el aula | Ampliar lección existente, conservar ID, ajustar `orden` | Estrategia según objetivo, contexto, evidencia |
| 4 | Planeación didáctica y evaluación formativa | Crear nueva lección | Alineación objetivo–evidencia–actividad–retroalimentación |

**No mover ni borrar** `Corrientes pedagógicas contemporáneas`: actualmente pertenece al módulo 2, «Corrientes Pedagógicas». No renombrar títulos existentes hasta resolver el acoplamiento por título de `loadCourseMap`. El frontend nuevo debe usar IDs estables, no depender de la lista hardcodeada `MODULES` para descubrir nuevas lecciones.

## 4. Contenido académico propuesto

### Lección 1 — ¿Qué es la Pedagogía?

**Pregunta orientadora:** ¿Por qué una buena actividad no es suficiente si no sabemos qué aprendizaje queremos producir?

**Objetivo:** diferenciar seis conceptos educativos y justificar qué decisiones pertenecen al ámbito pedagógico o didáctico.

**Desarrollo conceptual.** En un establecimiento educativo se realizan numerosas acciones: diseñar el proyecto institucional, definir propósitos de formación, escoger recursos, acompañar estudiantes, evaluar y ajustar. Todas forman parte de un proceso educativo, pero no son decisiones equivalentes. La **educación** comprende procesos de formación personal, social y cultural; en Colombia la Ley 115 de 1994, artículo 1, presenta esta dimensión integral de la educación. La **pedagogía** estudia críticamente el sentido, la finalidad, los sujetos y las condiciones de estos procesos: invita a preguntarnos a quién educamos, para qué, bajo qué principios y con qué consecuencias. La **didáctica** se ocupa de organizar situaciones de enseñanza y aprendizaje: qué secuencia, representación, interacción, recurso y apoyo permiten avanzar hacia un resultado previsto.

La distinción no implica separar teoría de práctica. Una decisión didáctica —por ejemplo, usar una simulación de reciclaje en séptimo grado— expresa una concepción pedagógica acerca de cómo aprenden los estudiantes y qué tipo de participación se desea promover. Del mismo modo, una finalidad pedagógica como desarrollar pensamiento crítico necesita traducirse en tareas, preguntas y evidencias concretas.

El **currículo** organiza la intencionalidad formativa, los referentes, experiencias y criterios de evaluación que orientan una trayectoria de aprendizaje. La **enseñanza** comprende las acciones intencionales mediante las cuales el docente crea condiciones para aprender, pero la actividad del profesor no garantiza por sí sola aprendizaje. El **aprendizaje** se evidencia en cambios de comprensión y desempeño que pueden transferirse a situaciones nuevas. La **evaluación** obtiene e interpreta evidencias para tomar decisiones acerca del avance y de los apoyos necesarios; no se reduce a asignar notas.

**Ejemplo guiado.** Un profesor observa que sus estudiantes pueden repetir la definición de clasificación de residuos, pero mezclan materiales cuando se les presenta una situación real. Si decide añadir diez diapositivas sin revisar el problema, está ampliando la exposición, no necesariamente mejorando el aprendizaje. Si pregunta qué criterios están usando, presenta dos residuos ambiguos para discutirlos, explicita la clasificación y propone una nueva tarea con retroalimentación, usa información del aprendizaje para modificar la enseñanza. La finalidad de formar ciudadanos responsables constituye una orientación pedagógica; el orden de actividades, las preguntas y el apoyo visual son decisiones didácticas; la clasificación observada es evidencia evaluativa.

**Errores frecuentes.** (a) Definir pedagogía exclusivamente como un método; (b) usar didáctica como sinónimo de tecnología o entretenimiento; (c) confundir evaluación con calificación; (d) afirmar que toda participación activa produce aprendizaje significativo. La calidad se juzga por la relación entre propósitos, tareas, contexto y evidencias.

**Actividad aplicada:** en una matriz de tres columnas, clasificar cinco decisiones de una clase (finalidad formativa, secuencia, criterio de logro, recurso, retroalimentación) y justificar dónde coinciden o se relacionan pedagogía, didáctica y evaluación. La actividad se revisa con criterios, no solo con una respuesta literal.

**Cierre:** antes de escoger una herramienta o metodología, definir el aprendizaje esperado y cómo se comprobará.

### Lección 2 — Aprendizaje, saberes previos y diversidad

**Pregunta orientadora:** ¿Qué cambia cuando dos estudiantes llegan a la misma actividad con experiencias, conocimientos y apoyos diferentes?

**Objetivo:** anticipar barreras de aprendizaje, activar saberes previos y proponer apoyos flexibles sin disminuir expectativas.

**Desarrollo conceptual.** Aprender no es recibir información de manera idéntica. Los estudiantes interpretan contenidos desde experiencias, conocimientos, lenguajes e intereses previos. Los planteamientos de Ausubel sobre relaciones con conocimientos previos, las contribuciones socioculturales de Vygotsky sobre mediación y la investigación contemporánea sobre apoyos educativos invitan a indagar qué sabe cada estudiante antes de decidir la secuencia. Esto no implica atribuir a un autor todas las estrategias contemporáneas ni dividir al grupo en supuestos «estilos de aprendizaje» rígidos.

La activación de conocimientos previos debe ser breve y diagnóstica: una pregunta que exija explicar, ordenar ejemplos, comparar dos fenómenos o realizar una predicción puede revelar ideas útiles y errores. A partir de esa información, el docente modela lo necesario, ofrece andamiajes temporales y retira apoyos gradualmente. La interacción entre pares puede contribuir al aprendizaje si tiene una tarea clara, roles y oportunidad de justificar ideas; reunir estudiantes en grupos sin estructura no equivale automáticamente a aprendizaje colaborativo.

La diversidad debe considerarse desde el diseño de la experiencia, no únicamente mediante adaptaciones improvisadas al final. Las directrices DUA 3.0 (CAST, 2024) proponen ofrecer opciones de compromiso, representación y acción/expresión, preservando metas significativas. Una actividad sobre calidad del agua puede presentar información mediante texto accesible y datos visuales, permitir justificar una conclusión oralmente o por escrito cuando el objetivo es argumentar científicamente y usar organizadores para apoyar la comparación. No obstante, si el objetivo explícito fuera redactar un informe escrito, la escritura forma parte de la evidencia y no puede sustituirse sin examinar qué se quiere evaluar.

**Caso.** En sexto, el grupo debe justificar por qué ciertos materiales permiten conducir electricidad. Algunos recuerdan la distinción entre conductor y aislante; otros asocian cualquier objeto brillante con conductividad y una estudiante requiere apoyo para procesar instrucciones largas. Una secuencia robusta comienza con predicciones y explicaciones, hace una demostración segura, compara resultados, ofrece instrucciones fragmentadas y verifica la generalización a un material nuevo. El apoyo no consiste en entregar la respuesta final ni en bajar la exigencia de explicar causas.

**Actividad aplicada:** redactar una pregunta diagnóstica para un tema de su área, identificar dos respuestas probables (una adecuada y otra con error conceptual), proponer un apoyo de acceso y una pregunta de transferencia.

**Cierre:** diferenciar la meta de aprendizaje de los distintos caminos posibles para alcanzarla.

### Lección 3 — Estrategias didácticas para el aula

**Pregunta orientadora:** ¿La metodología más llamativa es siempre la que mejor enseña?

**Objetivo:** seleccionar y justificar una estrategia de enseñanza a partir de objetivos, condiciones y evidencias.

**Desarrollo conceptual.** Una estrategia didáctica es un conjunto articulado de decisiones, no el nombre de una herramienta. Su valor depende de qué aprendizaje demanda el objetivo, qué saben los estudiantes, cuánto tiempo existe, qué recursos hay, cómo se observará el desempeño y qué apoyos necesitan quienes enfrentan barreras.

La enseñanza explícita puede ser útil cuando se introduce una técnica o procedimiento nuevo que requiere modelado, ejemplos resueltos y práctica guiada. La indagación resulta pertinente cuando interesa que el estudiante formule preguntas contrastables, examine evidencias y argumente. El aprendizaje basado en proyectos organiza la elaboración de un producto o respuesta a un desafío auténtico a lo largo de una secuencia y exige planificación, seguimiento, criterios claros y revisión. La resolución de problemas puede ser un episodio breve o una metodología más amplia; no debe confundirse automáticamente con todo proyecto. El aprendizaje cooperativo necesita interdependencia positiva, participación y responsabilidad, no solo mesas agrupadas. Una discusión estructurada puede fortalecer argumentación si las intervenciones se apoyan en pruebas y existen reglas de escucha.

**Ejemplo comparado.** En octavo, un docente quiere que sus estudiantes evalúen la credibilidad de información ambiental difundida en redes sociales. Pedir que diseñen un afiche atractivo puede aumentar motivación, pero no demuestra que contrasten afirmaciones con fuentes. Es más coherente presentar dos publicaciones, acordar criterios de credibilidad, modelar la comprobación de una fuente, pedir que cada equipo justifique su decisión y cerrar con una nueva publicación individual. El afiche puede ser el producto final si obliga a sustentar la selección de evidencia; no debería sustituir la actividad intelectual esencial.

Una decisión profesional consiste también en combinar estrategias: modelado breve → práctica guiada → análisis colaborativo → evidencia individual → retroalimentación. No existe una estrategia universalmente superior para todos los resultados. El objetivo y la respuesta del alumnado orientan la elección.

**Actividad aplicada:** elegir entre tres estrategias para un mismo tema, justificar cuál evidencia mejor el resultado de aprendizaje y describir una dificultad de implementación con su mitigación.

**Cierre:** elegir una estrategia por el pensamiento que permite desarrollar, no por su popularidad.

### Lección 4 — Planeación didáctica y evaluación formativa

**Pregunta orientadora:** ¿Cómo sabemos, durante la clase, que los estudiantes están aprendiendo y qué hacemos si no ocurre?

**Objetivo:** diseñar una microsecuencia que articule resultado observable, actividades, evidencia, criterios y retroalimentación.

**Desarrollo conceptual.** Una planeación útil debe responder de modo coherente a cuatro preguntas: qué se espera aprender, qué evidencias mostrarán el aprendizaje, qué experiencias permitirán construirlo y cómo se adaptará la enseñanza a los resultados observados. Es insuficiente escribir «comprender el medioambiente» como objetivo y evaluar únicamente la memorización de tres definiciones. Un resultado más observable sería «comparar dos prácticas de manejo de residuos y justificar cuál reduce el impacto ambiental utilizando dos criterios explícitos».

La coherencia entre resultado, actividad y evaluación evita que una prueba mida algo diferente de lo enseñado. Para el objetivo propuesto pueden usarse una situación cercana, una comparación guiada, una tabla de criterios y una breve justificación individual. Una rúbrica analítica sencilla puede considerar exactitud del concepto, uso de evidencia y justificación de la decisión. No hace falta que toda clase termine con una nota: conviene recoger evidencias durante la práctica y actuar sobre ellas.

La evaluación formativa constituye un ciclo de indagación pedagógica. Primero se establecen metas y criterios; después se obtienen evidencias mediante preguntas, observaciones, respuestas escritas o productos; luego se interpretan los errores; finalmente se ofrece retroalimentación que ayude a mejorar y se abre una nueva oportunidad para aplicar esa retroalimentación. Según la guía de la Education Endowment Foundation (2021), el valor de la retroalimentación depende más de su calidad y uso que de si se comunica oralmente o por escrito.

**Caso guiado.** En una clase sobre convivencia digital, la mitad del curso identifica qué es una noticia falsa, pero justifica sus respuestas con frases como «me parece sospechosa». El docente no debe concluir simplemente que la actividad fue exitosa porque los estudiantes participaron. Puede detenerse, mostrar cómo contrastar autor, fecha, fuente y evidencia, pedir una segunda justificación sobre otra publicación y comparar el desempeño. La segunda evidencia permite saber si hubo avance.

**Ejemplo de microsecuencia (45 minutos).** Inicio (5): dos titulares contradictorios y predicciones justificadas. Modelado (10): análisis público de criterios para verificar una afirmación. Práctica guiada (12): grupos comparan fuentes y anotan evidencias. Aplicación individual (10): elegir qué publicación difundir y justificar con dos criterios. Cierre (8): tarjeta de salida y retroalimentación sobre un criterio que deba mejorarse. Ajuste para siguiente clase: si se confunde popularidad con confiabilidad, dedicar un ejemplo contrastivo y una nueva transferencia.

**Actividad aplicada:** completar una ficha con objetivo observable, evidencia, criterio, estrategia, apoyo inclusivo, momento de retroalimentación y decisión de ajuste frente a un error frecuente.

**Cierre:** la planeación no termina al escribir actividades; debe permitir decidir qué hacer con lo que realmente aprendieron los estudiantes.

## 5. Actividades y evaluación del módulo

### Práctica formativa por lección

- **Mínimo 4 ítems originales por lección**, de respuesta múltiple con única respuesta, todos basados en situaciones de aula y distractores plausibles. Para la primera publicación, crear **16 ítems formativos** revisables.
- Después de responder, proporcionar explicación para la respuesta elegida, razonamiento pedagógico, error conceptual de cada distractor y referencia vinculada cuando corresponda.
- Permitir reintentos sin confundirlos con nota certificable; registrar el historial de práctica.
- En las actividades de reflexión no calificar con exactitud binaria una argumentación abierta. Usar criterios o rúbrica; para autoevaluación, ofrecer una respuesta modelo orientativa.

### Evaluación final del módulo

- **12 preguntas nuevas**, diferentes de las 16 de práctica, con casos extensos y 4 alternativas homogéneas.
- Tabla de especificaciones: 3 sobre conceptos y distinciones, 3 sobre aprendizaje/diversidad, 3 sobre selección de estrategias, 3 sobre planeación/evaluación.
- Claves distribuidas entre A/B/C/D, pero también aleatorización de orden por intento en servidor y persistencia de la presentación concreta del ítem.
- **Regla de producto propuesta**: máximo 2 intentos sumativos por módulo y puntuación de aprobación de **≥80 %** (10/12), con remediación después de un intento no aprobado. Debe ser configurable, no una regla legal ni oficial de la CNSC.
- Conservar el resultado del primer intento, del último y del mejor, diferenciando práctica, dominio y aprobación. La nota de la evaluación se asigna a su propio intento; no modificar en secreto resultados históricos por reintentos de práctica.
- Evitar revelar las claves del mismo examen durante un intento vigente; ofrecer análisis por competencias y feedback después del cierre, sin garantizar que se podrá repetir exactamente el mismo banco.
- **Evaluación de transferencia**: caso integrador y microsecuencia con rúbrica de 4 criterios (coherencia objetivo-evidencia, justificación de estrategia, atención a diversidad, uso de retroalimentación). Se recomienda retroalimentación automatizada orientativa y revisión humana en etapas posteriores; no calificar automáticamente mediante IA como si fuese una nota de alto impacto.

### Rúbrica orientativa para el caso integrador (cada criterio 0–3)

| Criterio | 0 — Ausente | 1 — Inicial | 2 — Adecuado | 3 — Sólido |
|---|---|---|---|---|
| Objetivo y evidencia | No se corresponden | Relación superficial | Evidencia pertinente | Evidencia permite observar transferencia |
| Decisión didáctica | No justificada | Método por moda | Justificación coherente | Justifica alternativas y condiciones |
| Inclusión | Omite barreras | Apoyo genérico | Identifica barrera y apoyo | Anticipa acceso sin rebajar objetivos |
| Retroalimentación | Solo nota | Comentario general | Acción específica de mejora | Prevé reuso de feedback y nueva evidencia |

**Criterio de preparación editorial:** todas las lecciones incluyen objetivo, activación, explicación, caso, actividad, síntesis, fuentes, referencia al siguiente tema; todas las preguntas tienen opciones plausibles y retroalimentación validada; registros versionados y publicación auditada. El **módulo sigue en borrador** hasta aprobación explícita.

## 6. Prototipos de ítems para calibrar rigor (NO importar automáticamente)

### Ítem M1-P1
Una docente de séptimo observa que, aunque sus estudiantes memorizan el concepto de reciclaje, no clasifican correctamente residuos en una práctica escolar. Quiere decidir qué ajustar en la siguiente sesión. ¿Cuál acción produce evidencia más útil para orientar su enseñanza?

A. Repetir la definición y pedir que la copien nuevamente para reforzar la memoria.
B. Aplicar una encuesta de satisfacción sobre lo entretenida que resultó la clase.
C. Pedir que justifiquen clasificaciones de residuos ambiguos, analizar errores y ajustar ejemplos.
D. Aumentar la cantidad de diapositivas del tema y evaluar asistencia al final.

**Clave editorial:** C. **Justificación:** conecta evidencia de desempeño con una decisión didáctica. A y D no identifican el error; B mide percepción, no comprensión.

### Ítem M1-P2
En quinto grado, varios estudiantes conocen las fracciones por repartir alimentos, pero confunden denominadores diferentes al comparar cantidades. ¿Qué inicio de clase es más coherente con una enseñanza sensible a conocimientos previos?

A. Presentar dos repartos con representaciones distintas, escuchar argumentos y contrastar los criterios usados.
B. Dar directamente la regla de multiplicar en cruz y prohibir explicaciones diferentes.
C. Calificar a cada estudiante antes de mostrar ejemplos para separar al grupo por rendimiento.
D. Reemplazar el concepto por un juego de velocidad centrado en respuestas memorizadas.

**Clave editorial:** A. **Justificación:** hace visibles concepciones iniciales y las conecta con una comparación; las otras opciones no recuperan los modelos previos de los estudiantes.

### Ítem M1-P3
Un docente desea fortalecer la evaluación de fuentes en un proyecto escolar. El producto final será un video, pero descubre que los estudiantes están copiando afirmaciones sin comprobarlas. ¿Qué ajuste favorece mejor el objetivo?

A. Ampliar la duración del video para que tenga más contenido, sin cambiar los criterios.
B. Priorizar la calidad estética del producto, porque la motivación asegura comprensión.
C. Reducir los criterios de evaluación a puntualidad y entrega del archivo.
D. Introducir una matriz de verificación de fuentes, modelar un caso y exigir evidencia en cada afirmación.

**Clave editorial:** D. **Justificación:** el ajuste produce evidencia del juicio crítico; los distractores sustituyen el objetivo por longitud, estética o cumplimiento.

### Ítem M1-P4
Una profesora usa una tarjeta de salida y encuentra que la mayoría confunde causa y correlación. En la clase siguiente, ¿qué acción demuestra uso de evaluación formativa?

A. Registrar el resultado únicamente como nota y avanzar sin detenerse.
B. Revisar dos ejemplos contrastivos, pedir una explicación nueva y comprobar si se corrigió el error.
C. Enviar un mensaje genérico de felicitación a todo el curso por participar.
D. Sustituir la meta de argumentación por recordar una definición del libro.

**Clave editorial:** B. **Justificación:** interpreta una evidencia y crea una nueva oportunidad de aprendizaje; las otras alternativas no cierran el ciclo de retroalimentación.

## 7. Fuentes verificadas para la versión editorial

1. Ministerio de Educación Nacional. (2022). *Estándares Básicos de Competencias*. https://www.mineducacion.gov.co/1780/w3-article-340021.html?_noredirect=1
2. Ministerio de Educación Nacional. (2026, julio). *Nuevos lineamientos curriculares para la formación integral, ciudadana y socioemocional*. https://www.mineducacion.gov.co/1780/w3-article-339975.html?_noredirect=1
3. Congreso de Colombia. (1994). *Ley 115 de 1994, artículo 1*. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=292
4. CAST. (2024). *Directrices del Diseño Universal para el Aprendizaje, versión 3.0*. https://udlguidelines.cast.org/es/
5. Education Endowment Foundation. (2021). *Teacher Feedback to Improve Pupil Learning*. https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback
6. Comisión Nacional del Servicio Civil. (2026, octubre). *Anexo técnico: procesos de selección Docentes y Directivos Docentes 2026*. https://www.cnsc.gov.co/node/69894

**Autores clásicos a contextualizar con bibliografía completa antes de publicación:** David Ausubel, Lev Vygotsky, John Dewey y Paulo Freire. Evitar citas textuales no verificadas. No afirmar que las preguntas del módulo son oficiales ni que una competencia está incluida en la prueba CNSC sin comprobar las reglas y ejes de la convocatoria vigente.

## 8. Condiciones de aceptación de implementación

1. El material proviene de una versión publicada de PostgreSQL y se visualiza correctamente en el sistema .lx-, no se incrusta en una constante del HTML.
2. Se conservan IDs de las lecciones existentes y el módulo 2 no se modifica.
3. Autenticación y autorización real para el contenido premium; endpoints públicos entregan únicamente resumen.
4. Prevención de XSS: renderizado de bloques con elementos permitidos o saneamiento robusto; no convertir JSON arbitrario en `innerHTML` sin validación.
5. Preguntas de práctica y evaluación final con reglas y persistencia diferenciadas; ninguna clave antes de responder.
6. Pruebas de duplicados, autorización, versiones, estados editoriales y progreso con bases aisladas.
7. Migración aditiva reversible de código sin eliminar registros ni progreso; transacción al publicar.
8. Importador validado y vista previa editorial; una ejecución que falla no deja cursos parcialmente publicados.
9. `npm test` y validación visual con datos reales de staging; la ausencia de acceso a staging se documenta sin inventar resultados.
10. **No ejecutar SQL de escritura sobre Supabase Production ni desplegar sin autorización.**
