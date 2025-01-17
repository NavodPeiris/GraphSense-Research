

from timeit import timeit

test_data = {
    "MALAYALAM": True,
    "String": False,
    "rotor": True,
    "level": True,
    "A": True,
    "BB": True,
    "ABC": False,
    "amanaplanacanalpanama": True,  
}

assert all((key == key[::-1]) is value for key, value in test_data.items())


def is_palindrome(s: str) -> bool:

    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


def is_palindrome_traversal(s: str) -> bool:
    end = len(s) // 2
    n = len(s)

    
    
    
    
    
    
    return all(s[i] == s[n - i - 1] for i in range(end))


def is_palindrome_recursive(s: str) -> bool:
    if len(s) <= 2:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False


def is_palindrome_slice(s: str) -> bool:
    return s == s[::-1]


def benchmark_function(name: str) -> None:
    stmt = f"all({name}(key) is value for key, value in test_data.items())"
    setup = f"from __main__ import test_data, {name}"
    number = 500000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f"{name:<35} finished {number:,} runs in {result:.5f} seconds")


if __name__ == "__main__":
    for key, value in test_data.items():
        assert is_palindrome(key) is is_palindrome_recursive(key)
        assert is_palindrome(key) is is_palindrome_slice(key)
        print(f"{key:21} {value}")
    print("a man a plan a canal panama")

    
    benchmark_function("is_palindrome_slice")
    
    benchmark_function("is_palindrome")
    
    benchmark_function("is_palindrome_recursive")
    
    benchmark_function("is_palindrome_traversal")
