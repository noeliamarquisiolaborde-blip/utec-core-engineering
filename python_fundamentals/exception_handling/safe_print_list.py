#!/usr/bin/env python3
"""Funciones para imprimir listas de forma segura."""


def safe_print_list(my_list=[], x=0):
    """Imprime hasta x elementos y devuelve cuántos imprimió."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
