import requests


respuesta = requests.get(
    "https://api.escuelajs.co/api/v1/categories", timeout=5)
print(f'Este es el código de respuesta: {respuesta.status_code}')
res_json = respuesta.json()
# print(res_json)


for diccionario in res_json:
    for value in diccionario.values():
        print(value)
