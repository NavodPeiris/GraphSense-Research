
PASSING = (1, 153, 370, 371, 1634, 24678051, 115132219018763992565095597973971522401)
FAILING: tuple = (-153, -1, 0, 1.2, 200, "A", [], {}, None)


def armstrong_number(n: int) -> bool:
    if not isinstance(n, int) or n < 1:
        return False

    
    total = 0
    number_of_digits = 0
    temp = n
    
    number_of_digits = len(str(n))
    
    temp = n
    while temp > 0:
        rem = temp % 10
        total += rem**number_of_digits
        temp //= 10
    return n == total


def pluperfect_number(n: int) -> bool:
    if not isinstance(n, int) or n < 1:
        return False

    
    digit_histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    digit_total = 0
    total = 0
    temp = n
    while temp > 0:
        temp, rem = divmod(temp, 10)
        digit_histogram[rem] += 1
        digit_total += 1

    for cnt, i in zip(digit_histogram, range(len(digit_histogram))):
        total += cnt * i**digit_total

    return n == total


def narcissistic_number(n: int) -> bool:
    if not isinstance(n, int) or n < 1:
        return False
    expo = len(str(n))  
    
    return n == sum(int(i) ** expo for i in str(n))


def main():
    num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
    print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")
    print(f"{num} is {'' if narcissistic_number(num) else 'not '}an Armstrong number.")
    print(f"{num} is {'' if pluperfect_number(num) else 'not '}an Armstrong number.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
