
import copy
import random

cities = {
    0: [0, 0],
    1: [0, 5],
    2: [3, 8],
    3: [8, 10],
    4: [12, 8],
    5: [12, 4],
    6: [8, 0],
    7: [6, 2],
}


def main(
    cities: dict[int, list[int]],
    ants_num: int,
    iterations_num: int,
    pheromone_evaporation: float,
    alpha: float,
    beta: float,
    q: float,  
) -> tuple[list[int], float]:
    
    cities_num = len(cities)
    pheromone = [[1.0] * cities_num] * cities_num

    best_path: list[int] = []
    best_distance = float("inf")
    for _ in range(iterations_num):
        ants_route = []
        for _ in range(ants_num):
            unvisited_cities = copy.deepcopy(cities)
            current_city = {next(iter(cities.keys())): next(iter(cities.values()))}
            del unvisited_cities[next(iter(current_city.keys()))]
            ant_route = [next(iter(current_city.keys()))]
            while unvisited_cities:
                current_city, unvisited_cities = city_select(
                    pheromone, current_city, unvisited_cities, alpha, beta
                )
                ant_route.append(next(iter(current_city.keys())))
            ant_route.append(0)
            ants_route.append(ant_route)

        pheromone, best_path, best_distance = pheromone_update(
            pheromone,
            cities,
            pheromone_evaporation,
            ants_route,
            q,
            best_path,
            best_distance,
        )
    return best_path, best_distance


def distance(city1: list[int], city2: list[int]) -> float:
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


def pheromone_update(
    pheromone: list[list[float]],
    cities: dict[int, list[int]],
    pheromone_evaporation: float,
    ants_route: list[list[int]],
    q: float,  
    best_path: list[int],
    best_distance: float,
) -> tuple[list[list[float]], list[int], float]:
    for a in range(len(cities)):  
        for b in range(len(cities)):
            pheromone[a][b] *= pheromone_evaporation
    for ant_route in ants_route:
        total_distance = 0.0
        for i in range(len(ant_route) - 1):  
            total_distance += distance(cities[ant_route[i]], cities[ant_route[i + 1]])
        delta_pheromone = q / total_distance
        for i in range(len(ant_route) - 1):  
            pheromone[ant_route[i]][ant_route[i + 1]] += delta_pheromone
            pheromone[ant_route[i + 1]][ant_route[i]] = pheromone[ant_route[i]][
                ant_route[i + 1]
            ]

        if total_distance < best_distance:
            best_path = ant_route
            best_distance = total_distance

    return pheromone, best_path, best_distance


def city_select(
    pheromone: list[list[float]],
    current_city: dict[int, list[int]],
    unvisited_cities: dict[int, list[int]],
    alpha: float,
    beta: float,
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    probabilities = []
    for city, value in unvisited_cities.items():
        city_distance = distance(value, next(iter(current_city.values())))
        probability = (pheromone[city][next(iter(current_city.keys()))] ** alpha) * (
            (1 / city_distance) ** beta
        )
        probabilities.append(probability)

    chosen_city_i = random.choices(
        list(unvisited_cities.keys()), weights=probabilities
    )[0]
    chosen_city = {chosen_city_i: unvisited_cities[chosen_city_i]}
    del unvisited_cities[next(iter(chosen_city.keys()))]
    return chosen_city, unvisited_cities


if __name__ == "__main__":
    best_path, best_distance = main(
        cities=cities,
        ants_num=10,
        iterations_num=20,
        pheromone_evaporation=0.7,
        alpha=1.0,
        beta=5.0,
        q=10,
    )

    print(f"{best_path = }")
    print(f"{best_distance = }")
