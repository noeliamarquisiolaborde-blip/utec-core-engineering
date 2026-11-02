#!/usr/bin/env python3
"""Define un cuadrado con representación personalizada."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Representa un cuadrado con descripción propia."""

    def __str__(self):
        """Devuelve la descripción del cuadrado."""
        return f"[Square] {self._Square__size}/{self._Square__size}"
