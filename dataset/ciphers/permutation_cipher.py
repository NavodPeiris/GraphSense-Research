

import random


def generate_valid_block_size(message_length: int) -> int:
    
    block_sizes = [
        block_size
        for block_size in range(2, message_length + 1)
        if message_length % block_size == 0
    ]
    return random.choice(block_sizes)


def generate_permutation_key(block_size: int) -> list[int]:
    
    digits = list(range(block_size))
    random.shuffle(digits)
    return digits


def encrypt(
    message: str, key: list[int] | None = None, block_size: int | None = None
) -> tuple[str, list[int]]:
   
    message = message.upper()
    message_length = len(message)

    if key is None or block_size is None:
        block_size = generate_valid_block_size(message_length)
        key = generate_permutation_key(block_size)

    encrypted_message = ""

    for i in range(0, message_length, block_size):
        block = message[i : i + block_size]
        rearranged_block = [block[digit] for digit in key]
        encrypted_message += "".join(rearranged_block)

    return encrypted_message, key


def decrypt(encrypted_message: str, key: list[int]) -> str:
    
    key_length = len(key)
    decrypted_message = ""

    for i in range(0, len(encrypted_message), key_length):
        block = encrypted_message[i : i + key_length]
        original_block = [""] * key_length
        for j, digit in enumerate(key):
            original_block[digit] = block[j]
        decrypted_message += "".join(original_block)

    return decrypted_message


def main() -> None:
    
    message = "HELLO WORLD"
    encrypted_message, key = encrypt(message)

    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
