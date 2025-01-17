import re




def split_input(str_: str) -> list:
    return [char.split() for char in re.split(r"[^ a-z A-Z 0-9 \s]", str_)]


def to_simple_case(str_: str) -> str:
    string_split = split_input(str_)
    return "".join(
        ["".join([char.capitalize() for char in sub_str]) for sub_str in string_split]
    )


def to_complex_case(text: str, upper: bool, separator: str) -> str:
    try:
        string_split = split_input(text)
        if upper:
            res_str = "".join(
                [
                    separator.join([char.upper() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        else:
            res_str = "".join(
                [
                    separator.join([char.lower() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        return res_str
    except IndexError:
        return "not valid string"



def to_pascal_case(text: str) -> str:
    return to_simple_case(text)


def to_camel_case(text: str) -> str:
    try:
        res_str = to_simple_case(text)
        return res_str[0].lower() + res_str[1:]
    except IndexError:
        return "not valid string"


def to_snake_case(text: str, upper: bool) -> str:
    return to_complex_case(text, upper, "_")


def to_kebab_case(text: str, upper: bool) -> str:
    return to_complex_case(text, upper, "-")


if __name__ == "__main__":
    __import__("doctest").testmod()
