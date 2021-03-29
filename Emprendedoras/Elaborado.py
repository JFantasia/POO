# Clase para los productos
from Producto import Producto

class Elaborado(Producto):
    def __init__(self,codigo,nombre,UM,emprendedora):
        super().__init__(codigo,nombre,UM)
        # Identificar el emprendedor/a del producto
        self.emprendedora = emprendedora
        # Referencia a la fórmula del producto
        self.formula = {}
    # El costo se calcula recorriendo cada uno de las materias primas de la formula y obteniendo el precio de la materia primas de la formula
    # se multiplica por la cantidad de esa materia prima para hacer el producto (cantidad en Componente).
    def costo(self):
        costo = 0
        for componente in self.formula:
            costo += float(self.formula[componente].prima.precio) * self.formula[componente].cantidad
            print("Carga de " + self.formula[componente].prima.nombre + " precio unitario " + str(self.formula[componente].prima.precio) + " cantidad " + str(self.formula[componente].cantidad) + " suma " + str(costo))
        return costo
