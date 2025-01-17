
from collections import defaultdict


def check_anagrams(first_str: str, second_str: str) -> bool:
    first_str = first_str.lower().strip()
    second_str = second_str.lower().strip()

    
    first_str = first_str.replace(" ", "")
    second_str = second_str.replace(" ", "")

    
    if len(first_str) != len(second_str):
        return False

    
    count: defaultdict[str, int] = defaultdict(int)

    
    
    for i in range(len(first_str)):
        count[first_str[i]] += 1
        count[second_str[i]] -= 1

    return all(_count == 0 for _count in count.values())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_a = input("Enter the first string ").strip()
    input_b = input("Enter the second string ").strip()

    status = check_anagrams(input_a, input_b)
    print(f"{input_a} and {input_b} are {'' if status else 'not '}anagrams.")
