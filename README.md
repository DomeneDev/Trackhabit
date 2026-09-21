# 📈 TrackHabit

### 🐍 Proyecto de práctica en Python | Rastreador de hábitos en consola

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Platform](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

---

### 📌 Descripción

TrackHabit guarda tus hábitos diarios o semanales en un archivo JSON, permite marcarlos como completados y calcula cuántos días seguidos llevas cumpliendo (tu racha). Sin bases de datos ni frameworks web — Python puro, pensado para consolidar POO paso a paso.

**Estado actual:** Fases 1-3 completadas (modelos, persistencia y lógica de rachas). Sin interfaz de usuario todavía — se usa por ahora instanciando `HabitTracker` directamente.

---

### ⚙️ Requisitos

- Python 3.10 o superior
- `pytest` (solo para la Fase 5, tests)

---

### 🚀 Instalación (Windows)

```powershell
git clone <tu-repo>
cd trackhabit
python -m venv .venv
.venv\Scripts\activate
pip install pytest
```

> 💡 CMD en lugar de PowerShell: `.venv\Scripts\activate.bat`
> 💡 Si `python` no se reconoce: usa el launcher `py -m venv .venv`

---

### 📂 Estructura del proyecto

```
trackhabit/
├── README.md
├── src/
│   └── main.py            # menú de consola (pendiente — Fase 4)
│   └──utils.py            # constantes de mensajes + validadores de entrada (pendiente — Fase 4)
│   └──models.py          # clases Habit y HabitLog
│   └──storage.py         # guardar y cargar hábitos y registros en JSON
│   └──tracker.py         # HabitTracker: crear hábito, marcar cumplido, calcular racha
├── tests/
│   └── test_tracker.py    # pendiente — Fase 5
└── data/
    ├── habits.json    # se crea solo al ejecutar el programa
    └── logs.json       # historial de cumplimiento, se crea al usar mark_done
```

---

### 🧩 Módulos

- **`models.py`** ✅ — Clases `Habit` (nombre, frecuencia) y `HabitLog` (habito, fecha). Frecuencia como texto simple (`"diario"` / `"semanal"`), sin `Enum` todavía.
- **`storage.py`** ✅ — `save_habits`/`load_habits` y `save_logs`/`load_logs`, usando `json` y `pathlib.Path` para que funcione igual en Windows. Ambas funciones de carga devuelven lista vacía si el archivo no existe.
- **`tracker.py`** ✅ — Clase `HabitTracker` con `add_habit`, `mark_done`, `get_streak`. Carga y guarda automáticamente en disco.
- **`utils.py`** ⏳ — Constantes de mensajes (ej. texto de confirmación al crear un hábito, centralizado en un solo sitio) y funciones de apoyo: mostrar el menú, validar que una entrada de consola sea un entero positivo, verificar el tipo de una entrada antes de usarla.
- **`main.py`** ⏳ — Menú de texto (`input()`): crear hábito, marcar cumplido, ver racha, salir. Usa las constantes y validadores de `utils.py` en vez de tenerlos sueltos en el propio menú.
- **`tests/test_tracker.py`** ⏳ — Tests con `pytest`: racha nueva = 0, tres días seguidos = racha 3.

---

### ▶️ Cómo ejecutar

```powershell
python main.py
pytest
```

---

### 🗺️ Roadmap

- [x] Fase 1 — Modelos básicos
- [x] Fase 2 — Guardar y cargar datos (JSON)
- [x] Fase 3 — Lógica de rachas
- [ ] Fase 4 — Interfaz de consola
- [ ] Fase 5 — Tests con pytest
