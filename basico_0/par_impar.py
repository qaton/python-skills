"""
Crea un programa que determine si un número es par o impar.
Deberá de obtener el dato a través de la consola.
Deberá mostrar el resultado por consola.
"""
def main():
    while True:
        entrada = input("Ingrese un número entero: ")
        if entrada.isnumeric():
            numero_usuario = int(entrada)
            break
        else:
            print("Por favor, ingrese un número entero válido")

    nro_par = numero_usuario % 2
    if nro_par == 0:
        print(f"El número ingresado {numero_usuario}, es par.")
    else:
        print(f"El número ingresado {numero_usuario}, no es par.")

# No borres esto 👇🏼
if __name__ == '__main__':
    main()
