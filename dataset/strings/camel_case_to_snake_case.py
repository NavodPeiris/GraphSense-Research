def camel_to_snake_case(input_str: str) -> str:

    
    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    snake_str = ""

    for index, char in enumerate(input_str):
        if char.isupper():
            snake_str += "_" + char.lower()

        
        elif input_str[index - 1].isdigit() and char.islower():
            snake_str += "_" + char

        
        elif input_str[index - 1].isalpha() and char.isnumeric():
            snake_str += "_" + char.lower()

        
        elif not char.isalnum():
            snake_str += "_"

        else:
            snake_str += char

    
    if snake_str[0] == "_":
        snake_str = snake_str[1:]

    return snake_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
