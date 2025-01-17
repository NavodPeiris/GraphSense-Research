def strip(user_string: str, characters: str = " \t\n\r") -> str:

    start = 0
    end = len(user_string)

    while start < end and user_string[start] in characters:
        start += 1

    while end > start and user_string[end - 1] in characters:
        end -= 1

    return user_string[start:end]
