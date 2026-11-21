# Instrucciones para la otra máquina

Copia y pega este prompt en OpenCode (o en la terminal) de la otra máquina.

---

## Prompt para OpenCode en la otra máquina

```
Tengo un repositorio público en GitHub: https://github.com/ecapdevilla/material-concurso-docente
Ya está clonado en esta máquina (o clónalo si no está).

Necesito que:
1. Sincronices el repo con GitHub (git pull origin master).
2. Identifiques todos los archivos de la otra máquina que puedan servir para el concurso docente (normas, guías, bancos de preguntas, material pedagógico, etc.) que NO estén ya en el repo.
3. Copies esos archivos a la carpeta "Estudio Concurso 2026/" del repo, en la subcarpeta correspondiente (01-fuentes-oficiales/, 02-normas/, 03-temario/, 06-banco-practica/, etc.).
4. Actualices el INVENTARIO-NORMAS.md y el NORMAS.md para reflejar las nuevas normas.
5. Hagas commit y push al repo (git add -A && git commit -m "Agrega archivos de la otra maquina" && git push origin master).

No borres ni modifiques archivos existentes. Solo agrega los nuevos.
No subas archivos personales (SIMO, evidencias, certificados, hojas de vida).
Solo sube material de estudio (normas, guías, bancos de preguntas, material pedagógico, presentaciones).

Después de hacer push, dime qué archivos agregaste y qué normas nuevas encontraste.
```

---

## Pasos manuales (si no usas OpenCode)

### En la otra máquina:
```bash
# 1. Clonar el repo (si no está clonado)
git clone https://github.com/ecapdevilla/material-concurso-docente.git

# 2. Entrar al repo
cd material-concurso-docente

# 3. Traer los últimos cambios
git pull origin master

# 4. Copiar los archivos nuevos a la carpeta correspondiente
# Ejemplo: copiar normas a 02-normas/, bancos a 06-banco-practica/, etc.
# cp /ruta/a/tus/archivos/* "Estudio Concurso 2026/02-normas/"

# 5. Hacer commit y push
git add -A
git commit -m "Agrega archivos de la otra maquina"
git push origin master
```

### En esta máquina:
```bash
cd "C:\Users\BS-TECNOLOGI02\AppData\Local\Temp\opencode\repo-remoto"
git pull origin master
```

## Archivos que probablemente tengas en la otra máquina y que sirven

- Normas en PDF (Ley 1098, Constitución, Decreto 1290, etc.)
- Guías de orientación de la CNSC
- Bancos de preguntas (simulacros, diagnósticos)
- Material pedagógico (aptitud verbal, pedagogía, tecnología)
- Cuadernillos de preguntas Saber Pro
- Presentaciones o resúmenes de estudio
- Proyecto del anexo técnico
- Tablas de valoración de antecedentes

## Archivos que NO debes subir

- Hojas de vida personales
- Certificados personales
- Documentos de SIMO (inscripciones, soportes)
- Credenciales o tokens
- Archivos de configuración personal (opencode.json, ayuda.txt)
