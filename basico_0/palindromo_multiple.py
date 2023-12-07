"""
Ya sé que te encantaron los palíndromos, así que vamos a practicar con palíndromos más extensos. El objetivo de este programa es el mismo: definir si una frase es palíndromo o no.

Muestra un mensaje indicando si la palabra es un palíndromo o no.

Ejemplos de palíndromos de una palabra:
"""

#"Anita lava la tina"  La ruta natural", No deseo yo ese don"

# ✨ Comienza tu código acá 👇🏼

def esta_frase_es_palindromo(frase):
    # método lower() convierte todas las letras en la cadena original en minúsculas
    # metodo replace() crea una nueva cadena con los reemplazos y no modifica la cadena original
    ## NOTA: Las cadenas en Python son inmutables ¡¡
    # por lo que debes asignar el resultado a una nueva variable si deseas conservar la cadena modificada

    frase = frase.replace(" ", "")
    frase_sin_espacios = frase.lower()

    #función list() convierte la cadena     en    una    lista
    #función reversed() invierte una secuencia, como una cadena (string), lista, tupla o rango
    return list(frase_sin_espacios) == list(reversed(frase_sin_espacios))

ingreso_frase = input("Ingresar frase:   ")

if esta_frase_es_palindromo(ingreso_frase):
        print(f"esta frase {ingreso_frase} es un palindromo")
else:
        print(f"esta frase {ingreso_frase} no es un palindromo")
