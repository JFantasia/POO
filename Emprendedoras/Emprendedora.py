# Clase para los emprendedores/as
class Emprendedora():
    def __init__(self,dni,nombre,apellido,email,emprendimiento,rubro):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.emprendimiento = emprendimiento
        self.rubro = rubro
        # Lista de productos que fabrica
        self.producto = {}