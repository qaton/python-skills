"""
Ya sé que te encantaron los palíndromos, así que vamos a practicar con palíndromos más extensos. El objetivo de este programa es el mismo: definir si una frase es palíndromo o no.

Muestra un mensaje indicando si la frase es un palíndromo o no.

Ejemplos de frases de palindromos:
A ti no bonita
Adan no cede con Eva y Yave no cede con nada
A luna ese anula
"""

# ✨ Comienza tu código acá 👇🏼
def frase_palindromo(frase):
    frase = frase.replace(" ", "") #reemplazamos los espacios por vacios
    frase_sin_espacios_minuscula = frase.lower() #convertimos a minuscula

    #método list conviente el string en una lista cada digito
    #método reserved modifical la secuencia original a una secuencia invertida
    return list(frase_sin_espacios_minuscula) == list(reversed(frase_sin_espacios_minuscula))

# Solicitar al usuario que ingrese una palabra
frase_usuario = input("Ingrese una frase para verificar si es un palíndromo: ")

# Verificar si la palabra es un palíndromo
if frase_palindromo(frase_usuario):
    print(f"La frase '{frase_usuario}' es un palíndromo.")
else:
    print(f"La frase '{frase_usuario}' no es un palíndromo.")
