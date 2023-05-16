# Tuples

my_tuple = tuple()
otra_tuple = () #Los dos son lo mismo

my_tuple = (35, 1.70, "Ivan", "Perez")
otra_tuple = (25, 60, 39)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
"""
Son parecidas las listas y las tuplas pero no son lo mismo
y se ocupan para diferentes cosas, las tuplas son valores constantes
mientras que las listas te permiten modificar sus indices
"""

print(my_tuple.count("Ivan"))
print(my_tuple.index("Perez")) #Te dice en que indice se encuentra el valor
"""
Index y Count son las unicas operaciones que se pueden hacer
con tuple a diferencia de las listas
"""
### my_tuple[1] = 1.80
### print(my_tuple) #Marcará error ya que en una tuple no se permite modificar el valor como en las listas

nueva_tupla = my_tuple + otra_tuple
print(nueva_tupla)

print(nueva_tupla[3:6])

# Si en dado caso de necesitar modificar una tuple seria asi:

my_tuple = list(my_tuple)
print(type(my_tuple)) # Los type() son para mostrar que si cambio a lista y despues a tupla

my_tuple[2] = "Negi"
my_tuple.insert(1, "Turquesa")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2]
"""
Marcará error ya que al igual que no se puede modificar el valor
no se pueden eliminar pero si puedes borrar completamente la tupla:
# del my_tuple si borraría todo
"""