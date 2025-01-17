def alternative_string_arrange(first_str: str, second_str: str) -> str:
    first_str_length: int = len(first_str)
    second_str_length: int = len(second_str)
    abs_length: int = (
        first_str_length if first_str_length > second_str_length else second_str_length
    )
    output_list: list = []
    for char_count in range(abs_length):
        if char_count < first_str_length:
            output_list.append(first_str[char_count])
        if char_count < second_str_length:
            output_list.append(second_str[char_count])
    return "".join(output_list)


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
