# Programación Funcional en Python: Filter, Map y Reduce

## 1. Fundamentos y Conceptos Esenciales

### 1.1 ¿Qué es la Programación Funcional?

La programación funcional es un paradigma de programación que trata la computación como la evaluación de funciones matemáticas. En Python, aunque no es un lenguaje puramente funcional, podemos aplicar muchos conceptos de este paradigma para escribir código más limpio, predecible y fácil de probar.

Los principios fundamentales incluyen:
- Inmutabilidad de datos
- Funciones puras (sin efectos secundarios)
- Funciones como ciudadanos de primera clase
- Composición de funciones

### 1.2 Las Tres Operaciones Fundamentales

Python proporciona tres operaciones fundamentales para la programación funcional:

1. **Filter**: Filtra elementos de una secuencia según un predicado
2. **Map**: Transforma cada elemento de una secuencia
3. **Reduce**: Combina los elementos de una secuencia en un único valor

### 1.3 Analogías y Ejemplos Conceptuales

Imaginemos una línea de producción en una fábrica:

1. **Filter** es como un control de calidad que decide qué productos pasan:
   - Solo los productos que cumplen ciertos criterios continúan
   - Los demás son descartados

2. **Map** es como una estación de modificación:
   - Cada producto que pasa se transforma de alguna manera
   - Todos los productos son procesados de la misma forma

3. **Reduce** es como el empaquetado final:
   - Todos los productos se combinan en una única unidad
   - El resultado es un único elemento que representa el proceso completo

## 2. Código de Demostración

### 2.1 Ejemplo Básico: Procesamiento de Datos de Estudiantes

```python
from functools import reduce

# Datos de ejemplo
estudiantes = [
    {'nombre': 'Ana', 'edad': 20, 'nota': 8.5},
    {'nombre': 'Juan', 'edad': 19, 'nota': 7.0},
    {'nombre': 'María', 'edad': 21, 'nota': 9.2},
    {'nombre': 'Pedro', 'edad': 20, 'nota': 6.8}
]

# Ejemplo de filter: Estudiantes con nota >= 8
aprobados = list(filter(
    lambda x: x['nota'] >= 8,
    estudiantes
))

# Ejemplo de map: Obtener solo los nombres
nombres = list(map(
    lambda x: x['nombre'],
    estudiantes
))

# Ejemplo de reduce: Calcular promedio de notas
suma_notas = reduce(
    lambda acc, x: acc + x['nota'],
    estudiantes,
    0
)
promedio = suma_notas / len(estudiantes)
```

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real 1: Procesamiento de Datos de Ventas

```python
# Datos de ventas
ventas = [
    {'producto': 'laptop', 'unidades': 5, 'precio': 800},
    {'producto': 'mouse', 'unidades': 10, 'precio': 25},
    {'producto': 'monitor', 'unidades': 8, 'precio': 300},
    {'producto': 'teclado', 'unidades': 12, 'precio': 45}
]

# Calcular total por producto
def calcular_total(venta):
    return {
        'producto': venta['producto'],
        'total': venta['unidades'] * venta['precio']
    }

# Filtrar ventas significativas
ventas_grandes = filter(
    lambda x: x['total'] > 1000,
    map(calcular_total, ventas)
)

# Sumar todos los totales
total_ventas = reduce(
    lambda acc, x: acc + x['total'],
    ventas_grandes,
    0
)
```

### 3.2 Caso de Uso Real 2: Análisis de Texto

```python
def analizar_texto(texto):
    # Dividir en palabras y limpiar
    palabras = texto.lower().split()
    
    # Filtrar palabras significativas (más de 3 letras)
    palabras_significativas = filter(
        lambda x: len(x) > 3,
        palabras
    )
    
    # Contar frecuencia de cada palabra
    return reduce(
        lambda acc, palabra: {
            **acc,
            palabra: acc.get(palabra, 0) + 1
        },
        palabras_significativas,
        {}
    )
```

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico
**Ejercicio 1: Procesamiento de Números**
* **Descripción**: Dado una lista de números, filtrar los pares, duplicarlos y sumar el resultado
* **Objetivo**: Practicar la composición de filter, map y reduce
* **Pistas**:
   1. Usar filter para los números pares
   2. Usar map para duplicar
   3. Usar reduce para sumar

### 4.2 Nivel Intermedio
**Ejercicio 2: Análisis de Diccionarios**
* **Descripción**: Procesar una lista de diccionarios con información de productos
* **Objetivo**: Practicar el procesamiento de estructuras de datos complejas
* **Pistas**:
   1. Filtrar productos por categoría
   2. Transformar la estructura de datos
   3. Calcular totales por categoría

### 4.3 Nivel Avanzado
**Ejercicio 3: Pipeline de Procesamiento**
* **Descripción**: Crear un pipeline de procesamiento de datos usando composición de funciones
* **Objetivo**: Implementar un flujo de procesamiento funcional completo
* **Pistas**:
   1. Crear funciones pequeñas y puras
   2. Componer las funciones usando los operadores funcionales
   3. Mantener la inmutabilidad de los datos

## 5. Recursos Adicionales
* **Documentación oficial**: 
   - Python Functional Programming HOWTO
   - functools documentation
* **Artículos relacionados**: 
   - "Functional Programming in Python"
   - "Understanding Map, Filter and Reduce"
* **Videos recomendados**: 
   - "Python Functional Programming Features"
   - "Advanced Functional Programming Concepts"

## 6. Solución de Ejercicios

### Solución Ejercicio 1: Procesamiento de Números
```python
def procesar_numeros(numeros):
    """
    Filtra números pares, los duplica y suma el resultado.
    
    Args:
        numeros: Lista de números enteros
        
    Returns:
        int: Suma de los números pares duplicados
    """
    return reduce(
        lambda acc, x: acc + x,
        map(
            lambda x: x * 2,
            filter(
                lambda x: x % 2 == 0,
                numeros
            )
        ),
        0
    )

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = procesar_numeros(numeros)
print(f"Resultado: {resultado}")  # 60 (suma de 4,8,12,16,20)

# Versión desglosada para mejor comprensión
def procesar_numeros_desglosado(numeros):
    # Filtrar números pares
    pares = filter(lambda x: x % 2 == 0, numeros)
    
    # Duplicar los números
    duplicados = map(lambda x: x * 2, pares)
    
    # Sumar todos los números
    suma = reduce(lambda acc, x: acc + x, duplicados, 0)
    
    return suma
```

### Solución Ejercicio 2: Análisis de Diccionarios
```python
def analizar_productos(productos):
    """
    Analiza una lista de productos y calcula totales por categoría.
    
    Args:
        productos: Lista de diccionarios con información de productos
        
    Returns:
        dict: Resumen por categoría
    """
    # Función auxiliar para calcular el valor total
    def calcular_valor(producto):
        return {
            **producto,
            'valor_total': producto['precio'] * producto['cantidad']
        }
    
    # Añadir valor total a cada producto
    productos_con_valor = map(calcular_valor, productos)
    
    # Agrupar por categoría y sumar valores
    return reduce(
        lambda acc, producto: {
            **acc,
            producto['categoria']: acc.get(producto['categoria'], 0) + 
                                 producto['valor_total']
        },
        productos_con_valor,
        {}
    )

# Ejemplo de uso
productos = [
    {'nombre': 'Laptop', 'categoria': 'Electrónica', 'precio': 1000, 'cantidad': 2},
    {'nombre': 'Mouse', 'categoria': 'Electrónica', 'precio': 20, 'cantidad': 5},
    {'nombre': 'Libreta', 'categoria': 'Papelería', 'precio': 5, 'cantidad': 10},
    {'nombre': 'Monitor', 'categoria': 'Electrónica', 'precio': 200, 'cantidad': 3}
]

resultado = analizar_productos(productos)
print("Totales por categoría:")
for categoria, total in resultado.items():
    print(f"{categoria}: ${total:,.2f}")
```

### Solución Ejercicio 3: Pipeline de Procesamiento
```python
from typing import List, Dict, Callable
from functools import reduce

def crear_pipeline(*funciones: Callable) -> Callable:
    """
    Crea un pipeline de procesamiento componiendo funciones.
    
    Args:
        *funciones: Funciones a componer
        
    Returns:
        Callable: Función compuesta
    """
    return reduce(
        lambda f, g: lambda x: g(f(x)),
        funciones
    )

def normalizar_datos(datos: List[Dict]) -> List[Dict]:
    """Normaliza los datos de entrada."""
    return map(
        lambda x: {
            'nombre': x['nombre'].strip().lower(),
            'valor': float(x['valor']),
            'categoria': x['categoria'].strip().lower()
        },
        datos
    )

def filtrar_valores_validos(datos: List[Dict]) -> List[Dict]:
    """Filtra registros con valores válidos."""
    return filter(
        lambda x: x['valor'] > 0,
        datos
    )

def agrupar_por_categoria(datos: List[Dict]) -> Dict:
    """Agrupa los datos por categoría."""
    return reduce(
        lambda acc, x: {
            **acc,
            x['categoria']: acc.get(x['categoria'], []) + [x]
        },
        datos,
        {}
    )

def calcular_estadisticas(datos: Dict) -> Dict:
    """Calcula estadísticas por categoría."""
    return {
        categoria: {
            'total': sum(item['valor'] for item in items),
            'promedio': sum(item['valor'] for item in items) / len(items),
            'cantidad': len(items)
        }
        for categoria, items in datos.items()
    }

# Crear pipeline
pipeline = crear_pipeline(
    normalizar_datos,
    filtrar_valores_validos,
    agrupar_por_categoria,
    calcular_estadisticas
)

# Ejemplo de uso
datos_entrada = [
    {'nombre': 'Producto A ', 'valor': '100.50', 'categoria': 'Electrónica '},
    {'nombre': 'Producto B', 'valor': '-50.00', 'categoria': 'Electrónica'},
    {'nombre': 'Producto C', 'valor': '75.25', 'categoria': 'Libros'},
    {'nombre': 'Producto D', 'valor': '200.00', 'categoria': 'Electrónica'}
]

resultado = pipeline(datos_entrada)
print("\nEstadísticas por categoría:")
for categoria, stats in resultado.items():
    print(f"\n{categoria.title()}:")
    print(f"Total: ${stats['total']:,.2f}")
    print(f"Promedio: ${stats['promedio']:,.2f}")
    print(f"Cantidad: {stats['cantidad']}")
```