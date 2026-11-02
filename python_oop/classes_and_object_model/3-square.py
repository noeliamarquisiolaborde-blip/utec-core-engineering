
#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado y valida su tamaño."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2
