# Decoradores. El concepto más avanzado de funciones

## 1. Decoradores

### 1.1 Introducción

Los decoradores son funciones que **modifican el comportamiento de otras funciones**, ayudan a acortar nuestro código y hacen que sea más Pythonico. Si alguna vez has visto `@`, estás ante un decorador.

Veamos un ejemplo muy sencillo. Tenemos una función `suma()` que vamos a decorar usando `mi_decorador()`. Para ello, antes de la declaración de la función suma, hacemos uso de `@mi_decorador`.

```python
def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)

# Se va a llamar
# Entra en funcion suma
# Se ha llamado
```

Lo que realiza `mi_decorador()` es definir una nueva función que encapsula o envuelve la función que se pasa como entrada. Concretamente lo que hace es hace uso de dos `print()`, uno antes y otro después de la llamada la función.

Por lo tanto, cualquier función que use `@mi_decorador` tendrá dos print, uno y al principio y otro al final, dando igual lo que realmente haga la función.

Veamos otro ejemplo usando el decorador sobre otra función.

```python
@mi_decorador
def resta(a ,b):
    print("Entra en funcion resta")
    return a - b

resta(5, 3)

# Se va a llamar
# Entra en funcion resta
# Se ha llamado
```

### 1.2 Definiendo decoradores

Antes de nada hay que entender que todo en Python es un objeto, incluso una función. De hecho se puede asignar una función a una variable. Nótese la diferencia entre:

- `di_hola()` llama a la función.
- `di_hola` hace referencia a la función, no la llama.

```python
def di_hola():
    print("Hola")

f1 = di_hola() # Llama a la función
f2 = di_hola   # Asigna a f2 la función

print(f1)      # None, di_hola no devuelve nada
print(f2)      # <function di_hola at 0x1077bf158>

#f1()          # Error! No es válido
f2()           # Llama a f2, que es di_hola()

del f2         # Borra el objeto que es la función
#f2()          # Error! Ya no existe

di_hola()      # Ok. Sigue existiendo
```

Entendido esto, demos un paso más. En Python se pueden definir funciones dentro de otras funciones. La función `operaciones` define `suma()` y `resta()`, y dependiendo del parámetro de entrada `op`, se devolverá una u otra.

```python
def operaciones(op):
    def suma(a, b):
        return a + b
    def resta(a, b):
        return a - b

    if op == "suma":
        return suma
    elif op == "resta":
        return resta

funcion_suma = operaciones("suma")
print(funcion_suma(5, 7)) # 12

funcion_suma = operaciones("resta")
print(funcion_suma(5, 7)) # -2
```

Si llamamos a la función devuelta con dos operandos, se realizará una operación distinta en función de si se uso suma o resta.

Ahora ya podemos dar la última vuelta de tuerca y **escribir nuestro propio decorador** sin hacer uso de `@`. Por un lado tenemos el `decorador`, que recibe como entrada una función y devuelve otra función decorada. Por el otro la función `suma()` que queremos decorar.

```python
def decorador(func):
    def envoltorio_func(a, b):
        print("Decorador antes de llamar a la función")
        c = func(a, b)
        print("Decorador después de llamar a la función")
        return c
    return envoltorio_func

def suma(a, b):
    print("Dentro de suma")
    return a + b

# Nueva funcion decorada
funcion_decorada = decorador(suma)

funcion_decorada(5, 8)
```

Entonces, haciendo uso de `decorador` y pasando como entrada `suma`, recibimos una nueva función decorada con una funcionalidad nueva, lista para ser usada. Sería el equivalente al uso de `@`.

### 1.3 Decoradores con parámetros

Tal vez quieras que tu decorador tenga algún parámetro de entrada para modificar su comportamiento. Se puede hacer envolviendo una vez más la función como se muestra a continuación.

```python
def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)
# Imprimer esto antes y después
# Entra en funcion suma
# Imprimer esto antes y después
```

### 1.4 Preservando la identidad de las funciones con functools.wraps

Cuando creamos decoradores, nos encontramos con un detalle importante que puede pasar desapercibido: las funciones decoradas pierden su identidad original. Veamos esto con un ejemplo:

```python
def mi_decorador(funcion):
    def wrapper(a, b):
        print("Antes de la función")
        resultado = funcion(a, b)
        print("Después de la función")
        return resultado
    return wrapper

@mi_decorador
def suma(a, b):
    """Esta función suma dos números."""
    return a + b

# Veamos qué ocurre con la identidad de nuestra función
print(suma.__name__)  # Imprime: 'wrapper'
print(suma.__doc__)   # Imprime: None

```

¿Qué ha pasado aquí? Nuestra función `suma` ha perdido tanto su nombre como su documentación. Esto sucede porque el decorador realmente está reemplazando nuestra función original con la función wrapper. Este comportamiento puede causar problemas cuando:

- Estamos depurando código y los mensajes de error muestran nombres de funciones incorrectos
- Utilizamos herramientas de generación automática de documentación
- Necesitamos acceder a los metadatos de la función original

Para solucionar este problema, Python nos proporciona `functools.wraps`. Veamos cómo lo utilizamos:

```python
from functools import wraps

def mi_decorador(funcion):
    @wraps(funcion)  # <- Esta es la magia
    def wrapper(a, b):
        print("Antes de la función")
        resultado = funcion(a, b)
        print("Después de la función")
        return resultado
    return wrapper

@mi_decorador
def suma(a, b):
    """Esta función suma dos números."""
    return a + b

# Ahora la función mantiene su identidad
print(suma.__name__)  # Imprime: 'suma'
print(suma.__doc__)   # Imprime: 'Esta función suma dos números.'

```

También funciona con decoradores que tienen parámetros:

```python
def mi_decorador_con_args(mensaje):
    def decorador(funcion):
        @wraps(funcion)  # Preservamos la identidad de la función original
        def wrapper(a, b):
            print(mensaje)
            resultado = funcion(a, b)
            print(mensaje)
            return resultado
        return wrapper
    return decorador

@mi_decorador_con_args("Ejecutando operación...")
def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

print(multiplicar.__name__)  # Imprime: 'multiplicar'
print(multiplicar.__doc__)   # Imprime: 'Multiplica dos números.'

```

`functools.wraps` copia los atributos importantes de la función original a la función wrapper, incluyendo:

- `__name__`: El nombre de la función
- `__doc__`: La documentación (docstring)
- `__module__`: El módulo donde está definida
- `__annotations__`: Las anotaciones de tipo
- `__qualname__`: El nombre cualificado completo

Por esta razón, se considera una buena práctica usar siempre `@wraps` cuando creamos decoradores, especialmente en código que otros desarrolladores utilizarán o que formará parte de una biblioteca.

## 2. Código de Demostración

### 2.1 Ejemplo Logger

Una de las utilidades más usadas de los decoradores son los **logger**. Su uso nos permite escribir en un fichero los resultados de ciertas operaciones, que funciones han sido llamadas, o cualquier información que en un futuro resulte útil para ver que ha pasado.

En el siguiente ejemplo tenemos un uso más completo del decorador `log()` que escribe en un fichero los resultados de las funciones que han sido llamadas.

```python
def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)
```

## 3. Ejemplos Prácticos

### 3.1 Uso Autorizado en Flask

Otro caso de uso muy importante y ampliamente usado en Flask, que es un framework de desarrollo web, es el uso de decoradores para asegurarse de que una función es llamada cuando el usuario se ha autenticado.

Realizando alguna simplificación, podríamos tener un decorador que requiriera que una variable `autenticado` fuera `True`. La función se ejecutará solo si dicha variable global es verdadera, y se dará un error de lo contrario.

```python
autenticado = True

def requiere_autenticación(f):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def di_hola():
    print("Hola")

di_hola()

```

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico

**Ejercicio 1: Temporizador de funciones**

- **Descripción**: Crea un decorador llamado `medir_tiempo` que mida y muestre el tiempo que tarda en ejecutarse una función.
- **Objetivo**: Practicar la creación de decoradores básicos y el uso del módulo `time`.
- **Pistas**:
    1. Utiliza `time.time()` para obtener el tiempo actual
    2. La diferencia entre dos tiempos te dará la duración
    3. Recuerda preservar los metadatos de la función usando `functools.wraps`

**Ejercicio 2: Validador de argumentos**

- **Descripción**: Implementa un decorador `validar_tipos` que verifique que los argumentos pasados a una función son del tipo esperado.
- **Objetivo**: Aprender a trabajar con tipos de datos y argumentos de funciones en decoradores.
- **Pistas**:
    1. Usa `isinstance()` para verificar los tipos
    2. Puedes usar anotaciones de tipo de Python como referencia
    3. Maneja tanto argumentos posicionales como de palabra clave

### 4.2 Nivel Intermedio

**Ejercicio 3: Cache con tiempo de expiración**

- **Descripción**: Desarrolla un decorador `cache_temporal` que almacene en caché los resultados de una función durante un tiempo específico (en segundos).
- **Objetivo**: Practicar el manejo de estado en decoradores y la gestión de tiempo.
- **Pistas**:
    1. Usa un diccionario para almacenar resultados y timestamps
    2. Verifica la antigüedad de los resultados antes de usarlos
    3. Implementa limpieza de resultados antiguos

**Ejercicio 4: Retry con backoff exponencial**

- **Descripción**: Crea un decorador `retry` que reintente ejecutar una función cuando falla, con un tiempo de espera exponencial entre intentos.
- **Objetivo**: Aprender a manejar excepciones y temporización en decoradores.
- **Pistas**:
    1. Usa un bucle para los reintentos
    2. Implementa tiempo de espera exponencial (2^n segundos)
    3. Permite configurar el número máximo de intentos

### 4.3 Nivel Avanzado

**Ejercicio 5: Decorador de rate limiting**

- **Descripción**: Implementa un decorador `rate_limit` que limite el número de veces que se puede llamar a una función en un período de tiempo.
- **Objetivo**: Manejar estado compartido y sincronización en decoradores.
- **Pistas**:
    1. Usa una cola para trackear timestamps de llamadas
    2. Implementa limpieza de llamadas antiguas
    3. Considera la sincronización en entornos multi-hilo

**Ejercicio 6: Decorador de dependencias**

- **Descripción**: Crea un decorador `require` que permita especificar qué otras funciones deben ejecutarse antes que la función decorada.
- **Objetivo**: Trabajar con decoradores que modifican el flujo de ejecución del programa.
- **Pistas**:
    1. Mantén un registro de funciones ejecutadas
    2. Verifica dependencias antes de la ejecución
    3. Maneja dependencias circulares

## 5. Recursos Adicionales

- **Documentación oficial**:
    - [Python Decorators - Python Documentation](https://docs.python.org/3/glossary.html#term-decorator)
    - [PEP 318 - Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- **Artículos relacionados**:
    - [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
    - [Python Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)
    - [Python Decorators: A Complete Guide](https://www.geeksforgeeks.org/decorators-in-python/)
    - https://mathspp.com/blog/pydonts/decorators
- **Videos recomendados**:
    - [Corey Schafer - Python Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U)
    - [Python Engineer - Closures in Python](https://www.youtube.com/watch?v=y6sYGhHKB4A)
