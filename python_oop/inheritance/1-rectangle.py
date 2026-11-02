#!/usr/bin/env python3
"""Define una clase para representar rectángulos."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y altura privados."""

    def __init__(self, width, height):
        """Inicializa el rectángulo con medidas válidas."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
