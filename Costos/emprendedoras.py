# Clase para las materias primas
class Prima():
    def __init__(self,codigo,nombre,UM,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.um = UM
        self.precio = precio

# Clase para los componentes de la fórmula de un producto
# producto: atributo del producto padre
# prima: atributo de la materia prima de la fórmula
# cantidad: proporción por unidad de producto padre
class Componente():
    def __init__(self,producto,prima,cantidad):
        self.producto = producto
        self.prima = prima
        self.cantidad = cantidad

# Clase para los productos
class Producto():
    def __init__(self,codigo,nombre,UM,emprendedora):
        self.codigo = codigo
        self.nombre = nombre
        self.um = UM
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


class Sistema():

    # Representaciones de los datos de registros de bases de datos
    # Notar las tablas en función de si es 1 a N o N a N y como son las referencias de los campos

    d_emprendedoras = ["1,Julio,Lopez,julio@lopez.ar,La cocina de Julio,Gastronomía",
                       "2,Juliana,Roig,juliana@roig.ar,Mederitas,Carpintería",
                       "3,Luis,Luque,luis@luque.ar,Amasado,Gastronomía",
                       "4,Juana,De Arco,juana@dearco.ar,El caballo de Juana,Juguetes"]

    d_productos = ["1,Tortilla,Unidad,1",
                   "2,Pizza,Unidad,1",
                   "3,Cubo,Unidad,2",
                   "4,Mesa,Unidad,2",
                   "5,Pan,Kg,3"]

    d_primas = ["1,Papa,Kg,80",
                "2,Huevos,Unidad,10",
                "3,Cebolla,Kg,60",
                "4,Levadura,Kg,600",
                "5,Sal,Kg,100",
                "6,Placa,Mts2,700",
                "7,Tornillo,Unidad,5",
                "8,Masilla,Kg,250",
                "9,Harina,Kg,45",
                "10,Liston 10x10,Mts,100"]

    d_formulas = ["1,1,0.4",
                  "1,2,3",
                  "1,3,0,3",
                  "1,5,0.5",
                  "2,9,0.2",
                  "2,4,0.05",
                  "2,5,0.05",
                  "3,6,1",
                  "3,7,12",
                  "3,8,0.2"]

    def __init__(self):
        print("Bienvenide al sisrema de costos de emprendedores")
        self.emprendedoras = {}
        self.productos = {}
        self.primas = {}
        self.inicializar()

    def inicializar(self):
        print("Inicializando Sistema")
        print("Cargando emprendedores")
        for emprendedora in self.d_emprendedoras:
            datos = emprendedora.split(",")
            v_emprendedora = Emprendedora(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
            self.emprendedoras[v_emprendedora.dni] = v_emprendedora
        print("Cargando productos")
        for producto in self.d_productos:
            datos = producto.split(",")
            v_producto = Producto(datos[0],datos[1],datos[2],datos[3])
            self.productos[v_producto.codigo] = v_producto
            # Busca y agrega el producto al emprendero/a que corresponda
            v_emp = self.emprendedoras[v_producto.emprendedora]
            v_emp.producto[v_producto.codigo] = v_producto
            self.emprendedoras[v_producto.emprendedora] = v_emp
            print("Agregando producto " + v_producto.nombre + " a " + v_emp.nombre)
        print("Cargando materias primas")
        for prima in self.d_primas:
            datos = prima.split(",")
            v_prima = Prima(datos[0], datos[1], datos[2], int(datos[3]))
            self.primas[v_prima.codigo] = v_prima
            print("Agregando prima " + v_prima.nombre)
        print("Cargando fórmulas")
        for item in self.d_formulas:
            datos = item.split(",")
            v_producto = self.productos[datos[0]]
            v_prima = self.primas[datos[1]]
            v_componente = Componente(v_producto, v_prima, float(datos[2]))
            # Ingreso el componente en el diccionario de formula con la clave de la materia prima
            v_producto.formula[datos[1]] = v_componente
            self.productos[datos[0]] = v_producto
            print("Agregando prima " + v_prima.nombre + " a " + v_producto.nombre)

        for producto in self.productos:
            print("Costo de " + self.productos[producto].nombre + " es " + str(self.productos[producto].costo()))


inicio = Sistema()

