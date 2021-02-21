# -*- coding: utf-8 -*-

#importa la clase Persona
from persona import Persona
# Se importa la librería time de Python para trabajar con fechas
import time


class Estudiante(Persona):

    def __init__(self, v_legajo, v_dni, v_nombre, v_direccion, v_ciudad, v_provincia, v_pais, v_email, v_telefono):
        super().__init__(v_dni, v_nombre, v_direccion, v_ciudad, v_provincia, v_pais, v_email, v_telefono)
        self.legajo = v_legajo
        self.carreras = {}
        self.matriculaciones = {}
        print(type(self.carreras))

    def inscribir_carrera(self, v_codigo):
        # Desde python 3 no se usa el has_key sino el "in" o "not in"
        if(v_codigo in self.carreras):
            print("Ya se encuentra inscripto en la carrera " + v_codigo)
        else:
            self.carreras[v_codigo] = 1
            print("Acaba de inscribirse en " + v_codigo)

    def matricularse(self, v_codigo_carrera, v_codigo_materia):
        # Desde python 3 no se usa el has_key sino el "in" o "not in"
        if(v_codigo_carrera not in self.carreras):
            print("No está inscripto en la carrera " + v_codigo_carrera)
        else:
            if(v_codigo_materia in self.matriculaciones):
                print("Ya se encuentra matriculado en la materia " + v_codigo_materia)
            else:
                # matriculaciones es un diccionario que tiene como clave la materias
                # y una lista con información de fecha de matriculación y tres notas
                # para primer modulo del año, segundo módulo del año y final.
                self.matriculaciones[v_codigo_materia] = [time.strftime("%d/%m/%y"),0,0,0]
                print(self.matriculaciones)
                print("Acaba de matricularse en " + v_codigo_materia + " perteneciente a la carrera " + v_codigo_carrera)


est = Estudiante(123,22222222,"Juan","Paz 120","Tandil","Bs As","Argentina","juan@juan.ar",2494556677)
print(est)
print(est.nombre)
print(est.carreras)
est.inscribir_carrera("Arte")
print(est.carreras)
est.inscribir_carrera("Arte")
est.matricularse("Arte","Sacra")
est.matricularse("Matemática","Lógica")

