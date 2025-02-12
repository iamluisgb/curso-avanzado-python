# Closures en Python

## 1. Closures

### 1.1 Introducción

Un closure (o clausura) es una función que recuerda los valores del entorno donde fue creada, incluso cuando ese entorno ya no está disponible en el código. En otras palabras, es una función que tiene acceso a variables en su ámbito exterior incluso después de que la función exterior haya terminado de ejecutarse.

Para entender los closures, primero necesitamos comprender tres conceptos fundamentales:

1. Las funciones son objetos en Python
2. Podemos definir funciones dentro de otras funciones
3. Las funciones pueden acceder a variables definidas en funciones que las contienen

### 1.2 Funciones Anidadas y Ámbito

Veamos un ejemplo simple para entender cómo funcionan las funciones anidadas:

```python
def funcion_exterior(mensaje):
    def funcion_interior():
        print(mensaje)

    funcion_interior()

funcion_exterior("Hola mundo")  # Imprime: Hola mundo

```

En este ejemplo, `funcion_interior` puede acceder a la variable `mensaje` que está definida en `funcion_exterior`. Esto se llama ámbito léxico: una función puede acceder a variables definidas en el ámbito que la contiene.

### 1.3 Creando un Closure

Para crear un closure, necesitamos devolver la función interior:

```python
def crear_multiplicador(x):
    def multiplicador(n):
        return x * n
    return multiplicador

# Creamos dos multiplicadores diferentes
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

# Los usamos
print(duplicar(5))   # Imprime: 10
print(triplicar(5))  # Imprime: 15

```

Lo fascinante aquí es que `duplicar` y `triplicar` son funciones que "recuerdan" el valor de `x` con el que fueron creadas, incluso después de que `crear_multiplicador` haya terminado su ejecución.

### 1.4 Verificando Closures

Python nos permite verificar si una función es un closure y qué variables recuerda:

```python
def crear_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

# Creamos un contador
mi_contador = crear_contador()

# Verificamos las variables libres (las que el closure recuerda)
print(mi_contador.__closure__)  # Muestra la celda de memoria
print(mi_contador.__code__.co_freevars)  # Muestra los nombres de las variables

# Usamos el contador
print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3

```

### 1.5 Casos de Uso Prácticos

Los closures son especialmente útiles en varios escenarios:

1. **Encapsulación de estado**:

```python
def crear_cuenta_bancaria(saldo_inicial):
    def depositar(cantidad):
        nonlocal saldo_inicial
        saldo_inicial += cantidad
        return saldo_inicial

    def retirar(cantidad):
        nonlocal saldo_inicial
        if cantidad <= saldo_inicial:
            saldo_inicial -= cantidad
            return True
        return False

    def consultar_saldo():
        return saldo_inicial

    return {
        'depositar': depositar,
        'retirar': retirar,
        'consultar': consultar_saldo
    }

# Uso
mi_cuenta = crear_cuenta_bancaria(1000)
mi_cuenta['depositar'](500)
mi_cuenta['retirar'](200)
print(mi_cuenta['consultar']())  # 1300

```

1. **Configuración de funciones**:

```python
def crear_formateador(prefijo):
    def formatear(texto):
        return f"{prefijo}: {texto}"
    return formatear

log_error = crear_formateador("ERROR")
log_info = crear_formateador("INFO")

print(log_error("Algo salió mal"))  # ERROR: Algo salió mal
print(log_info("Operación exitosa"))  # INFO: Operación exitosa

```

### 1.6 La Palabra Clave nonlocal

Cuando necesitamos modificar una variable de un ámbito exterior (no global), usamos `nonlocal`:

```python
def crear_acumulador():
    total = 0
    def acumular(valor):
        nonlocal total  # Sin esto, tendríamos un error
        total += valor
        return total
    return acumular

sumar = crear_acumulador()
print(sumar(5))  # 5
print(sumar(3))  # 8
print(sumar(2))  # 10

```

### 1.7 Closures vs Clases

Los closures pueden ser una alternativa más ligera a las clases cuando solo necesitamos mantener algún estado simple:

```python
# Usando closure
def crear_contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

# Usando clase
class Contador:
    def __init__(self):
        self.count = 0

    def incrementar(self):
        self.count += 1
        return self.count

# Ambos funcionan de manera similar
contador_closure = crear_contador()
contador_clase = Contador()

print(contador_closure())  # 1
print(contador_clase.incrementar())  # 1

```

## 2. Ejercicios Propuestos

### 2.1 Ejercicio Básico: Generador de Saludos Personalizados

**Descripción**: Crea un sistema de saludos personalizados utilizando closures. La función exterior debe recibir un idioma y devolver una función que genere saludos en ese idioma. Los saludos deben variar según la hora del día (mañana, tarde, noche).

**Requisitos**:

1. Soportar al menos tres idiomas (español, inglés, francés)
2. Distinguir entre diferentes momentos del día
3. Permitir personalizar el nombre de la persona a saludar

**Ejemplo de uso deseado**:

```python
saludar_es = crear_saludador("español")
saludar_en = crear_saludador("inglés")

print(saludar_es("Juan", "mañana"))  # ¡Buenos días, Juan!
print(saludar_en("John", "noche"))   # Good night, John!

```

### 2.2 Ejercicio Intermedio: Sistema de Descuentos por Cliente

**Descripción**: Implementa un sistema de descuentos para una tienda utilizando closures. El sistema debe permitir crear diferentes funciones de descuento basadas en el tipo de cliente (normal, VIP, premium) y las características de la compra.

**Requisitos**:

1. Crear descuentos basados en el tipo de cliente
2. Aplicar descuentos adicionales por volumen de compra
3. Permitir descuentos especiales en días específicos
4. Validar que el descuento no exceda un máximo permitido

**Ejemplo de uso deseado**:

```python
descuento_vip = crear_descuento("VIP", descuento_base=20)
descuento_normal = crear_descuento("normal", descuento_base=5)

print(descuento_vip(1000))  # Calcula descuento VIP para compra de 1000
print(descuento_normal(500))  # Calcula descuento normal para compra de 500

```

### 2.3 Ejercicio Avanzado: Sistema de Validación de Datos

**Descripción**: Desarrolla un sistema de validación flexible utilizando closures que permita crear validadores personalizados para diferentes tipos de datos y reglas de negocio. El sistema debe poder encadenar múltiples reglas de validación y proporcionar mensajes de error detallados.

**Requisitos**:

1. Crear validadores para diferentes tipos de datos (strings, números, emails, etc.)
2. Permitir establecer reglas personalizadas (longitud, rango, formato, etc.)
3. Combinar múltiples reglas de validación
4. Generar mensajes de error descriptivos
5. Mantener un registro de las validaciones realizadas

**Ejemplo de uso deseado**:

```python
validar_email = crear_validador("email", min_length=5, dominio_permitido="empresa.com")
validar_edad = crear_validador("numero", min_valor=18, max_valor=99)

print(validar_email("usuario@empresa.com"))  # True
print(validar_edad(25))  # True

```

## 4. Solución de Ejercicios

### 4.1 Solución: Generador de Saludos Personalizados

```python
from datetime import datetime

def crear_saludador(idioma):
    """
    Crea un generador de saludos en el idioma especificado.
    """
    # Definimos los saludos para cada idioma y momento del día
    saludos = {
        "español": {
            "mañana": "¡Buenos días",
            "tarde": "¡Buenas tardes",
            "noche": "¡Buenas noches"
        },
        "inglés": {
            "mañana": "Good morning",
            "tarde": "Good afternoon",
            "noche": "Good night"
        },
        "francés": {
            "mañana": "Bonjour",
            "tarde": "Bon après-midi",
            "noche": "Bonne nuit"
        }
    }

    def determinar_momento():
        """Determina el momento del día basado en la hora actual."""
        hora = datetime.now().hour
        if 5 <= hora < 12:
            return "mañana"
        elif 12 <= hora < 20:
            return "tarde"
        else:
            return "noche"

    def saludar(nombre, momento=None):
        """Genera un saludo personalizado."""
        if momento is None:
            momento = determinar_momento()

        if idioma not in saludos:
            return f"Idioma {idioma} no soportado"

        saludo_base = saludos[idioma][momento]

        # Añadimos la puntuación según el idioma
        if idioma == "español":
            return f"{saludo_base}, {nombre}!"
        else:
            return f"{saludo_base}, {nombre}"

    return saludar

# Ejemplo de uso
saludar_es = crear_saludador("español")
saludar_en = crear_saludador("inglés")
saludar_fr = crear_saludador("francés")

print(saludar_es("Juan", "mañana"))
print(saludar_en("John", "noche"))
print(saludar_fr("Pierre"))  # Usa el momento actual del día

```

### 4.2 Solución: Sistema de Descuentos por Cliente

```python
def crear_descuento(tipo_cliente, descuento_base):
    """
    Crea una función de descuento personalizada según el tipo de cliente.
    """
    # Configuración de descuentos adicionales
    descuentos_volumen = {
        500: 5,    # 5% extra para compras mayores a 500
        1000: 10,  # 10% extra para compras mayores a 1000
        5000: 15   # 15% extra para compras mayores a 5000
    }

    # Límites de descuento por tipo de cliente
    limites_descuento = {
        "normal": 25,
        "VIP": 40,
        "premium": 50
    }

    def calcular_descuento_adicional(monto):
        """Calcula el descuento adicional por volumen de compra."""
        for limite, descuento in sorted(descuentos_volumen.items(), reverse=True):
            if monto >= limite:
                return descuento
        return 0

    def aplicar_descuento(monto, es_dia_especial=False):
        """Calcula el descuento total a aplicar."""
        # Descuento base según tipo de cliente
        descuento_total = descuento_base

        # Añadir descuento por volumen
        descuento_total += calcular_descuento_adicional(monto)

        # Descuento adicional en días especiales
        if es_dia_especial:
            descuento_total += 5

        # Aplicar límite según tipo de cliente
        limite = limites_descuento.get(tipo_cliente, 25)
        descuento_total = min(descuento_total, limite)

        # Calcular monto final
        monto_descuento = (monto * descuento_total) / 100
        monto_final = monto - monto_descuento

        return {
            "descuento_porcentaje": descuento_total,
            "monto_descuento": monto_descuento,
            "monto_final": monto_final
        }

    return aplicar_descuento

# Ejemplo de uso
descuento_vip = crear_descuento("VIP", 20)
descuento_normal = crear_descuento("normal", 5)

print(descuento_vip(1000))
print(descuento_normal(500))

```

### 4.3 Solución: Sistema de Validación de Datos

```python
import re
from typing import Any, Callable, List, Dict

def crear_validador(tipo: str, **config):
    """
    Crea un validador personalizado según el tipo y configuración.
    """
    # Registro de validaciones para debugging
    registro_validaciones: List[Dict[str, Any]] = []

    # Funciones auxiliares de validación
    def validar_email(valor: str) -> tuple[bool, str]:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}
        if not re.match(patron, valor):
            return False, "Formato de email inválido"
        if 'dominio_permitido' in config:
            if not valor.endswith(config['dominio_permitido']):
                return False, f"El email debe pertenecer al dominio {config['dominio_permitido']}"
        return True, "Email válido"

    def validar_numero(valor: int) -> tuple[bool, str]:
        if not isinstance(valor, (int, float)):
            return False, "El valor debe ser un número"
        if 'min_valor' in config and valor < config['min_valor']:
            return False, f"El valor debe ser mayor o igual a {config['min_valor']}"
        if 'max_valor' in config and valor > config['max_valor']:
            return False, f"El valor debe ser menor o igual a {config['max_valor']}"
        return True, "Número válido"

    def validar_texto(valor: str) -> tuple[bool, str]:
        if not isinstance(valor, str):
            return False, "El valor debe ser texto"
        if 'min_length' in config and len(valor) < config['min_length']:
            return False, f"El texto debe tener al menos {config['min_length']} caracteres"
        if 'max_length' in config and len(valor) > config['max_length']:
            return False, f"El texto debe tener máximo {config['max_length']} caracteres"
        return True, "Texto válido"

    # Seleccionar el tipo de validación
    validadores = {
        "email": validar_email,
        "numero": validar_numero,
        "texto": validar_texto
    }

    validador = validadores.get(tipo)
    if not validador:
        raise ValueError(f"Tipo de validador no soportado: {tipo}")

    def validar(valor: Any) -> bool:
        """Función de validación que será retornada."""
        resultado, mensaje = validador(valor)

        # Registrar la validación
        registro_validaciones.append({
            "tipo": tipo,
            "valor": valor,
            "resultado": resultado,
            "mensaje": mensaje,
            "config": config
        })

        return resultado

    # Añadir acceso al registro
    validar.obtener_registro = lambda: registro_validaciones

    return validar

# Ejemplo de uso
validar_email = crear_validador("email", dominio_permitido="empresa.com")
validar_edad = crear_validador("numero", min_valor=18, max_valor=99)
validar_nombre = crear_validador("texto", min_length=2, max_length=50)

# Probamos las validaciones
print(validar_email("usuario@empresa.com"))  # True
print(validar_edad(25))  # True
print(validar_nombre("Ana"))  # True

# Verificamos el registro de validaciones
print(validar_email.obtener_registro())

```

## 3. Relación con Decoradores

Los closures son la base fundamental para entender los decoradores en Python. Un decorador es esencialmente un closure que envuelve una función y puede modificar su comportamiento. Cuando aprendemos sobre decoradores, estamos realmente aplicando los conceptos de closures de una manera más especializada.

La principal diferencia es que mientras un closure típico crea una nueva función con algún estado "recordado", un decorador específicamente modifica o aumenta el comportamiento de una función existente.

Este concepto nos lleva naturalmente al siguiente tema: los decoradores, donde aplicaremos todo lo que hemos aprendido sobre closures de una manera más específica y poderosa.

## 4. Recursos Adicionales

### **Documentación Oficial**
- [Python Documentation - Nested Scopes](https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example)
- [Python Glossary - Closure](https://docs.python.org/3/glossary.html#term-closure)

### **Artículos Relacionados**
- [Real Python - Understanding Python Closures](https://realpython.com/inner-functions-what-are-they-good-for/#understanding-python-closures)
- [Towards Data Science - Python Closures Explained](https://towardsdatascience.com/python-closures-explained-with-examples-2f0dabd5dbd8)
- [Geeks for Geeks - Closures in Python](https://www.geeksforgeeks.org/python-closures/)
- [Mathspp - Python Closures and How They Work](https://mathspp.com/blog/pydonts/closures)
- [Código Facilito - Closures en Python](https://codigofacilito.com/articulos/closures-python)

### **Videos Recomendados**
- [Corey Schafer - Python Closures](https://www.youtube.com/watch?v=swU3c34d2NQ)
- [Programming with Mosh - Python Closures Explained](https://www.youtube.com/watch?v=3lKtwvlSxak)
- [Python Engineer - Closures in Python](https://www.youtube.com/watch?v=y6sYGhHKB4A)

