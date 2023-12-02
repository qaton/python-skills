from random import randint

CONSTANTE = 1


def main():
    aleatorio = randint(1, 1000)
    print(aleatorio)

    if CONSTANTE == 1:
        print('Hola soy uno')

        if CONSTANTE != 5:
            no_acceso = "no se puede leer desde afuera"
            print("no soy un cinco")
            print(no_acceso)


def suma(val1, val2):
    print(val1 + val2)


class MiClase:

    def saludar(self):
        print('hola')


if __name__ == '__main__':
    valor1 = int(input("ingresa el primer número: "))
    valor2 = int(input("ingresa el segundo número: "))

    suma(valor1, valor2)
    suma(valor1 + 1, valor2 + 1)
    suma(valor1 - 1, valor2 - 1)
