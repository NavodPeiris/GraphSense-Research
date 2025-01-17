def job_sequencing_with_deadlines(jobs: list) -> list:

    
    jobs = sorted(jobs, key=lambda value: value[2], reverse=True)

    
    
    max_deadline = max(jobs, key=lambda value: value[1])[1]
    time_slots = [-1] * max_deadline

    
    count = 0
    max_profit = 0
    for job in jobs:
        
        
        for i in range(job[1] - 1, -1, -1):
            if time_slots[i] == -1:
                time_slots[i] = job[0]
                count += 1
                max_profit += job[2]
                break
    return [count, max_profit]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
