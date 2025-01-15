import random

# Lista de usuarios
usuarios = [
    "HaggardCoder - Eduardo",
    "YuUs01 - Youssef",
    "Lowri-ui - Laura",
    "KUERVO - Angel",
    "ItsKein - Juan",
    "JaimeRuiz06 - Jaime",
    "AshysCoffee - Ashley",
    "naroa0699 - Naroa",
    "Karls3fni - Manu",
    "tamasi17 - Mati",
    "rodr1313 - Rodrigo",
    "daniela898 - Daniela",
    "Montez - JorgeMontez",
    "Nezeon7 - Rubén",
    "Alexandra024 - Sara",
    "Ces216 - César",
    "symn369 - Simona",
    "Marcos-18-11 - Marcos",
    "DanielHe22 - Daniel",
    "AlexWhut - Alex",
    "DGuelar - David",
    "Eugenia-2024 - Eugenia",
    "Sosoloogic - Yassin",
    "ErGeorgi - Jorge",
    "AMou - Amir"
]

def generar_usuario_aleatorio():
    return random.choice(usuarios)

# Generar y mostrar un usuario aleatorio
usuario_aleatorio = generar_usuario_aleatorio()
print("Usuario aleatorio generado:", usuario_aleatorio)