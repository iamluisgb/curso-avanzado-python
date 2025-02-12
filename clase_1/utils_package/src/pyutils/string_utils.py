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
