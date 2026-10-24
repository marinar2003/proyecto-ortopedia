# Convenciones de trabajo del equipo

## Ramas
- `main`: siempre estable y funcionando. **Nadie sube directo a main.**
- Una rama por tarea, saliendo de `main`:
  - `feature/<descripcion>` -> funcionalidad nueva (ej: `feature/login`)
  - `fix/<descripcion>` -> corrección de errores
  - `docs/<descripcion>` -> documentación

## Commits
Formato: `tipo: descripción corta en presente`

| Tipo | Uso |
|------|-----|
| feat | funcionalidad nueva |
| fix | corrección de error |
| docs | documentación |
| style | formato, sin cambio de lógica |
| test | pruebas |
| chore | tareas de mantenimiento |

Ejemplos: `feat: agrega listado de cirugías`, `docs: actualiza README`.

## Flujo de trabajo
1. `git checkout main` y `git pull`
2. `git checkout -b feature/mi-tarea`
3. Trabajar y hacer commits chicos y frecuentes
4. `git push -u origin feature/mi-tarea`
5. Abrir Pull Request en GitHub y pedir revisión a un compañero
6. Tras la aprobación, se hace merge a `main` y se borra la rama

## Reglas
- Commits chicos y frecuentes, no uno gigante antes de la entrega.
- Nunca subir contraseñas, claves ni archivos `.env`.
- Antes de abrir un PR: correr los tests.
