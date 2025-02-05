import random


class Onepad:
    @staticmethod
    def encrypt(text: str) -> tuple[list[int], list[int]]:
        
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    @staticmethod
    def decrypt(cipher: list[int], key: list[int]) -> str:
        
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - (key[i]) ** 2) / key[i])
            plain.append(chr(p))
        return "".join(plain)


if __name__ == "__main__":
    c, k = Onepad().encrypt("Hello")
    print(c, k)
    print(Onepad().decrypt(c, k))
