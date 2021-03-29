# Clase para los componentes de la fórmula de un producto
# producto: atributo del producto padre
# prima: atributo de la materia prima de la fórmula
# cantidad: proporción por unidad de producto padre
class Componente():
    def __init__(self,producto,prima,cantidad):
        self.producto = producto
        self.prima = prima
        self.cantidad = cantidad