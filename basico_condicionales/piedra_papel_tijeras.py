"""
Desarrolla un algoritmo que permita recrear el juego de piedra,
papel o tijeras.

- El jugador debe poder ingresar la opción que desea jugar.
- La computadora deberá de elegir una opción de forma aleatoria.
- Utiliza el método randint():
    💡 from random import randint
        aleatorio = randint(1, 3)

- Debes mostrar por pantalla la opción que eligió el jugador y la que eligió
la computadora.
- Utiliza condicionales y operadores lógicos para definir quién ganó.
"""
from random import randint

# Constantes para las opciones del juego
PIEDRA, PAPEL, TIJERAS = "piedra", "papel", "tijeras"
OPCIONES = [PIEDRA, PAPEL, TIJERAS]


def elegir_aleatorio():
    # Devuelve una elección aleatoria entre piedra, papel o tijeras
    return OPCIONES[randint(0, 2)]


def obtener_eleccion_jugador():
    # Pide al jugador elegir entre piedra, papel o tijeras
    eleccion = input("Elija (piedra, papel, tijeras): ").lower()
    # Valida la elección del jugador
    while eleccion not in OPCIONES:
        eleccion = input("Opción inválida. Elija de nuevo: ").lower()
    return eleccion


def determinar_ganador(jugador, computadora):
    # Compara las elecciones para determinar el ganador
    if jugador == computadora:
        return "Empate"
    # Define las combinaciones ganadoras
    ganadores = {(PIEDRA, TIJERAS), (PAPEL, PIEDRA), (TIJERAS, PAPEL)}
    # Determina si el jugador ganó o perdió
    if (jugador, computadora) in ganadores:
        print("Soy el mejor")
        return "Jugador"
    else:
        print("Perdiste humano")
        return "Computadora"


def juego_de_piedra_papel_tijeras():
    victorias_jugador, victorias_computadora = 0, 0

    while max(victorias_jugador, victorias_computadora) < 4:
        jugador, computadora = obtener_eleccion_jugador(), elegir_aleatorio()

        ganador = determinar_ganador(jugador, computadora)
        if ganador == "Empate":
            print("Empate")
        elif ganador == "Jugador":
            victorias_jugador += 1
        else:
            victorias_computadora += 1

        print(f"Marcador - Jugador: {victorias_jugador}, "
              "Computadora: {victorias_computadora}")

    if victorias_jugador > victorias_computadora:
        print("¡El jugador ha ganado la serie!")
    else:
        print("¡La computadora ha ganado la serie!")

# Inicia el juego


juego_de_piedra_papel_tijeras()
