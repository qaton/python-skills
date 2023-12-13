import requests


def test_primer_test_status_200_categories():
    respuesta = requests.get(
        "https://api.escuelajs.co/api/v1/categories", timeout=5)
    print(f'Este es el código de respuesta: {respuesta.status_code}')

    assert respuesta.status_code == 200, "Estatus erroneo"
    # res_json = respuesta.json()
    # print(res_json)


def test_suma_es_par():
    numero_a = 2
    numero_b = 4
    suma = numero_a + numero_b
    es_par = None
    if suma % 2 == 0:
        es_par = True
    else:
        es_par = False
    assert es_par == True
