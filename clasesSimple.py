# -*- coding: utf-8 -*-

class Instrumento:
  def __init__(self, precio):
    self.precio = precio
  def tocar(self):
    print("Estamos tocando musica")
  def romper(self):
    print ("Debes pagar ", self.precio, "$$$")


class Bateria(Instrumento):
	def romper(self, quecosa):
		print("Debes pagar " + quecosa + ", son ", self.precio, "pesos")

class Guitarra(Instrumento):
  pass


b = Bateria(900)
b.romper('parche')

g = Guitarra(100)
g.romper()