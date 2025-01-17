

def power(base: int, exponent: int) -> float:
    return base * power(base, (exponent - 1)) if exponent else 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Raise base to the power of exponent using recursion...")
    base = int(input("Enter the base: ").strip())
    exponent = int(input("Enter the exponent: ").strip())
    result = power(base, abs(exponent))
    if exponent < 0:  
        result = 1 / result
    print(f"{base} to the power of {exponent} is {result}")
