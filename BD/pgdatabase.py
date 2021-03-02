import sys

# https://www.psycopg.org/install/

import psycopg2
from psycopg2 import Error

# TABLA DE LA BASE DE DATOS
#
# CREATE TABLE public.profesor (
# 	dni varchar(8) NOT NULL,
# 	nombre varchar(40) NOT NULL,
# 	mail varchar(50) NULL,
# 	CONSTRAINT profesor_pk PRIMARY KEY (dni)
# );


class DB():

    def __init__(self, parent=None):
        self.cursor = self.db_connect()

    def cargar(self):
        self.cursor.execute("SELECT * FROM profesor ORDER BY DNI asc;")
        # Fetch result
        records = self.cursor.fetchall()
        for row in records:
            dni = row[0]
            nombre = row[1]
            correo = row[2]
            print(dni + " " + nombre + " " + correo)

    def editarDatos(self):

        ids = input("Ingrese el identificador: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")

        try:
            # Executing a SQL query
            self.cursor.execute("UPDATE profesor "
                                "set nombre = '" + nombre + "' , "
                                "mail = '" + correo + "' "
                                "where dni = '" + ids + "'; ")

            self.connect.commit()
            self.cargar()

        except (Exception, Error) as error:
            print("Mapea error")
            self.connect.rollback()
            print("Error while update to PostgreSQL", error)


    def insertarDatos(self):
        ids = input("Ingrese el identificador: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")

        try:
            # Executing a SQL query
            self.cursor.execute("INSERT INTO profesor "
                                "(dni, nombre, mail) "
                                "VALUES ('" + ids + "', '" + nombre + "', '" + correo + "');")
            self.connect.commit()
            self.cargar()

        except (Exception, Error) as error:
            print("Mapea error")
            self.connect.rollback()
            print("Error while insert to PostgreSQL", error)

    def eliminarDatos(self):

        ids = input("Ingrese el identificador a eliminar: ")

        try:
            # Executing a SQL query
            self.cursor.execute("DELETE FROM profesor where dni = '" + ids + "';")
            self.connect.commit()
            self.cargar()

        except (Exception, Error) as error:
            self.connect.rollback()
            print("Error while delete to PostgreSQL", error)


    def db_connect(self):
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="poo")

            # Create a cursor to perform database operations
            self.connect = connection
            cursor = connection.cursor()
            return cursor

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)



if __name__ == '__main__':
    base = DB()
    base.cargar()
    base.eliminarDatos()
    base.insertarDatos()
    base.editarDatos()

