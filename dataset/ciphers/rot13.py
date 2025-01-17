def dencrypt(s: str, n: int = 13) -> str:
    
    out = ""
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out


def main() -> None:
    s0 = input("Enter message: ")

    s1 = dencrypt(s0, 13)
    print("Encryption:", s1)

    s2 = dencrypt(s1, 13)
    print("Decryption: ", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
