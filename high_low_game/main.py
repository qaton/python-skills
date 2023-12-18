""" Higher Lower Game """
import random
from art import logo, vs
from game_data import data
from replit import clear


def format_data(account):
    """ Takes the account data and return the printable format """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_fallowers, b_fallowers):
    """ Take the user guess and follower counts and returns
    if they got it right. """
    if a_fallowers > b_fallowers:
        if guess == "a":
            return guess == "a"
    else:
        return guess == "b"


# Desplegar arte ASCII
print(logo)
SCORE = 0
GAME_SHOULD_CONTINUE = True
# Generar una cuenta aleatoria a partir de los datos del juego
account_b = random.choice(data)

# Hacer el juego repetible
while GAME_SHOULD_CONTINUE:

    # Haciendo que la cuenta en la posición B se convirtiera en la siguiente
    # cuenta en la posición A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_a = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("vs")
    print(f"Against B: {format_data(account_b)}.")

    # Pedir al usuario que adivine
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Comprobar si el usuario es correcto
    # Obtener el número de seguidores de cada cuenta
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Borrar la pantalla entre rondas
    clear()
    print(logo)

    # Dar feedback al usuario sobre sus conjeturas
    # Llevar la cuenta
    if is_correct:
        SCORE += 1
        print(f"You're right! Current score: {SCORE}.")
    else:
        GAME_SHOULD_CONTINUE = False
        print(f"Sorry, that's wrong! Final score: {SCORE}.")
