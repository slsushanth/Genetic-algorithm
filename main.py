import random
import string

# Define the target string
target_string = "HELLO, GENETIC ALGORITHM!"

# Define genetic algorithm parameters
population_size = 100
mutation_rate = 0.01


# Generate a random individual (string)
def generate_individual(length):
    return ''.join(random.choice(string.ascii_uppercase + ' ,!') for _ in range(length))


# Initialize the population
def initialize_population(pop_size, target):
    return [generate_individual(len(target)) for _ in range(pop_size)]


# Calculate the fitness of an individual (number of correct characters)
def calculate_fitness(individual, target):
    return sum(1 for i, j in zip(individual, target) if i == j)


# Select two individuals based on their fitness
def select_parents(population, target):
    fitness_scores = [calculate_fitness(individual, target) for individual in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]

    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]

    return parent1, parent2


# Crossover operator (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Mutation operator (randomly change a character)
def mutate(individual, mutation_rate):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = random.choice(string.ascii_uppercase + ' ,!')
    return ''.join(mutated_individual)


# Main genetic algorithm loop
def genetic_algorithm(target, pop_size, mutation_rate):
    population = initialize_population(pop_size, target)

    for generation in range(1, 10001):
        fitness_scores = [calculate_fitness(individual, target) for individual in population]
        best_individual = population[fitness_scores.index(max(fitness_scores))]

        if best_individual == target:
            print(f"Generation {generation}: {best_individual}")
            print("Target found!")
            break

        print(f"Generation {generation}: {best_individual} (Fitness: {max(fitness_scores)})")

        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, target)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population


# Run the genetic algorithm
genetic_algorithm(target_string, population_size, mutation_rate)
