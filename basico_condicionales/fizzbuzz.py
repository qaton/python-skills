"""
FizzBuzz es un problema comúnmente utilizado en entrevistas de programación.
El objetivo es imprimir una serie de números desde 1 hasta un número dado,
pero con algunas reglas especiales:

1. Si el número es divisible por 3, en lugar de imprimir el número,
debes imprimir "Fizz".
2. Si el número es divisible por 5, en lugar de imprimir el número,
debes imprimir "Buzz".
3. Si el número es divisible tanto por 3 como por 5,
en lugar de imprimir el número,
debes imprimir "FizzBuzz".

Tu tarea es escribir un programa que imprima la serie de números siguiendo
estas reglas.
A continuación, se muestra un ejemplo de cómo debería ser la salida para
los números del 1 al 15:

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


for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
