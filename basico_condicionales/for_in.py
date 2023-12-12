"""
Este módulo proporciona una función para calcular la longitud de una lista.
"""


def calcular_longitud(lista):
    """
    Calcula la longitud de una lista.

    Argumentos:
        lista (list): La lista para la cual se calculará la longitud.

    Returns:
        int: La longitud de la lista.
    """
    cont = 0
    for _ in lista:
        cont += 1
    return cont


MI_LISTA_PERSONAL = [1, 2, 3, 4, 5]
RESULTADO = calcular_longitud(MI_LISTA_PERSONAL)
print("Longitud de la lista:", RESULTADO)
