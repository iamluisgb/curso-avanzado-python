import sys
from .config import cargar_config
from .nucleo.procesador import procesar_datos

def main():
    config = cargar_config()
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
        procesar_datos(nombre_archivo, config)
    else:
        print("Por favor proporciona un nombre de archivo")

if __name__ == '__main__':
    main()
