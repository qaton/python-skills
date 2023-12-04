"""
Escribe un programa que permita al usuario ingresar una
temperatura en grados Celsius.

Luego, convierte esta temperatura a grados Fahrenheit utilizando la fórmula:
Fahrenheit = (Celsius * 9/5) + 32 y muestra el resultado.
Muestra el resultado en la terminal.
"""

# ✨ Comienza tu código acá 👇🏼

# Pide al usuario que ingrese la temperatura en Celsius
temperatura_celsius = float(input("Ingrese temperatura en grados Celsius: "))

# Convierte la temperatura a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Muestra el resultado
print(f"Temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")
