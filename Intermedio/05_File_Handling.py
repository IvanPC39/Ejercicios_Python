# Manejo de ficheros

import os

# .txt file

txt_file = open("Intermedio/My_file.txt", "r+")
# La "r" significa que le permites leerlo "read()" si pongo "w" es que se pueda escribir
# r+ es para leer y escribir
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nPero siento que no estoy aprendiendo")
print(txt_file.read())

txt_file.close()

"""
txt_file = open("Intermedio/My_file.txt", "w+")

txt_file.write("Mi nombre es Ivan\nMi apellido es Carrizosa\nMi edad es 25 Anios\nEstoy aprendiendo Python")

txt_file.write("\nPero siento que no estoy aprendiendo")
print(txt_file.readline())

os.remove("Intermedio/My_file.txt")
# Aqui es un ejemplo de como seria crear el fichero en caso de que lo borrara o lo perdiera
y tambien de como eliminarlo despues de usarlo
"""

# .json file

import json

json_file = open("Intermedio/My_file.json", "w+")

json_test = {
    "name": "Ivan", 
    "surname": "Perez", 
    "age": 25, 
    "languages": ["Python", "Swift", "JavaScript"]
    }

json.dump(json_test, json_file, indent = 1)

json_file.close()

with open("Intermedio/My_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/My_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
import csv
# csv son tablas como las de excel o numbers
# Este ejemplo no lo registra bien excel y numbers creo que solo es de mac
csv_file = open("Intermedio/My_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Ivan", "Perez", "25", "Python"])

csv_file.close()

# .xlsx file
# import xlrd # Debe instalars el modulo

# xml file
import xml