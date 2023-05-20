# Funciones de orden superior

from functools import reduce # Filter y Map si estan dentro de la especificación general de python pero Reduce no

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one(3, 6, sum_one))
print(sum_two_values_and_add_one(3, 6, sum_five))

# Closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))

# Built-in higher order funtion

numbers = [2, 5, 10, 21]

#Map
# Map recorre todos los valores y ejecuta una funcion sore ellos para modificar su valor

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
"""Filter recorre todos los valores y ejecuta una funcion que retorna True o False para saber como 
fitrar los valores del iterado"""

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
"""Reduce opera entre los valores que va recorriendo y va operando con los valores que va teniendo en cada caso 
a medida que vamos recorriendo el iterable"""

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers)) # Reduce ira sumando los valores hasta obtener un unico resultado