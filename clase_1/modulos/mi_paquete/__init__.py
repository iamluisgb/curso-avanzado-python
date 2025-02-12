from .base_datos import ejecutar_consulta, obtener_todos
# mi_paquete/__init__.py

print("Inicializando mi_paquete...")

# Configuración global del paquete
CONFIGURACION_GLOBAL = {
    'modo_debug': False,
    'tamaño_cache': 1000,
    'version': '1.0.0'
}

# Inicialización de recursos compartidos
conexion_base_datos = None
