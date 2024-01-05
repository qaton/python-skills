"""
Crea un programa que determine si un número es par o impar.
Deberá de obtener el dato a través de la consola.
Deberá mostrar el resultado por consola.
"""


def main():
    """
    ✨ Comienza tu código acá 👇🏼
    """

# Pide al usuario que ingrese un número


numero = int(input("Ingresa un número: "))

# Determina si el número es par o impar


if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


# No borres esto 👇🏼
if __name__ == '__main__':
    main()
