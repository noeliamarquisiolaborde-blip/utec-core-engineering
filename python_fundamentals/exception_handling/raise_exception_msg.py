#!/usr/bin/env python3
"""Lanza NameError con un mensaje personalizado."""


def raise_exception_msg(message=""):
    """Lanza una excepcion con el mensaje recibido."""
    raise NameError(message)
