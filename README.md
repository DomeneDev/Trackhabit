# TrackHabit

Rastreador de hábitos con arquitectura en capas y API REST, diseñado como proyecto de práctica para consolidar POO, testing y diseño de software en Python.

## Descripción

TrackHabit permite registrar hábitos diarios o semanales, marcar su cumplimiento y calcular rachas (_streaks_) de constancia. El proyecto expone tanto una interfaz de línea de comandos (CLI) como una API REST con FastAPI, pensada para integrarse con herramientas de automatización externas (por ejemplo, n8n) mediante peticiones HTTP.

## Requisitos

- Python 3.10 o superior
- `pip` y (recomendado) un entorno virtual (`venv`)

## Instalación

```bash
git clone <tu-repo>
cd trackhabit
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Dependencias principales sugeridas en `pyproject.toml`:

```
fastapi
uvicorn
pydantic
pytest
pytest-cov
ruff
```

## Estructura de carpetas recomendada

```
trackhabit/
├── README.md
├── pyproject.toml
├── src/
│   └── trackhabit/
│       ├── __init__.py
│       ├── models.py        # Entidades: Habit, HabitLog, Frequency
│       ├── repository.py    # Abstracción de persistencia + implementación SQLite
│       ├── services.py      # Lógica de negocio: rachas, estadísticas
│       ├── api.py           # Endpoints FastAPI
│       └── cli.py           # Interfaz de línea de comandos
├── tests/
│   ├── test_models.py
│   ├── test_repository.py
│   ├── test_services.py
│   └── test_api.py
└── data/
    └── trackhabit.db        # Base de datos SQLite (generada en tiempo de ejecución)
```

## Módulos a construir

- **`models.py`** — Entidades de dominio (`Habit`, `HabitLog`) usando `dataclass` y `Enum` para la frecuencia.
- **`repository.py`** — Interfaz `HabitRepository` (ABC) y su implementación concreta `SQLiteHabitRepository`. Aquí se practica el patrón _Repository_ para desacoplar la lógica de negocio del almacenamiento.
- **`services.py`** — `HabitService`, que recibe un repositorio por inyección de dependencias y contiene la lógica de cálculo de rachas.
- **`api.py`** — App de FastAPI con endpoints para crear hábitos, marcar cumplimiento y consultar rachas.
- **`cli.py`** — Comandos de terminal que reutilizan `HabitService` (misma lógica, dos interfaces distintas).
- **`tests/`** — Suite de `pytest` con al menos un test por módulo, incluyendo casos límite (racha rota, hábito inexistente, fecha futura).

## Cómo ejecutar

```bash
# CLI
python -m trackhabit.cli --help

# API
uvicorn trackhabit.api:app --reload

# Tests
pytest --cov=src/trackhabit
```
