#!/usr/bin/env python3
"""Módulo que define un cuadrado con tamaño validado."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado y valida su tamaño."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        