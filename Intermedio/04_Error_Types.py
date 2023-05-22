# Tipos de error

# SyntaxError

# print "Hola Mundo!" #SyntaxError
print("Hola Mundo!") #Bien escrita la sintaxis

# NameError
# print(variable) #NameError (No esta definida la variable)
variable = "Ahora esta definido"
print(variable) 

#IndexError

my_list = ["Python", "swift", "JavaScript", "C++"]
print(my_list[0])
print(my_list[3])
print(my_list[-1])
# print(my_list[4]) #IndexError (El indice 4 ya no existe en la lista)

# ModuleNotFoundError

# import maths #ModuleNotFoundError (El modulo importado no existe)
import math

#AttributeError

#print(math.PI) #AttributeError (El atributo "pi" esta mal escrito o no existe)
print(math.pi)

# KeyError

my_dict = {"Nombre": "Ivan", "Apellido": "Pérez", "Edad": 25, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) #KeyError (La clave dentro del diccionario no existe o esta mal escrita)

# TypeError
# print(my_list["Nombre"]) #TypeError (El indice en una lista debe ser de tipo integer no string)
print(my_list[0])

# ImportError

# from math import PI #ImportError (La función PI no existe o esta mal escrito)
from math import pi
print(pi)

# ValueError

my_int = int("10")
# my_int = int("10 Años") #ValueError ("Años" es imposible pasarlo a integer)
print(type(my_int))

# ZeroDivisionError

print(4/2)
# print(4/0) #ZeroDivisionError (Error unico cuando quieres dividir con 0)