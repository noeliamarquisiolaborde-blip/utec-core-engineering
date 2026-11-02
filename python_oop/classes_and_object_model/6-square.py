
#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y establece el tamaño."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y establece la posición."""
        if (not isinstance(value, tuple) or len(value) != 2
                or any(type(n) is not int or n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calcula el área."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelve la representación del cuadrado."""
        if self.__size == 0:
            return ""
        lines = []
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
