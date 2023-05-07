# Diccionario

my_dict = dict()
other_dict = {} # Ambos son diccionarios pero no olvidar que los {} tambien son para los sets

other_dict = {"Nombre": "Ivan", "Apellido": "Pérez", "Edad": 25, 1: "Python"}

my_dict = {
    "Nombre": "Ivan", 
    "Apellido": "Pérez", 
    "Edad": 25, 
    "Lenguaje": {"Python", "Java", "C++"}
    }

print(other_dict)
print(my_dict)

print(len(other_dict)) #Saldrán 4 elementos
print(len(my_dict)) #También saldrán 4 elementos

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" # Para cambiar el dato
print(my_dict["Nombre"])

my_dict["Calle"] = "Tonantzin" # Para agregar un nuevo elemento
print(my_dict)

del my_dict["Calle"] # Aquí solo puedes eliminar usando del
print(my_dict)

print("Ivan" in my_dict)
print("Iván" in my_dict) # Ambas marcan false
print("Nombre" in my_dict) # Aquí si da true

print(my_dict.items()) # Retorna un listado del diccionario
print(my_dict.keys()) # Las keys son las claves dentro del diccionario
print(my_dict.values()) #Muestra los valores dentro de las claves

new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(new_dict) # Se crea un nuevo diccionario sin valores

# Se puede hacer un diccionario con una lista
my_list = ["Nombre", 1, "Piso"]
new_dict = dict.fromkeys((my_list))
print(new_dict)

new_dict = dict.fromkeys(my_dict, ("Ivan", "Perez"))
print(new_dict) # Así los datos se guardan en todas las claves