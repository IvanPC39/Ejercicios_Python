# If

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecución continúa") 

my_condition = False

if my_condition:
    print("Se ejecuta la condición del primer if") 

print("La ejecución continúa") 

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta el tercer if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25") 
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa") 

my_string = "" #El string vacío lo toma como false

if not my_string: # Agregando not se esta cumpliendo la condición por lo que pasa a ser true
    print("Mi cadena de texto es vacía")

my_string = "Mi cadena de texto" 

if my_string:
    print("Mi cadena de texto no es vacía")

if my_string == "Mi cadena de texto":
    print("Mi cadena de texto coincide")