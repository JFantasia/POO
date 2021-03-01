# -*- coding: utf-8 -*-

#Ejercicio 1: Convertir una cadena de texto con unidades de información a un diccionario

texto='123 libro 20;324 cuaderno 35;425 lápiz 50;284 regla 25'
lista_texto=texto.split(';')
print(lista_texto)
d={}
for e in lista_texto:
    # sepata la información de la lista de datos que esta separada por un espacio
    dato=e.split(' ')
    clave=int(dato[0])
    nomb=dato[1]
    cant=int(dato[2])
    # Crear la entreda en el diccionario
    d[clave]=[nomb,cant]
# Imprimir el diccionario de valores
print(d)


#Ejercicio 2: crear un diccionario con lectura de datos ingresados por pantalla
dic={}
n=int(input('Cuantos datos desea cargar: '))

# Itera la cantidad de veces ingresada para la carga de datos
for i in range(n):
    # Solicita datos
    cla=int(input('Clave: '))
    nom=input('Nombre: ')
    ed=int(input('Edad: '))
    # Crear la entreda en el diccionario
    dic[cla]=[nom,ed]
    print('\nSalida: ')

# Imprime los datos ingresados
for cod in dic:
    print('\nNombre: ',dic[cod][0])
    print('Edad:',dic[cod][1])


x=int(input('Clave para buscar: '))
# Consulta si la clave solicitada se encuentra como clave del diccionario
if x in dic:
    print('Nombre: ',dic[x][0])
    print('Edad:',dic[x][1])
else:
    print('No está')