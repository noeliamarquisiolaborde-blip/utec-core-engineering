#!/usr/bin/env python3
"""Escritura de archivos de texto en UTF-8."""


def write_file(filename="", text=""):
    """Escribe el texto y devuelve la cantidad de caracteres."""
    with open(filename, "w", encoding="utf-8") as archivo:
        return archivo.write(text)
