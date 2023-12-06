"""
Escribe un programa que permita al usuario ingresar una temperatura en grados Celsius.

Luego, convierte esta temperatura a grados Fahrenheit utilizando la fórmula:
Fahrenheit = (Celsius * 9/5) + 32 y muestra el resultado.
Muestra el resultado en la terminal.
"""

# ✨ Comienza tu código acá 👇🏼


def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def principal_temperatura():
    while True:
        entrada_temperatura_celsius = input("Ingrese la temperatura en grados Celsius: ")

        try:
            temperatura_usuario = float(entrada_temperatura_celsius)
            temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_usuario)
            print(f"La temperatura {temperatura_usuario} grados Celsius, son {temperatura_fahrenheit} grados Fahrenheit.")
        except ValueError:
            print("Por favor, ingrese temperatura válida.")
principal_temperatura()
