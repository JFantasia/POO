# -*- coding: utf-8 -*-

#Ejercicio: Convertir una cadena de texto con unidades de información a un diccionario

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
    d[clave]=[nomb,cant]
# Imprimir el diccionario de valores
print(d)


dic={}
n=int(input('Cuantos datos desea cargar: '))

for i in range(n):
    cla=int(input('Clave: '))
    nom=input('Nombre: ')
    ed=int(input('Edad: '))
    dic[cla]=[nom,ed]
    print('\nSalida: ')

for cod in dic:
    print('\nNombre: ',dic[cod][0])
    print('Edad:',dic[cod][1])

x=int(input('Clave para buscar: '))
if x in dic:
    print('Nombre: ',dic[x][0])
    print('Edad:',dic[x][1])
else:
    print('No está')