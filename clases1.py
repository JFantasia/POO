class Persona:
    especie = 'Humano/a'

    def __init__(self, nombre, dni, pais):
        self.nombre = nombre
        self.dni = dni
        self.pais = pais

    # Devuelve una cadena representativa de Persona
    def __str__(self):
        return (self.nombre + ' de ' + self.pais)

    def esExtranjera(self):
        if self.pais != 'Argentina':
            print("Es una persona Extranjera")
            return True
        else:
            print("Es una persona Argentina")
            return False


# Instancias de una clase >> objeto CONCRETO en memoria
silvia = Persona("Silvia", 20788650, 'Argentina')
print(silvia)
fidel = Persona("Fidel", 20788650, 'Uruguay')

print('Hola soy ' + silvia.nombre + ' y soy de ' + silvia.pais + ' y soy ' + silvia.especie)
print('Hola soy ' + fidel.nombre + ' y soy de ' + fidel.pais + ' y soy ' + fidel.especie)

print(fidel.esExtranjera())
