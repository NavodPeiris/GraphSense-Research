

from collections import Counter
from timeit import timeit






def can_string_be_rearranged_as_palindrome_counter(
    input_str: str = "",
) -> bool:
    return sum(c % 2 for c in Counter(input_str.replace(" ", "").lower()).values()) < 2


def can_string_be_rearranged_as_palindrome(input_str: str = "") -> bool:
    if len(input_str) == 0:
        return True
    lower_case_input_str = input_str.replace(" ", "").lower()
    
    character_freq_dict: dict[str, int] = {}

    for character in lower_case_input_str:
        character_freq_dict[character] = character_freq_dict.get(character, 0) + 1
    odd_char = 0

    for character_count in character_freq_dict.values():
        if character_count % 2:
            odd_char += 1
    return not odd_char > 1


def benchmark(input_str: str = "") -> None:
    print("\nFor string = ", input_str, ":")
    print(
        "> can_string_be_rearranged_as_palindrome_counter()",
        "\tans =",
        can_string_be_rearranged_as_palindrome_counter(input_str),
        "\ttime =",
        timeit(
            "z.can_string_be_rearranged_as_palindrome_counter(z.check_str)",
            setup="import __main__ as z",
        ),
        "seconds",
    )
    print(
        "> can_string_be_rearranged_as_palindrome()",
        "\tans =",
        can_string_be_rearranged_as_palindrome(input_str),
        "\ttime =",
        timeit(
            "z.can_string_be_rearranged_as_palindrome(z.check_str)",
            setup="import __main__ as z",
        ),
        "seconds",
    )


if __name__ == "__main__":
    check_str = input(
        "Enter string to determine if it can be rearranged as a palindrome or not: "
    ).strip()
    benchmark(check_str)
    status = can_string_be_rearranged_as_palindrome_counter(check_str)
    print(f"{check_str} can {'' if status else 'not '}be rearranged as a palindrome")
