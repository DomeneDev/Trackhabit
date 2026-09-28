# 📈 TrackHabit

### 🐍 Proyecto de práctica en Python | Rastreador de hábitos en consola

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Platform](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

---

### 📌 Descripción

TrackHabit guarda tus hábitos diarios o semanales en un archivo JSON, permite marcarlos como completados y calcula cuántos días seguidos llevas cumpliendo (tu racha). Sin bases de datos ni frameworks web — Python puro, pensado para consolidar POO paso a paso.

**Estado actual:** Fases 1-4 completadas (modelos, persistencia, lógica de rachas e interfaz de consola). Aplicación usable de principio a fin desde la terminal. Pendiente: tests automatizados (Fase 5).

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

````
trackhabit/
├── README.md
├── main.py            # punto de entrada: bucle del menú de consola
├── constants.py       # constantes de mensajes y rutas de archivo
├── utils.py           # menú, validador de entrada, lectura de datos de consola
├── models.py          # clases Habit y HabitLog
├── storage.py         # guardar y cargar hábitos y registros en JSON
├── tracker.py         # HabitTracker: crear hábito, marcar cumplido, calcular racha
├── tests/
│   └── test_tracker.py    # pendiente — Fase 5
└── data/
    ├── habits.json    # se crea solo al ejecutar el programa
    └── habits_log.json # historial de cumplimiento, se crea al usar mark_done

---

### 🧩 Módulos

- **`models.py`** ✅ — Clases `Habit` (nombre, frecuencia) y `HabitLog` (habito, fecha). Frecuencia como texto simple (`"diario"` / `"semanal"`), sin `Enum` todavía.
- **`storage.py`** ✅ — `save_habits`/`load_habits` y `save_logs`/`load_logs`, usando `json` y `pathlib.Path` para que funcione igual en Windows. Ambas funciones de carga devuelven lista vacía si el archivo no existe.
- **`tracker.py`** ✅ — Clase `HabitTracker` con `add_habit`, `mark_done`, `get_streak`. Carga y guarda automáticamente en disco.
- **`constants.py`** ✅ - Todos los textos que se muestran al usuario (bienvenida, menú, confirmaciones, errrores) y rutas de los archivos de datos, centralizados en un solo sitio
- **`utils.py`** ⏳ — Funciones de apoyo a la consola: menu() (muestra las opciones), validar_opcion() (valida que la entrada sea un entero positivo, repreguntando si no lo es), read_new_habit() y read_habit() (lectura de datos por teclado)
- **`main.py`** ⏳ — Bucle principal con match/case: crea un único HabitTracker al arrancar y lo reutiliza en cada opción del menú (crear hábito, marcar cumplido, ver racha, salir), sin releer el disco en cada acción.
- **`tests/test_tracker.py`** ⏳ — Tests con `pytest`: racha nueva = 0, tres días seguidos = racha 3.

---

### ▶️ Cómo ejecutar

```powershell
python main.py
pytest
````

---

### 🗺️ Roadmap

- [x] Fase 1 — Modelos básicos
- [x] Fase 2 — Guardar y cargar datos (JSON)
- [x] Fase 3 — Lógica de rachas
- [x] Fase 4 — Interfaz de consola
- [ ] Fase 5 — Tests con pytest
