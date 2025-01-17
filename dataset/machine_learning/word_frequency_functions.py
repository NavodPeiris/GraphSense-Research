import string
from math import log10



def term_frequency(term: str, document: str) -> int:
    
    document_without_punctuation = document.translate(
        str.maketrans("", "", string.punctuation)
    ).replace("\n", "")
    tokenize_document = document_without_punctuation.split(" ")  
    return len([word for word in tokenize_document if word.lower() == term.lower()])


def document_frequency(term: str, corpus: str) -> tuple[int, int]:
    corpus_without_punctuation = corpus.lower().translate(
        str.maketrans("", "", string.punctuation)
    )  
    docs = corpus_without_punctuation.split("\n")
    term = term.lower()
    return (len([doc for doc in docs if term in doc]), len(docs))


def inverse_document_frequency(df: int, n: int, smoothing=False) -> float:
    if smoothing:
        if n == 0:
            raise ValueError("log10(0) is undefined.")
        return round(1 + log10(n / (1 + df)), 3)

    if df == 0:
        raise ZeroDivisionError("df must be > 0")
    elif n == 0:
        raise ValueError("log10(0) is undefined.")
    return round(log10(n / df), 3)


def tf_idf(tf: int, idf: int) -> float:
    return round(tf * idf, 3)
