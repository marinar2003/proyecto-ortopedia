# Aved Medical - Sistema de Gestión

Proyecto de **Práctica Profesionalizante 1** - Tecnicatura en Desarrollo de Software, ISSD (2026).

Sistema de información para **Aved Medical S.A.** (comercialización y distribución de implantes traumatológicos).

## Equipo
| Integrante | Rol |
|-----------|-----|
| Marina Revol | _a definir_ |
| Alex Martinez | _a definir_ |
| Florencia Rosales | _a definir_ |

**Docente:** Nadia Gallardo

## Tecnologías
- Python 3 + Flask
- SQLite (desarrollo)
- HTML / CSS
- Git + GitHub

## Puesta en marcha

```bash
# 1. Clonar
git clone <URL-DEL-REPO>
cd aved-medical-sgc

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python run.py
```
Abrir http://127.0.0.1:5000 en el navegador.

## Tests
```bash
python -m unittest discover tests
```

## Estructura
```
app/            código de la aplicación (rutas, templates, estáticos)
tests/          pruebas
docs/           documentación y entregas
run.py          punto de entrada
```

## Convenciones
Ver [docs/CONVENCIONES.md](docs/CONVENCIONES.md).
