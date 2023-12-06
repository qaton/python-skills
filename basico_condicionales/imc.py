"""
Escribe un programa que interprete el índice de masa corporal (IMC) basado en el peso y la altura de un usuario.
La formula es: peso (kg)/ [estatura (m)]**2.

Debería indicarles la interpretación de su IMC en función del valor del IMC.

Por debajo de 18.5 están bajo peso.
Más de 18.5, pero por debajo de 25 tienen un peso normal.
Más de 25, pero por debajo de 30 tienen sobrepeso.
Más de 30, pero por debajo de 35 tienen obesidad.
Por encima de 35 tienen obesidad clínica.
"""

def formula_imc(peso, talla):
    return (peso / (talla * talla))
def principal_imc():
    while True:
        entrada_peso = input("Ingrese su peso (kg): ")
        entrada_talla = input("Ingrese su estatura (m): ")
        try:
            entrada_peso = float(entrada_peso)
            entrada_talla = float(entrada_talla)
            calculo_imc = int(formula_imc(entrada_peso,entrada_talla))
            if calculo_imc < 18.5:
                print(f"Su peso es {entrada_peso} Kg, su talla es {entrada_talla} mt, por lo que su IMC es {calculo_imc}, estás bajo de peso.")
            elif calculo_imc > 18.5 and calculo_imc <= 25:
                print(f"Su peso es {entrada_peso} Kg, su talla es {entrada_talla} mt, por lo que su IMC es {calculo_imc}, tienes un peso normal.")
            elif calculo_imc > 25 and calculo_imc <= 30:
                print(f"Su peso es {entrada_peso} Kg, su talla es {entrada_talla} mt, por lo que su IMC es {calculo_imc}, tienes sobrepeso.")
            elif calculo_imc > 30 and calculo_imc <= 35:
                print(f"Su peso es {entrada_peso} Kg, su talla es {entrada_talla} mt, por lo que su IMC es {calculo_imc}, tienes obesidad.")
            elif calculo_imc > 35:
                print(f"Su peso es {entrada_peso} Kg, su talla es {entrada_talla} mt, por lo que su IMC es {calculo_imc}, tienes obesidad clínica.")
        except ValueError:
            print("Por favor, datos válidos.")
principal_imc()
