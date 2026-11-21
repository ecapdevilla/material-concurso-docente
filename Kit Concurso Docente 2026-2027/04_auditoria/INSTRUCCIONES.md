# Auditoría local de archivos
Desde la raíz del repositorio, ejecuta:

```bash
python ruta/al/kit/04_auditoria/auditar_repo.py .
```

Se crearán `inventario_repo.csv` y `resumen_repo.txt` en la ruta en la que se encuentra el script, sin modificar el repositorio. El inventario enumera rutas, extensiones, tamaños y SHA-256; **no verifica la calidad del contenido de preguntas**. Sube después el CSV y los simulacros relevantes para auditoría semántica.
