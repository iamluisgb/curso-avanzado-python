# Organización de Grandes Programas en Python

## 1. Organización de Grandes Programas en Python

### 1.1 Introducción

La organización de grandes programas en Python es un arte que va más allá de simplemente escribir código funcional. Es un sistema integral que utiliza paquetes, módulos y diversos mecanismos de importación para crear estructuras de código mantenibles, escalables y comprensibles. En el corazón de esta organización está el sistema de paquetes de Python, que proporciona una manera elegante de estructurar código en unidades lógicas y reutilizables.

### 1.2 Fundamentos Clave

### El Sistema de Paquetes y el archivo `__init__.py`

El archivo `__init__.py` es como el director de orquesta de un paquete Python. Su presencia en un directorio le dice a Python: "esto no es solo una carpeta con archivos Python, es un paquete cohesivo y organizado". Veamos sus roles fundamentales:

1. **Inicialización del Paquete**
Cuando importas un paquete, Python ejecuta primero el código en `__init__.py`. Esto te permite configurar recursos importantes:

```python
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

```

1. **Definición de la Interfaz del Paquete**
El archivo `__init__.py` actúa como la "recepción" de tu paquete, controlando qué funcionalidades están disponibles para los usuarios:

```python
# mi_paquete/base_datos/consultas.py
def ejecutar_consulta(sql):
    """Ejecuta una consulta SQL."""
    pass

def obtener_todos(tabla):
    """Obtiene todos los registros de una tabla."""
    pass

# mi_paquete/base_datos/__init__.py
from .consultas import ejecutar_consulta, obtener_todos

# mi_paquete/__init__.py
from .base_datos import ejecutar_consulta, obtener_todos

# Ahora los usuarios pueden hacer:
from mi_paquete import ejecutar_consulta  # En lugar de mi_paquete.base_datos.consultas.ejecutar_consulta

```

1. **Elevación de Atributos (Hoisting)**
Una característica poderosa de `__init__.py` es su capacidad para "elevar" funcionalidades desde submódulos profundos hasta niveles más accesibles. Esto es especialmente útil para crear APIs intuitivas:

```python
# Estructura del proyecto:
mi_proyecto/
    __init__.py
    utilidades/
        __init__.py
        validacion.py
        formateo.py
    modelos/
        __init__.py
        usuario.py
        perfil.py

# mi_proyecto/utilidades/validacion.py
def validar_email(email):
    """Valida un email."""
    pass

# mi_proyecto/utilidades/__init__.py
from .validacion import validar_email
from .formateo import formatear_fecha

# mi_proyecto/__init__.py
from .utilidades import validar_email, formatear_fecha

# Los usuarios ahora pueden hacer:
from mi_proyecto import validar_email
# En lugar de:
# from mi_proyecto.utilidades.validacion import validar_email

```

### Importaciones Relativas

Las importaciones relativas son como dar direcciones usando "aquí" como punto de referencia. Son útiles dentro de un paquete, pero deben usarse con criterio:

```python
# Estructura:
mi_app/
    __init__.py
    modelos/
        __init__.py
        usuario.py
        perfil.py
    utils/
        __init__.py
        helpers.py

# En mi_app/modelos/usuario.py:
# Importación relativa (usando ..)
from ..utils.helpers import formatear_fecha  # Subir un nivel, luego entrar a utils
# Importación relativa (usando .)
from . import perfil                        # Mismo directorio
from .perfil import Perfil                  # Mismo directorio, módulo específico

```

Las importaciones relativas son más apropiadas cuando:

1. Trabajas con módulos estrechamente relacionados dentro del mismo paquete
2. Planeas refactorizar código que se moverá como una unidad
3. Creas componentes reutilizables

Sin embargo, es mejor evitarlas cuando:

1. La estructura del paquete es compleja y profunda
2. El código necesita ser inmediatamente claro para nuevos desarrolladores
3. Los módulos podrían moverse independientemente

### **`sys.path`: Dónde Python Busca los Módulos**

Cuando importas un módulo en Python (`import modulo_x`), el intérprete sigue un orden de búsqueda definido en `sys.path`, que es una lista de directorios donde Python busca los archivos `.py`.

Puedes ver su contenido ejecutando:

```python
import sys
print(sys.path)

```

Ejemplo de salida:

```python
[
    '',  # Directorio actual
    '/usr/lib/python3.10',  # Biblioteca estándar
    '/usr/lib/python3.10/site-packages',  # Módulos instalados con pip
]

```

Python busca los módulos en este orden:

- **El directorio actual (`''`)**
- **Las rutas definidas en la variable de entorno `PYTHONPATH`**
- **Las bibliotecas estándar de Python (`/usr/lib/python3.x/`)**
- **El directorio `site-packages/` donde están las librerías instaladas con `pip`**

Si el módulo no se encuentra en ninguna de estas rutas, Python lanza un `ModuleNotFoundError`.

---

### Paquetes Namespace

Los paquetes namespace son una característica avanzada que permite dividir un paquete entre varios directorios. A diferencia de los paquetes normales, no utilizan `__init__.py`:

```python
# Estructura en diferentes ubicaciones:
/ruta1/mi_empresa/
    herramientas/
        inspector.py
        validador.py

/ruta2/mi_empresa/
    base_datos/
        conector.py
        consulta.py
# Si agregas **ambas rutas a sys.path**, Python considerará mi_empresa como un único paquete:
import sys
sys.path.append("/ruta1")
sys.path.append("/ruta2")

# Ambos pueden importarse como mi_empresa
import mi_empresa.herramientas.inspector
import mi_empresa.base_datos.conector

```

 **Lo importante aquí es que `mi_empresa` no tiene `__init__.py`**, lo que permite que Python lo trate como un **paquete namespace** y combine todas sus rutas en `sys.path`.

Cuando importas `mi_empresa.herramientas.inspector`, Python hace lo siguiente:

- Busca en **todas las rutas de `sys.path`** si existe un directorio llamado `mi_empresa/`.
- Encuentra `mi_empresa/` en `/ruta1` y en `/ruta2`.
- **Fusiona ambos directorios**, creando un paquete namespace dinámicamente.
- Ahora puedes importar `mi_empresa.herramientas.inspector` (de `/ruta1`) y `mi_empresa.base_datos.conector` (de `/ruta2`).

### Directorios Ejecutables

Los directorios ejecutables se crean colocando un archivo `__main__.py` en un directorio. Esto permite ejecutar el paquete directamente:

```python
# mi_app/
#   __main__.py
#   config.py
#   nucleo/
#     __init__.py
#     procesador.py

# mi_app/__main__.py
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

# Ahora puedes ejecutar:
# python -m mi_app entrada.txt

```

### 1.3 Analogías y Ejemplos Conceptuales

Para entender mejor la organización de programas Python, podemos compararla con la estructura de una biblioteca:

1. **La Biblioteca (El Proyecto)**
    - El edificio completo representa tu proyecto Python
    - Los pisos son como paquetes principales
    - Las secciones en cada piso son como subpaquetes
    - Los libros son módulos individuales
    - El catálogo (`__init__.py`) te dice qué hay disponible en cada sección
2. **El Sistema de Navegación (Importaciones)**
    - Las señales absolutas (importaciones absolutas) dan la ubicación exacta desde la entrada
    - Las señales relativas (importaciones relativas) dan direcciones desde tu ubicación actual
    - Los atajos (elevación de atributos) permiten acceso rápido a recursos populares
3. **El Personal (Mecanismos de Python)**
    - El bibliotecario principal (`__main__.py`) coordina las operaciones principales
    - Los catálogos de sección (`__init__.py`) organizan cada área
    - Los sistemas de referencia cruzada (paquetes namespace) conectan diferentes secciones

[El resto de las secciones de la template continúan como antes...]

## 2. Código de Demostración

### 2.1 Ejemplo Básico

```python
# Título: Implementación de una estructura de proyecto Python profesional
# Objetivo: Demostrar la organización modular de un proyecto real

# Estructura del proyecto:
proyecto_analytics/
    ├── docs/                    # Documentación del proyecto
    │   ├── api.md
    │   └── guia_usuario.md
    ├── src/                     # Código fuente principal
    │   └── analytics/          # Paquete principal
    │       ├── __init__.py     # Define la API pública del paquete
    │       ├── preprocessing/   # Subpaquete para preprocesamiento
    │       │   ├── __init__.py
    │       │   ├── cleaner.py
    │       │   └── validator.py
    │       ├── analysis/       # Subpaquete para análisis
    │       │   ├── __init__.py
    │       │   ├── statistical.py
    │       │   └── visualization.py
    │       └── utils/          # Utilidades comunes
    │           ├── __init__.py
    │           └── helpers.py
    ├── tests/                  # Pruebas unitarias y de integración
    │   ├── __init__.py
    │   ├── test_cleaner.py
    │   └── test_statistical.py
    ├── requirements.txt        # Dependencias del proyecto
    └── setup.py               # Configuración de instalación

# Ejemplo de __init__.py en el paquete principal
# src/analytics/__init__.py

"""
Analytics Package
----------------
Un paquete para análisis de datos que proporciona herramientas
de preprocesamiento y análisis estadístico.
"""

from .preprocessing.cleaner import DataCleaner
from .preprocessing.validator import DataValidator
from .analysis.statistical import describe_dataset
from .analysis.visualization import plot_distribution

# Definimos la API pública del paquete
__all__ = [
    'DataCleaner',
    'DataValidator',
    'describe_dataset',
    'plot_distribution'
]

# Información sobre la versión
__version__ = '1.0.0'

```

### Errores comunes a prevenir:

1. Importaciones circulares:
    - Módulo A importa de B, que importa de A
    - Solución: Reestructurar la dependencia o mover el código compartido a un tercer módulo
2. Módulos demasiado grandes:
    - Archivos con miles de líneas de código
    - Solución: Dividir en módulos más pequeños y específicos

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real 1

**Contexto**: Sistema de procesamiento de datos financieros

```python
# financial_analysis/data_processing/__init__.py

"""
Módulo de procesamiento de datos financieros
Proporciona herramientas para importar, limpiar y validar datos financieros.
"""

from datetime import datetime
from typing import List, Dict, Optional

class FinancialDataProcessor:
    def __init__(self, data_source: str):
        self.data_source = data_source
        self.validation_rules = {}
        self._initialize_rules()

    def _initialize_rules(self):
        """Configura las reglas de validación básicas para datos financieros."""
        self.validation_rules = {
            'price': lambda x: isinstance(x, (int, float)) and x >= 0,
       from      'date': lambda x: isinstance(x, datetime),
            'symbol': lambda x: isinstance(x, str) and len(x) <= 6
        }

    def process_batch(self, data: List[Dict]) -> List[Dict]:
        """
        Procesa un lote de registros financieros.

        Args:
            data: Lista de diccionarios con datos financieros

        Returns:
            Lista de registros procesados y validados
        """
        validated_data = []
        for record in data:
            if self._validate_record(record):
                processed_record = self._process_record(record)
                validated_data.append(processed_record)
        return validated_data

```

**Puntos Importantes**:

- Uso de type hints para mejorar la claridad del código
- Implementación de validación modular y extensible
- Separación clara entre la interfaz pública y los métodos privados

### 3.2 Caso de Uso Real 2

**Contexto**: Sistema de plugins para generación de reportes

```python
# reporting_system/plugins/__init__.py

"""
Sistema de plugins para reportes
Permite la extensión dinámica de formatos de reporte.
"""

import importlib
import pkgutil
from typing import Dict, Type

class PluginRegistry:
    """Registro central de plugins de reportes."""

    def __init__(self):
        self._plugins: Dict[str, Type['ReportGenerator']] = {}

    def discover_plugins(self):
        """
        Descubre automáticamente los plugins disponibles en el directorio de plugins.
        """
        plugins_package = 'reporting_system.plugins'
        for _, name, _ in pkgutil.iter_modules([plugins_package]):
            module = importlib.import_module(f'{plugins_package}.{name}')
            if hasattr(module, 'register_plugin'):
                module.register_plugin(self)

    def register(self, name: str, plugin_class: Type['ReportGenerator']):
        """
        Registra un nuevo plugin de generación de reportes.
        """
        if name in self._plugins:
            raise ValueError(f"Plugin '{name}' ya está registrado")
        self._plugins[name] = plugin_class

    def get_plugin(self, name: str) -> Type['ReportGenerator']:
        """
        Obtiene una clase de plugin por nombre.
        """
        if name not in self._plugins:
            raise KeyError(f"Plugin '{name}' no encontrado")
        return self._plugins[name]

```

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico

**Ejercicio 1: Creación de un paquete de utilidades**

**Descripción**: Desarrollar un paquete de utilidades básicas que incluya funciones para manipulación de strings, fechas y números.

**Objetivo**: Practicar la organización básica de código en módulos y paquetes.

**Pistas**:

1. Comenzar con una estructura básica de directorios
2. Implementar cada tipo de utilidad en su propio módulo
3. Usar `__init__.py` para exponer una API limpia

### 4.2 Nivel Intermedio

**Ejercicio 2: Sistema de procesamiento de logs**

**Descripción**: Crear un sistema modular para procesar y analizar archivos de log.

**Objetivo**: Practicar el diseño de sistemas extensibles y la organización de código complejo.

**Pistas**:

1. Separar la lectura, el procesamiento y el análisis en módulos distintos
2. Implementar un sistema de plugins para diferentes formatos de log
3. Usar type hints y documentación apropiada

### 4.3 Nivel Avanzado

**Ejercicio 3: Framework de ETL**

**Descripción**: Desarrollar un framework simple de ETL (Extract, Transform, Load) con plugins.

**Objetivo**: Aplicar conceptos avanzados de organización de código y diseño de sistemas.

**Pistas**:

1. Usar abstract base classes para definir interfaces
2. Implementar un sistema de registro de componentes
3. Utilizar namespace packages para plugins de terceros

## 5. Recursos Adicionales

### Documentación Oficial

- [Python Packaging User Guide](https://packaging.python.org/)
- [Python Modules and Packages](https://docs.python.org/3/tutorial/modules.html)
- [PEP 420 – Namespace Packages](https://www.python.org/dev/peps/pep-0420/)

### Artículos Relacionados

- "Clean Architecture in Python" por Leonardo Giordani
- "Python Application Layouts: A Reference" en Real Python
- "Modular Programming with Python" por Erik Westra

### Ejemplo de Paquete Básico

- https://github.com/rcamuccio/simplemath/tree/master

## 6. Solución de Ejercicios

## Ejercicio 1: Creación de un Paquete de Utilidades (Nivel Básico)

Comenzaremos desarrollando un paquete de utilidades que demuestra los principios básicos de organización de código en Python. La solución incluirá utilidades para manipulación de strings, fechas y números.

### Estructura del Proyecto

```
utils_package/
├── README.md
├── setup.py
├── requirements.txt
└── src/
    └── pyutils/
        ├── __init__.py
        ├── string_utils.py
        ├── date_utils.py
        ├── number_utils.py
        └── tests/
            ├── __init__.py
            ├── test_string_utils.py
            ├── test_date_utils.py
            └── test_number_utils.py

```

### Implementación

1. Primero, creamos el archivo `setup.py` para configurar nuestro paquete:

```python
from setuptools import setup, find_packages

setup(
    name="pyutils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-dateutil>=2.8.0",
    ],
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Un paquete de utilidades Python",
    keywords="utils, string, date, number",
    python_requires=">=3.7",
)

```

Este script `setup.py` se usa para empaquetar y distribuir un paquete de Python utilizando `setuptools`. Explicación breve de sus partes:

1. **`name="pyutils"`** → Nombre del paquete.
2. **`version="0.1.0"`** → Versión del paquete.
3. **`packages=find_packages(where="src")`** → Busca y encuentra los subpaquetes dentro del directorio `src`.
4. **`package_dir={"": "src"}`** → Indica que el código fuente está en la carpeta `src`.
5. **`install_requires=["python-dateutil>=2.8.0"]`** → Especifica dependencias necesarias.
6. **`author` y `author_email`** → Información del autor.
7. **`description`** → Breve descripción del paquete.
8. **`keywords`** → Palabras clave para búsqueda en PyPI.
9. **`python_requires=">=3.7"`** → Define la versión mínima de Python requerida.

Este script permite instalar el paquete con:

```bash
pip install .

```

o publicarlo en PyPI con `twine`y.

1. Implementación de las utilidades de strings (`string_utils.py`):

```python
"""
Utilidades para manipulación de strings.
Proporciona funciones comunes para el procesamiento de texto.
"""
from typing import List, Optional
import re

def slugify(text: str) -> str:
    """
    Convierte un texto en un slug URL-friendly.

    Args:
        text: El texto a convertir

    Returns:
        str: El texto convertido en slug

    Example:
        >>> slugify("Hola Mundo!")
        'hola-mundo'
    """
    # Convertir a minúsculas
    text = text.lower().strip()
    # Reemplazar espacios y otros separadores con un solo guion
    text = re.sub(r'[\s_]+', '-', text)
    # Remover caracteres especiales (excepto guiones y letras/números)
    text = re.sub(r'[^a-z0-9-]', '', text)
    # Eliminar guiones dobles o múltiples
    text = re.sub(r'-+', '-', text)
    return text

def truncate(text: str, length: int, suffix: str = "...") -> str:
    """
    Trunca un texto a una longitud específica.

    Args:
        text: Texto a truncar
        length: Longitud máxima
        suffix: Sufijo a añadir al texto truncado

    Returns:
        str: Texto truncado
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

def split_words(text: str) -> List[str]:
    """
    Divide un texto en palabras, eliminando espacios extra.

    Args:
        text: Texto a dividir

    Returns:
        List[str]: Lista de palabras
    """
    return [word for word in text.split() if word]

```

1. Implementación de utilidades de fechas (`date_utils.py`):

```python
"""
Utilidades para manipulación de fechas.
Proporciona funciones para trabajar con fechas y tiempos.
"""
from datetime import datetime, timedelta
from typing import Optional, List, Union
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

class DateUtils:
    """Clase para manipulación de fechas."""

    @staticmethod
    def parse_date(date_str: str) -> Optional[datetime]:
        """
        Parsea una fecha en formato string a datetime.

        Args:
            date_str: String con la fecha

        Returns:
            datetime o None si no se puede parsear

        Example:
            >>> DateUtils.parse_date("2024-02-08")
            datetime.datetime(2024, 2, 8, 0, 0)
        """
        try:
            return parse(date_str)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def add_business_days(
        date: datetime,
        days: int,
        holidays: Optional[List[datetime]] = None
    ) -> datetime:
        """
        Añade días hábiles a una fecha.

        Args:
            date: Fecha inicial
            days: Número de días hábiles a añadir
            holidays: Lista opcional de fechas festivas

        Returns:
            datetime: Nueva fecha después de añadir los días hábiles
        """
        if holidays is None:
            holidays = []

        current_date = date
        remaining_days = days

        while remaining_days > 0:
            current_date += timedelta(days=1)
            if (current_date.weekday() < 5 and  # Lunes a Viernes
                current_date not in holidays):
                remaining_days -= 1

        return current_date

```

1. Implementación de utilidades numéricas (`number_utils.py`):

```python
"""
Utilidades para manipulación de números.
Proporciona funciones matemáticas y de formateo numérico.
"""
from typing import Union, List
from decimal import Decimal, ROUND_HALF_UP

class NumberUtils:
    """Clase para manipulación de números."""

    @staticmethod
    def round_currency(
        amount: Union[float, Decimal],
        decimal_places: int = 2
    ) -> Decimal:
        """
        Redondea un número para uso en moneda.

        Args:
            amount: Cantidad a redondear
            decimal_places: Número de decimales

        Returns:
            Decimal: Cantidad redondeada

        Example:
            >>> NumberUtils.round_currency(10.126)
            Decimal('10.13')
        """
        if isinstance(amount, float):
            amount = Decimal(str(amount))
        return Decimal(amount).quantize(
            Decimal(f'0.{"0" * decimal_places}'),
            rounding=ROUND_HALF_UP
        )

    @staticmethod
    def calculate_percentage(
        value: Union[int, float],
        total: Union[int, float],
        decimal_places: int = 2
    ) -> float:
        """
        Calcula el porcentaje de un valor sobre un total.

        Args:
            value: Valor a calcular
            total: Total sobre el que calcular
            decimal_places: Decimales a mantener

        Returns:
            float: Porcentaje calculado
        """
        if total == 0:
            return 0.0
        percentage = (value / total) * 100
        return round(percentage, decimal_places)

```

1. Implementación del archivo `__init__.py` principal:

```python
"""
PyUtils
-------
Un paquete de utilidades Python que proporciona funciones
comunes para manipulación de strings, fechas y números.
"""

from .string_utils import slugify, truncate, split_words
from .date_utils import DateUtils
from .number_utils import NumberUtils

__version__ = "0.1.0"
__all__ = [
    'slugify',
    'truncate',
    'split_words',
    'DateUtils',
    'NumberUtils',
]

```

### Tests

Ejemplo de tests para `string_utils.py`:

```python
# tests/test_string_utils.py
import unittest
from pyutils.string_utils import slugify, truncate, split_words

class TestStringUtils(unittest.TestCase):

    def test_slugify(self):
        test_cases = [
            ("Hola Mundo!", "hola-mundo"),
            ("Python 3.9", "python-39"),
            ("¡Áéíóú!", "aeiou"),
        ]
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(slugify(input_text), expected)

    def test_truncate(self):
        text = "Hello World"
        self.assertEqual(truncate(text, 5), "He...")
        self.assertEqual(truncate(text, 20), text)
        self.assertEqual(truncate(text, 8, "..."), "Hello...")

    def test_split_words(self):
        text = "  Hello   World  Python  "
        expected = ["Hello", "World", "Python"]
        self.assertEqual(split_words(text), expected)

if __name__ == '__main__':
    unittest.main()

```

## Ejercicio 2: Sistema de Procesamiento de Logs (Nivel Intermedio)

Para el sistema de procesamiento de logs, crearemos una estructura modular que permita procesar diferentes formatos de logs y realizar análisis sobre ellos.

### Estructura del Proyecto

```
log_processor/
├── README.md
├── setup.py
└── src/
    └── logprocessor/
        ├── __init__.py
        ├── core/
        │   ├── __init__.py
        │   ├── parser.py
        │   ├── processor.py
        │   └── analyzer.py
        ├── plugins/
        │   ├── __init__.py
        │   ├── apache.py
        │   ├── nginx.py
        │   └── custom.py
        └── utils/
            ├── __init__.py
            └── patterns.py

```

### Implementación

1. Primero, definimos las interfaces base (`core/parser.py`):

```python
"""
Interfaces base para el sistema de procesamiento de logs.
Define las abstracciones principales del sistema.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Iterator
from datetime import datetime

class LogEntry:
    """Representa una entrada de log normalizada."""

    def __init__(
        self,
        timestamp: datetime,
        level: str,
        message: str,
        metadata: Dict[str, Any]
    ):
        self.timestamp = timestamp
        self.level = level
        self.message = message
        self.metadata = metadata

    def __repr__(self) -> str:
        return (f"LogEntry(timestamp={self.timestamp}, "
                f"level={self.level}, message={self.message!r})")

class LogParser(ABC):
    """Interfaz base para parsers de logs."""

    @abstractmethod
    def parse_line(self, line: str) -> LogEntry:
        """
        Parsea una línea de log y retorna una entrada normalizada.

        Args:
            line: Línea de log a parsear

        Returns:
            LogEntry: Entrada de log normalizada
        """
        pass

    @abstractmethod
    def get_format_name(self) -> str:
        """
        Retorna el nombre del formato de log que maneja este parser.

        Returns:
            str: Nombre del formato
        """
        pass

```

1. Implementación de un parser específico (`plugins/nginx.py`):

```python
"""
Parser para logs de Nginx.
Implementa el parsing de logs en formato Nginx común.
"""
import re
from datetime import datetime
from typing import Dict, Optional
from ..core.parser import LogParser, LogEntry

class NginxLogParser(LogParser):
    """Parser para logs de Nginx en formato común."""

    # Patrón para el formato común de Nginx
    PATTERN = re.compile(
        r'(?P<ip>[\\d.]+)\\s+'  # Dirección IP
        r'(?P<identity>\\S*)\\s+'  # Identidad
        r'(?P<user>\\S*)\\s+'  # Usuario
        r'\\[(?P<timestamp>.*?)\\]\\s+'  # Timestamp
        r'"(?P<request>.*?)"\\s+'  # Solicitud
        r'(?P<status>\\d+)\\s+'  # Código de estado
        r'(?P<size>\\d+)\\s+'  # Tamaño
        r'"(?P<referer>.*?)"\\s+'  # Referer
        r'"(?P<user_agent>.*?)"'  # User Agent
    )

    def parse_line(self, line: str) -> LogEntry:
        """
        Parsea una línea de log de Nginx.

        Args:
            line: Línea de log a parsear

        Returns:
            LogEntry: Entrada de log normalizada

        Raises:
            ValueError: Si la línea no coincide con el formato esperado
        """
        match = self.PATTERN.match(line)
        if not match:
            raise ValueError(f"Línea no coincide con formato Nginx: {line}")

        data = match.groupdict()

        # Parsear timestamp
        timestamp = datetime.strptime(
            data['timestamp'],
            '%d/%b/%Y:%H:%M:%S %z'
        )

        # Extraer método y path de la solicitud
        request_parts = data['request'].split()
        method = path = protocol = ''
        if len(request_parts) >= 3:
            method, path, protocol = request_parts

        # Construir metadata
        metadata = {
            'ip': data['ip'],
            'method': method,
            'path': path,
            'protocol': protocol,
            'status': int(data['status']),
            'size': int(data['size']),
            'referer': data['referer'],
            'user_agent': data['user_agent']
        }

        # Determinar nivel basado en código de estado
        level = self._get_level_from_status(int(data['status']))

        return LogEntry(
            timestamp=timestamp,
            level=level,
            message=f"{method} {path} - {data['status']}",
            metadata=metadata
        )

    def get_format_name(self) -> str:
        return "nginx"

    def _get_level_from_status(self, status: int) -> str:
        """Determina el nivel de log basado en el código de estado."""
        if status < 400:
            return "INFO"
        elif status < 500:
            return "WARNING"
        return "ERROR"

```

1. Implementación del procesador principal (`core/processor.py`):

```python
"""
Procesador principal de logs.
Coordina el parsing y análisis de logs.
"""
from typing import Dict, List, Iterator, Type
from pathlib import Path
from .parser import LogParser, LogEntry

class LogProcessor:
    """
    Procesador principal de logs.
    Maneja múltiples formatos y realiza análisis básicos.
    """

    def __init__(self):
        self._parsers: Dict[str, LogParser] = {}

    def register_parser(self, parser: LogParser) -> None:
        """
        Registra un nuevo parser de logs.

        Args:
            parser: Instancia de LogParser a registrar
        """
        format_name = parser.get_format_name()
        self._parsers[format_name] = parser

    def process_file(
        self,
        file_path: Path,
        format_name: str
    ) -> Iterator[LogEntry]:
        """
        Procesa un archivo de log completo.

        Args:
            file_path: Ruta al archivo de log
            format_name: Nombre del formato de log a utilizar

        Yields:
            LogEntry: Cada entrada de log procesada

        Raises:
            KeyError: Si el formato especificado no está registrado
            ValueError: Si hay errores en el parsing
        """
        if format_name not in self._parsers:
            raise KeyError(f"Formato de log no registrado: {format_name}")

        parser = self._parsers[format_name]

        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    entry = parser.parse_line(line.strip())
                    yield entry
                except ValueError as e:
                    print(f"Error en línea {line_num}: {e}")
                    continue

    def analyze_logs(
        self,
        entries: Iterator[LogEntry]
    ) -> Dict[str, Any]:
        """
        Realiza análisis básico sobre las entradas de log.

        Args:
            entries: Iterator de entradas de log

        Returns:
            Dict con estadísticas y análisis
        """
        stats = {
            'total_entries': 0,
            'by_level': {},
            'by_hour': {},
            'status_codes': {},
            'top_ips': {},
            'errors': []
        }

        for entry in entries:
            stats['total_entries'] += 1

            # Conteo por nivel
            stats['by_level'][entry.level] = \\
                stats['by_level'].get(entry.level, 0) + 1

            # Conteo por hora
            hour = entry.timestamp.strftime('%H:00')
            stats['by_hour'][hour] = \\
                stats['by_hour'].get(hour, 0) + 1

            # Análisis específico para logs web
            if 'status' in entry.metadata:
                status = str(entry.metadata['status'])
                stats['status_codes'][status] = \\
                    stats['status_codes'].get(status, 0) + 1

            if 'ip' in entry.metadata:
                ip = entry.metadata['ip']
                stats['top_ips'][ip] = \\
                    stats['top_ips'].get(ip, 0) + 1

            # Guardar errores
            if entry.level == 'ERROR':
                stats['errors'].append({
                    'timestamp': entry.timestamp,
                    'message': entry.message,
                    'metadata': entry.metadata
                })

        # Ordenar resultados
        stats['top_ips'] = dict(
            sorted(
                stats['top_ips'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
        )

        return stats

4. Implementación del analizador de logs (`core/analyzer.py`):

```python
"""
Analizador avanzado de logs.
Proporciona funcionalidades de análisis y visualización.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
from .parser import LogEntry

class LogAnalyzer:
    """
    Analizador avanzado de logs con capacidades de visualización.
    """

    def __init__(self):
        self.entries: List[LogEntry] = []

    def add_entries(self, entries: List[LogEntry]) -> None:
        """
        Añade entradas de log para análisis.

        Args:
            entries: Lista de entradas de log
        """
        self.entries.extend(entries)

    def get_time_series(
        self,
        interval_minutes: int = 60,
        level: Optional[str] = None
    ) -> Dict[datetime, int]:
        """
        Genera una serie temporal de eventos.

        Args:
            interval_minutes: Tamaño del intervalo en minutos
            level: Opcional, filtrar por nivel de log

        Returns:
            Dict con timestamps y conteos
        """
        if not self.entries:
            return {}

        # Inicializar intervalos
        start_time = min(entry.timestamp for entry in self.entries)
        end_time = max(entry.timestamp for entry in self.entries)

        intervals = defaultdict(int)
        interval_delta = timedelta(minutes=interval_minutes)

        current_interval = start_time
        while current_interval <= end_time:
            intervals[current_interval] = 0
            current_interval += interval_delta

        # Contar eventos por intervalo
        for entry in self.entries:
            if level and entry.level != level:
                continue

            interval_start = entry.timestamp.replace(
                minute=0 if interval_minutes >= 60 else
                (entry.timestamp.minute // interval_minutes) * interval_minutes,
                second=0,
                microsecond=0
            )
            intervals[interval_start] += 1

        return dict(sorted(intervals.items()))

    def plot_time_series(
        self,
        interval_minutes: int = 60,
        level: Optional[str] = None,
        title: Optional[str] = None
    ) -> None:
        """
        Genera un gráfico de serie temporal.

        Args:
            interval_minutes: Tamaño del intervalo en minutos
            level: Opcional, filtrar por nivel de log
            title: Opcional, título del gráfico
        """
        time_series = self.get_time_series(interval_minutes, level)

        plt.figure(figsize=(12, 6))
        plt.plot(
            list(time_series.keys()),
            list(time_series.values()),
            marker='o'
        )

        plt.title(title or 'Eventos de Log por Tiempo')
        plt.xlabel('Tiempo')
        plt.ylabel('Número de Eventos')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        return plt

5. Ejemplo de uso del sistema:

```python
from pathlib import Path
from logprocessor.core.processor import LogProcessor
from logprocessor.core.analyzer import LogAnalyzer
from logprocessor.plugins.nginx import NginxLogParser

# Crear y configurar el procesador
processor = LogProcessor()
processor.register_parser(NginxLogParser())

# Procesar archivo de logs
log_file = Path('access.log')
entries = list(processor.process_file(log_file, 'nginx'))

# Realizar análisis básico
stats = processor.analyze_logs(entries)

print(f"Total de entradas: {stats['total_entries']}")
print("\\nDistribución por nivel:")
for level, count in stats['by_level'].items():
    print(f"  {level}: {count}")

print("\\nTop 5 IPs:")
for ip, count in list(stats['top_ips'].items())[:5]:
    print(f"  {ip}: {count} requests")

# Análisis avanzado con visualización
analyzer = LogAnalyzer()
analyzer.add_entries(entries)

# Generar gráfico de serie temporal
plt = analyzer.plot_time_series(
    interval_minutes=30,
    title='Tráfico Web por Intervalos de 30 Minutos'
)
plt.savefig('traffic_analysis.png')

```

## Ejercicio 3: Framework de ETL (Nivel Avanzado)

Para el framework de ETL, implementaremos un sistema extensible que permita definir y ejecutar pipelines de procesamiento de datos.

### Estructura del Proyecto

```
data_etl/
├── README.md
├── setup.py
└── src/
    └── etl/
        ├── __init__.py
        ├── core/
        │   ├── __init__.py
        │   ├── pipeline.py
        │   ├── extractors.py
        │   ├── transformers.py
        │   └── loaders.py
        ├── plugins/
        │   ├── __init__.py
        │   ├── csv_plugin.py
        │   ├── json_plugin.py
        │   └── sql_plugin.py
        └── utils/
            ├── __init__.py
            └── validation.py

```

Implementaremos cada componente del framework ETL, comenzando por las interfaces base y progresando hacia implementaciones específicas.

### Implementación del Core ETL

1. Primero, definimos las interfaces base (`core/pipeline.py`):

```python
"""
Interfaces base para el framework ETL.
Define las abstracciones principales y el flujo de datos.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Generic, TypeVar, Optional
from dataclasses import dataclass
from datetime import datetime

# Tipos genéricos para datos de entrada y salida
T_in = TypeVar('T_in')
T_out = TypeVar('T_out')

@dataclass
class ETLContext:
    """Contexto de ejecución para operaciones ETL."""
    start_time: datetime
    parameters: Dict[str, Any]
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

class DataSource(ABC, Generic[T_out]):
    """Interfaz base para fuentes de datos."""

    @abstractmethod
    def read(self, context: ETLContext) -> T_out:
        """
        Lee datos de la fuente.

        Args:
            context: Contexto de ejecución ETL

        Returns:
            Datos leídos de la fuente
        """
        pass

class DataTransformer(ABC, Generic[T_in, T_out]):
    """Interfaz base para transformaciones de datos."""

    @abstractmethod
    def transform(self, data: T_in, context: ETLContext) -> T_out:
        """
        Transforma los datos de entrada.

        Args:
            data: Datos a transformar
            context: Contexto de ejecución ETL

        Returns:
            Datos transformados
        """
        pass

class DataSink(ABC, Generic[T_in]):
    """Interfaz base para destinos de datos."""

    @abstractmethod
    def write(self, data: T_in, context: ETLContext) -> None:
        """
        Escribe datos en el destino.

        Args:
            data: Datos a escribir
            context: Contexto de ejecución ETL
        """
        pass

class Pipeline:
    """
    Pipeline ETL que coordina la extracción, transformación y carga de datos.
    """

    def __init__(
        self,
        source: DataSource,
        transformers: List[DataTransformer],
        sink: DataSink,
        name: str = "ETL Pipeline"
    ):
        self.source = source
        self.transformers = transformers
        self.sink = sink
        self.name = name

    def execute(self, parameters: Dict[str, Any] = None) -> ETLContext:
        """
        Ejecuta el pipeline ETL completo.

        Args:
            parameters: Parámetros de ejecución opcionales

        Returns:
            Contexto de ejecución con metadata
        """
        # Crear contexto de ejecución
        context = ETLContext(
            start_time=datetime.now(),
            parameters=parameters or {}
        )

        try:
            # Extraer datos
            data = self.source.read(context)
            context.metadata['records_read'] = self._count_records(data)

            # Aplicar transformaciones
            for transformer in self.transformers:
                data = transformer.transform(data, context)
                context.metadata['records_transformed'] = self._count_records(data)

            # Cargar datos
            self.sink.write(data, context)

            # Registrar finalización exitosa
            context.metadata['status'] = 'success'
            context.metadata['end_time'] = datetime.now()

        except Exception as e:
            # Registrar error
            context.metadata['status'] = 'error'
            context.metadata['error'] = str(e)
            context.metadata['end_time'] = datetime.now()
            raise

        return context

    def _count_records(self, data: Any) -> Optional[int]:
        """Intenta contar los registros en los datos."""
        try:
            return len(data)
        except TypeError:
            return None

```

1. Implementación de extractores comunes (`core/extractors.py`):

```python
"""
Implementaciones de extractores de datos comunes.
Proporciona clases para leer datos de diferentes fuentes.
"""
import csv
import json
from typing import List, Dict, Any
from pathlib import Path
import pandas as pd
from .pipeline import DataSource, ETLContext

class CSVDataSource(DataSource[List[Dict[str, Any]]]):
    """Extractor para archivos CSV."""

    def __init__(
        self,
        file_path: Path,
        encoding: str = 'utf-8',
        delimiter: str = ',',
        **csv_options
    ):
        self.file_path = Path(file_path)
        self.encoding = encoding
        self.delimiter = delimiter
        self.csv_options = csv_options

    def read(self, context: ETLContext) -> List[Dict[str, Any]]:
        """
        Lee datos de un archivo CSV.

        Args:
            context: Contexto de ejecución ETL

        Returns:
            Lista de diccionarios con los datos del CSV

        Raises:
            FileNotFoundError: Si el archivo no existe
            csv.Error: Si hay errores en el formato CSV
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"No se encuentra el archivo: {self.file_path}")

        with open(self.file_path, 'r', encoding=self.encoding) as f:
            reader = csv.DictReader(
                f,
                delimiter=self.delimiter,
                **self.csv_options
            )
            data = list(reader)

        # Registrar metadata
        context.metadata['source_file'] = str(self.file_path)
        context.metadata['record_count'] = len(data)

        return data

class JSONDataSource(DataSource[Dict[str, Any]]):
    """Extractor para archivos JSON."""

    def __init__(
        self,
        file_path: Path,
        encoding: str = 'utf-8',
        record_path: List[str] = None
    ):
        self.file_path = Path(file_path)
        self.encoding = encoding
        self.record_path = record_path

    def read(self, context: ETLContext) -> Dict[str, Any]:
        """
        Lee datos de un archivo JSON.

        Args:
            context: Contexto de ejecución ETL

        Returns:
            Datos del JSON como diccionario

        Raises:
            FileNotFoundError: Si el archivo no existe
            json.JSONDecodeError: Si el JSON es inválido
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"No se encuentra el archivo: {self.file_path}")

        with open(self.file_path, 'r', encoding=self.encoding) as f:
            data = json.load(f)

        # Navegar al path especificado si existe
        if self.record_path:
            for key in self.record_path:
                data = data[key]

        # Registrar metadata
        context.metadata['source_file'] = str(self.file_path)

        return data

class SQLDataSource(DataSource[pd.DataFrame]):
    """Extractor para bases de datos SQL."""

    def __init__(
        self,
        connection_string: str,
        query: str,
        parameters: Dict[str, Any] = None
    ):
        self.connection_string = connection_string
        self.query = query
        self.parameters = parameters or {}

    def read(self, context: ETLContext) -> pd.DataFrame:
        """
        Lee datos de una base de datos SQL.

        Args:
            context: Contexto de ejecución ETL

        Returns:
            DataFrame con los resultados de la consulta

        Raises:
            SQLAlchemyError: Si hay errores en la conexión o consulta
        """
        import sqlalchemy as sa

        engine = sa.create_engine(self.connection_string)

        with engine.connect() as connection:
            df = pd.read_sql(
                self.query,
                connection,
                params=self.parameters
            )

        # Registrar metadata
        context.metadata['source_query'] = self.query
        context.metadata['record_count'] = len(df)

        return df

```

1. Implementación de transformadores (`core/transformers.py`):

```python
"""
Implementaciones de transformadores de datos comunes.
Proporciona clases para modificar y limpiar datos.
"""
from typing import List, Dict, Any, Callable
import pandas as pd
from .pipeline import DataTransformer, ETLContext

class DataFrameTransformer(DataTransformer[pd.DataFrame, pd.DataFrame]):
    """
    Transformador base para operaciones con DataFrames.
    Permite encadenar múltiples operaciones de transformación.
    """

    def __init__(self):
        self.operations: List[Callable[[pd.DataFrame], pd.DataFrame]] = []

    def add_operation(
        self,
        operation: Callable[[pd.DataFrame], pd.DataFrame]
    ) -> 'DataFrameTransformer':
        """
        Añade una operación de transformación.

        Args:
            operation: Función que transforma un DataFrame

        Returns:
            Self para encadenamiento
        """
        self.operations.append(operation)
        return self

    def transform(
        self,
        data: pd.DataFrame,
        context: ETLContext
    ) -> pd.DataFrame:
        """
        Aplica todas las operaciones registradas al DataFrame.

        Args:
            data: DataFrame a transformar
            context: Contexto de ejecución ETL

        Returns:
            DataFrame transformado
        """
        result = data.copy()

        for operation in self.operations:
            result = operation(result)

            # Registrar metadata de la transformación
            op_name = operation.__name__
            context.metadata[f'transform_{op_name}_records'] = len(result)

        return result

class DataCleaner(DataTransformer[pd.DataFrame, pd.DataFrame]):
    """
    Transformador para limpieza común de datos.
    """

    def __init__(
        self,
        drop_duplicates: bool = True,
        drop_na: bool = False,
        string_columns: List[str] = None,
        numeric_columns: List[str] = None
    ):
        self.drop_duplicates = drop_duplicates
        self.drop_na = drop_na
        self.string_columns = string_columns or []
        self.numeric_columns = numeric_columns or []

    def transform(
        self,
        data: pd.DataFrame,
        context: ETLContext
    ) -> pd.DataFrame:
        """
        Limpia el DataFrame según la configuración.

        Args:
            data: DataFrame a limpiar
            context: Contexto de ejecución ETL

        Returns:
            DataFrame limpio
        """
        result = data.copy()

        # Registrar estado inicial
        context.metadata['initial_records'] = len(result)

        # Eliminar duplicados si se solicita
        if self.drop_duplicates:
            result = result.drop_duplicates()
            context.metadata['after_dedup_records'] = len(result)

        # Eliminar nulos si se solicita
        if self.drop_na:
            result = result.dropna()
            context.metadata['after_dropna_records'] = len(result)

        # Limpiar columnas de texto
        for col in self.string_columns:
            if col in result.columns:
                result[col] = result[col].str.strip()
                result[col] = result[col].str.lower()

        # Convertir columnas numéricas
        for col in self.numeric_columns:
            if col in result.columns:
                result[col] = pd.to_numeric(result[col], errors='coerce')

        return result

class DataEnricher(DataTransformer[pd.DataFrame, pd.DataFrame]):
    """
    Transformador para enriquecer datos con información adicional.
    """

    def __init__(
        self,
        enrichment_functions: Dict[str, Callable[[pd.DataFrame], pd.Series]]
    ):
        self.enrichment_functions = enrichment_functions

    def transform(
        self,
        data: pd.DataFrame,
        context: ETLContext
    ) -> pd.DataFrame:
        """
        Enriquece el DataFrame con nuevas columnas.

        Args:
            data: DataFrame a enriquecer
            context: Contexto de ejecución ETL

        Returns:
            DataFrame enriquecido
        """
        result = data.copy()

        for col_name, func in self.enrichment_functions.items():
            result[col_name] = func(result)

            # Registrar metadata del enriquecimiento
            context.metadata[f'enriched_{col_name}_nulls'] = \\
                result[col_name].isnull().sum()

        return result

```

1. Implementación de cargadores (`core/loaders.py`):

```python
"""
Implementaciones de cargadores de datos comunes.
Proporciona clases para escribir datos en diferentes destinos.
"""
import csv
import json
from typing import List, Dict, Any
from pathlib import Path
import pandas as pd
from .pipeline import DataSink, ETLContext

class CSVDataSink(DataSink[pd.DataFrame]):
    """Cargador para archivos CSV."""

    def __init__(
        self,
        file_path: Path,
        encoding: str = 'utf-8',
        index: bool = False,
        **csv_options
    ):
        self.file_path = Path(file_path)
        self.encoding = encoding
        self.index = index
        self.csv_options = csv_options

    def write(self, data: pd.DataFrame, context: ETLContext) -> None:
        """
        Escribe el DataFrame en un archivo CSV.

        Args:
            data: DataFrame a escribir
            context: Contexto de ejecución ETL

        Raises:
            IOError: Si hay errores al escribir el archivo
        """
        # Crear directorio si no existe
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        # Escribir CSV
        data.to_csv(
            self.file_path,
            encoding=self.encoding,
            index=self.index,
            **self.csv_options
        )

        # Registrar metadata
        context.metadata['output_file'] = str(self.file_path)
        context.metadata['records_written'] = len(data)

class SQL
```
