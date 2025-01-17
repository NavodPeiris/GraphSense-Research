
from __future__ import annotations


def all_construct(target: str, word_bank: list[str] | None = None) -> list[list[str]]:

    word_bank = word_bank or []
    
    table_size: int = len(target) + 1

    table: list[list[list[str]]] = []
    for _ in range(table_size):
        table.append([])
    
    table[0] = [[]]  

    
    for i in range(table_size):
        
        if table[i] != []:
            for word in word_bank:
                
                if target[i : i + len(word)] == word:
                    new_combinations: list[list[str]] = [
                        [word, *way] for way in table[i]
                    ]
                    
                    
                    table[i + len(word)] += new_combinations

    
    for combination in table[len(target)]:
        combination.reverse()

    return table[len(target)]


if __name__ == "__main__":
    print(all_construct("jwajalapa", ["jwa", "j", "w", "a", "la", "lapa"]))
    print(all_construct("rajamati", ["s", "raj", "amat", "raja", "ma", "i", "t"]))
    print(
        all_construct(
            "hexagonosaurus",
            ["h", "ex", "hex", "ag", "ago", "ru", "auru", "rus", "go", "no", "o", "s"],
        )
    )
