

def temp_input_value(
    min_val: int = 10, max_val: int = 1000, option: bool = True
) -> int:
    assert (
        isinstance(min_val, int)
        and isinstance(max_val, int)
        and isinstance(option, bool)
    ), "Invalid type of value(s) specified to function!"

    if min_val > max_val:
        raise ValueError("Invalid value for min_val or max_val (min_value < max_value)")
    return min_val if option else max_val


def get_avg(number_1: int, number_2: int) -> int:
    return int((number_1 + number_2) / 2)


def guess_the_number(lower: int, higher: int, to_guess: int) -> None:
    assert (
        isinstance(lower, int) and isinstance(higher, int) and isinstance(to_guess, int)
    ), 'argument values must be type of "int"'

    if lower > higher:
        raise ValueError("argument value for lower and higher must be(lower > higher)")

    if not lower < to_guess < higher:
        raise ValueError(
            "guess value must be within the range of lower and higher value"
        )

    def answer(number: int) -> str:
        if number > to_guess:
            return "high"
        elif number < to_guess:
            return "low"
        else:
            return "same"

    print("started...")

    last_lowest = lower
    last_highest = higher

    last_numbers = []

    while True:
        number = get_avg(last_lowest, last_highest)
        last_numbers.append(number)

        if answer(number) == "low":
            last_lowest = number
        elif answer(number) == "high":
            last_highest = number
        else:
            break

    print(f"guess the number : {last_numbers[-1]}")
    print(f"details : {last_numbers!s}")


def main() -> None:
    lower = int(input("Enter lower value : ").strip())
    higher = int(input("Enter high value : ").strip())
    guess = int(input("Enter value to guess : ").strip())
    guess_the_number(lower, higher, guess)


if __name__ == "__main__":
    main()
