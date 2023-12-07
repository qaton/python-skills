"""
Crea una función que reciba una palabra como entrada y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Muestra un mensaje indicando si la palabra es un palíndromo o no.

Ejemplos de palíndromos de una palabra: oso, ana, ojo, radar, orejero, reconocer
"""

# ✨ Comienza tu código acá 👇🏼
#texto = input("Ingresa palabra :")
#if str(texto) == str(texto)[::-1]:
 #   print ("Es palíndromo")
#else:
  #  print("No es palíndromo")
## codificación usando variables

def esta_palabra_es_palindromo(palabra):
    # método lower() convierte todas las letras en la cadena original en minúsculas
    palabra = palabra.lower()
    #función list() convierte la cadena     en    una    lista
    #función reversed() invierte una secuencia, como una cadena (string), lista, tupla o rango
    return list(palabra) == list(reversed(palabra))

ingreso_palabra = input("Ingresar palabra:   ")

if esta_palabra_es_palindromo(ingreso_palabra):
        print(f"esta palabra {ingreso_palabra} es un palindromo")
else:
        print(f"esta palabra {ingreso_palabra} no es un palindromo")






