#!/usr/bin/env python3
"""Demostración de herencia y polimorfismo."""


class Animal:
    """Clase base que representa un animal."""

    def speak(self):
        """Devuelve un sonido genérico."""
        return "Some sound"


class Dog(Animal):
    """Clase que representa un perro."""

    def speak(self):
        """Devuelve el sonido de un perro."""
        return "Woof"


class Cat(Animal):
    """Clase que representa un gato."""

    def speak(self):
        """Devuelve el sonido de un gato."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
