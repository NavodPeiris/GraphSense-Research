

def is_isogram(string: str) -> bool:
    if not all(x.isalpha() for x in string):
        raise ValueError("String must only contain alphabetic characters.")

    letters = sorted(string.lower())
    return len(letters) == len(set(letters))


if __name__ == "__main__":
    input_str = input("Enter a string ").strip()

    isogram = is_isogram(input_str)
    print(f"{input_str} is {'an' if isogram else 'not an'} isogram.")
