import secrets
from random import shuffle
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation


def password_generator(length: int = 8) -> str:
    chars = ascii_letters + digits + punctuation
    return "".join(secrets.choice(chars) for _ in range(length))





def alternative_password_generator(chars_incl: str, i: int) -> str:
    
    
    
    i -= len(chars_incl)
    quotient = i // 3
    remainder = i % 3
    
    
    chars = (
        chars_incl
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    list_of_chars = list(chars)
    shuffle(list_of_chars)
    return "".join(list_of_chars)

    


def random(chars_incl: str, i: int) -> str:
    return "".join(secrets.choice(chars_incl) for _ in range(i))


def is_strong_password(password: str, min_length: int = 8) -> bool:

    if len(password) < min_length:
        return False

    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    return upper and lower and num and spec_char


def main():
    length = int(input("Please indicate the max length of your password: ").strip())
    chars_incl = input(
        "Please indicate the characters that must be in your password: "
    ).strip()
    print("Password generated:", password_generator(length))
    print(
        "Alternative Password generated:",
        alternative_password_generator(chars_incl, length),
    )
    print("[If you are thinking of using this password, You better save it.]")


if __name__ == "__main__":
    main()
