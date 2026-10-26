#!/usr/bin/env python3
"""Agrega texto a archivos en UTF-8."""


def append_write(filename="", text=""):
    """Agrega texto y devuelve la cantidad de caracteres añadidos."""
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)
