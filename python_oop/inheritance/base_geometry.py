#!/usr/bin/env python3
"""Define la clase base para figuras geométricas."""


class BaseGeometry:
    """Representa una figura geométrica básica."""

    def area(self):
        """Indica que el cálculo del área no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Comprueba que un valor sea un entero positivo."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
