# Clases
# Para nombrar clases una buena practica es escribiendo en mayúscula las primeras letras, sin espacios y sin guión bajo

class MyEmptyPerson: #Para definir que es una clase
    pass # se usa para declarar un null y que se evite un error

print(MyEmptyPerson)
print(MyEmptyPerson())

# def _init_(self) debe escribirse asi para que sea un constructor de clase

class Person:
    def __init__(self, name, surname): # Sirve para crear un constructor de clase #Quitar el none para que pueda recibir parametros
        self.name = name
        self.surname = surname # Debes almacenar los valores para poder usarlos fuera de la clase

my_person = Person("Ivan", "Perez")
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): #El alias es el mismo ejemplo que en funciones
        self.full_name = f"{name} {surname} {alias}" # Otra manera de poder hacerse
    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Ivan", "Perez")
print(my_person.full_name)
my_person.walk()

