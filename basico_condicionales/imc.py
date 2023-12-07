"""
Escribe un programa que interprete el índice de masa corporal (IMC) basado en el peso y la altura de un usuario. La formula es: peso (kg)/ [estatura (m)]**2.

Debería indicarles la interpretación de su IMC en función del valor del IMC.

Por debajo de 18.5 están bajo peso.
Más de 18.5, pero por debajo de 25 tienen un peso normal.
Más de 25, pero por debajo de 30 tienen sobrepeso.
Más de 30, pero por debajo de 35 tienen obesidad.
Por encima de 35 tienen obesidad clínica.
"""
def formular_imc(peso, altura):
    return peso % (altura * altura)

def resolver_imc():

    while True:
        entrada_peso = float(input("Ingrese su peso- Kg : "))
        entrada_altura = float(input("Ingrese su altura - m  :"))

        try:
            resultado_imc =  formular_imc(entrada_peso,entrada_altura)
            if resultado_imc < 18.5:
                print(f"El peso que tiene es {entrada_peso} kg,  su altura es {entrada_altura} metros y el resultado de su IMC es {resultado_imc}, lo cual indica que estas bajo de peso")
            elif resultado_imc > 18.5 and resultado_imc < 25:
                print(f"El peso que tiene es {entrada_peso} kg,  su altura es {entrada_altura} metros y el resultado de su IMC es {resultado_imc}, lo cual indica que estas bien de peso")
            elif resultado_imc > 25 and resultado_imc < 30:
                print(f"El peso que tiene es {entrada_peso} kg,  su altura es {entrada_altura} metros y el resultado de su IMC es {resultado_imc}, lo cual indica que estas con sobrepeso")
            elif resultado_imc > 30 and resultado_imc < 35:
                 print(f"El peso que tiene es {entrada_peso} kg,  su altura es {entrada_altura} metros y el resultado de su IMC es {resultado_imc}, lo cual indica que estas obeso")
            elif resultado_imc > 35:
                print(f"El peso que tiene es {entrada_peso} kg,  su altura es {entrada_altura} metros y el resultado de su IMC es {resultado_imc}, lo cual indica que tienes obsesidad clinica")


        except ValueError:
            print("Ingrese información válida")

resolver_imc()


