
def is_valid(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> bool:
    
    for i in range(len(word)):
        if vertical:
            if row + i >= len(puzzle) or puzzle[row + i][col] != "":
                return False
        elif col + i >= len(puzzle[0]) or puzzle[row][col + i] != "":
            return False
    return True


def place_word(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> None:
    
    for i, char in enumerate(word):
        if vertical:
            puzzle[row + i][col] = char
        else:
            puzzle[row][col + i] = char


def remove_word(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> None:
    
    for i in range(len(word)):
        if vertical:
            puzzle[row + i][col] = ""
        else:
            puzzle[row][col + i] = ""


def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
   
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == "":
                for word in words:
                    for vertical in [True, False]:
                        if is_valid(puzzle, word, row, col, vertical):
                            place_word(puzzle, word, row, col, vertical)
                            words.remove(word)
                            if solve_crossword(puzzle, words):
                                return True
                            words.append(word)
                            remove_word(puzzle, word, row, col, vertical)
                return False
    return True


if __name__ == "__main__":
    PUZZLE = [[""] * 3 for _ in range(3)]
    WORDS = ["cat", "dog", "car"]

    if solve_crossword(PUZZLE, WORDS):
        print("Solution found:")
        for row in PUZZLE:
            print(" ".join(row))
    else:
        print("No solution found:")
