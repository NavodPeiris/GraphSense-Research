

def factorial(digit: int) -> int:

    return 1 if digit in (0, 1) else (digit * factorial(digit - 1))


def krishnamurthy(number: int) -> bool:

    fact_sum = 0
    duplicate = number
    while duplicate > 0:
        duplicate, digit = divmod(duplicate, 10)
        fact_sum += factorial(digit)
    return fact_sum == number


if __name__ == "__main__":
    print("Program to check whether a number is a Krisnamurthy Number or not.")
    number = int(input("Enter number: ").strip())
    print(
        f"{number} is {'' if krishnamurthy(number) else 'not '}a Krishnamurthy Number."
    )
