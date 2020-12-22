# -*- coding: utf-8 -*-

class Terrestre:
  def desplazar(self):
    print("El animal se desplaza")

  def caminar(self):
    print("El animal camina")

class Acuatico:
  def nadar(self):
    print("El animal nada")

class Cocodrilo(Terrestre, Acuatico):
  pass

c = Cocodrilo()
c.desplazar()
c.caminar()
c.nadar()