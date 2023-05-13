# Modules
### Los ficheros no pueden llevar números en el nombre
import module
# from 09_Funciones import sum_two_values ## Esto da error por el número en el nombre

module.sum(3, 9, 1)
module.printValue("Hola Python")

from module import sum, printValue

sum(3, 9, 1)
printValue("Hola Python")

# Modulos creados en el sistema (pandas, math, etc)

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value 

print(pi_value)