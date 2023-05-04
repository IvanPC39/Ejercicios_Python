# Listas

mi_lista = list()
otra_lista = [] # Las dos son listas

print(len(mi_lista))

mi_lista = [25, 20, 23, 30, 17, 25]
print(mi_lista)
print(len(mi_lista))

otra_lista = [25, 1.70, "Ivan", "Perez"] #Se puede guardar diferentes tipos de datos en una misma lista

print(otra_lista[0])
print(otra_lista[2])
print(otra_lista[-1])
print(otra_lista[-3])
print(mi_lista.count(25))

edad, altura, nombre, apellido = otra_lista
print(nombre)
print(edad)

print(mi_lista + otra_lista) #se pueden concatenar listas

otra_lista.append("Sora") #agrega nuevos elementos en la lista
print(otra_lista)

otra_lista.insert(1, "turquesa") #agrega nuevos elementos en la posición que quieras
print(otra_lista)

otra_lista.remove("turquesa") #Elimina elementos
print(otra_lista)

otra_lista.pop() #remueve el ultimo elemento pero no lo elimina
print(otra_lista.pop())
print(otra_lista)

otra_lista.pop(2) #Así eliges que elemento quitar
print(otra_lista)

del mi_lista[2] # eliminas el elemento
"""Con remove() eliminas un elemento que conoces y el del elimina por indice"""

mi_nueva_lista = mi_lista.copy()

mi_lista.clear() #Borra completamente la lista
print(mi_lista)
print(mi_nueva_lista)

mi_nueva_lista.reverse() # Invierte las posiciones de los elementos
print(mi_nueva_lista)

mi_nueva_lista.sort() #Por defecto ordena de menor a mayor
print(mi_nueva_lista)