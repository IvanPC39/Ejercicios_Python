# Strings

mi_string = "Mi string"
mi_otro_string = "Otro string"

print(len(mi_string))
print(len(mi_otro_string))
print(mi_string + " " + mi_otro_string)

line_string = "Es otro string\ncon salto de linea"
print(line_string)
tab_string = "\tEs un string tabulado"
print(tab_string)
scape_string = "\\tEs un string \\n escapado" #con doble barra \\ ya no hace caso al tab ni al salto de linea
print(scape_string)

#Formateo
"""Para formatear se usa el operador %
%s - String
%d - Integers
%f - Floating
"%.number of figitsf" - Floating with fixed precision"""

nombre, apellido, edad = "Ivan", "Perez", 25

print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad)) #Se usa {} si quiers que se imprima el dato tal cual esta
print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad)) #se usa % si trabajas con el dato formateado
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}") #Inferencia de datos (es mejor usar este, si se esta formateando es preferible usar %)

#Desempaquetado de caracteres
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(f)

#División

segmento_lenguaje = lenguaje[1:3]
print(segmento_lenguaje)
segmento_lenguaje = lenguaje[-2]
print(segmento_lenguaje)

#Invertida
lenguaje_reversa = lenguaje[::-1]
print(lenguaje_reversa)

#Funciones

print(lenguaje.capitalize()) #La primer letra será mayúscula
print(lenguaje.upper()) #Todas las letras serán mayúsculas
print(lenguaje.count("y")) #Cuanta cuantas "y" hay en la varaible  
print(lenguaje.isnumeric()) #Te dice si es o no un número
print("39".isnumeric()) 
print(lenguaje.lower()) #Todas las letras serán minusculas
print(lenguaje.upper().isupper())#Se pueden combinar y isupper es para saber si esta en upper o no