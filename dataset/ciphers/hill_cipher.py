

import string

import numpy as np

from maths.greatest_common_divisor import greatest_common_divisor


class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    
    
    modulus = np.vectorize(lambda x: x % 36)

    to_int = np.vectorize(round)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        
        self.encrypt_key = self.modulus(encrypt_key)  
        self.check_determinant() 
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        
        det = round(np.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            msg = (
                f"determinant modular {req_l} of encryption key({det}) "
                f"is not co prime w.r.t {req_l}.\nTry another key."
            )
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        
        chars = [char for char in text.upper() if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        
        det = round(np.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
        )

        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


def main() -> None:
    n = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        hill_matrix.append(row)

    hc = HillCipher(np.array(hill_matrix))

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
    option = input("\n1. Encrypt\n2. Decrypt\n")
    if option == "1":
        text_e = input("What text would you like to encrypt?: ")
        print("Your encrypted text is:")
        print(hc.encrypt(text_e))
    elif option == "2":
        text_d = input("What text would you like to decrypt?: ")
        print("Your decrypted text is:")
        print(hc.decrypt(text_d))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
