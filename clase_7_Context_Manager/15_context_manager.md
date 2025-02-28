# Context Managers en Python

## 1. Fundamentos y Conceptos Esenciales

### 1.1 ¿Qué son los Context Managers?

Los Context Managers (Administradores de Contexto) son una característica poderosa de Python que proporciona una sintaxis elegante para el manejo de recursos externos, como archivos, conexiones de red o bases de datos. Su principal propósito es automatizar la adquisición y liberación de recursos, asegurando que estos procesos ocurran correctamente incluso cuando se producen errores.

Según la documentación oficial de Python, un Context Manager es:

> "Un objeto que controla el entorno visto en una sentencia with definiendo los métodos __enter__() y __exit__()."
> 

Este concepto puede entenderse como un "mayordomo digital" que:

1. Prepara un recurso para su uso
2. Te permite utilizarlo
3. Se asegura de limpiarlo adecuadamente cuando terminas

### 1.2 El Problema que Resuelven

Para entender por qué los Context Managers son tan útiles, consideremos un escenario común: trabajar con archivos.

**Enfoque tradicional:**

```python
# Abrir un archivo y escribir contenido
archivo = open('libros.txt', 'w')
archivo.write('El código Da Vinci - Dan Brown')
archivo.close()

```

Este código funciona correctamente si no hay errores. Sin embargo, si ocurre una excepción entre la apertura y el cierre del archivo, el método `close()` nunca se ejecutará, lo que podría provocar:

- **Pérdida de recursos**: El archivo quedará abierto hasta que finalice el programa
- **Pérdida de datos**: Los datos no se guardarán correctamente
- **Fugas de memoria**: Si esto ocurre repetidamente, el programa podría quedarse sin recursos

**Enfoque mejorado con try-finally:**

```python
archivo = open('libros.txt', 'w')
try:
    archivo.write('El código Da Vinci - Dan Brown')
finally:
    archivo.close()  # Siempre se ejecutará, incluso si hay errores

```

Este enfoque es más robusto, pero resulta verboso y propenso a errores si necesitamos repetirlo en múltiples lugares.

### 1.3 La Solución Elegante: `with`

Python proporciona la sentencia `with` que, junto con los Context Managers, simplifica enormemente este proceso:

```python
with open('libros.txt', 'w') as archivo:
    archivo.write('El código Da Vinci - Dan Brown')
# El archivo se cierra automáticamente al salir del bloque

```

Esta sintaxis proporciona varias ventajas:

- **Simplicidad**: Código más limpio y legible
- **Seguridad**: Garantiza la liberación de recursos incluso con excepciones
- **Mantenibilidad**: Reduce la posibilidad de errores humanos

## 2. Código de Demostración

### 2.1 Ejemplo Básico: Uso de Context Managers Incorporados

```python
def demonstrar_context_manager_basico():
    """
    Demuestra el uso básico de context managers con archivos.
    Compara el enfoque tradicional con el enfoque moderno.
    """
    # Enfoque tradicional
    print("Enfoque tradicional:")
    archivo = open('ejemplo.txt', 'w')
    try:
        archivo.write('Línea 1: Usando try-finally\n')
    finally:
        archivo.close()
        print("  Archivo cerrado explícitamente")

    # Enfoque con context manager
    print("\nEnfoque con context manager:")
    with open('ejemplo.txt', 'a') as archivo:
        archivo.write('Línea 2: Usando with statement\n')
    print("  Archivo cerrado automáticamente")

    # Verificar el contenido
    with open('ejemplo.txt', 'r') as archivo:
        contenido = archivo.read()
    print(f"\nContenido del archivo:\n{contenido}")

```

### 2.2 Notas

- **Puntos clave a enfatizar:**
    1. Los Context Managers garantizan la limpieza adecuada de recursos
    2. La sentencia `with` hace el código más legible y menos propenso a errores
    3. El mecanismo trabaja incluso cuando ocurren excepciones
- **Errores comunes a prevenir:**
    1. Intentar acceder al recurso fuera del bloque `with`
    2. No entender que las variables creadas dentro del bloque siguen existiendo fuera
    3. Olvidar que el Context Manager solo gestiona la adquisición y liberación del recurso

## 3. Ejemplos Prácticos

### 3.2 Caso de Uso Real 2: Medición de Tiempo de Ejecución

```python
import time
from contextlib import contextmanager

@contextmanager
def temporizador(nombre="Operación"):
    """
    Context manager para medir el tiempo de ejecución.

    Args:
        nombre: Descripción de la operación a medir
    """
    inicio = time.time()
    try:
        print(f"Iniciando: {nombre}")
        yield  # No se devuelve ningún valor, solo se cede el control
    finally:
        fin = time.time()
        print(f"Finalizado: {nombre} - Tiempo: {fin - inicio:.4f} segundos")

def ejemplo_temporizador():
    """Demuestra el uso del context manager temporizador."""
    # Medir tiempo de cálculo intensivo
    with temporizador("Cálculo de números primos"):
        # Simulamos una operación que consume tiempo
        primos = []
        for num in range(2, 10000):
            es_primo = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
            if es_primo:
                primos.append(num)
        print(f"  Encontrados {len(primos)} números primos")

```

### El Decorador `@contextmanager`

El decorador `@contextmanager` es una herramienta poderosa que simplifica enormemente la creación de context managers en Python. Este decorador, proporcionado por el módulo `contextlib`, nos permite transformar una función generadora simple en un context manager completamente funcional.

### ¿Cómo funciona?

Cuando decoramos una función con `@contextmanager`, estamos convirtiendo una función generadora en un objeto que implementa el protocolo de context manager (con los métodos `__enter__` y `__exit__`) de forma automática. La magia ocurre gracias a la estructura específica que debe tener la función generadora:

1. **Fase de configuración**: Todo el código antes del `yield` forma parte del método `__enter__`.
2. **Punto de cesión**: La instrucción `yield` define lo que se devolverá al contexto del `with`.
3. **Fase de limpieza**: Todo el código después del `yield` forma parte del método `__exit__`.

El decorador permite escribir context managers de manera mucho más concisa y legible que la implementación basada en clases. Para entender cómo funciona internamente, veamos qué está haciendo realmente el decorador:

```python
# Esta función decorada...
@contextmanager
def mi_context_manager():
    # Configuración (equivalente a __enter__)
    recurso = adquirir_recurso()
    try:
        yield recurso  # Cede el control al bloque with
    finally:
        # Limpieza (equivalente a __exit__)
        liberar_recurso(recurso)

# ...es equivalente (conceptualmente) a esta clase
class MiContextManager:
    def __enter__(self):
        self.recurso = adquirir_recurso()
        return self.recurso

    def __exit__(self, exc_type, exc_val, exc_tb):
        liberar_recurso(self.recurso)

```

### Ventajas del decorador `@contextmanager`

1. **Simplicidad**: Reduce significativamente la cantidad de código necesario.
2. **Legibilidad**: El flujo lógico (configuración → uso → limpieza) es mucho más evidente.
3. **Manejo de excepciones integrado**: La estructura `try/finally` asegura la limpieza adecuada.

### Elementos clave para recordar

- El `yield` debe aparecer exactamente una vez en la función decorada.
- Todo el código antes del `yield` se ejecuta cuando se entra al bloque `with`.
- El valor que se proporciona al `yield` es lo que se pasa a la variable después de `as` en la declaración `with`.
- Todo el código después del `yield` se ejecuta cuando se sale del bloque `with`, incluso si ocurre una excepción.
- Para manejar excepciones específicamente, puedes usar un bloque `try/except` alrededor del `yield`.

En nuestro ejemplo del temporizador, podemos ver claramente estas fases:

- Antes del `yield`: Registramos el tiempo de inicio y mostramos un mensaje.
- El `yield` no devuelve ningún valor (solo cede el control).
- Después del `yield`: Calculamos el tiempo transcurrido y mostramos el resultado.

Esta estructura simple pero poderosa permite crear context managers de manera elegante y mantener el código limpio y bien organizado.

## 4. Creación de Context Managers Personalizados

### 4.1 Enfoque Basado en Clases

```python
class GestorArchivo:
    """
    Context Manager personalizado para manejo de archivos.
    Demuestra la implementación basada en clases.
    """

    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None

    def __enter__(self):
        """Se ejecuta al iniciar el bloque with."""
        print(f"Abriendo archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, self.modo)
        return self.archivo

    def __exit__(self, tipo_exc, valor_exc, traceback_exc):
        """
        Se ejecuta al finalizar el bloque with.

        Args:
            tipo_exc: Tipo de excepción o None
            valor_exc: Valor de la excepción o None
            traceback_exc: Traceback de la excepción o None
        """
        print(f"Cerrando archivo: {self.nombre_archivo}")
        if self.archivo:
            self.archivo.close()
        # Manejar excepciones si es necesario
        if tipo_exc:
            print(f"Ocurrió una excepción: {valor_exc}")
        # Retornar True para suprimir la excepción, False para propagarla
        return False

```

### 4.2 Enfoque Basado en Generadores

```python
from contextlib import contextmanager

@contextmanager
def gestor_archivo(nombre_archivo, modo):
    """
    Context Manager personalizado para manejo de archivos.
    Demuestra la implementación basada en generadores.

    Args:
        nombre_archivo: Ruta al archivo
        modo: Modo de apertura ('r', 'w', etc.)
    """
    print(f"Abriendo archivo: {nombre_archivo}")
    archivo = open(nombre_archivo, modo)
    try:
        yield archivo  # Cede el control y devuelve el archivo
    except Exception as e:
        print(f"Ocurrió una excepción: {e}")
        raise  # Re-lanza la excepción
    finally:
        print(f"Cerrando archivo: {nombre_archivo}")
        archivo.close()

```

## 5. Ejercicios Propuestos

### 5.1 Nivel Básico

**Ejercicio 1: Implementación de un Context Manager para Registro**

- **Descripción**: Crear un Context Manager que registre el inicio y fin de operaciones
- **Objetivo**: Practicar la creación básica de Context Managers
- **Pistas**:
    1. Usar el decorador `@contextmanager`
    2. Implementar mensajes de inicio y fin

### 5.2 Nivel Intermedio

**Ejercicio 2: Context Manager para Conexión a Redis**

- **Descripción**: Crear un Context Manager para gestionar conexiones a Redis
- **Objetivo**: Practicar la gestión de recursos externos más complejos
- **Pistas**:
    1. Utilizar el enfoque de clase
    2. Asegurar la liberación adecuada de la conexión

**¿Qué es Redis?**

Redis (Remote Dictionary Server) es una base de datos en memoria de código abierto que funciona como un almacén de estructura de datos. A diferencia de bases de datos relacionales tradicionales como MySQL o PostgreSQL, Redis almacena los datos en memoria principal (RAM), lo que le permite ofrecer un rendimiento extremadamente rápido con tiempos de respuesta generalmente inferiores a un milisegundo.

Redis es especialmente útil para:

- Almacenamiento en caché
- Colas de mensajes
- Contador de visitas en tiempo real
- Gestión de sesiones
- Clasificaciones y tablas de posiciones
- Datos geoespaciales

Redis admite varias estructuras de datos como cadenas, hashes, listas, conjuntos, conjuntos ordenados y más. La conexión a Redis se realiza típicamente a través de un cliente que abre una conexión TCP, envía comandos y lee respuestas. Es fundamental gestionar adecuadamente estas conexiones para evitar fugas de recursos, especialmente en aplicaciones de alto rendimiento donde se abren y cierran numerosas conexiones.

Un Context Manager para Redis sería particularmente valioso porque aseguraría que las conexiones se cierren correctamente incluso cuando ocurren excepciones, evitando posibles problemas de memoria y conexiones huérfanas.

### 5.3 Nivel Avanzado

**Ejercicio 3: Context Manager Anidados**

- **Descripción**: Implementar y utilizar múltiples Context Managers anidados
- **Objetivo**: Dominar escenarios complejos con múltiples recursos
- **Pistas**:
    1. Combinar múltiples Context Managers en una sola sentencia `with`
    2. Asegurar el orden correcto de liberación de recursos

## 6. Solución de Ejercicios

### Solución Ejercicio 1: Context Manager para Registro

```python
from contextlib import contextmanager
import time

@contextmanager
def registrador(nombre_operacion):
    """
    Context manager que registra el inicio y fin de una operación.

    Args:
        nombre_operacion: Nombre descriptivo de la operación
    """
    print(f"[{time.strftime('%H:%M:%S')}] INICIO: {nombre_operacion}")
    try:
        yield
    finally:
        print(f"[{time.strftime('%H:%M:%S')}] FIN: {nombre_operacion}")

# Ejemplo de uso
def demo_registrador():
    with registrador("Procesamiento de datos"):
        # Simulamos una operación
        for i in range(3):
            print(f"  Procesando lote {i+1}...")
            time.sleep(0.5)

```

### Solución Ejercicio 2: Context Manager para Conexión a Redis

```python
import redis

class ConexionRedis:
    """
    Context manager para gestionar conexiones a Redis.
    """

    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.cliente = None

    def __enter__(self):
        """Establece la conexión con Redis."""
        self.cliente = redis.Redis(
            host=self.host,
            port=self.port,
            db=self.db
        )
        return self.cliente

    def __exit__(self, tipo_exc, valor_exc, traceback_exc):
        """Cierra la conexión con Redis."""
        if self.cliente:
            self.cliente.close()

        if tipo_exc:
            print(f"Error en la conexión Redis: {valor_exc}")

        return False  # Propaga las excepciones

# Ejemplo de uso
def demo_redis():
    try:
        with ConexionRedis() as r:
            r.set('clave', 'valor')
            valor = r.get('clave')
            print(f"Valor obtenido: {valor}")
    except redis.RedisError as e:
        print(f"No se pudo conectar a Redis: {e}")

```

### Solución Ejercicio 3: Context Managers Anidados

```python
import sqlite3
from contextlib import contextmanager
import os

@contextmanager
def crear_archivo_temporal(nombre_base):
    """Crea un archivo temporal y lo elimina al finalizar."""
    nombre_completo = f"{nombre_base}_{time.strftime('%Y%m%d%H%M%S')}.tmp"
    print(f"Creando archivo temporal: {nombre_completo}")
    try:
        yield nombre_completo
    finally:
        if os.path.exists(nombre_completo):
            os.remove(nombre_completo)
            print(f"Eliminando archivo temporal: {nombre_completo}")

class ConexionBD:
    """Context manager para conexión a SQLite."""

    def __init__(self, ruta_bd):
        self.ruta_bd = ruta_bd

    def __enter__(self):
        self.conexion = sqlite3.connect(self.ruta_bd)
        return self.conexion

    def __exit__(self, tipo_exc, valor_exc, traceback_exc):
        if self.conexion:
            self.conexion.close()
        return False

def demo_anidados():
    """Demuestra el uso de context managers anidados."""
    # Forma 1: Anidamiento explícito
    with crear_archivo_temporal("datos") as nombre_archivo:
        with ConexionBD(nombre_archivo) as conexion:
            cursor = conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS prueba (id INTEGER PRIMARY KEY)")
            print("Tabla creada en base de datos temporal")

    # Forma 2: Anidamiento en una línea
    with crear_archivo_temporal("backup") as nombre_archivo, ConexionBD(nombre_archivo) as conexion:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS respaldo (id INTEGER PRIMARY KEY)")
        print("Tabla creada en segunda base de datos temporal")

```

Los Context Managers representan uno de los patrones más elegantes y útiles en Python para la gestión de recursos. Dominando este concepto, podrás escribir código más limpio, seguro y mantenible.