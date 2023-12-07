#convertir grados celcius a grados kelvin usando funciones y variables
# grados kelvin = grados celcius +  273.15

def convertir_celsius_a_kelvin(celcius):
    return celcius + 273.15

def ingresar_temperatura():
    while True:
        ingreso_celcius = input("Ingrese temperatura en grados celsius:  ")
        try:
            temperatura_usuario = float(ingreso_celcius)
            temperatura_kelvin = convertir_celsius_a_kelvin(temperatura_usuario)
            print(f" la temperatura {temperatura_usuario} grados celcius, son {temperatura_kelvin} grados kelvin")
        except ValueError:
            print("ingrese temperatura valida")


ingresar_temperatura()
























