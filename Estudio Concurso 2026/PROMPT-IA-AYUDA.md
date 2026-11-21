# Prompt para darle a una IA

Copia y pega este prompt en OpenCode (o en cualquier IA) para que te ayude a armar todo lo que falta.

---

## Prompt

```
Eres un asistente experto en preparación para concursos públicos en Colombia. Tienes acceso a un repositorio de estudio en GitHub y debes ayudarme a armar material de estudio completo.

## Contexto

Tengo dos repositorios en GitHub:

1. **Concurso docente 2026 (Barranquilla, Proceso 2948):**
   - URL: https://github.com/ecapdevilla/material-concurso-docente
   - Carpeta local: "concurso-docente-2026" en el escritorio
   - Cargo: Docente de aula, tecnología e informática
   - Normas descargadas: 15 de 22
   - Simulacros creados: 7 (A, B, C, D, E, F, G) con 65 preguntas de nivel alto
   - Modelos de DeepSeek: 9 archivos con 90 preguntas de referencia

2. **Concurso Procuraduría 2026 (Sustanciador 4SU-11):**
   - URL: https://github.com/ecapdevilla/material-concurso-procuraduria
   - Carpeta local: "concurso-procuraduria-2027" en el escritorio
   - Cargo: Sustanciador (4SU-11), nivel técnico, planta global
   - Normas descargadas: 0 de 10
   - Simulacros creados: 1 (10 preguntas de práctica)
   - Temario: ya armado

## Lo que necesito que hagas

### Para el concurso docente (material-concurso-docente):

1. **Descarga las normas que faltan** (prioridad A y B):
   - Ley 1098 de 2006 (Código de Infancia y Adolescencia)
   - Constitución Política (arts. 67, 68, 125, 130, 209)
   - Ley 1346 de 2009 (Convención sobre discapacidad)
   - Decreto 3782 de 2007 (Evaluación de directivos)
   - Ley 2418 de 2024 (Reserva del 7%)
   - Ley 1437 de 2011 (CPACA)
   - Decreto 1743 de 1994 (PRAE)
   - Decreto Legislativo 1384 de 2026 (Medidas por el sismo)
   - Busca en mineducacion.gov.co > Normatividad y funcionpublica.gov.co > Gestor Normativo

2. **Crea 3 simulacros de alto rigor** (formato DeepSeek) sobre:
   - Valoración de antecedentes (factores, techos, doble contabilización, fecha de corte)
   - VRM (requisitos mínimos, afinidad disciplinar, certificaciones válidas)
   - Psicotécnica (compromiso social, iniciativa, comunicación)
   - Usa el formato de los modelos de DeepSeek en la carpeta "11-modelos-deepseek/"

3. **Actualiza el INVENTARIO-NORMAS.md** para marcar las normas descargadas.

4. **Sincroniza con GitHub** (git add -A, git commit, git push).

### Para el concurso de la Procuraduría (material-concurso-procuraduria):

1. **Descarga las normas que faltan**:
   - Constitución Política (arts. 114-124, 209, 277-284)
   - Decreto Ley 262 de 2000 (Estatuto de la Procuraduría)
   - Ley 1437 de 2011 (CPACA)
   - Ley 640 de 2001 (Estatuto de Conciliación)
   - Ley 1581 de 2012 (Protección de datos)
   - Ley 1755 de 2015 (Derecho de petición)
   - Ley 594 de 2000 (Ley General de Archivos)
   - Ley 734 de 2002 (Código Disciplinario)
   - Ley 1474 de 2011 (Estatuto Anticorrupción)
   - Decreto 263 de 2000 (Estatuto de la Carrera Administrativa)
   - Diccionario de Competencias Comportamentales (procuraduria.gov.co)

2. **Crea 3 simulacros de alto rigor** (formato DeepSeek) sobre:
   - Derecho administrativo y procedimiento administrativo
   - Conciliación extrajudicial
   - Gestión documental y bases de datos

3. **Crea un simulacro de alto rigor** con preguntas sobre la estructura de la Procuraduría.

4. **Sincroniza con GitHub** (git add -A, git commit, git push).

## Formato de las preguntas (modelo DeepSeek)

Sigue el formato de los archivos en "11-modelos-deepseek/":
- Marco normativo al inicio (lista de artículos y reglas).
- Nota de diseño (explica que las opciones incorrectas incorporan normas reales pero las aplican torcidamente).
- Situación detallada (caso concreto).
- Opciones de longitud y densidad comparables (isometría formal).
- Clave con justificación técnica (explica por qué fallan las otras).
- Nota metodológica al final.

## Reglas

- No borres ni modifiques archivos existentes. Solo agrega los nuevos.
- No subas archivos personales (SIMO, evidencias, certificados, hojas de vida).
- Solo sube material de estudio (normas, guías, bancos de preguntas, material pedagógico, presentaciones).
- Marca cada norma descargada en NORMAS.md e INVENTARIO-NORMAS.md.
- Sincroniza con GitHub después de cada cambio importante.

## Lo que ya está en el repo del concurso docente

- 15 normas descargadas (de 22 totales).
- 9 modelos de DeepSeek (90 preguntas de referencia).
- 7 simulacros (A, B, C, D, E, F, G) con 65 preguntas.
- Inventario de normas y enlaces para descargar las que faltan.
- Prompt para sincronizar la otra máquina.

## Lo que ya está en el repo de la Procuraduría

- Ficha del concurso, temario, plan de 16 semanas, banco de práctica, pendientes, estudio general, simulacro 1.
- Normas por descargar (10 normas).
- Índice de entrada (index.html).

## Agentes disponibles (en OpenCode)

Si usas OpenCode, tienes estos agentes disponibles:
- @software-engineer: para implementar, refactorizar y depurar en una capa.
- @python-pro: para trabajo en Python.
- @docs-writer: para documentación.
- @tech-researcher: para comparar librerías y enfoques.
- @scalability-architect: para planificación de crecimiento.
- @fullstack-feature-builder: para features completos.

Usa @docs-writer para crear la documentación y @software-engineer para crear los simulacros HTML.

## Instrucciones finales

1. Empieza por descargar las normas de prioridad A del concurso docente.
2. Luego crea los simulacros de alto rigor.
3. Sincroniza con GitHub.
4. Repite el proceso para el concurso de la Procuraduría.
5. Al final, dime qué hiciste y qué queda pendiente.
```

---

## Cómo usar este prompt

1. Abre OpenCode en la máquina donde quieres trabajar.
2. Pega el prompt completo.
3. La IA te ayudará a descargar normas, crear simulacros y sincronizar con GitHub.

## Agentes que puedes usar en OpenCode

- `@docs-writer`: para crear documentación y simulacros HTML.
- `@software-engineer`: para crear archivos y estructura.
- `@tech-researcher`: para buscar normas y fuentes.

## Archivos de referencia

- Modelos de DeepSeek: `11-modelos-deepseek/` en el repo del concurso docente.
- Simulacros existentes: `10-simulacros/` en el repo del concurso docente.
- Enlaces para descargar normas: `02-normas/LINKS-NORMAS-FALTANTES.md` en el repo del concurso docente.
- Inventario de normas: `02-normas/INVENTARIO-NORMAS.md` en el repo del concurso docente.
- Prompt para sincronizar la otra máquina: `PROMPT-OTRA-MAQUINA.md` en el repo del concurso docente.
