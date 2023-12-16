"""
FizzBuzz es un problema comúnmente utilizado en entrevistas de programación. El objetivo es imprimir una serie
de números desde 1 hasta un número dado, pero con algunas reglas especiales:

1. Si el número es divisible por 3, en lugar de imprimir el número, debes imprimir "Fizz".
2. Si el número es divisible por 5, en lugar de imprimir el número, debes imprimir "Buzz".
3. Si el número es divisible tanto por 3 como por 5, en lugar de imprimir el número, debes imprimir "FizzBuzz".

Tu tarea es escribir un programa que imprima la serie de números siguiendo estas reglas. A continuación, se muestra un ejemplo de cómo debería ser la salida para los números del 1 al 15:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

# ✨ Comienza tu código acá 👇🏼

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero

for numero in range(1, 16):  #crea una secuencia de números desde 1 hasta 15 (el último número, 16, no se incluye)
    print(fizzbuzz(numero))


mi_lista = 5
def longitud(mi_lista):
    cont = 0
    for _ in mi_lista:
        cont += 1
    return cont
