import os
import random
import math

# Retorna a lista de valores
def get_data_valores():
    list_valores = []         
    with open('valores.txt', 'r') as valores:
        values_valores = valores.read().splitlines()
        for line in values_valores:
            list_valores.append(int(line.strip()))
    return list_valores

# Retorna a lista de pesos
def get_data_pesos():
    list_pesos = []
    with open('pesos.txt', 'r') as pesos:
        values_pesos = pesos.read().splitlines()
        for line in values_pesos:
            list_pesos.append(int(line.strip()))
    return list_pesos
    total = 0
    for w in weight:
        total += w
    return total

# Inicializa a solução inicial aleatoria determinando quais objetos vao entrar na mochila (1) ou n vao (0)
def initialize_solutions(beam_width):
	list_initial_solution = []
	for _ in range(beam_width):
		solution = []
		for _ in range(num_items):
			solution.append(random.randint(0, 1))
		list_initial_solution.append(solution)
	return list_initial_solution

# Função de avaliação usando tempera simulada
def simulated_annealing_evaluation(solution):
    total_weight = 0
    for i in range(num_items):
        if solution[i]:
            total_weight += weights[i]

        # Se o peso total dos itens ultrapassar a capacidade da mochila, terá sua solução penalizada
        if total_weight > knapsack_capacity:
            return 0 
        
        total_value = 0
        for i in range(num_items):
            # Verifica o valor total dos itens que estao dentro da mochila e estao respeitado o valor total
            if solution[i]:
                total_value += values[i]
        return total_value

#Gera os vizinhos obtidos através de pertubação da solução atual
def generate_neighbor(solution):
    vizinho = list(solution)
    rand_index = random.randint(0, len(vizinho)-1)
    vizinho[rand_index] = 1-vizinho[rand_index] #inverte o valor do item
    return vizinho

def beam_width_algorithm():
    #Gera o conjunto de soluções iniciais
    list_initial_solution = initialize_solutions(beam_width)
    
    # Roda x vezes, parando ao encontrar a melhor solução   
    for _ in range(num_interations):
        next_solutions = []
        temperature = 10
        # Gerar vizinhos e avaliar soluções atuais
        for solution in list_initial_solution:
            
            neighbors = [generate_neighbor(solution) for _ in range(num_neighbors)] # Gera num_neighbors vizinhos perturbando a solução atual
            neighbors_with_scores = [(neighbor, simulated_annealing_evaluation(neighbor)) for neighbor in neighbors] # Aplicando a função avaliativa para cada solução
            neighbors_with_scores.sort(key=lambda x: x[1], reverse=True) # Classificando os vizinhos pela avaliação em ordem decrescente
            
            next_solutions.extend([neighbor for neighbor, _ in neighbors_with_scores[:beam_width]]) # Seleciona os beam_width melhores vizinhos para a próxima iteração
            
        # Processo de Tempera Simulada para aceitar/rejeitar soluções perturbadas
        for i in range(len(next_solutions)):
            old_score = simulated_annealing_evaluation(next_solutions[i])
            perturbed_solution = generate_neighbor(next_solutions[i])

            new_score = simulated_annealing_evaluation(perturbed_solution)
            if new_score > old_score or random.random() < math.exp((new_score - old_score) / temperature):
                next_solutions[i] = perturbed_solution
            
        # Atualiza as soluções atuais para as próximas soluções geradas
        current_solutions = next_solutions

        # Diminui a temperatura para controlar a probabilidade de aceitar soluções piores
        temperature *= 0.95  # Fator de resfriamento
        
    # Encontra a melhor solução entre as soluções atuais
    best_solution = max(current_solutions, key=simulated_annealing_evaluation)
    return best_solution      

# Definir uma heurística para estes parâmetros
weights = get_data_pesos()
values = get_data_valores()
knapsack_capacity = 80
num_items = len(weights)
beam_width = 5
num_neighbors = 5
temperature = 10
num_interations = 10
    
best_solution = beam_width_algorithm()

print(best_solution)
    