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
