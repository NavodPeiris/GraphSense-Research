NUMBERS_PLUS_LETTER = "Input must be a string of 8 numbers plus letter"
LOOKUP_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"


def is_spain_national_id(spanish_id: str) -> bool:

    if not isinstance(spanish_id, str):
        msg = f"Expected string as input, found {type(spanish_id).__name__}"
        raise TypeError(msg)

    spanish_id_clean = spanish_id.replace("-", "").upper()
    if len(spanish_id_clean) != 9:
        raise ValueError(NUMBERS_PLUS_LETTER)

    try:
        number = int(spanish_id_clean[0:8])
        letter = spanish_id_clean[8]
    except ValueError as ex:
        raise ValueError(NUMBERS_PLUS_LETTER) from ex

    if letter.isdigit():
        raise ValueError(NUMBERS_PLUS_LETTER)

    return letter == LOOKUP_LETTERS[number % 23]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
