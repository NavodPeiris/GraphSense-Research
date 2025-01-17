


from __future__ import annotations

import math
from collections import Counter
from string import ascii_lowercase


def calculate_prob(text: str) -> None:
    single_char_strings, two_char_strings = analyze_text(text)
    my_alphas = list(" " + ascii_lowercase)
    
    all_sum = sum(single_char_strings.values())

    
    my_fir_sum = 0
    
    for ch in my_alphas:
        if ch in single_char_strings:
            my_str = single_char_strings[ch]
            prob = my_str / all_sum
            my_fir_sum += prob * math.log2(prob)  

    
    print(f"{round(-1 * my_fir_sum):.1f}")

    
    all_sum = sum(two_char_strings.values())
    my_sec_sum = 0
    
    for ch0 in my_alphas:
        for ch1 in my_alphas:
            sequence = ch0 + ch1
            if sequence in two_char_strings:
                my_str = two_char_strings[sequence]
                prob = int(my_str) / all_sum
                my_sec_sum += prob * math.log2(prob)

    
    print(f"{round(-1 * my_sec_sum):.1f}")

    
    print(f"{round((-1 * my_sec_sum) - (-1 * my_fir_sum)):.1f}")


def analyze_text(text: str) -> tuple[dict, dict]:
    single_char_strings = Counter()  
    two_char_strings = Counter()  
    single_char_strings[text[-1]] += 1

    
    two_char_strings[" " + text[0]] += 1
    for i in range(len(text) - 1):
        single_char_strings[text[i]] += 1
        two_char_strings[text[i : i + 2]] += 1
    return single_char_strings, two_char_strings


def main():
    import doctest

    doctest.testmod()
    
    
    
    
    
    
    
    
    
    
    
    

    


if __name__ == "__main__":
    main()
