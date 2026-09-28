"""
MÓDULO: main.py
PROYECTO : TrackHabit (Fase 4.3 - Intefaz de consola)

DESCRIPCIÓN GENERAL:
Este archivo es el punto de entrada principal de la aplicación en la Terminal.
Se encarga de orquestar la interaccíon del usuario controlando el bucle de
ejecución del menú, cooridando las respuestas según la opción elegida e
integrando la persistencia del sistema.

FLUJO PRINCIAPL Y RESPONSABILIDADES:

1. Inicializando y Carga de Datos:
    - Al arrancar la aplicación, invoca la función de carga desde storage.py
    para recuperar el estado previo de los hábitos desde el archivo de datos
    - Instancia la clase HabitTracker con la información recuperada.

2. Bucle Interactivo del menú:
    - Muestra el menú de opciones disponible al usuario apoyándose en utils.py
    - Procesa la opción seleccionada conectando cada una con las funciones
    correspondientes:
        * Opción 1: Crear nuevo hábito (add_habit)
        * Opción 2: Marcar un hábito completado (mark_done)
        * Opción 3: Consultar racha actal de un hábito (get_streak)
        * Opción 4: Finalizar la ejecución del programa

3. Persistencia al Salir:
    - Guarda automáticamente el estado actualizado de los habitos mediante
    storage.py antes de cerrar la aplicación.

NOTAS PARA DESARROLLADORES:
    - Este fichero NO debe definir textos de mensajes ni realizar válidaciones
    directas; todas las entradas e impresiones se delegan a utils.py
    - Toda la lógica del cálculo de rachas o gestión de hábitos se delega a
    tracker.py
"""
import constants
from storage import save_habits, save_logs
from tracker import HabitTracker
from utils import menu, validar_opcion, read_new_habit, read_habit

# Mensaje de bienvenida
print(constants.MSG_BIENVENIDA)

# Carga de ficheros
tracker = HabitTracker(
    constants.RUTA_HABITOS, constants.RUTA_LOGS
)

# Bucle principal del progama
while True:
    # Mostrar menú
    menu()
    # Selección de opción
    opcion = validar_opcion(
        constants.MSG_INTRODUCE_OPCION, constants.MSG_OPCION_NO_VALIDA
    )
    # Procesamiento de opción
    match opcion:
        case 1:
            # Creación de nuevo hábito
            nuevo_habito = read_new_habit()
            tracker.add_habit(
                nuevo_habito["nombre"],
                nuevo_habito["frecuencia"]
            )
            print(constants.MSG_CONFIRMACION_CREACION)
        case 2:
            # Marcar hábito completo
            habito_a_completar = read_habit()
            for h in tracker.habits:
                if h.nombre == habito_a_completar:
                    tracker.mark_done(h.nombre)
                    print(constants.MSG_HABITO_COMPLETADO)
                    break
            else:
                print(constants.MSG_HABITO_NO_ENCONTRADO)
        case 3:
            # Mostrar rachas por hábitos
            habito_a_mostrar = read_habit()
            for h in tracker.habits:
                if h.nombre == habito_a_mostrar:
                    racha = tracker.get_streak(h.nombre)
                    print(constants.MSG_RACHA + str(racha) + constants.MSG_DIAS)
                    break
            else:
                print(constants.MSG_HABITO_NO_ENCONTRADO)
        case 4:
            # Guardar todos los datos y salir
            save_habits(tracker.habits, constants.RUTA_HABITOS)
            save_logs(tracker.habits_historial, constants.RUTA_LOGS)
            print(constants.MSG_DATOS_GUARDADOS)
            print(constants.MSG_DESPEDIDA)
            break
        case _:
            # Caso por defecto, opción no válida
            print(constants.MSG_OPCION_NO_VALIDA)
