

def perfect(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("number must be an integer")
    if number <= 0:
        return False
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0) == number


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Program to check whether a number is a Perfect number or not...")
    try:
        number = int(input("Enter a positive integer: ").strip())
    except ValueError:
        msg = "number must be an integer"
        raise ValueError(msg)

    print(f"{number} is {'' if perfect(number) else 'not '}a Perfect Number.")
