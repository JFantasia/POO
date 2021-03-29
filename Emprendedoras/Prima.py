# Clase para las materias primas
from Producto import Producto

class Prima(Producto):
    def __init__(self,codigo,nombre,UM,precio):
        super().__init__(codigo,nombre,UM)
        self.precio = precio