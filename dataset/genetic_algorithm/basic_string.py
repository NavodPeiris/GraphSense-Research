
from __future__ import annotations

import random


N_POPULATION = 200


N_SELECTED = 50


MUTATION_PROBABILITY = 0.4

random.seed(random.randint(0, 1000))


def evaluate(item: str, main_target: str) -> tuple[str, float]:
    score = len([g for position, g in enumerate(item) if g == main_target[position]])
    return (item, float(score))


def crossover(parent_1: str, parent_2: str) -> tuple[str, str]:
    random_slice = random.randint(0, len(parent_1) - 1)
    child_1 = parent_1[:random_slice] + parent_2[random_slice:]
    child_2 = parent_2[:random_slice] + parent_1[random_slice:]
    return (child_1, child_2)


def mutate(child: str, genes: list[str]) -> str:
    child_list = list(child)
    if random.uniform(0, 1) < MUTATION_PROBABILITY:
        child_list[random.randint(0, len(child)) - 1] = random.choice(genes)
    return "".join(child_list)



def select(
    parent_1: tuple[str, float],
    population_score: list[tuple[str, float]],
    genes: list[str],
) -> list[str]:
    pop = []
    
    child_n = int(parent_1[1] * 100) + 1
    child_n = 10 if child_n >= 10 else child_n
    for _ in range(child_n):
        parent_2 = population_score[random.randint(0, N_SELECTED)][0]

        child_1, child_2 = crossover(parent_1[0], parent_2)
        
        pop.append(mutate(child_1, genes))
        pop.append(mutate(child_2, genes))
    return pop


def basic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]:

    
    if N_POPULATION < N_SELECTED:
        msg = f"{N_POPULATION} must be bigger than {N_SELECTED}"
        raise ValueError(msg)
    
    not_in_genes_list = sorted({c for c in target if c not in genes})
    if not_in_genes_list:
        msg = f"{not_in_genes_list} is not in genes list, evolution cannot converge"
        raise ValueError(msg)

    
    population = []
    for _ in range(N_POPULATION):
        population.append("".join([random.choice(genes) for i in range(len(target))]))

    
    generation, total_population = 0, 0

    
    while True:
        generation += 1
        total_population += len(population)

        

        
        
        
        
        
        
        
        
        
        
        
        
        population_score = [evaluate(item, target) for item in population]

        
        population_score = sorted(population_score, key=lambda x: x[1], reverse=True)
        if population_score[0][0] == target:
            return (generation, total_population, population_score[0][0])

        
        
        if debug and generation % 10 == 0:
            print(
                f"\nGeneration: {generation}"
                f"\nTotal Population:{total_population}"
                f"\nBest score: {population_score[0][1]}"
                f"\nBest string: {population_score[0][0]}"
            )

        
        
        population_best = population[: int(N_POPULATION / 3)]
        population.clear()
        population.extend(population_best)
        
        population_score = [
            (item, score / len(target)) for item, score in population_score
        ]

        
        for i in range(N_SELECTED):
            population.extend(select(population_score[int(i)], population_score, genes))
            
            
            
            
            if len(population) > N_POPULATION:
                break


if __name__ == "__main__":
    target_str = (
        "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string!"
    )
    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    generation, population, target = basic(target_str, genes_list)
    print(
        f"\nGeneration: {generation}\nTotal Population: {population}\nTarget: {target}"
    )
