"""
Crea una función que reciba una palabra como entrada y
determine si es un palíndromo (se lee igual de izquierda a derecha
que de derecha a izquierda).

Muestra un mensaje indicando si la palabra es un palíndromo o no.

Ejemplos de palíndromos de una palabra:
oso, ana, ojo, radar, orejero, reconocer
"""

# ✨ Comienza tu código acá 👇🏼


def es_palindromo(palabra):
    # Eliminar espacios y convertir a minúsculas para una comparación precisa
    palabra = palabra.replace(" ", "").lower()

    # Comparar la palabra con su versión invertida
    if palabra == palabra[::-1]:
        return f"La palabra '{palabra}' es un palíndromo."
    else:
        return f"La palabra '{palabra}' no es un palíndromo."

# Prueba de la función con algunas palabras


print(es_palindromo("oso"))
print(es_palindromo("ana"))
print(es_palindromo("palabra"))
