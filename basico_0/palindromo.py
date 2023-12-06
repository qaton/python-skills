"""
Crea una función que reciba una palabra como entrada y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Muestra un mensaje indicando si la palabra es un palíndromo o no.

Ejemplos de palíndromos de una palabra: oso, ana, ojo, radar, orejero, reconocer
"""

# ✨ Comienza tu código acá 👇🏼
# Definición de la función para verificar si una palabra es un palíndromo


def es_palindromo(palabra):
    palabra = palabra.lower() #convierto a minuscula
    #método list conviente el string en una lista cada digito de la palabra
    #método reserved modifical la secuencia original a una secuencia invertida
    return list(palabra) == list(reversed(palabra))

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Verificar si la palabra es un palíndromo
if es_palindromo(palabra_usuario):
    print(f"La palabra '{palabra_usuario}' es un palíndromo.")
else:
    print(f"La palabra '{palabra_usuario}' no es un palíndromo.")
