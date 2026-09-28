"""
MODULO: constants.py
PROYECTO: TrackHabit (Fase 4.1 - Archivo de constantes)

DESCRIPCIÓN GENERAL:
Almacenan los mensajes que se muestran al usuario durante la ejecución del
programa; confirmación al crear/marcar un habito, mensajes de error o
desdpedida.

NOTAS PARA DESARROLLADORES:
    - Ningún texto de mensaje ni validación de entrada debe escribirse
    directamente en main.py; todo deve reutilizarse desde este módulo.
"""
# Ruta de guardado de archivos JSON
RUTA_HABITOS = "data/habits.json"
RUTA_LOGS = "data/habits_log.json"

# Constantes bienvenida y despedida
MSG_BIENVENIDA = "👋 Bienvenido a TrackHabit 1.0"
MSG_DESPEDIDA = "👋 Vuelve pronto a TrackHabit 1.0"

# Constantes de mensajes de menú
TITULO_MENU = "📝 TRACKHABIT 1.0 - MENU 📝"
OPCION_CREAR_HABITO = " - 1) Crear hábito 🆕"
OPCION_MARCAR_COMPLETO = " - 2) Marcar completado ✅"
OPCION_VER_RACHA = " - 3) Ver racha 🏃‍♂️"
OPCION_SALIR = " - 4) Salir 🚪"

# MENSAJES DE INPUTS
MSG_INTRODUCE_OPCION = "Introduce una opción: "
MSG_NOMBRE_HABITO = "Introduce el habito: "
MSG_FRECUENCIA_HABITO = "Introduce la frecuencia: "

# MENSAJES DE ERROR
MSG_OPCION_NO_VALIDA = "❌ Opción no válida...."
MSG_HABITO_NO_ENCONTRADO = "❌ Hábito no registrado..."

# MENSAJES DE CONFIRMACIÓN
MSG_CONFIRMACION_CREACION = "✅ Hábito creado y guardado correctamente..."
MSG_HABITO_COMPLETADO = "✅ Hábito completado correctamente ..."
MSG_RACHA = "La racha acutal del habito: "
MSG_DIAS = " Días... enhorabuena 🔝"
MSG_DATOS_GUARDADOS = "💾 Datos guardadados..."
