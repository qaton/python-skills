"""
Escribe un programa que interprete el índice de masa corporal (IMC) basado
en el peso y la altura de un usuario.
La formula es: peso (kg)/ [estatura (m)]**2.

Debería indicarles la interpretación de su IMC en función del valor del IMC.

Por debajo de 18.5 están bajo peso.
Más de 18.5, pero por debajo de 25 tienen un peso normal.
Más de 25, pero por debajo de 30 tienen sobrepeso.
Más de 30, pero por debajo de 35 tienen obesidad.
Por encima de 35 tienen obesidad clínica.
"""


def interpretar_imc():
    # Solicitando al usuario que ingrese su peso y estatura
    peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
    estatura = float(input("Por favor, ingresa tu estatura en metros: "))

    # Calculando el IMC
    imc = peso / (estatura ** 2)

    # Interpretando el IMC
    if imc < 18.5:
        resultado = f"Tu IMC es {imc:.2f}. Estás bajo peso."
    elif 18.5 <= imc < 25:
        resultado = f"Tu IMC es {imc:.2f}. Tienes un peso normal."
    elif 25 <= imc < 30:
        resultado = f"Tu IMC es {imc:.2f}. Tienes sobrepeso."
    elif 30 <= imc < 35:
        resultado = f"Tu IMC es {imc:.2f}. Tienes obesidad."
    else:
        resultado = f"Tu IMC es {imc:.2f}. Tienes obesidad clínica."

    # Imprimiendo el resultado
    print(resultado)

# Llamada a la función


interpretar_imc()
