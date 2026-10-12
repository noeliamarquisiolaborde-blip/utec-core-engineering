#!/usr/bin/env python3
for primero in range(10):
    for segundo in range(primero + 1, 10):
        if primero == 8 and segundo == 9:
            print("{}{}".format(primero, segundo))
        else:
            print("{}{}".format(primero, segundo), end=", ")
