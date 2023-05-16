# Funciones

def  my_function (): # Para definir una función
    print("Esto es una función")

my_function ()
my_function ()

def sum_two_values (first_value, second_value): #Dentro del parentesis puedes agregar los parametros
    print(first_value + second_value)

sum_two_values(5, 4) # al llamar la función debes darles valor a los parametros
sum_two_values(14, 25)
sum_two_values("3", "9")
sum_two_values(1.3, 2.9)

def sum_two_values_with_return (first_value, second_value): 
    return first_value + second_value #para imprimir el resultado es necesario asignarlo a una variable

""" def sum_two_values_with_return (first_value, second_value):
        my_sum = first_value + second_value 
        return my_sum """

my_result = sum_two_values_with_return(10, 5)
print(my_result)

my_result = sum_two_values(14, 25)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Perez", "Ivan")
print_name(surname="Perez", name="Ivan")

def print_name_with_default(name, surname, nickname = "sin nickname"): #puedes darle un valor por efecto 
    print(f"{name} {surname} {nickname}")

print_name_with_default("Ivan", "Perez", "Sora")
print_name_with_default("Ivan", "Perez") #Si no le das el valor por defecto saldra el que ya le diste anteriormente

def print_texts(*texts):#Agregando el * puedes agregar varios valores 
    print(texts)

print_texts("Hola", "Python", "Ivan")

def print_texts(*texts):
    for text in texts: 
        print(text)

print_texts("Hola", "Python", "Ivan")