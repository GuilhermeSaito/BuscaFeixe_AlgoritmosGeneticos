import os
import json

def get_data():
    with open(os.getcwd() + "/../sample.txt", "r") as f:
        data = f.read()

    data_list = json.loads(data)

    return data_list


teste = get_data()

count = 0
for i in teste:
    print(i)
    print(type(i))

    if count == 10:
        break

    count += 1

print(count)