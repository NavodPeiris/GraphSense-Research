
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  

REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encrypt(message: str) -> str:
    
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())


def decrypt(message: str) -> str:
    
    return "".join(REVERSE_DICT[char] for char in message.split())


def main() -> None:
    
    message = "Morse code here!"
    print(message)
    message = encrypt(message)
    print(message)
    message = decrypt(message)
    print(message)


if __name__ == "__main__":
    main()
