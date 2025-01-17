
from statistics import mean

import numpy as np


def calculate_turn_around_time(
    process_name: list, arrival_time: list, burst_time: list, no_of_process: int
) -> list:

    current_time = 0
    
    finished_process_count = 0
    
    
    finished_process = [0] * no_of_process
    
    turn_around_time = [0] * no_of_process

    
    burst_time = [burst_time[i] for i in np.argsort(arrival_time)]
    process_name = [process_name[i] for i in np.argsort(arrival_time)]
    arrival_time.sort()

    while no_of_process > finished_process_count:
        i = 0
        while finished_process[i] == 1:
            i += 1
        current_time = max(current_time, arrival_time[i])

        response_ratio = 0
        
        loc = 0
        
        temp = 0
        for i in range(no_of_process):
            if finished_process[i] == 0 and arrival_time[i] <= current_time:
                temp = (burst_time[i] + (current_time - arrival_time[i])) / burst_time[
                    i
                ]
            if response_ratio < temp:
                response_ratio = temp
                loc = i

        
        turn_around_time[loc] = current_time + burst_time[loc] - arrival_time[loc]
        current_time += burst_time[loc]
        
        finished_process[loc] = 1
        
        finished_process_count += 1

    return turn_around_time


def calculate_waiting_time(
    process_name: list,  
    turn_around_time: list,
    burst_time: list,
    no_of_process: int,
) -> list:

    waiting_time = [0] * no_of_process
    for i in range(no_of_process):
        waiting_time[i] = turn_around_time[i] - burst_time[i]
    return waiting_time


if __name__ == "__main__":
    no_of_process = 5
    process_name = ["A", "B", "C", "D", "E"]
    arrival_time = [1, 2, 3, 4, 5]
    burst_time = [1, 2, 3, 4, 5]

    turn_around_time = calculate_turn_around_time(
        process_name, arrival_time, burst_time, no_of_process
    )
    waiting_time = calculate_waiting_time(
        process_name, turn_around_time, burst_time, no_of_process
    )

    print("Process name \tArrival time \tBurst time \tTurn around time \tWaiting time")
    for i in range(no_of_process):
        print(
            f"{process_name[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t"
            f"{turn_around_time[i]}\t\t\t{waiting_time[i]}"
        )

    print(f"average waiting time : {mean(waiting_time):.5f}")
    print(f"average turn around time : {mean(turn_around_time):.5f}")
