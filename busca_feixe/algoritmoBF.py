import random
import math

max_capacity = 80

def total_weight(peso):
    total = 0
    for p in peso:
        total += p
    return total


def funcao_avaliacao_TemperaSimulada(solution):
    total_value = 0
    for i, item in enumerate(solution):
        if solution[i]:
            total_value += item
    # total_value = sum(item[1] for i, item in enumerate(solution) if solution[i])
    if total_weight(solution) > max_capacity:
        return -total_value #definir qual o parâmetro de penalização
    # print("tempera simulada")
    return total_value

def gerando_vizinhos(solucao):
    vizinho = list(solucao)
    rand_index = random.randint(0, len(vizinho)-1)
    vizinho[rand_index] = 1-vizinho[rand_index] #inverte o valor do item
    # print("gerei vizinho")
    return vizinho

def busca_feixe(largura_feixe, num_vizinhos, temperatura, iteracoes):

    solucoes = [random.choices([0,1], k=10) for _ in range(largura_feixe)] #verificar o k
    
    for _ in range(iteracoes):
        prox_solucao = []

        for solucao in solucoes:
            vizinhos = [gerando_vizinhos(solucao) for _ in range(num_vizinhos)]
            vizinhos_pontos = [(vizinho, funcao_avaliacao_TemperaSimulada(vizinho)) for vizinho in vizinhos]
            vizinhos_pontos.sort(key=lambda x: x[1], reverse=True)

            prox_solucao.extend([vizinho for vizinho, _ in vizinhos_pontos[:largura_feixe]])
            
            count = 0

            for i in range(len(prox_solucao)):
                old_score = funcao_avaliacao_TemperaSimulada(prox_solucao[i])
                pertubed_solution = gerando_vizinhos(prox_solucao[i])

                new_score = funcao_avaliacao_TemperaSimulada(pertubed_solution)
                if new_score > old_score or random.random() < math.exp((new_score-old_score)/temperatura):
                    prox_solucao[i]=pertubed_solution
                count+=1
                # print(i)
                # print(len(prox_solucao))
                # print("cheguei aqui1")
            solucoes = prox_solucao
            temperatura *= 0.95
            print("cheguei aqui2")
        print("cheguei aqui3")

    best_solution = max(solucoes, key=funcao_avaliacao_TemperaSimulada)
    return best_solution

beam_width = 5
num_neighbors = 10
temperature = 10.0
iterations = 1

best_solution = busca_feixe(beam_width, num_neighbors, temperature, iterations)
print("Melhor solução encontrada:", best_solution)