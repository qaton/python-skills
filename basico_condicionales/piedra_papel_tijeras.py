"""
Desarrolla un algoritmo que permita recrear el juego de piedra, papel o tijeras.

- El jugador debe poder ingresar la opción que desea jugar.
- La computadora deberá de elegir una opción de forma aleatoria.
- Utiliza el método randint():
    💡 from random import randint
        aleatorio = randint(1, 3)

- Debes mostrar por pantalla la opción que eligió el jugador y la que eligió la computadora.
- Utiliza condicionales y operadores lógicos para definir quién ganó.
"""

import random
def obtener_jugada_usuario():
    print(" \n 1. Piedra \n 2. Papel \n 3. Tijera \n ")
    jugada_usuario= int(input("Selecciona la opción que desees jugar:"))

    if jugada_usuario == 1:
        print("Elegiste: Piedra")
    elif jugada_usuario == 2:
        print("Elegiste: Papel")
    elif jugada_usuario == 3:
        print("Elegiste: Tijera")
    else:
        print("Ingresa una opción válida")

    return jugada_usuario

def obtener_jugada_computadora():
    jugada_computadora = random.randint(1, 3)

    if jugada_computadora == 1:
        print("La computadora eligió: Piedra")
    elif jugada_computadora == 2:
        print("La computadora eligió: Papel")
    else:
        print("La computadora eligió: Tijera")
    return jugada_computadora

def obtener_ganador(jugada_usuario, jugada_computadora):

    if jugada_usuario == jugada_computadora:
        return "Empataron"
    elif (jugada_usuario == 1 and jugada_computadora == 3) or (jugada_usuario == 2 and jugada_computadora == 1) or (jugada_usuario == 3 and jugada_computadora == 2):
        return "Resultado: Ganaste"
    else:
        return "Resultado: Perdiste"

def jugar():
    jugada_usuario = obtener_jugada_usuario()
    jugada_computadora = obtener_jugada_computadora()
    resultado = obtener_ganador(jugada_usuario, jugada_computadora)
    print(resultado)

jugar()
