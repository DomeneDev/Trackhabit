"""
MÓDULO: models.py
PROYECTO: TrackHabit (Fase 1 - Modelos básicos)

DESCRIPCIÓN GENERAL:
Este archivo actúa como la capa de modelado de datos del proyecto. Su función
es definir la estructura y la forma que tendrán los datos con los que operará
el sistema, sin incluir lógica de negocio ni persistencia.

NOTAS PARA DESARROLADORES:
    - Este fichero solo almacena la estructura (moldes).
    - La gestión de guardado/lectura de datos se realiza en storage.py
    - El cálculo de rachas y lógica principal se gestiona en tracker.py
"""


class Habit:
    """
    Próposito: Representar la definición de un hábito a rastrear.
    """

    def __init__(self, nombre: str, frecuencia: str) -> None:
        """
        Args:
            nombre (str): El nombre o la descrpición del hábito.
            frecuencia (str): La periocidad del habito (diario, semanal,etc)
        """
        self.nombre = nombre
        self.frecuencia = frecuencia

    def __str__(self):
        """
        Próposito mostrar información formateada del hábito
        """
        return (
            f"Hábito: {self.nombre}\n"
            + f"Frecuencia: {self.frecuencia}\n"
            + "-"*30
        )


class HabitLog:
    """
    Próposito: Registrar cada ocasión individual en la que el hábito es
    completado.
    """

    def __init__(self, habito: str, fecha: str):
        """
        Args:
            habito (str): El nombre del hábito al que pertenece el registro.
            fecha (str): La fecha concreta en la que se completo el hábito.
        """
        self.habito = habito
        self.fecha = fecha


if __name__ == "__main__":
    habito_1 = Habit("Estudiar una lección de programación", "Diario")
    habito_2 = Habit("Practiar ejercicios de programación", "Semanal")
    habito_3 = Habit("Crear un miniproyecto con todo los aprendido", "Mensual")

    print(habito_1)
    print(habito_2)
    print(habito_3)
