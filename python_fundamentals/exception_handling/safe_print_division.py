#!/usr/bin/env python3
"""Division de dos enteros con manejo de excepciones."""


def safe_print_division(a, b):
    """Devuelve la division o None si ocurre una excepcion."""
    resultado = None
    try:
        resultado = a / b
    except Exception:
        resultado = None
    finally:
        print("Inside result: {}".format(resultado))
    return resultado
