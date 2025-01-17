def snake_to_camel_case(input_str: str, use_pascal: bool = False) -> str:

    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)
    if not isinstance(use_pascal, bool):
        msg = f"Expected boolean as use_pascal parameter, found {type(use_pascal)}"
        raise ValueError(msg)

    words = input_str.split("_")

    start_index = 0 if use_pascal else 1

    words_to_capitalize = words[start_index:]

    capitalized_words = [word[0].upper() + word[1:] for word in words_to_capitalize]

    initial_word = "" if use_pascal else words[0]

    return "".join([initial_word, *capitalized_words])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
