#!/usr/bin/env python3
"""Define un rectángulo con cálculo de área y representación en texto."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y altura privados."""

    def __init__(self, width, height):
        """Inicializa el rectángulo y valida sus medidas."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve una descripción del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
