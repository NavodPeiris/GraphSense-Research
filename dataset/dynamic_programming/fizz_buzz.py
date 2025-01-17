


def fizz_buzz(number: int, iterations: int) -> str:
    
    if not isinstance(iterations, int):
        raise ValueError("iterations must be defined as integers")
    if not isinstance(number, int) or not number >= 1:
        raise ValueError(
            """starting number must be
                         and integer and be more than 0"""
        )
    if not iterations >= 1:
        raise ValueError("Iterations must be done more than 0 times to play FizzBuzz")

    out = ""
    while number <= iterations:
        if number % 3 == 0:
            out += "Fizz"
        if number % 5 == 0:
            out += "Buzz"
        if 0 not in (number % 3, number % 5):
            out += str(number)

        # print(out)
        number += 1
        out += " "
    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
