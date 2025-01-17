

def optimal_merge_pattern(files: list) -> float:
    optimal_merge_cost = 0
    while len(files) > 1:
        temp = 0
        
        for _ in range(2):
            min_index = files.index(min(files))
            temp += files[min_index]
            files.pop(min_index)
        files.append(temp)
        optimal_merge_cost += temp
    return optimal_merge_cost


if __name__ == "__main__":
    import doctest

    doctest.testmod()
