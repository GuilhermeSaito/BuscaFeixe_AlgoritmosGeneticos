import random

list_id = []
list_valores = []
list_pesos = []

# Definindo a quantidade de dados para 1k amostras
for i in range(1000):
    list_id.append(i)
    list_valores.append(random.randint(0, 100))
    list_pesos.append(random.randint(1, 50))

with open("ids.txt", "w") as f:
    for item in list_id:
        f.write(str(item) + "\n")
with open("valores.txt", "w") as f:
    for item in list_valores:
        f.write(str(item) + "\n")
with open("pesos.txt", "w") as f:
    for item in list_pesos:
        f.write(str(item) + "\n")