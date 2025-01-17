import math



def main() -> None:
    message = input("Enter message: ")
    key = int(input(f"Enter key [2-{len(message) - 1}]: "))
    mode = input("Encryption/Decryption [e/d]: ")

    if mode.lower().startswith("e"):
        text = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        text = decrypt_message(key, message)

    
    print(f"Output:\n{text + '|'}")


def encrypt_message(key: int, message: str) -> str:
    
    cipher_text = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return "".join(cipher_text)


def decrypt_message(key: int, message: str) -> str:
    
    num_cols = math.ceil(len(message) / key)
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(message)
    plain_text = [""] * num_cols
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_cols) or (
            (col == num_cols - 1) and (row >= num_rows - num_shaded_boxes)
        ):
            col = 0
            row += 1

    return "".join(plain_text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
