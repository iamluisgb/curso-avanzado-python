"""
Utilidades para manipulación de fechas.
Proporciona funciones para trabajar con fechas y tiempos.
"""
from datetime import datetime, timedelta
from typing import Optional, List,  Union
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
