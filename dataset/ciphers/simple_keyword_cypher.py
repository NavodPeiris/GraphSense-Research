def remove_duplicates(key: str) -> str:
    

    key_no_dups = ""
    for ch in key:
        if ch == " " or (ch not in key_no_dups and ch.isalpha()):
            key_no_dups += ch
    return key_no_dups


def create_cipher_map(key: str) -> dict[str, str]:
    
    alphabet = [chr(i + 65) for i in range(26)]
    
    key = remove_duplicates(key.upper())
    offset = len(key)
    
    cipher_alphabet = {alphabet[i]: char for i, char in enumerate(key)}
    
    for i in range(len(cipher_alphabet), 26):
        char = alphabet[i - offset]
        
        while char in key:
            offset -= 1
            char = alphabet[i - offset]
        cipher_alphabet[alphabet[i]] = char
    return cipher_alphabet


def encipher(message: str, cipher_map: dict[str, str]) -> str:
    
    return "".join(cipher_map.get(ch, ch) for ch in message.upper())


def decipher(message: str, cipher_map: dict[str, str]) -> str:
    
    rev_cipher_map = {v: k for k, v in cipher_map.items()}
    return "".join(rev_cipher_map.get(ch, ch) for ch in message.upper())


def main() -> None:
    
    message = input("Enter message to encode or decode: ").strip()
    key = input("Enter keyword: ").strip()
    option = input("Encipher or decipher? E/D:").strip()[0].lower()
    try:
        func = {"e": encipher, "d": decipher}[option]
    except KeyError:
        raise KeyError("invalid input option")
    cipher_map = create_cipher_map(key)
    print(func(message, cipher_map))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
