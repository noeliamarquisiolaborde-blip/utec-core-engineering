#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño y posición."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado y valida sus atributos."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza el tamaño."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y actualiza la posición."""
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado según su tamaño y posición."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

        for i in range(self.__position[1]):
            print()

    def __str__(self):
        """Devuelve la representación del cuadrado."""
        if self.__size == 0:
            return ""

        lines = []
        for i in range(self.__size):
            lines.append(
                " " * self.__position[0] + "#" * self.__size
            )

        return "\n".join(lines)
