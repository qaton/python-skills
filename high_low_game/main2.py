import random
from art import logo
from art import vs
from game_data import data
#from replit import clear
import os

score = 0 #Se declara la variable score que llevara la cuenta de los aciertos del jugador
def crear_user():
    user = random.choice(data) #seleccionamos el usuario aleatorio del archivo data, para el usuario
    name = user["name"]
    description = user["description"]
    country = user["country"]
    follower = user["follower_count"]
    #print(f'Usuario es {name}, es {description}, de {country} y tiene {follower} seguidores.')
    return name, description, country, follower

def juego():

    score = 0
    name_user_a, description_user_a, country_user_a, follower_user_a = crear_user()

    while True:

        print(logo)
        print(f'Compara el usuario A: {name_user_a}, quien es: {description_user_a}, de {country_user_a} y tiene {follower_user_a} seguidores.')

        name_user_b, description_user_b, country_user_b, follower_user_b = crear_user()

        if name_user_a == name_user_b:# Evitar usuarios iguales
            name_user_b, description_user_b, country_user_b, follower_user_b = crear_user()

        print(vs)

        print(f'Contra usuario B: {name_user_b}, quien es: {description_user_b}, de {country_user_b}, y tiene {follower_user_b} seguidores.')


        option_elegida = input("¿Quién crees que tenga mas seguidores? Escribe A o B: ").upper()


        if (option_elegida == "A" and follower_user_a > follower_user_b) or (option_elegida == "B" and follower_user_b > follower_user_a) :
            score += 1
            if option_elegida=="A":
                ganador = name_user_a
            else:
                ganador = name_user_b
            print(f"Acertaste! El ganador es {ganador}, tu puntuación es: {score}.\n\n")



            if option_elegida == "B":
                name_user_a, description_user_a, country_user_a, follower_user_a = name_user_b, description_user_b, country_user_b, follower_user_b

            os.system('cls')
            # actualizamos el usuario A al usuario B (quien es el ganador)  para la siguiente ronda
        else:
            print(f"\n\nPerdiste👎😪, tu puntuación final fue: {score}.\n")
            os.system('cls')
            break

juego()
