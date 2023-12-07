"""
Escribe un programa que permita al usuario ingresar una temperatura en grados Celsius.

Luego, convierte esta temperatura a grados Fahrenheit utilizando la fórmula:
Fahrenheit = (Celsius * 9/5) + 32 y muestra el resultado.
Muestra el resultado en la terminal.
"""

# ✨ Comienza tu código acá 👇🏼

#celsius = int(input("ingresa temperatura en ° celcius: "))
#Fahrenheit = (celsius * 9/5) + 32
#print(Fahrenheit)

#codificar usando funciones y variables

def convertir_celcius_a_farenheit(celcius):
    return (celcius * 9/5) +32

def ingresar_temperatura():
    while True:
        entrada_temperatura_celcius = input("Ingrese temperatura en celcius: ")
        try:
            temperatura_usuario = float(entrada_temperatura_celcius)
            temperatura_farenheit = convertir_celcius_a_farenheit(temperatura_usuario)
            print(f"La temperatura {temperatura_usuario} en grados celcius, son {temperatura_farenheit} grados farenheit")
        except ValueError:
            print("Ingrese dato valido de temperatura")

ingresar_temperatura()




