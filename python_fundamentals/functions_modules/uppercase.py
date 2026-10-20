#!/usr/bin/env python3


def uppercase(str):
    resultado = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            resultado += chr(ord(c) - 32)
        else:
            resultado += c
    print("{}".format(resultado))
