def alternative_list_arrange(first_input_list: list, second_input_list: list) -> list:
    first_input_list_length: int = len(first_input_list)
    second_input_list_length: int = len(second_input_list)
    abs_length: int = (
        first_input_list_length
        if first_input_list_length > second_input_list_length
        else second_input_list_length
    )
    output_result_list: list = []
    for char_count in range(abs_length):
        if char_count < first_input_list_length:
            output_result_list.append(first_input_list[char_count])
        if char_count < second_input_list_length:
            output_result_list.append(second_input_list[char_count])

    return output_result_list


if __name__ == "__main__":
    print(alternative_list_arrange(["A", "B", "C"], [1, 2, 3, 4, 5]), end=" ")
