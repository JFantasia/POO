# Declaramos nuestra clase
# class Animal(object):

#     # Primer método
#     def setName(self, name):
#         self.name = name

#     # Segundo método
#     def getName(self):
#         return self.name

# animal = Animal() # Instancia de nuestra clase
# animal.setName("Perro") # Asignación de nombre
# print(animal.getName())


import abc
from abc import ABC


# Declaramos nuestra clase
class Animal(ABC):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Primer método
    # Decorador para métodos absctractos
    @abc.abstractmethod
    def setNombre(self, nombre):
        self.nombre = nombre

    # Segundo método
    # Decorador para métodos absctractos
    @abc.abstractmethod
    def getNombre(self):
        return self.nombre


class Perro(Animal):
    """docstring for Perro"""
    tipo = "domestico"

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre


an = Perro('Nombre Antes', 32)
print(an.nombre)
an.nombre = 'Nombre Luego'
print(an.nombre)
print(an.tipo)

# animal = Animal()
