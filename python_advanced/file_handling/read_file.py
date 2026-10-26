#!/usr/bin/env python3
"""Lectura de archivos de texto en UTF-8."""


def read_file(filename=""):
    """Lee un archivo y muestra su contenido en pantalla."""
    with open(filename, "r", encoding="utf-8") as archivo:
        print(archivo.read(), end="")
