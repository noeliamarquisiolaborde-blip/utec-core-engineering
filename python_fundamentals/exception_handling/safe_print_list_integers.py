#!/usr/bin/env python3
"""Impresion segura de enteros de una lista."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime los enteros entre los primeros x elementos."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
