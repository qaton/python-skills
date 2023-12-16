#

mi_lista = ["a","b"]

def longitud(mi_lista):
    cont = 0
    for _ in mi_lista:
        cont = cont + 1
        #cont += 1  abreviación
    return cont


longitud(mi_lista)
