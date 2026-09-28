"""
MÓDULO: storage.py
PROYECTO: TrackHabit (Fase 2 - Guardar y cargar datos en JSON)

DESCRIPCIÓN GENERAL:
Este archivo se encarga de la persistencia de los datos del proyecto. Su función
es guardar y recuperar la información de los hábitos desde un archivo en formato
JSON, permitiendo que los datos se mantengan guardados incluso al cerrar la
aplicación.

NOTAS PARA DESARROLLADORES:
    - Este módulo no define la estructura de las clases(eso pertenece a
    models.py)
    - Tampoco contiene la lógica para calcular rachas ni interactuar con el
    usuario.
    - Es conveniente asegurar que la carpeta de destino (/data) exista antes de
    guardar
"""

# Biblioteca para el manejo de archivos JSON
import json
# Biclioteca Path para manejar las rutas como objetos path y manejar rutas
from pathlib import Path

# Importamos models.py para que se comprenda los datos a guardar.
from models import Habit, HabitLog

# funcion para convertir objeto Habit en un Dict manejable por JSON


def habit_to_dict(habit: Habit) -> dict:
    """
    Convierte una instancia de Habit en un diccionario serializable a JSON

    Args:
        habit (Habit): Objeto de clase Habit

    Returns:
        dict: Diccionario serializable JSON
    """
    return {
        "nombre": habit.nombre,
        "frecuencia": habit.frecuencia
    }

# Función pra convertir un Dict del archivo JSON a un Objeto Habit


def dict_to_habit(dict_habit: dict) -> Habit:
    """
    Reconstruye el objeto Habit desde un diccionario cargado del JSON

    Args:
        dict_habit (dict): Diccionario de habito extraido de JSON

    Returns:
        Habit: Objeto Habit
    """
    return Habit(
        nombre=dict_habit["nombre"],
        frecuencia=dict_habit["frecuencia"]
    )


# Función para guardar Habits
def save_habits(habits: list[Habit], path: str) -> None:
    """
    Guardar la lista actual de hábitos en un archivo JSON

    Args:
        habits (list): Lista de objetos habit que se van a almacenar.
        path (str): Ruta del archivo donde se guardará la información.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    data_habits = [habit_to_dict(h) for h in habits]
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data_habits, f, indent=4)


# Función para cargar Habits
def load_habits(path: str) -> list[Habit]:
    """
    Cargar los hábitos guardados previamente desde el archivo JSON.

    Args:
        path (str): Ruta del archivo JSON

    Returns:
            list: Lista de hábitos existentes en el archivo JSON

    Comportamiento
        * Lee el archivo y devuelve las clasese (models.py)
        * Si el archivo no existe, no se encuentra en la ruta o esta corrupto,
        maneja la situación devolviendo una lista vacía([]) sin interumpir
        el programa.
    """
    try:
        with open(path, 'r', encoding="utf-8") as f:
            data_habits_json = json.load(f)
            data_habits = [dict_to_habit(h) for h in data_habits_json]
            return data_habits
    except (FileNotFoundError, json.JSONDecodeError):
        data_habits = []
        return data_habits

# Función para convertir los objetos HabitLog a dict serializable por JSON


def log_to_dict(log: HabitLog) -> dict:
    """
    Convierte una instancia de HabitLog en un diccionario a JSON

    Args:
        log (HabitLog): Objeto de clase HabitLog

    Returns:
        dict: Diccionario serializable JSON
    """
    return {
        "nombre": log.habito,
        "fecha": log.fecha
    }

# Función para convetir los dict del archivo Joson a Objetos HabitLog


def dict_to_log(dict_log: dict) -> HabitLog:
    """
    Reconstruye el objeto HabitLog desde un diccionario cargado del JSON

    Args:
        dict_log (dict): Diccionario de registro extraído de JSON

    Returns:
        HabitLog: Objeto HabitLog
    """
    return HabitLog(
        habito=dict_log["nombre"],
        fecha=dict_log["fecha"]
    )


# Función para guardar los logs de HabitLog
def save_logs(logs: list[HabitLog], path: str) -> None:
    """
    Guardar lista actual de registros de cumplimiento en un archivo JSON

    Args:
        logs (list[HabitLog]): Lista de Objetos HabitLog a almacenar.
        path (str): Ruta del archivo donde se guardará la información.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    data_logs = [log_to_dict(l) for l in logs]
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data_logs, f, indent=4)


# Función para cargar los logs de HabitLog
def load_logs(path: str) -> list[HabitLog]:
    """
    Cargar los registros de cumplimiento guardados previamente desde JSON

    Args:
        path (str): Ruta del archivo JSON

    Returns:
        list: Lista de registos existentes en el archivo JSON
    """
    try:
        with open(path, 'r', encoding="utf-8") as f:
            data_log_json = json.load(f)
            data_log = [dict_to_log(l) for l in data_log_json]
            return data_log
    except (FileNotFoundError, json.JSONDecodeError):
        data_log = []
        return data_log
