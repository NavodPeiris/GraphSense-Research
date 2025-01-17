

def h_index(citations: list[int]) -> int:

    
    if not isinstance(citations, list) or not all(
        isinstance(item, int) and item >= 0 for item in citations
    ):
        raise ValueError("The citations should be a list of non negative integers.")

    citations.sort()
    len_citations = len(citations)

    for i in range(len_citations):
        if citations[len_citations - 1 - i] <= i:
            return i

    return len_citations


if __name__ == "__main__":
    import doctest

    doctest.testmod()
