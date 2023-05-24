# Expreciones Regulares

# Match

import re #Primero debes impotar re (regular expression)

my_string = "Esta es la lección número 6: Lección Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Expresiones Regulares"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta es la lección", my_other_string)
# if not (match == None): # Otra manera de comprobar el none
# if match != None: # Otra manera de comprobar el none
if match is not None:
   print(match)
   start, end = match.span()
   print(my_other_string[start:end])

# print(re.match("Expresiones Regulares", my_string))

# Search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall

findall = re.match("lección", my_string, re.I)
print(findall)

# Split

print(re.split(":", my_string))

# Sub

print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("lección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))

# Patterns

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

email = "ivancarrizosap@gmail.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))