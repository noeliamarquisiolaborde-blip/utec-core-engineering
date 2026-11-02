#!/usr/bin/env python3
"""Define una clase para representar cuadrados."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa el cuadrado con un tamaño válido."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2
