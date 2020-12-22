# -*- coding: utf-8 -*-

class Direccion:
	
	# definición de atributos de clase, son aquellos comunes a todas las instancias
	
	local = 'Tandil'
	
	# self es una convención y es una referencia al objeto que estamos creando
	# en la llamada al objeto no es necesario poner self, se recibe de forma implícita

	def __init__(self, calle, nro, piso, dpto, ciudad, provincia, pais):
		# definición de atributos de instancia, son aquellos específicos de cada instancia
		self.calle = calle
		self.nro = nro
		self.piso = piso
		self.dpto = dpto
		self.ciudad = ciudad
		self.provincia = provincia
		self.pais = pais

	def esLocal(self):
		if self.ciudad == self.local:
			return True
		else:
			return False

class Persona:
	
	# self es una convención y es una referencia al objeto que estamos creando
	# en la llamada al objeto no es necesario poner self, se recibe de forma implícita
	
	def __init__(self, nombre, apellido, sexo, 
		dni, email, celular, calle, nro, piso, dpto, 
		ciudad, provincia, pais):
	
		self.nombre = nombre
		self.apellido = apellido
		self.sexo = sexo
		self.dni = dni
		self.email = email
		self.celular = celular
		# Agregacion >> Persona tiene un atributo que es un objeto Dirección
		self.direccion = Direccion(calle, nro, piso, dpto, ciudad, provincia, pais)

	# def __str__(self):
	# 	return (self.nombre + ' ' + self.apellido)

	def esLocal(self):
		return self.direccion.esLocal()




luca = Persona('Luca', 'Fantasia', 'M', '52788700', 'luca@gmail.com', '2494380999', 'SS', 3070, '', '', 'Tandil', 'BsAs', 'Argentina')

print (luca)
print (luca.nombre)
print (luca.direccion)

if luca.esLocal():
	print ('Luca es tandilense')
else:
	print ('Luca es de afuera')