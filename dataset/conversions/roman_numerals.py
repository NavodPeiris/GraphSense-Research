ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def roman_to_int(roman: str) -> int:
    
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    return total


def int_to_roman(number: int) -> str:
    
    result = []
    for arabic, roman in ROMAN:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
