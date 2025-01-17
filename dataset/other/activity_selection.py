


def print_max_activities(start: list[int], finish: list[int]) -> None:
   
    n = len(finish)
    print("The following activities are selected:")

    i = 0
    print(i, end=",")

    
    for j in range(n):
        
        
        
        if start[j] >= finish[i]:
            print(j, end=",")
            i = j


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print_max_activities(start, finish)
