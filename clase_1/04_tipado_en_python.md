# Tipado  en Python

## 1. Introducción

### 1.1 Definición

El tipado estático en Python es una característica introducida a partir de Python 3.5 que permite declarar explícitamente los tipos de datos que una función espera recibir y retornar, así como los tipos de las variables. A diferencia del tipado dinámico tradicional de Python, el tipado estático ayuda a detectar errores de tipo en tiempo de desarrollo, mejora la documentación del código y facilita el mantenimiento de aplicaciones grandes.

### 1.2 Fundamentos Clave

El tipado estático en Python se construye sobre varios conceptos fundamentales que trabajan en conjunto para proporcionar un sistema de tipos robusto:

1. **Anotaciones de Tipo**: Permiten especificar el tipo esperado de variables, parámetros y valores de retorno.
2. **Verificación de Tipos**: Aunque Python no verifica los tipos en tiempo de ejecución por defecto, herramientas como mypy pueden realizar verificaciones estáticas.
3. **Type Hints**: El módulo `typing` proporciona tipos especiales como `List`, `Dict`, `Optional`, etc., que permiten expresar tipos más complejos.

### 1.3 Tipado Dinámico y Fuerte en Python

Python es un lenguaje de **tipado dinámico**, lo que significa que el tipo de una variable puede cambiar en tiempo de ejecución. Por ejemplo, una variable puede ser inicialmente un entero y luego asignársele una cadena sin generar errores. Además, Python es de **tipado fuerte**, es decir, no permite operaciones entre tipos incompatibles sin una conversión explícita; intentar sumar un entero y una cadena resultará en un error.

Aunque Python es dinámico por naturaleza, a partir de la versión 3.5 se introdujeron las **anotaciones de tipo** que permiten especificar el tipo de las variables y funciones. Estas anotaciones no son verificadas en tiempo de ejecución por el intérprete, pero herramientas como `mypy` o `Pyre` pueden usarlas para realizar comprobaciones estáticas y detectar posibles errores antes de ejecutar el código.

### 1.4 Introducción a `typing` y `mypy`

Para facilitar el tipado estático en Python, se introdujo el módulo `typing`, que proporciona herramientas para definir tipos explícitos en el código. Algunas de sus características más importantes incluyen:

- Tipos genéricos como `List`, `Dict`, `Tuple`, `Set`, entre otros.
- `Optional`, que permite indicar que una variable puede ser de un tipo específico o `None`.
- `Union`, que permite definir múltiples tipos para una misma variable.

Por otro lado, `mypy` es una herramienta que permite analizar el código de Python y detectar errores de tipado antes de la ejecución. Se ejecuta como una verificación estática independiente y ayuda a mantener el código más robusto y seguro. Su uso es simple, y se puede ejecutar con:

```
mypy script.py

```

Esto analizará el archivo `script.py` y reportará posibles errores de tipado según las anotaciones proporcionadas.

### 1.5 TypedDict: Diccionarios con Tipos Definidos

TypedDict es una característica especial del módulo `typing` que permite definir diccionarios con tipos específicos para sus claves. A diferencia de los diccionarios normales, TypedDict garantiza que todas las claves tengan tipos definidos y consistentes.

### Sintaxis Básica

```python
from typing import TypedDict

class Usuario(TypedDict):
    nombre: str
    edad: int
    activo: bool

```

### Características Principales

1. **Definición de Estructura**:

```python
# Definición básica
class ConfiguracionDB(TypedDict):
    host: str
    puerto: int
    usuario: str
    contraseña: str
    max_conexiones: int

# Uso
config: ConfiguracionDB = {
    "host": "localhost",
    "puerto": 5432,
    "usuario": "admin",
    "contraseña": "secreto",
    "max_conexiones": 100
}

```

1. **Campos Opcionales**:

```python
from typing import TypedDict, NotRequired

class Producto(TypedDict):
    id: int                    # Campo requerido
    nombre: str                # Campo requerido
    descripcion: NotRequired[str]  # Campo opcional
    precio: float              # Campo requerido
    stock: NotRequired[int]    # Campo opcional

# Uso válido
producto: Producto = {
    "id": 1,
    "nombre": "Laptop",
    "precio": 999.99
}

```

1. **Herencia**:

```python
class PersonaBase(TypedDict):
    nombre: str
    apellido: str

class Empleado(PersonaBase):
    id_empleado: int
    departamento: str
    salario: float

# Uso
empleado: Empleado = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "id_empleado": 12345,
    "departamento": "IT",
    "salario": 50000.0
}

```

### Casos de Uso Comunes

1. **Configuraciones**:

```python
class ConfiguracionApp(TypedDict):
    debug: bool
    log_level: str
    max_usuarios: int
    tiempo_sesion: int
    rutas_permitidas: list[str]

config: ConfiguracionApp = {
    "debug": True,
    "log_level": "INFO",
    "max_usuarios": 1000,
    "tiempo_sesion": 3600,
    "rutas_permitidas": ["/api", "/web"]
}

```

1. **Respuestas API**:

```python
class ErrorResponse(TypedDict):
    codigo: int
    mensaje: str
    detalles: NotRequired[str]

class SuccessResponse(TypedDict):
    datos: dict
    timestamp: str
    status: str

# Uso en una función
def procesar_respuesta(exito: bool) -> ErrorResponse | SuccessResponse:
    if not exito:
        return {
            "codigo": 404,
            "mensaje": "Recurso no encontrado"
        }
    return {
        "datos": {"resultado": "ok"},
        "timestamp": "2024-02-09T12:00:00",
        "status": "success"
    }

```

1. **Estructuras de Datos Complejas**:

```python
class Direccion(TypedDict):
    calle: str
    ciudad: str
    codigo_postal: str
    pais: str

class ContactoEmergencia(TypedDict):
    nombre: str
    telefono: str
    relacion: str

class Empleado(TypedDict):
    id: int
    nombre: str
    departamento: str
    direccion: Direccion
    contacto_emergencia: ContactoEmergencia
    fecha_ingreso: str
    salario: float
    activo: bool

# Uso
empleado: Empleado = {
    "id": 1,
    "nombre": "Ana García",
    "departamento": "Ventas",
    "direccion": {
        "calle": "Calle Principal 123",
        "ciudad": "Madrid",
        "codigo_postal": "28001",
        "pais": "España"
    },
    "contacto_emergencia": {
        "nombre": "Juan García",
        "telefono": "555-0123",
        "relacion": "Hermano"
    },
    "fecha_ingreso": "2024-01-15",
    "salario": 45000.0,
    "activo": True
}

```

### Ventajas y Consideraciones

1. **Ventajas**:
    - Documentación clara de la estructura de datos
    - Detección temprana de errores de tipo
    - Mejor autocompletado en IDEs
    - Facilita el mantenimiento del código
2. **Consideraciones**:
    - Los tipos son verificados solo en tiempo de desarrollo
    - No hay validación en tiempo de ejecución
    - Todos los campos deben tener tipos definidos
    - Los campos requeridos deben estar presentes
3. **Mejores Prácticas**:

```python
from typing import TypedDict, NotRequired, Literal

# Usar tipos literales para valores específicos
class ConfiguracionLog(TypedDict):
    nivel: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    formato: str
    archivo: NotRequired[str]

# Combinar con otros tipos
from datetime import datetime
class Registro(TypedDict):
    id: int
    timestamp: datetime
    tipo: Literal["entrada", "salida"]
    detalles: NotRequired[dict[str, str]]

# Documentar estructuras complejas
class TransaccionBancaria(TypedDict):
    """
    Representa una transacción bancaria.

    Fields:
        id: Identificador único de la transacción
        monto: Cantidad de la transacción
        tipo: Tipo de transacción (débito/crédito)
        fecha: Fecha y hora de la transacción
        estado: Estado actual de la transacción
    """
    id: str
    monto: float
    tipo: Literal["debito", "credito"]
    fecha: datetime
    estado: Literal["pendiente", "completada", "fallida"]

```

### Integración con mypy

TypedDict se integra perfectamente con mypy para la verificación de tipos:

```python
# archivo: transacciones.py
from typing import TypedDict

class Transaccion(TypedDict):
    id: int
    monto: float

def procesar_transaccion(t: Transaccion) -> None:
    print(f"Procesando transacción {t['id']} por {t['monto']}")

# Este código generará un error en mypy
transaccion = {  # type: Transaccion
    "id": "123",  # Error: tipo incorrecto
    "monto": 100.0
}

```

Al ejecutar mypy:

```bash
$ mypy transacciones.py
transacciones.py:12: error: Dict entry "id" has incompatible type "str"; expected "int"

```

## 2. Código de Demostración

### 2.1 Ejemplo Básico

```python
#IDs de empleados
id1: int = 101
id2: int = 102

#Sumar los IDs
total_id: int = id1 + id2

#Mostrar resultado
print(total_id)
```

```python
def add_employee_ids(id1: int, id2:int) -> int:
	return id1+id2

print(add_employee_ids(201,202))
```

```python
class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola, me llamo {self.name}, tengo {self.age}"

employee1 = Employee('Carlos', 30, 3500.0)
print(employee1.introduce())
```

```python
from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None
```

```python
from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)
```

```python
# Título: Implementación básica de tipado estático
# Objetivo: Demostrar el uso fundamental de type hints

from typing import List, Dict, Optional, Union
from datetime import datetime

class GestorInventario:
    """
    Clase que demuestra el uso de tipado estático en Python.
    """

    def __init__(self) -> None:
        # Anotaciones de tipo para atributos de clase
        self.productos: Dict[str, int] = {}
        self.ultimo_inventario: Optional[datetime] = None

    def agregar_producto(
        self,
        codigo: str,
        cantidad: int,
        precio: float = 0.0
    ) -> bool:
        """
        Agrega un producto al inventario.

        Args:
            codigo: Identificador único del producto
            cantidad: Cantidad a agregar
            precio: Precio unitario del producto

        Returns:
            bool: True si se agregó correctamente
        """
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero positivo")

        if codigo in self.productos:
            self.productos[codigo] += cantidad
        else:
            self.productos[codigo] = cantidad

        self.ultimo_inventario = datetime.now()
        return True

    def obtener_stock(
        self,
        codigo: str
    ) -> Optional[int]:
        """
        Obtiene el stock de un producto.

        Args:
            codigo: Identificador del producto

        Returns:
            Optional[int]: Cantidad en stock o None si no existe
        """
        return self.productos.get(codigo)

    def listar_productos_bajos(
        self,
        umbral: int = 5
    ) -> List[str]:
        """
        Lista productos con stock bajo.

        Args:
            umbral: Cantidad mínima considerada como stock bajo

        Returns:
            List[str]: Códigos de productos con stock bajo
        """
        return [
            codigo
            for codigo, cantidad in self.productos.items()
            if cantidad < umbral
        ]

```

### 2.2 Ejemplo en Colab

```python
!pip install mypy
```

```python
%%writefile callable_example.py
from typing import Callable

def multiply(x: float, y: float) -> float:
    return x * y

def multiply_then_divide_by_two(multiply_func: Callable[[float, float], float], x: float, y: float) -> float:
    return multiply_func(x, y) / 2

res = multiply_then_divide_by_two(multiply, 2, 3)
```

```python
!mypy callable_example.py
```

### 2.3 Notas para el Instructor

- **Puntos clave a enfatizar:**
    1. La importancia de importar tipos específicos del módulo `typing`
    2. El uso de `>` para indicar el tipo de retorno
    3. La diferencia entre tipos simples y compuestos
    4. El uso de `Optional` para valores que pueden ser None
- **Posibles preguntas de los estudiantes:**
    1. "¿Por qué usar tipado estático si Python es dinámico?"
    2. "¿Cómo afecta el rendimiento el tipado estático?"
    3. "¿Cuándo usar `Union` vs `Optional`?"
- **Errores comunes a prevenir:**
    1. Olvidar importar tipos del módulo `typing`
    2. Confundir tipos básicos con sus equivalentes de `typing`
    3. No manejar correctamente los casos de `None`

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real 1: API REST

**Contexto**: Desarrollo de una API REST con tipado estático

```python
from typing import TypedDict, List, Optional
from datetime import datetime

class Usuario(TypedDict):
    """
    Define la estructura de un usuario usando TypedDict.
    """
    id: int
    nombre: str
    email: str
    fecha_registro: datetime
    ultima_sesion: Optional[datetime]

class APIUsuarios:
    def __init__(self) -> None:
        self.usuarios: List[Usuario] = []

    def crear_usuario(
        self,
        nombre: str,
        email: str
    ) -> Usuario:
        """
        Crea un nuevo usuario.

        Args:
            nombre: Nombre del usuario
            email: Email del usuario

        Returns:
            Usuario: Datos del usuario creado
        """
        nuevo_usuario: Usuario = {
            'id': len(self.usuarios) + 1,
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'ultima_sesion': None
        }

        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def buscar_por_email(
        self,
        email: str
    ) -> Optional[Usuario]:
        """
        Busca un usuario por su email.

        Args:
            email: Email a buscar

        Returns:
            Optional[Usuario]: Usuario encontrado o None
        """
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None

```

### 3.2 Caso de Uso Real 2: Procesamiento de Datos

**Contexto**: Sistema de procesamiento de datos con tipos genéricos

```python
from typing import TypeVar, Generic, Sequence, Callable

T = TypeVar('T')
R = TypeVar('R')

class Procesador(Generic[T, R]):
    """
    Procesador genérico de datos con tipado estático.
    """

    def __init__(
        self,
        transformacion: Callable[[T], R]
    ) -> None:
        self.transformacion = transformacion
        self.datos_procesados: List[R] = []

    def procesar_lote(
        self,
        datos: Sequence[T]
    ) -> List[R]:
        """
        Procesa una secuencia de datos.

        Args:
            datos: Secuencia de datos a procesar

        Returns:
            List[R]: Resultados procesados
        """
        resultados = [
            self.transformacion(dato)
            for dato in datos
        ]
        self.datos_procesados.extend(resultados)
        return resultados

# Ejemplo de uso con tipos específicos
def duplicar_numero(x: int) -> int:
    return x * 2

procesador_numeros = Procesador[int, int](duplicar_numero)
resultados = procesador_numeros.procesar_lote([1, 2, 3, 4])

```

## 4. Ejercicios Propuestos

### 4.1: Sistema de Gestión de Biblioteca (Nivel Básico)

**Código Original**

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False
        self.fecha_prestamo = None

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.prestamos = []

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            return True
        return False

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if not libro.prestado:
                libro.prestado = True
                libro.fecha_prestamo = obtener_fecha_actual()
                self.prestamos.append({
                    'libro': libro,
                    'usuario': usuario,
                    'fecha': libro.fecha_prestamo
                })
                return True
        return False

    def devolver_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if libro.prestado:
                libro.prestado = False
                libro.fecha_prestamo = None
                return True
        return False

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio, None) == valor:
                resultados.append(libro)
        return resultados

def obtener_fecha_actual():
    from datetime import datetime
    return datetime.now()

```

### Tarea

Tu tarea es convertir este código a una versión con tipado estático. Deberás:

1. Importar los tipos necesarios del módulo `typing`
2. Agregar anotaciones de tipo a:
    - Atributos de clase
    - Parámetros de métodos
    - Valores de retorno
3. Crear tipos personalizados si es necesario
4. Utilizar `Optional` donde corresponda

### Pistas

- Considera qué tipos necesitarás para representar fechas
- Piensa en cómo representar el diccionario de libros y la lista de préstamos
- La función `getattr` puede recibir diferentes tipos de atributos

### 4.2: Procesador de Datos CSV (Nivel Intermedio)

Código Original

```python
class ProcesadorCSV:
    def __init__(self, separador=','):
        self.separador = separador
        self.cabeceras = None
        self.datos = []
        self.resumen_estadistico = {}

    def cargar_archivo(self, ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if lineas:
                self.cabeceras = lineas[0].strip().split(self.separador)
                for linea in lineas[1:]:
                    valores = linea.strip().split(self.separador)
                    if len(valores) == len(self.cabeceras):
                        self.datos.append(dict(zip(self.cabeceras, valores)))

    def filtrar_datos(self, columna, valor):
        return [fila for fila in self.datos if fila.get(columna) == valor]

    def calcular_estadisticas(self, columna):
        valores = []
        for fila in self.datos:
            try:
                valor = float(fila.get(columna, 0))
                valores.append(valor)
            except ValueError:
                continue

        if valores:
            self.resumen_estadistico[columna] = {
                'minimo': min(valores),
                'maximo': max(valores),
                'promedio': sum(valores) / len(valores),
                'total': sum(valores)
            }
            return self.resumen_estadistico[columna]
        return None

    def exportar_resultados(self, ruta_salida, datos_filtrados):
        with open(ruta_salida, 'w') as archivo:
            if datos_filtrados and self.cabeceras:
                archivo.write(self.separador.join(self.cabeceras) + '\\n')
                for fila in datos_filtrados:
                    valores = [str(fila.get(cab, '')) for cab in self.cabeceras]
                    archivo.write(self.separador.join(valores) + '\\n')

```

### Tarea

Convierte este procesador CSV a una versión con tipado estático. Deberás:

1. Definir tipos personalizados para las estructuras de datos usadas
2. Agregar anotaciones de tipo a todos los métodos
3. Manejar correctamente los casos opcionales
4. Considerar el manejo de errores en la conversión de tipos

### Pistas

- Usa `TypedDict` para representar las filas de datos
- Considera usar `Path` de `pathlib` para las rutas de archivo
- Piensa en cómo manejar los valores que pueden ser numéricos o texto

### 4.3: Sistema de Comercio Electrónico (Nivel Avanzado)

Código Original

```python
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Carrito:
    def __init__(self):
        self.items = {}
        self.total = 0

    def agregar_item(self, producto, cantidad):
        if cantidad <= producto.stock:
            if producto.codigo in self.items:
                self.items[producto.codigo]['cantidad'] += cantidad
            else:
                self.items[producto.codigo] = {
                    'producto': producto,
                    'cantidad': cantidad
                }
            self.total += producto.precio * cantidad
            producto.stock -= cantidad
            return True
        return False

    def remover_item(self, codigo_producto):
        if codigo_producto in self.items:
            item = self.items[codigo_producto]
            item['producto'].stock += item['cantidad']
            self.total -= item['producto'].precio * item['cantidad']
            del self.items[codigo_producto]
            return True
        return False

class SistemaVentas:
    def __init__(self):
        self.productos = {}
        self.ventas = []
        self.carritos_activos = {}

    def registrar_producto(self, producto):
        if producto.codigo not in self.productos:
            self.productos[producto.codigo] = producto
            return True
        return False

    def crear_carrito(self, id_cliente):
        if id_cliente not in self.carritos_activos:
            self.carritos_activos[id_cliente] = Carrito()
            return self.carritos_activos[id_cliente]
        return None

    def procesar_venta(self, id_cliente):
        if id_cliente in self.carritos_activos:
            carrito = self.carritos_activos[id_cliente]
            if carrito.items:
                venta = {
                    'id_cliente': id_cliente,
                    'items': carrito.items.copy(),
                    'total': carrito.total,
                    'fecha': obtener_fecha_actual()
                }
                self.ventas.append(venta)
                del self.carritos_activos[id_cliente]
                return venta
        return None

```

### Tarea

Convierte este sistema de comercio electrónico a una versión con tipado estático completo. Deberás:

1. Definir tipos personalizados para todas las estructuras de datos
2. Implementar el tipado estático en las tres clases
3. Manejar correctamente las relaciones entre clases
4. Considerar el uso de genéricos si es apropiado

### Pistas

- Usa `TypedDict` para estructuras de datos complejas
- Considera usar `Decimal` para valores monetarios
- Piensa en cómo representar las relaciones entre Producto, Carrito y Venta
- Define tipos personalizados para las estructuras de venta

### Nota importante para todos los ejercicios

Para cada ejercicio, asegúrate de:

1. Verificar tu código con mypy: `mypy --strict tu_script.py`
2. Documentar los tipos complejos que definas
3. Mantener la funcionalidad original del código intacta
4. Considerar casos límite y manejo de errores

## 5. Recursos Adicionales

- **Documentación oficial**:
    - PEP 484 - Type Hints
    - Python typing module
    - El Libro de Python: https://ellibrodepython.com/function-annotations
    - https://dev.to/leolas95/tipado-estatico-y-dinamico-tipado-fuerte-y-debil-133n
    - https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- **Herramientas**:
    - mypy
    - pytype
    - pyre

## 6. Solución de Ejercicios

### 6.1: Sistema de Gestión de Biblioteca

Comencemos analizando cómo convertir el sistema de biblioteca a una versión con tipado estático. La clave está en identificar claramente los tipos de datos que fluyen a través del sistema.

```python
from typing import Dict, List, Optional, TypedDict
from datetime import datetime

# Definimos un tipo personalizado para los préstamos usando TypedDict
class RegistroPrestamo(TypedDict):
    """
    Estructura que representa un registro de préstamo.
    """
    libro: 'Libro'  # Usamos string para evitar referencias circulares
    usuario: str
    fecha: datetime

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """
    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str
    ) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.isbn: str = isbn
        self.prestado: bool = False
        self.fecha_prestamo: Optional[datetime] = None

class Biblioteca:
    """
    Sistema de gestión de biblioteca con tipado estático.
    """
    def __init__(self) -> None:
        # Especificamos los tipos de las estructuras de datos
        self.libros: Dict[str, Libro] = {}
        self.prestamos: List[RegistroPrestamo] = []

    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un nuevo libro al inventario.

        Args:
            libro: Instancia de Libro a agregar

        Returns:
            bool: True si se agregó correctamente, False si ya existía
        """
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            return True
        return False

    def prestar_libro(self, isbn: str, usuario: str) -> bool:
        """
        Registra el préstamo de un libro.

        Args:
            isbn: Identificador único del libro
            usuario: Nombre o identificador del usuario

        Returns:
            bool: True si el préstamo fue exitoso
        """
        if isbn in self.libros:
            libro = self.libros[isbn]
            if not libro.prestado:
                libro.prestado = True
                libro.fecha_prestamo = obtener_fecha_actual()

                # Creamos el registro de préstamo con el tipo correcto
                prestamo: RegistroPrestamo = {
                    'libro': libro,
                    'usuario': usuario,
                    'fecha': libro.fecha_prestamo
                }
                self.prestamos.append(prestamo)
                return True
        return False

    def devolver_libro(self, isbn: str) -> bool:
        """
        Registra la devolución de un libro.

        Args:
            isbn: Identificador único del libro

        Returns:
            bool: True si la devolución fue exitosa
        """
        if isbn in self.libros:
            libro = self.libros[isbn]
            if libro.prestado:
                libro.prestado = False
                libro.fecha_prestamo = None
                return True
        return False

    def buscar_libros(
        self,
        criterio: str,
        valor: str
    ) -> List[Libro]:
        """
        Busca libros según un criterio específico.

        Args:
            criterio: Campo por el cual buscar
            valor: Valor a buscar

        Returns:
            List[Libro]: Lista de libros que coinciden con el criterio
        """
        resultados: List[Libro] = []
        for libro in self.libros.values():
            if getattr(libro, criterio, None) == valor:
                resultados.append(libro)
        return resultados

def obtener_fecha_actual() -> datetime:
    """
    Obtiene la fecha y hora actual.

    Returns:
        datetime: Fecha y hora actual
    """
    return datetime.now()

```

### 6.2: Procesador de Datos CSV

Para el procesador CSV, necesitamos manejar diferentes tipos de datos y considerar las estructuras de datos complejas que se utilizan para almacenar la información.

```python
from typing import Dict, List, Optional, TypedDict, Union
from pathlib import Path
import csv
from decimal import Decimal

# Definimos tipos personalizados para nuestras estructuras de datos
class EstadisticasColumna(TypedDict):
    """
    Estadísticas calculadas para una columna numérica.
    """
    minimo: float
    maximo: float
    promedio: float
    total: float

# Tipo para una fila de datos, que puede contener strings o números
FilaCSV = Dict[str, Union[str, float]]

class ProcesadorCSV:
    """
    Procesador de archivos CSV con tipado estático.
    """
    def __init__(self, separador: str = ',') -> None:
        self.separador: str = separador
        self.cabeceras: Optional[List[str]] = None
        self.datos: List[FilaCSV] = []
        self.resumen_estadistico: Dict[str, EstadisticasColumna] = {}

    def cargar_archivo(self, ruta_archivo: Union[str, Path]) -> None:
        """
        Carga y procesa un archivo CSV.

        Args:
            ruta_archivo: Ruta al archivo CSV
        """
        ruta = Path(ruta_archivo)
        with ruta.open('r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            if lineas:
                self.cabeceras = lineas[0].strip().split(self.separador)
                for linea in lineas[1:]:
                    valores = linea.strip().split(self.separador)
                    if len(valores) == len(self.cabeceras):
                        fila: FilaCSV = dict(zip(self.cabeceras, valores))
                        self.datos.append(fila)

    def filtrar_datos(
        self,
        columna: str,
        valor: Union[str, float]
    ) -> List[FilaCSV]:
        """
        Filtra los datos según un criterio.

        Args:
            columna: Nombre de la columna
            valor: Valor a buscar

        Returns:
            List[FilaCSV]: Filas que cumplen el criterio
        """
        return [
            fila
            for fila in self.datos
            if fila.get(columna) == valor
        ]

    def calcular_estadisticas(
        self,
        columna: str
    ) -> Optional[EstadisticasColumna]:
        """
        Calcula estadísticas para una columna numérica.

        Args:
            columna: Nombre de la columna

        Returns:
            Optional[EstadisticasColumna]: Estadísticas calculadas o None
        """
        valores: List[float] = []

        for fila in self.datos:
            try:
                valor = float(fila.get(columna, 0))
                valores.append(valor)
            except ValueError:
                continue

        if valores:
            estadisticas: EstadisticasColumna = {
                'minimo': min(valores),
                'maximo': max(valores),
                'promedio': sum(valores) / len(valores),
                'total': sum(valores)
            }
            self.resumen_estadistico[columna] = estadisticas
            return estadisticas
        return None

    def exportar_resultados(
        self,
        ruta_salida: Union[str, Path],
        datos_filtrados: List[FilaCSV]
    ) -> None:
        """
        Exporta resultados filtrados a un archivo CSV.

        Args:
            ruta_salida: Ruta del archivo de salida
            datos_filtrados: Datos a exportar
        """
        ruta = Path(ruta_salida)
        with ruta.open('w', encoding='utf-8') as archivo:
            if datos_filtrados and self.cabeceras:
                archivo.write(self.separador.join(self.cabeceras) + '\\n')
                for fila in datos_filtrados:
                    valores = [
                        str(fila.get(cab, ''))
                        for cab in self.cabeceras
                    ]
                    archivo.write(self.separador.join(valores) + '\\n')

```
