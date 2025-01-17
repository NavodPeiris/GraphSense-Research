

from collections import defaultdict


def word_occurrence(sentence: str) -> dict:
    occurrence: defaultdict[str, int] = defaultdict(int)
    
    for word in sentence.split():
        occurrence[word] += 1
    return occurrence


if __name__ == "__main__":
    for word, count in word_occurrence("INPUT STRING").items():
        print(f"{word}: {count}")
