# Loops/Bucles
#Iterar significa repetir algo en este caso es pasar por el codigo varias veces (en bucle)

# Loop While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # El += es para incrementar el número cada que se repita la condición
else: # Else dentro de un while no todos los lenguajes lo tienen pero es opcional su uso
    print("Mi condición es mayor o igual a 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Se detiene la ejecución")   
        break
    print("Mi condición es menor que 20")

print("La ejecución continua")

# Bucle For
# Sirve para iterar un listado de elementos

my_list = [25, 23, 20, 52, 30, 17]

"""
Sintaxis del for: for Nombre de los valores in variable 
en c++ y java el "nombre de los valores" lo llamaba i
"""
for element in my_list:
    print(element)

my_tuple = (35, 1.70, "Ivan", "Perez")

for element in my_tuple:
    print(element)

my_set = {25, "Ivan", "Perez"}

for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Ivan", 
    "Apellido": "Pérez", 
    "Edad": 25, 
    "Lenguaje": {"Python", "Java", "C++"}
    }

for element in my_dict:
    print(element)# En el diccionario imprime las keys no los valores
    if element == "Edad":
        break
else: # Si se usa el break ya no se ejecuta else
     print("El bucle for para el diccionario a finalizado")

"""for element in my_dict.values(): ## Agregando el .values() si imprimiría los valores y no las keys
    print(element)"""

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Cuando se cumple la condición continua imprimiendo el for pero sin imprimir lo que haya debajo
    print("Se ejecuta")
else: 
    print("El bucle for para el diccionario a finalizado")