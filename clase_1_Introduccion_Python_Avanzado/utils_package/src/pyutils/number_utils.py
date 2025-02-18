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
