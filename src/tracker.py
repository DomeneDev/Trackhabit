"""
MÓDULO: tracker.py
PROYECTO: TrackHabit (Fase 3 - Lógica de rachas)

DESCRIPICIÓN GENERAL:
Este módulo contiene la lógica principal del negocio. Define las clase HabitTracker,
encargada de vincular la información de los hábitos con sus registros de cumplimiento,
así como de calcular las rachas de días consecutivos completados.

NOTAS PARA DESARROLLADORES:
    - Esté módulo no gestiona menús ni interacción por pantalla.
    - No realiza lectura o escritura directa en disco.
"""
from datetime import date

from models import Habit, HabitLog
from storage import load_habits, save_habits, load_logs, save_logs


class HabitTracker:
    """
    Gestionar la colección de hábitos y controlar las acciones sobre ellos.
    """

    def __init__(self, path: str, log_path: str) -> None:
        """
        Args:
            path (str): Ruta de donde se encuentra el archivo que almacena hábitos
        """
        self.path = path
        self.logs_path = log_path
        self.habits: list[Habit] = load_habits(path)
        self.habits_historial: list[HabitLog] = load_logs(log_path)

    def add_habit(self, nombre: str, frecuencia: str) -> None:
        """
        Registrar un hábito nuevo

        Args:
            nombre (str): Nombre del hábito
            frecuencia (str): Frecuencia del habito
        """
        habito_add = Habit(nombre, frecuencia)
        self.habits.append(habito_add)
        save_habits(self.habits, self.path)

    def mark_done(self, nombre: str, fecha: str | None = None) -> None:
        """
        Registrar que un hábito ha sido completado en una fecha específica.

        Args:
            nombre (str): Nombre del hábito
            fecha (str, optional): Fecha en la que se realizó. Si no se especifica
            el sistema utiizará la fecha actual por defecto.
        """
        if fecha is None:
            fecha = str(date.today())
        for habit in self.habits:
            if habit.nombre == nombre:
                habito_completo = HabitLog(nombre, fecha)
                self.habits_historial.append(habito_completo)
        save_logs(self.habits_historial, self.logs_path)

    def get_streak(self, nombre: str) -> int:
        """
        Calcular el número total de días consecutivos que el hábito ha sido
        completado.

        COMPORTAMIENTO ESPERADO:
            * Devuelve 0 para hábitos recién creados o sin registros acumulados
            * Si el hábito se marca en días consecutivos, incrementa la racha
            (ejemplo: 3 días seguidos = 3)
            * Si se omite un día, la racha se reinicia según las reglas establecidas.

        Args:
            nombre (str): nombre del hábito

        Returns:
            int: Valor de racha
        """
        registros = [
            log for log in self.habits_historial if log.habito == nombre]
        if not registros:
            return 0
        else:
            fechas = [
                date.fromisoformat(log.fecha) for log in registros
            ]
            fechas_ordenadas = sorted(fechas, reverse=True)
            racha = 1
            for fecha_actual, fecha_siguiente in zip(
                fechas_ordenadas, fechas_ordenadas[1:]
            ):
                diferencia = (fecha_actual - fecha_siguiente).days
                if diferencia == 1:
                    racha += 1
                else:
                    break
        return racha
