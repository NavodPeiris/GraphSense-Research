from __future__ import annotations


def knuth_morris_pratt(text: str, pattern: str) -> int:

    
    failure = get_failure_array(pattern)

    
    i, j = 0, 0  
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return i - j
            j += 1

        
        
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return -1


def get_failure_array(pattern: str) -> list[int]:
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert knuth_morris_pratt(text1, pattern)
    assert knuth_morris_pratt(text2, pattern)

    
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert knuth_morris_pratt(text, pattern)

    
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert knuth_morris_pratt(text, pattern)

    
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert knuth_morris_pratt(text, pattern)

    
    kmp = "knuth_morris_pratt"
    assert all(
        knuth_morris_pratt(kmp, s) == kmp.find(s)
        for s in ("kn", "h_m", "rr", "tt", "not there")
    )

    
    pattern = "aabaabaaa"
    assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
