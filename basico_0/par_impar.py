"""
Crea un programa que determine si un número es par o impar.
Deberá de obtener el dato a través de la consola.
Deberá mostrar el resultado por consola.
"""


def main():

    """
    ✨ Comienza tu código acá 👇🏼
    """
def pedir_numero():
    numero = int(input("Ingrese un numero entero:    "))
    return numero
def es_par(digitos):
    if digitos % 2 == 0:
        print("es par")
    else:
        print("no es par")

numero = pedir_numero()
es_par(numero)

# No borres esto 👇🏼
if __name__ == '__main__':
    main()
