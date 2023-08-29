import os
import random

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


weights = get_data_pesos()
values = get_data_valores()
knapsack_capacity = 70
num_items = len(weights)
population_size = 50
num_generations = 100
mutation_probability = 0.2

# Inicializa a populacao determinando quais objetos vao entrar na mochila (1) ou n vao (0)
def initialize_population(size):
	list_population = []
	for _ in range(size):
		population = []
		for _ in range(num_items):
			population.append(random.randint(0, 1))
		list_population.append(population)

	return list_population

# Verifica o valor de cada individuo (cada vetorzinho do vetorzao populacao)
def evaluate_individual(individual):
	total_weight = 0
	for i in range(num_items):
		# Vai contar o peso dos itens somente os itens que estao dentro da mochila (1)
		if individual[i]:
			total_weight += weights[i]

	# Se o peso total dos itens ultrapassar a capacidade da mochila, entao tem que ser penalizado
	if total_weight > knapsack_capacity:
		return 0  # Penalize solutions that exceed capacity
	
	total_value = 0
	for i in range(num_items):
		# Verifica o valor total dos itens que estao dentro da mochila e estao respeitado o valor total
		if individual[i]:
			total_value += values[i]

	return total_value

# Gera a crianca a paritr de 2 pais
def crossover(parent1, parent2):
	# Index para pegar os genes dos pais
	crossover_point = random.randint(1, int((num_items - 1) / 2))

	child = parent1[:crossover_point] + parent2[crossover_point:]
	
	return child

# Altera os genes da crianca (muta) caso a probabilidade seja maior que o numero randomico float de 0 a 1, serve para nao ficar parado em um maximo local
def mutate(individual):
    for i in range(num_items):
        if random.random() < mutation_probability:
			# Caso um numero randomico float entre 1 e 0 for menor que a probabilidade de mutacao, ele vai flipar o binario, 1 vira 0 e 0 vira 1
            individual[i] = 1 - individual[i]

def genetic_algorithm():
	# Gera a populacao inicial
	population = initialize_population(population_size)

	# Vai rodar x geracoes especificadas por mim, caso encontre a melhor solucao, pode parar
	for generation in range(num_generations):
		fitness_values = []
		for ind in population:
			# Verifica o valor total dos itens de cada individuo da populacao
			fitness_values.append(evaluate_individual(ind))

		# Pega o maior valor dos itens de todos os individuos da populacao
		best_fitness = max(fitness_values)
		print(f"Generation {generation+1}: Best Fitness = {best_fitness}")

		# Caso tenha encontrado algum individuo que possua o maior valor possivel (maximo global), pode parar
		if best_fitness == 382:
			break

		# Olhando todas as population_size, escolher uma quantidade population_size dos vetores, sendo que a probabilidade de ser escolhida eh pelo fitness_values
		parents = random.choices(population, weights = fitness_values, k = population_size)

		# Para cada dupla de parentes, cria 2 criancas pegando parte de genes de cada 1, sendo esses genes aleatorios
		offspring = []
		for i in range(0, population_size, 2):
			parent1, parent2 = parents[i], parents[i + 1]
			child1 = crossover(parent1, parent2)
			child2 = crossover(parent2, parent1)
			mutate(child1)
			mutate(child2)
			offspring.extend([child1, child2])

		# Atualiza a populacao para as novas criancas
		population = offspring
	
	# Acha o index em que tem o maior valor dos itens dos individuos na populacao
	best_fitness_index = fitness_values.index(max(fitness_values))
	# Com o index achado, eh possivel ver qual individuo produzio tal resultado e mostra ele
	best_individual = population[best_fitness_index]

	print("Best Solution:")
	print("Chromosome:", best_individual)
	print("Total Value:", evaluate_individual(best_individual))

# Run the genetic algorithm
genetic_algorithm()



# O que daria pra fazer ainda, seria pegar o maior fitness e o individuo correspondente para printar, para q ele mostre ele e n vendo para o valor maximo q eu achei
# Colocar a punicao do artigo tbm