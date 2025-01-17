
from random import randint, random


def construct_highway(
    number_of_cells: int,
    frequency: int,
    initial_speed: int,
    random_frequency: bool = False,
    random_speed: bool = False,
    max_speed: int = 5,
) -> list:
    

    highway = [[-1] * number_of_cells]  
    i = 0
    initial_speed = max(initial_speed, 0)
    while i < number_of_cells:
        highway[0][i] = (
            randint(0, max_speed) if random_speed else initial_speed
        )  
        i += (
            randint(1, max_speed * 2) if random_frequency else frequency
        )  
    return highway


def get_distance(highway_now: list, car_index: int) -> int:
    
    distance = 0
    cells = highway_now[car_index + 1 :]
    for cell in range(len(cells)): 
        if cells[cell] != -1:  
            return distance  
        distance += 1
    
    return distance + get_distance(highway_now, -1)


def update(highway_now: list, probability: float, max_speed: int) -> list:
    

    number_of_cells = len(highway_now)
    
    next_highway = [-1] * number_of_cells

    for car_index in range(number_of_cells):
        if highway_now[car_index] != -1:
            
            next_highway[car_index] = min(highway_now[car_index] + 1, max_speed)
            
            dn = get_distance(highway_now, car_index) - 1
            
            next_highway[car_index] = min(next_highway[car_index], dn)
            if random() < probability:
                
                next_highway[car_index] = max(next_highway[car_index] - 1, 0)
    return next_highway


def simulate(
    highway: list, number_of_update: int, probability: float, max_speed: int
) -> list:
    

    number_of_cells = len(highway[0])

    for i in range(number_of_update):
        next_speeds_calculated = update(highway[i], probability, max_speed)
        real_next_speeds = [-1] * number_of_cells

        for car_index in range(number_of_cells):
            speed = next_speeds_calculated[car_index]
            if speed != -1:
                
                index = (car_index + speed) % number_of_cells
                
                real_next_speeds[index] = speed
        highway.append(real_next_speeds)

    return highway


if __name__ == "__main__":
    import doctest

    doctest.testmod()
