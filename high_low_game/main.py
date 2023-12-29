import random
from art import logo
from art import vs
from game_data import data
from os import system

print(logo)
score = 0 #Se declara la variable score que llevara la cuenta de los aciertos del jugador
user_a = random.choice(data) #seleccionamos el usuario aleatorio del archivo data, para el usuario A

while True:
    system("cls")
    #Definiendo el usuario A
    name_user_a = user_a["name"]
    description_user_a = user_a["description"].lower()
    country_user_a = user_a["country"]
    follower_user_a = user_a["follower_count"]
    print(f'Compara a usuario 🅰️: {name_user_a}, a {description_user_a}, de {country_user_a}. {follower_user_a}\n')
    print(vs)

    user_b = random.choice(data)
    #Nos cersioramos que el usuario A sea diferente al usuario B
    if user_a == user_b:
        user_b = random.choice(data)

    #Definiendo el usuario B
    name_user_b = user_b["name"]
    description_user_b = user_b["description"].lower()
    country_user_b = user_b["country"]
    follower_user_b = user_b["follower_count"]
    print(f'🆚 usuario 🅱️: {name_user_b}, a {description_user_b}, de {country_user_b}. {follower_user_b}\n')

    option_elegida = input("¿Quién crees que tenga mas seguidores? Escribe A o B: ").upper()

    if option_elegida == "A" and follower_user_a > follower_user_b:
        score += 1
        print(f"Acertaste👍🏆! El ganador es {name_user_a}, tu puntuación es: {score}.\n\n")
        print("💚" * 30)

    elif option_elegida == "B" and follower_user_b > follower_user_a:
        score += 1
        print(f"Acertaste👍🏆! El ganador es {name_user_b}, tu puntuación es: {score}.\n\n")
        print("💚" * 30)
        user_a = user_b #actualizamos el usuario A al usuario B (quien es el ganador)  para la siguiente ronda
    else:

        print(f"\n\nPerdiste👎😪, tu puntuación final fue: {score}.\n")
        system("cls")
        break #Terminamos el while

