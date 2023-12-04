"""
Ya sé que te encantaron los palíndromos, así que vamos a practicar con
palíndromos más extensos. El objetivo de este programa es el mismo:
definir si una frase es palíndromo o no.

Muestra un mensaje indicando si la palabra es un palíndromo o no.

Ejemplos de palíndromos de una palabra:
Anita lava la tina
La ruta natural
No deseo yo ese don
"""

# ✨ Comienza tu código acá 👇🏼


def es_palindromo(frase):
    # Eliminar espacios y convertir a minúsculas
    frase = frase.replace(" ", "").lower()

    # Comparar la frase con su versión invertida
    if frase == frase[::-1]:
        return f"La frase '{frase}' es un palíndromo."
    else:
        return f"La frase '{frase}' no es un palíndromo."

# Prueba de la función con algunas frases


print(es_palindromo("Anita lava la tina"))
print(es_palindromo("La ruta natural"))
print(es_palindromo("No deseo yo ese don"))
