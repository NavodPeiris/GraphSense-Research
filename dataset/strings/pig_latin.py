def pig_latin(word: str) -> str:
    if not (word or "").strip():
        return ""
    word = word.lower()
    if word[0] in "aeiou":
        return f"{word}way"
    for i, char in enumerate(word):  
        if char in "aeiou":
            break
    return f"{word[i:]}{word[:i]}ay"


if __name__ == "__main__":
    print(f"{pig_latin('friends') = }")
    word = input("Enter a word: ")
    print(f"{pig_latin(word) = }")
