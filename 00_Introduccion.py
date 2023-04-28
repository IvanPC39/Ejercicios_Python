# Aunque ya conozco lo basico prefiero tenerlo guardado en un solo archivo c:
""" 
Aqui guardare desde el "Hola Mundo" 
pero no se hasta donde lo dejare
"""
# Hola Mundo
print("Hola Mundo!!")

# Consultar tipo de dato
print(type("Soy un string")) #Tipo str
print(type(39)) #Tipo int # No metere los demas tipos de dato para no tener demasiadas lineas de codigo 

# Variables
variable_str = "Es un string" """ Recuerda que en Python no es necesario agregar el tipo de dato a la variable 
como en otros lenguajes y tampoco poner ; al final de cada codigo
"""
variable_int = 39

variable_bool = True # variable tipo boolean y solo regresa true o false
print(variable_str, variable_int, variable_bool)

varaible_int_a_string = str(variable_int) # Hay muchas mas funciones integradas ademas de str(), int(), type() o input()
print(varaible_int_a_string, type(varaible_int_a_string))

# Multiples variables en una sola linea
nombre, apellido, edad = "Ivan", "Perez Carrizosa", 25 #Es otra manera de escribir las variables pero no se recomienda hacerlo asi
print("Me llamo", nombre, apellido, "y tengo", edad, "años")

# input
nombre = input("¿Cual es tu nombre? ")
edad = input("¿Cual es tu edad? ") 