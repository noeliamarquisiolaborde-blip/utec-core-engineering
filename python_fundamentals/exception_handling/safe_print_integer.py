#!/usr/bin/env python3
"""Impresion segura de enteros."""


def safe_print_integer(value):
    """Imprime un entero y devuelve si pudo hacerlo."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
