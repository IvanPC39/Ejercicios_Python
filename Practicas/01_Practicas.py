"""
EL FAMOSO "FIZZ BUZZ" (Fácil)
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101): # index es por indice # en range si imprime el primer numero pero excluye el ultimo por eso puse 101
        if index % 3 == 0 and index % 5 == 0:
            print("fizbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()


"""
¿ES UN ANAGRAMA? (Media)
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
 """

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor", "Omar"))
print(is_anagram("Amor", "Amor"))
print(is_anagram("Amor", "Roma"))


"""
LA SUCESIÓN DE FIBONACCI (Difícil)
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1

    for index in range(1, 51):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()



"""
¿ES UN NÚMERO PRIMO? (Media)
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():

    for number in range(1, 101):
        
        if number >= 2:
           is_divisible = False
        
           for index in range(2, number):
               if number % index == 0:
                   is_divisible = True
                   break
               
           if not is_divisible:
               print(number)
                      
is_prime()    


"""
INVIRTIENDO CADENAS (Fácil)
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    text_len = len(text)
    reverse_text = ""
    for index in range(0, text_len):
        reverse_text += text[text_len - index - 1]
    return reverse_text

print(reverse("Hola mundo"))   


"""
ÁREA DE UN POLÍGONO (Fácil)
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def poligono(base, height):
    
    if base == height:
        result = base * height
        print("El area del caudrado es: " + str(result))
        return result
    elif base > height:
        result = base * height
        print("El area del rectangulo es: " + str(result))
        return result
    elif base < height:
        result = (base * height) / 255
        print("El area del triangulo es: " + str(result))
        return result
    else:
        print("Esto no es un cuadrado, triangulo o rectangulo")

base = int(input("Base: "))
height = int(input("Altura: "))

poligono(base, height)
