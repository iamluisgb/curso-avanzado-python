# Funciones Lambda en Python

## 1. Funciones Lambda

### 1.1 Introducción

Las funciones lambda en Python representan una característica poderosa del lenguaje que permite escribir funciones anónimas y compactas. A diferencia de las funciones normales definidas con la palabra clave `def`, las lambdas son expresiones que evalúan a un objeto función. Estas funciones son llamadas "anónimas" porque no necesitan tener un nombre asociado, aunque pueden asignarse a variables si es necesario.

El término "lambda" proviene del cálculo lambda, un sistema formal en lógica matemática desarrollado por Alonzo Church en la década de 1930. En programación, las expresiones lambda son una característica común de los lenguajes de programación funcional, aunque Python las incorpora de manera elegante en su paradigma multiparadigma.

### 1.2 Fundamentos Clave

La comprensión de las funciones lambda se basa en varios conceptos fundamentales:

- **Sintaxis única**: Las lambdas siguen la estructura `lambda argumentos: expresión`, donde la expresión se evalúa y retorna automáticamente
- **Expresiones vs. Declaraciones**: Las lambdas solo pueden contener expresiones, no declaraciones como if, for, while, etc. (aunque pueden usar expresiones condicionales)
- **Alcance léxico**: Las lambdas pueden acceder a variables en su ámbito envolvente (closure)
- **Evaluación perezosa**: Cuando se usan como argumentos por defecto o en comprensiones de lista, las lambdas se evalúan en el momento de la llamada
- **Inmutabilidad funcional**: Las lambdas son objetos función inmutables; una vez definidas, no pueden modificarse

### 1.3 Analogías y Ejemplos Conceptuales

Para entender mejor las funciones lambda, podemos usar varias analogías:

**Analogía de la Calculadora:**
Imagina una calculadora científica con botones de función programable:

- Una función normal es como programar un botón con varios pasos y guardarlo permanentemente
- Una lambda es como usar la función de composición temporal: introduces una operación simple que usarás una vez

**Analogía del Post-it:**

- Una función normal es como escribir instrucciones detalladas en un documento que guardarás
- Una lambda es como escribir una nota rápida en un Post-it: breve, específica y generalmente para uso inmediato

**Analogía de la Cocina:**

- Una función normal es como una receta completa con varios pasos
- Una lambda es como una instrucción rápida de cocina: "cortar en cubos", "servir caliente"

## 2. Código de Demostración

### 2.1 Ejemplos Básicos y Progresión

```python
# Título: Progresión de Funciones Lambda
# Objetivo: Mostrar la evolución desde funciones normales hasta lambdas

# 1. Función tradicional
def cuadrado_tradicional(x):
    return x ** 2

# 2. Versión lambda equivalente
cuadrado_lambda = lambda x: x ** 2

# 3. Lambda con múltiples argumentos
operacion = lambda x, y, z: x + y * z

# 4. Lambda con expresión condicional
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"

# 5. Lambda en una estructura de datos
operaciones = {
    'suma': lambda x, y: x + y,
    'resta': lambda x, y: x - y,
    'multiplicacion': lambda x, y: x * y
}

# Ejemplos de uso
print(cuadrado_tradicional(5))      # Output: 25
print(cuadrado_lambda(5))           # Output: 25
print(operacion(2, 3, 4))          # Output: 14
print(es_par(4))                   # Output: "Par"
print(operaciones['suma'](5, 3))   # Output: 8

```

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real 1: Procesamiento de Datos

**Contexto**: Análisis de datos de ventas con diferentes transformaciones

```python
# Datos de ejemplo
ventas = [
    {'producto': 'A', 'cantidad': 50, 'precio': 10},
    {'producto': 'B', 'cantidad': 30, 'precio': 15},
    {'producto': 'C', 'cantidad': 20, 'precio': 20}
]

# Transformaciones con lambdas
total_por_venta = list(map(
    lambda v: {**v, 'total': v['cantidad'] * v['precio']},
    ventas
))

ventas_grandes = list(filter(
    lambda v: v['cantidad'] > 25,
    ventas
))

ordenado_por_ingreso = sorted(
    total_por_venta,
    key=lambda v: v['total'],
    reverse=True
)

# Análisis funcional encadenado
from functools import reduce

total_ingresos = reduce(
    lambda acc, v: acc + (v['cantidad'] * v['precio']),
    ventas,
    0
)

print("Total ingresos:", total_ingresos)

```

**Puntos Importantes**:

- Las lambdas permiten transformaciones de datos claras y concisas
- Se pueden encadenar operaciones funcionales
- Ideal para operaciones de mapeo, filtrado y reducción

### 3.2 Caso de Uso Real 2: GUI y Callbacks

**Contexto**: Creación de una interfaz gráfica simple con comportamiento dinámico

```python
import tkinter as tk
from functools import partial

class CalculadoraSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Lambda")

        # Entrada
        self.entrada = tk.Entry(root)
        self.entrada.pack()

        # Operaciones usando lambdas
        operaciones = [
            ('+', lambda x, y: x + y),
            ('-', lambda x, y: x - y),
            ('*', lambda x, y: x * y),
            ('/', lambda x, y: x / y if y != 0 else "Error")
        ]

        # Crear botones dinámicamente
        for simbolo, operacion in operaciones:
            # Usar partial para "congelar" la operación
            comando = partial(self.calcular, operacion)
            tk.Button(
                root,
                text=simbolo,
                command=comando
            ).pack(side=tk.LEFT)

    def calcular(self, operacion):
        try:
            nums = [float(x) for x in self.entrada.get().split()]
            if len(nums) == 2:
                resultado = operacion(nums[0], nums[1])
                tk.Label(self.root, text=f"Resultado: {resultado}").pack()
        except ValueError:
            tk.Label(self.root, text="Error: Entrada inválida").pack()

# Uso
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraSimple(root)
    root.mainloop()

```

**Puntos Importantes**:

- Las lambdas son excelentes para callbacks
- Permiten crear comportamiento dinámico
- Facilitan la parametrización de funciones

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico

**Ejercicio 1: Transformaciones Simples**

- **Descripción**: Crear una serie de lambdas para transformaciones matemáticas básicas
- **Objetivo**: Familiarizarse con la sintaxis y uso básico de lambdas
- **Tareas**:
    1. Crear lambda para convertir Celsius a Fahrenheit
    2. Crear lambda para calcular el área de un círculo
    3. Crear lambda para verificar si un número es positivo
- **Pistas**:
    1. F = C * 9/5 + 32
    2. Área = π * r²
    3. Usar operador ternario

**Ejercicio 2: Manipulación de Strings**

- **Descripción**: Crear lambdas para procesamiento de texto
- **Objetivo**: Practicar lambdas con strings
- **Tareas**:
    1. Lambda para capitalizar palabras
    2. Lambda para contar vocales
    3. Lambda para invertir string
- **Pistas**:
    1. Usar métodos de string
    2. Usar set para vocales
    3. Usar slice notation

### 4.2 Nivel Intermedio

**Ejercicio 3: Procesamiento de Datos**

- **Descripción**: Usar lambdas con listas de diccionarios
- **Objetivo**: Practicar transformaciones de datos complejas
- **Datos de ejemplo**:

```python
productos = [
    {'nombre': 'laptop', 'precio': 1000, 'stock': 5},
    {'nombre': 'mouse', 'precio': 20, 'stock': 10},
    {'nombre': 'monitor', 'precio': 200, 'stock': 3}
]

```

- **Tareas**:
    1. Filtrar productos con stock bajo (< 5)
    2. Calcular valor total por producto (precio * stock)
    3. Ordenar por valor total descendente
- **Pistas**:
    1. Usar filter y lambda
    2. Usar map para nueva lista
    3. Usar sorted con key

### 4.3 Nivel Avanzado

**Ejercicio 4: Pipeline de Procesamiento**

- **Descripción**: Crear un pipeline de procesamiento usando lambdas
- **Objetivo**: Comprender composición de funciones y procesamiento en cadena
- **Tareas**:
    1. Crear pipeline para procesar datos de texto
    2. Aplicar múltiples transformaciones
    3. Manejar errores y casos especiales
- **Pistas**:
    1. Usar reduce para composición
    2. Encadenar operaciones
    3. Usar operadores ternarios para validación

## 5. Recursos Adicionales

### 5.1 Documentación Oficial y Tutoriales

- [Python Lambda Expressions (Documentación Oficial)](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Real Python - Lambda Functions](https://realpython.com/python-lambda/)

### 5.2 Artículos Profundos

- [Python Tips - Lambda Functions](https://book.pythontips.com/en/latest/lambda.html)
- [Programación Funcional en Python](https://docs.python.org/3/howto/functional.html)

### 5.3 Videos Recomendados

- "Python Lambda Functions Explained" - Corey Schafer
- "Functional Programming in Python" - Raymond Hettinger (PyCon)

## 6. Solución de Ejercicios

### 6.1 Soluciones
# Ejercicio 1: Transformaciones Simples
# Estas transformaciones demuestran el uso básico de lambdas con operaciones matemáticas
celsius_a_fahrenheit = lambda c: c * 9/5 + 32
area_circulo = lambda r: 3.14159 * r ** 2
es_positivo = lambda x: "Positivo" if x > 0 else "No positivo"

# Pruebas
print(celsius_a_fahrenheit(25))  # 77.0
print(area_circulo(5))          # 78.54
print(es_positivo(10))          # "Positivo"

# Ejercicio 2: Manipulación de Strings
# Estas funciones demuestran cómo las lambdas pueden trabajar con strings y sus métodos
# También muestran cómo combinar lambdas con comprensiones de lista
capitalizar = lambda s: ' '.join(word.capitalize() for word in s.split())
contar_vocales = lambda s: len([c for c in s.lower() if c in 'aeiou'])
invertir = lambda s: s[::-1]

# Pruebas
print(capitalizar("hola mundo"))      # "Hola Mundo"
print(contar_vocales("python"))       # 1
print(invertir("lambda"))             # "adbmal"

### 6.2 Soluciones Nivel Intermedio

Las soluciones de nivel intermedio demuestran cómo las lambdas pueden trabajar con estructuras de datos más complejas y cómo se pueden combinar con funciones de orden superior como map, filter y sorted.

```python
# Ejercicio 3: Procesamiento de Datos
# Este ejercicio demuestra cómo usar lambdas para transformar y analizar datos
# estructurados en forma de diccionarios
productos = [
    {'nombre': 'laptop', 'precio': 1000, 'stock': 5},
    {'nombre': 'mouse', 'precio': 20, 'stock': 10},
    {'nombre': 'monitor', 'precio': 200, 'stock': 3}
]

# 1. Filtrar productos con stock bajo
stock_bajo = list(filter(lambda p: p['stock'] < 5, productos))

# 2. Calcular valor total por producto
con_valor_total = list(map(
    lambda p: {**p, 'valor_total': p['precio'] * p['stock']},
    productos
))

# 3. Ordenar por valor total
ordenados = sorted(
    con_valor_total,
    key=lambda p: p['valor_total'],
    reverse=True
)

# Pruebas
print("Productos con stock bajo:", stock_bajo)
print("Productos con valor total:", con_valor_total)
print("Productos ordenados:", ordenados)

### 6.3 Soluciones Nivel Avanzado

```python
# Ejercicio 4: Pipeline de Procesamiento
from functools import reduce

# Funciones de procesamiento
normalizar = lambda s: s.lower().strip()
remover_especiales = lambda s: ''.join(c for c in s if c.isalnum() or c.isspace())
tokenizar = lambda s: s.split()
filtrar_cortas = lambda words: [w for w in words if len(w) > 3]

# Crear pipeline usando composición de funciones
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions[::-1])

# Pipeline completo
pipeline = compose(
    filtrar_cortas,
    tokenizar,
    remover_especiales,
    normalizar
)

# Función para procesar texto de manera segura
procesar_texto_seguro = lambda texto: pipeline(texto) if isinstance(texto, str) else []

# Ejemplo de uso
texto_ejemplo = "¡Hola! Este es un texto de prueba con palabras cortas y largas..."
resultado = procesar_texto_seguro(texto_ejemplo)
print("Resultado del pipeline:", resultado)

# Manejo de casos especiales
textos_prueba = [
    "¡Hola Mundo!",
    None,
    123,
    "   Espacios   extra   y   símbolos   !!!   ",
]

for texto in textos_prueba:
    print(f"Procesando: {texto}")
    print(f"Resultado: {procesar_texto_seguro(texto)}")
