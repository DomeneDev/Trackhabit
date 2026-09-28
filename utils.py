"""
MODULO: utils.py
PROYECTO: TrackHabit (Fase 4.2 - Archivo de auxiliares)

DESCRIPCIÓN GENERAL:
Este archivo contiene las funciones auxiliares de interfaz
y validaciones de entrada de datos.
Su objetivo es descoplar la lógica de representación y la interacción básica
con el usuario, evitando escribir cadenas de texto o comprobaciones directamente
en el flujo principal.

NOTAS PARA DESARROLLADORES:
    - No contiene lógica de almacenamiento, ni de negocio.
"""
import constants

# Visualizacion de la interfaz


def menu():
    """
    Desplegar en pantalla las opciones disponibles de la aplicación
    """
    print(constants.TITULO_MENU)
    print(constants.OPCION_CREAR_HABITO)
    print(constants.OPCION_MARCAR_COMPLETO)
    print(constants.OPCION_VER_RACHA)
    print(constants.OPCION_SALIR)
    print("\n")


# Validador de opción
def validar_opcion(msg_input_opcion: str, msg_error_opcion_no_valida) -> int:
    """
    Verificar que la entrada de la opción sea un número entero positivo.

    Comportameinte esperado: Solicitar nuevamente el dato al usuario en caso de
    introducir un valor no permitido.

    Args:
        msg_input_opcion (str): Mensaje de input
        msg_error_opcion_no_valiad (_type_): Mensaje de error

    Return
        (int): Opción validada
    """
    while True:
        try:
            opcion = input(msg_input_opcion)
            opcion = int(opcion)
            if opcion > 0:
                break
            print(msg_error_opcion_no_valida)
        except ValueError:
            print(msg_error_opcion_no_valida)
    return opcion


# Leer datos de habito nuevo
def read_new_habit() -> dict:
    """
    Realizar la lectura de los valores necesarios para crear un objeto Habit

    Returns:
        dict: Diccionario con los valores nombre y frecuencia
    """
    habito_nuevo = input(constants.MSG_NOMBRE_HABITO)
    frecuencia_habito = input(constants.MSG_FRECUENCIA_HABITO)
    habito_dict = {
        "nombre": habito_nuevo,
        "frecuencia": frecuencia_habito
    }
    return habito_dict


# Leer nombre de hábito
def read_habit() -> str:
    """
    Realizar la lectura del nombre del hábito

    Returns:
        str: Nombre del hábito a buscar
    """
    nombre = input(constants.MSG_NOMBRE_HABITO)
    return nombre
