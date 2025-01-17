
from __future__ import annotations


TEST_CHARACTER_TO_NUMBER = {
    "A": "111", "B": "112", "C": "113", "D": "121", "E": "122", "F": "123", "G": "131",
    "H": "132", "I": "133", "J": "211", "K": "212", "L": "213", "M": "221", "N": "222",
    "O": "223", "P": "231", "Q": "232", "R": "233", "S": "311", "T": "312", "U": "313",
    "V": "321", "W": "322", "X": "323", "Y": "331", "Z": "332", "+": "333",
}


TEST_NUMBER_TO_CHARACTER = {val: key for key, val in TEST_CHARACTER_TO_NUMBER.items()}


def __encrypt_part(message_part: str, character_to_number: dict[str, str]) -> str:
    
    one, two, three = "", "", ""
    for each in (character_to_number[character] for character in message_part):
        one += each[0]
        two += each[1]
        three += each[2]

    return one + two + three


def __decrypt_part(
    message_part: str, character_to_number: dict[str, str]
) -> tuple[str, str, str]:
    
    this_part = "".join(character_to_number[character] for character in message_part)
    result = []
    tmp = ""
    for digit in this_part:
        tmp += digit
        if len(tmp) == len(message_part):
            result.append(tmp)
            tmp = ""

    return result[0], result[1], result[2]


def __prepare(
    message: str, alphabet: str
) -> tuple[str, str, dict[str, str], dict[str, str]]:
    
    alphabet = alphabet.replace(" ", "").upper()
    message = message.replace(" ", "").upper()

    
    if len(alphabet) != 27:
        raise KeyError("Length of alphabet has to be 27.")
    if any(char not in alphabet for char in message):
        raise ValueError("Each message character has to be included in alphabet!")

    
    character_to_number = dict(zip(alphabet, TEST_CHARACTER_TO_NUMBER.values()))
    number_to_character = {
        number: letter for letter, number in character_to_number.items()
    }

    return message, alphabet, character_to_number, number_to_character


def encrypt_message(
    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
) -> str:
    
    message, alphabet, character_to_number, number_to_character = __prepare(
        message, alphabet
    )

    encrypted_numeric = ""
    for i in range(0, len(message) + 1, period):
        encrypted_numeric += __encrypt_part(
            message[i : i + period], character_to_number
        )

    encrypted = ""
    for i in range(0, len(encrypted_numeric), 3):
        encrypted += number_to_character[encrypted_numeric[i : i + 3]]
    return encrypted


def decrypt_message(
    message: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period: int = 5
) -> str:
   
    message, alphabet, character_to_number, number_to_character = __prepare(
        message, alphabet
    )

    decrypted_numeric = []
    for i in range(0, len(message), period):
        a, b, c = __decrypt_part(message[i : i + period], character_to_number)

        for j in range(len(a)):
            decrypted_numeric.append(a[j] + b[j] + c[j])

    return "".join(number_to_character[each] for each in decrypted_numeric)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    msg = "DEFEND THE EAST WALL OF THE CASTLE."
    encrypted = encrypt_message(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    decrypted = decrypt_message(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
