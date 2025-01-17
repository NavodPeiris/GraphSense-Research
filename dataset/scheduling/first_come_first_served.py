



from __future__ import annotations


def calculate_waiting_times(duration_times: list[int]) -> list[int]:
    waiting_times = [0] * len(duration_times)
    for i in range(1, len(duration_times)):
        waiting_times[i] = duration_times[i - 1] + waiting_times[i - 1]
    return waiting_times


def calculate_turnaround_times(
    duration_times: list[int], waiting_times: list[int]
) -> list[int]:
    return [
        duration_time + waiting_times[i]
        for i, duration_time in enumerate(duration_times)
    ]


def calculate_average_turnaround_time(turnaround_times: list[int]) -> float:
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: list[int]) -> float:
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    
    processes = [1, 2, 3]

    
    if len(processes) == 0:
        print("Zero amount of processes")
        raise SystemExit(0)

    
    duration_times = [19, 8, 9]

    
    if len(duration_times) != len(processes):
        print("Unable to match all id's with their duration time")
        raise SystemExit(0)

    
    waiting_times = calculate_waiting_times(duration_times)
    turnaround_times = calculate_turnaround_times(duration_times, waiting_times)

    
    average_waiting_time = calculate_average_waiting_time(waiting_times)
    average_turnaround_time = calculate_average_turnaround_time(turnaround_times)

    
    print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(processes):
        print(
            f"{process}\t\t{duration_times[i]}\t\t{waiting_times[i]}\t\t"
            f"{turnaround_times[i]}"
        )
    print(f"Average waiting time = {average_waiting_time}")
    print(f"Average turn around time = {average_turnaround_time}")
