import os

def get_data_ids():
    list_ids = []

    with open(os.getcwd() + "/../ids.txt", "r") as f:
        for line in f:
            list_ids.append(int(line.strip()))

    return list_ids

def get_data_valores():
    list_valores = []
    
    with open(os.getcwd() + "/../valores.txt", "r") as f:
        for line in f:
            list_valores.append(int(line.strip()))

    return list_valores

def get_data_pesos():
    list_pesos = []
    
    with open(os.getcwd() + "/../pesos.txt", "r") as f:
        for line in f:
            list_pesos.append(int(line.strip()))

    return list_pesos

ids = get_data_ids()
valores = get_data_valores()
pesos = get_data_pesos()

print(ids)
print(valores)
print(pesos)