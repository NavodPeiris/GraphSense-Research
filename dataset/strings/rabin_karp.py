
alphabet_size = 256

modulus = 1000003


def rabin_karp(pattern: str, text: str) -> bool:
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return False

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(t_len - p_len + 1):
        if text_hash == p_hash and text[i : i + p_len] == pattern:
            return True
        if i == t_len - p_len:
            continue
        
        text_hash = (
            (text_hash - ord(text[i]) * modulus_power) * alphabet_size
            + ord(text[i + p_len])
        ) % modulus
    return False


def test_rabin_karp() -> None:
    
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(pattern, text1)
    assert not rabin_karp(pattern, text2)

    
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert rabin_karp(pattern, text)

    
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)

    
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)

    
    pattern = "Lü"
    text = "Lüsai"
    assert rabin_karp(pattern, text)
    pattern = "Lue"
    assert not rabin_karp(pattern, text)
    print("Success.")


if __name__ == "__main__":
    test_rabin_karp()
