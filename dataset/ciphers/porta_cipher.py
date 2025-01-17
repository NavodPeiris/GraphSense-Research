alphabet = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}


def generate_table(key: str) -> list[tuple[str, str]]:
   
    return [alphabet[char] for char in key.upper()]


def encrypt(key: str, words: str) -> str:
    
    cipher = ""
    count = 0
    table = generate_table(key)
    for char in words.upper():
        cipher += get_opponent(table[count], char)
        count = (count + 1) % len(table)
    return cipher


def decrypt(key: str, words: str) -> str:
    
    return encrypt(key, words)


def get_position(table: tuple[str, str], char: str) -> tuple[int, int]:
    
    row = 0 if char in table[0] else 1
    col = table[row].index(char)
    return row, col


def get_opponent(table: tuple[str, str], char: str) -> str:
    
    row, col = get_position(table, char.upper())
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char


if __name__ == "__main__":
    import doctest

    doctest.testmod()  
    
    key = input("Enter key: ").strip()
    text = input("Enter text to encrypt: ").strip()
    cipher_text = encrypt(key, text)

    print(f"Encrypted: {cipher_text}")
    print(f"Decrypted with key: {decrypt(key, cipher_text)}")
