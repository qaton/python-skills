import time


cosas_que_le_gustan_a_manu = [
    "los aviones", "viajar", "la mañana", "el viento", "soñar", "la mar"]


def me_gusta(parametro):
    print(f"Me gustan {parametro}, me gustas tú")


for cosa in cosas_que_le_gustan_a_manu:
    me_gusta(cosa)
    time.sleep(4)
