# Cómo iniciar el proyecto

API REST sencilla de biblioteca (Library API) hecha con FastAPI y almacenamiento en memoria.

## Requisitos

- Python 3.10 o superior
- `pip`
- Módulo `venv` (en Debian/Ubuntu: `sudo apt install python3.10-venv`)

## 1. Crear el entorno virtual e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Arrancar la API

```bash
python3 -m uvicorn app.main:app --reload
```

Se usa `python3 -m uvicorn` (en lugar de `uvicorn` a secas) para garantizar que se ejecuta el uvicorn del mismo Python donde se instalaron las dependencias y no el del sistema, que provoca `ModuleNotFoundError: No module named 'fastapi'`.

La API queda disponible en `http://127.0.0.1:8000`.

- Documentación interactiva (Swagger UI): `http://127.0.0.1:8000/docs`
- Documentación alternativa (ReDoc): `http://127.0.0.1:8000/redoc`
- Healthcheck: `http://127.0.0.1:8000/health`

## 3. Probar los endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Estado del servicio |
| GET | `/books` | Listar libros (admite filtros `title`, `author` y `year`) |
| POST | `/books` | Crear un libro |
| GET | `/books/{id}` | Obtener un libro |
| PUT | `/books/{id}` | Reemplazar un libro |
| DELETE | `/books/{id}` | Eliminar un libro |

Ejemplos con `curl`:

```bash
# Crear un libro
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune", "author": "Frank Herbert", "year": 1965}'

# Listar libros
curl http://127.0.0.1:8000/books

# Filtrar libros (los filtros se combinan con AND)
curl "http://127.0.0.1:8000/books?title=dune"
curl "http://127.0.0.1:8000/books?author=herbert&year=1965"

# Obtener el libro 1
curl http://127.0.0.1:8000/books/1

# Actualizar el libro 1
curl -X PUT http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune", "author": "Frank Herbert", "year": 1966}'

# Eliminar el libro 1
curl -X DELETE http://127.0.0.1:8000/books/1
```

Los campos `title` y `author` son obligatorios y no pueden estar vacíos; `year` es opcional.

Filtros de `GET /books` (todos opcionales y combinables):

| Query param | Tipo | Comportamiento |
|-------------|------|----------------|
| `title` | string (no vacío) | Contiene el texto, sin distinguir mayúsculas |
| `author` | string (no vacío) | Contiene el texto, sin distinguir mayúsculas |
| `year` | entero | Coincidencia exacta |

Sin coincidencias devuelve `200` con una lista vacía; un valor inválido (p. ej. `year=abc` o `title=`) devuelve `422`.

## 4. Ejecutar los tests

```bash
python3 -m pytest
```

## Notas

- Los datos se guardan en memoria: se pierden al reiniciar el servidor.
- Las mejoras planificadas están en [IMPROVEMENTS.md](IMPROVEMENTS.md).
