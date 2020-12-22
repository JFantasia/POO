class Persona:
     def __init__(self):
          self._edad = 0
       
     # using property decorator
     # a getter function
     @property
     def edad(self):
         print("Recupera pasando por Get")
         return self._edad
       
     # a setter function
     @edad.setter
     def edad(self, anios):
         print("Actualiza pasando por Set")
         self._edad = anios
  
juan = Persona()
  
juan.edad = 19
  
print("La edad de Juan es " + str(juan.edad))