

def running_key_encrypt(key: str, plaintext: str) -> str:
    
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    key_length = len(key)
    ciphertext = []
    ord_a = ord("A")

    for i, char in enumerate(plaintext):
        p = ord(char) - ord_a
        k = ord(key[i % key_length]) - ord_a
        c = (p + k) % 26
        ciphertext.append(chr(c + ord_a))

    return "".join(ciphertext)


def running_key_decrypt(key: str, ciphertext: str) -> str:
    
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    key_length = len(key)
    plaintext = []
    ord_a = ord("A")

    for i, char in enumerate(ciphertext):
        c = ord(char) - ord_a
        k = ord(key[i % key_length]) - ord_a
        p = (c - k) % 26
        plaintext.append(chr(p + ord_a))

    return "".join(plaintext)


def test_running_key_encrypt() -> None:
   pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_running_key_encrypt()

    plaintext = input("Enter the plaintext: ").upper()
    print(f"\n{plaintext = }")

    key = "How does the duck know that? said Victor"
    encrypted_text = running_key_encrypt(key, plaintext)
    print(f"{encrypted_text = }")

    decrypted_text = running_key_decrypt(key, encrypted_text)
    print(f"{decrypted_text = }")
