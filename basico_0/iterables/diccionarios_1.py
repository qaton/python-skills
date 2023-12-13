mi_bici = {
    "marca": "Trek",
    "modelo": "fx3",
    "rodada": 700,
    "manillar": {
        "freno_izq": True,
        "freno_der": True,
        "numero_de_cambios": 12,
        "lista": [1, 2, 3, 4, 5, 6]
    }
}

# print(mi_bici["marca"])
# print(mi_bici["modelo"])
# print(mi_bici["rodada"])

mi_bici["color"] = "negro"

for llave, valor in mi_bici.items():
    print(f'La llave es: {llave}, el valor es: {valor}')

mi_bici["asiento"] = True
print(mi_bici)
