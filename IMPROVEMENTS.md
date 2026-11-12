# Mejoras futuras

Lista de mejoras candidatas para ir implementándolas poco a poco (un ticket de Jira + un PR por cada una) y probar el generador de documentación. La columna "Tipo" sugiere el tipo de ticket y "Qué ejercita" indica qué parte de la documentación debería reflejar el cambio.

## Funcionalidad

| # | Mejora | Tipo | Qué ejercita |
|---|--------|------|--------------|
| 1 | Paginación en `GET /books` (`limit`, `offset`) | Story | Cambio de contrato de un endpoint existente |
| 2 | Filtros y búsqueda por título/autor/año | Story | Nuevos query params |
| 3 | Ordenación (`sort_by`, `order`) | Story | Query params, combinación con filtros |
| 4 | Campo `isbn` único con validación de formato | Story | Cambio de modelo, nuevo error 409 |
| 5 | Campo `genre` / categorías de libros | Story | Cambio de modelo, migración |
| 6 | Entidad `Author` con relación a `Book` | Epic | Nuevo modelo, endpoints y relaciones |
| 7 | Gestión de préstamos (`/loans`): prestar y devolver libros | Epic | Nueva funcionalidad con reglas de negocio |
| 8 | Entidad `Member` (socios de la biblioteca) | Story | Nuevo recurso, dependencia con préstamos |
| 9 | Fecha de vencimiento y multas por retraso | Story | Reglas de negocio, cálculos |
| 10 | Endpoint de estadísticas (`/stats`): libros más prestados, etc. | Story | Endpoint agregado |
| 11 | `PATCH /books/{id}` para actualizaciones parciales | Task | Nuevo endpoint, diferencia con PUT |
| 12 | Importar/exportar libros en CSV | Story | Subida de ficheros, formatos |

## Persistencia y arquitectura

| # | Mejora | Tipo | Qué ejercita |
|---|--------|------|--------------|
| 13 | Sustituir el almacenamiento en memoria por SQLite + SQLAlchemy | Epic | Cambio arquitectónico grande |
| 14 | Migraciones con Alembic | Task | Infraestructura |
| 15 | Refactor: separar capa de servicios de las rutas | Task | Refactor sin cambio funcional |
| 16 | Configuración por variables de entorno (`pydantic-settings`) | Task | Documentación de configuración |
| 17 | Versionado de la API (`/v1/books`) | Story | Breaking change |
| 18 | Renombrar `PUT /books/{id}` para exigir el recurso completo y devolver 409 en conflictos | Story | Breaking change |

## Seguridad y calidad

| # | Mejora | Tipo | Qué ejercita |
|---|--------|------|--------------|
| 19 | Autenticación con API key o JWT | Story | Seguridad, cabeceras |
| 20 | Roles (admin / lector) con permisos por endpoint | Story | Autorización |
| 21 | Rate limiting | Task | Comportamiento no funcional |
| 22 | Manejo de errores unificado con formato de respuesta común | Task | Contrato de errores |
| 23 | Logging estructurado y `request_id` | Task | Observabilidad |
| 24 | Healthcheck extendido (`/health/ready` con comprobación de BD) | Task | Operaciones |

## Bugs a introducir y corregir (para tickets tipo Bug)

| # | Bug | Qué ejercita |
|---|-----|--------------|
| 25 | Se pueden crear libros duplicados (mismo título y autor) | Bug funcional |
| 26 | El campo `year` acepta años futuros o negativos | Bug de validación |
| 27 | `DELETE` de un libro prestado no debería permitirse | Bug de regla de negocio |
| 28 | La paginación devuelve resultados repetidos si cambian los datos | Bug sutil |

## DevOps y documentación

| # | Mejora | Tipo | Qué ejercita |
|---|--------|------|--------------|
| 29 | Dockerfile y `docker-compose.yml` | Task | Despliegue |
| 30 | Pipeline de CI con GitHub Actions (tests + lint) | Task | Infraestructura |
| 31 | Linter y formateador (`ruff`) con pre-commit | Task | Tooling |
| 32 | Cobertura de tests con umbral mínimo | Task | Calidad |

## Sugerencia de orden

1. Empezar por mejoras pequeñas e independientes (1, 2, 11, 25) para probar PRs sencillos.
2. Seguir con un cambio de modelo (4, 5) para ver cómo se documentan los cambios de esquema.
3. Hacer un refactor puro (15) para comprobar que el generador lo distingue de una feature.
4. Abordar una épica completa (7 + 8 + 9) para probar la agregación de varios tickets y PRs.
5. Introducir un breaking change (17 o 18) y comprobar que queda reflejado.
