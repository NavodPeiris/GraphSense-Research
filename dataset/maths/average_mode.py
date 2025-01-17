from typing import Any


def mode(input_list: list) -> list[Any]:
    if not input_list:
        return []
    result = [input_list.count(value) for value in input_list]
    y = max(result)  
    
    return sorted({input_list[i] for i, value in enumerate(result) if value == y})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
