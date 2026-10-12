#!/usr/bin/env python3
for numero in range(100):
    if numero == 99:
        print("{:02d}".format(numero))
    else:
        print("{:02d}".format(numero), end=", ")
