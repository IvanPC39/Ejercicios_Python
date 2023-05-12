#Excepciones
### Mecanismos para prevenir errores

num_one = 3
num_two = 9
num_two = "9"

# try except
try:
    print(num_one + num_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error") 

# try except else finally
try:
    print(num_one + num_two)
    print("No se ha producido un error")
except:#Si hay un try debe haber un except
    print("Se ha producido un error") 
else:#Opcional ponerlo
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:#Opcional ponerlo
    #Se ejecuta siempre
    print("La ejecución continúa")

# excepciones por tipo
### Estos son para evitar errores muy concretos
try:
    print(num_one + num_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError") 
except TypeError: 
    print("Se ha producido un TypeError") 

# Captura de la información de la excepción
try:
    print(num_one + num_two)
    print("No se ha producido un error")
except ValueError as error: # --- as Nombre Variable
    print(error) 
except Exception as error:
    print(error)
    