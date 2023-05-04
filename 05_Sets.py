#Sets

my_set = set()
otro_set = {} # asi solo el programa lo lee como un diccioneario
print(type(my_set))
print(type(otro_set))

otro_set = {25, "Ivan", "Perez"} # al definir las variables ya lo lee como un set
print(type(otro_set))

otro_set.add("Sora")
print(otro_set) # No tiene una estructura ordenada 
# por lo que no puedes acceder a los elementos dentro del set
otro_set.add("Ivan")
print(otro_set) # Un set no admite elementos repetidos

print("Sora" in otro_set)
print("Zora" in otro_set) # Asi se buscan los elementos dentro del set

otro_set.remove("Sora")
print(otro_set) #Se pueden remover elementos

otro_set.clear()
print(otro_set) #Igual funciona normal el clear

my_set = {25, "Ivan", "Perez"}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # Es arriesgado hacer esto ya que regresandolo a set se desordenaria el orde

otro_set = {20, "Juan", "Gonzales"}

nuevo_set = my_set.union(otro_set)
print(nuevo_set.union("Monse")) # Solo lo unes aqui pero no se agrega dentro del set

print(nuevo_set.difference(my_set))