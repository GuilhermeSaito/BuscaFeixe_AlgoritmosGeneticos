import random
import json

list_save = []

# Definindo a quantidade de dados para 1kk amostras
for i in range(1000000):
    dados = {
        "id": i,
        "valor": random.randint(0, 100),
        "peso": random.randint(1, 50)
    }

    list_save.append(dados)

with open("sample.txt", "w") as f:
    json.dump(list_save, f)