
from random import choice, randint, shuffle





WORDS = ["cat", "dog", "snake", "fish"]

WIDTH = 10
HEIGHT = 10


class WordSearch:

    def __init__(self, words: list[str], width: int, height: int) -> None:
        self.words = words
        self.width = width
        self.height = height

        
        self.board: list[list[str | None]] = [[None] * width for _ in range(height)]

    def insert_north(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length > row + 1:
                continue

            
            for col in cols:
                
                
                letters_above = [self.board[row - i][col] for i in range(word_length)]
                if all(letter is None for letter in letters_above):
                    
                    for i in range(word_length):
                        self.board[row - i][col] = word[i]
                    return

    def insert_northeast(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length > row + 1:
                continue

            
            for col in cols:
                
                if word_length + col > self.width:
                    continue

                
                
                letters_diagonal_left = [
                    self.board[row - i][col + i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    
                    for i in range(word_length):
                        self.board[row - i][col + i] = word[i]
                    return

    def insert_east(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            for col in cols:
                
                if word_length + col > self.width:
                    continue

                
                
                letters_left = [self.board[row][col + i] for i in range(word_length)]
                if all(letter is None for letter in letters_left):
                    
                    for i in range(word_length):
                        self.board[row][col + i] = word[i]
                    return

    def insert_southeast(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length + row > self.height:
                continue

            
            for col in cols:
                
                if word_length + col > self.width:
                    continue

                
                
                letters_diagonal_left = [
                    self.board[row + i][col + i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    
                    for i in range(word_length):
                        self.board[row + i][col + i] = word[i]
                    return

    def insert_south(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length + row > self.height:
                continue

            
            for col in cols:
                
                
                letters_below = [self.board[row + i][col] for i in range(word_length)]
                if all(letter is None for letter in letters_below):
                    
                    for i in range(word_length):
                        self.board[row + i][col] = word[i]
                    return

    def insert_southwest(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length + row > self.height:
                continue

            
            for col in cols:
                
                if word_length > col + 1:
                    continue

                
                
                letters_diagonal_left = [
                    self.board[row + i][col - i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    
                    for i in range(word_length):
                        self.board[row + i][col - i] = word[i]
                    return

    def insert_west(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            for col in cols:
                
                if word_length > col + 1:
                    continue

                
                
                letters_left = [self.board[row][col - i] for i in range(word_length)]
                if all(letter is None for letter in letters_left):
                    
                    for i in range(word_length):
                        self.board[row][col - i] = word[i]
                    return

    def insert_northwest(self, word: str, rows: list[int], cols: list[int]) -> None:
        word_length = len(word)
        
        for row in rows:
            
            if word_length > row + 1:
                continue

            
            for col in cols:
                
                if word_length > col + 1:
                    continue

                
                
                letters_diagonal_left = [
                    self.board[row - i][col - i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    
                    for i in range(word_length):
                        self.board[row - i][col - i] = word[i]
                    return

    def generate_board(self) -> None:
        directions = (
            self.insert_north,
            self.insert_northeast,
            self.insert_east,
            self.insert_southeast,
            self.insert_south,
            self.insert_southwest,
            self.insert_west,
            self.insert_northwest,
        )
        for word in self.words:
            
            
            rows, cols = list(range(self.height)), list(range(self.width))
            shuffle(rows)
            shuffle(cols)

            
            choice(directions)(word, rows, cols)


def visualise_word_search(
    board: list[list[str | None]] | None = None, *, add_fake_chars: bool = True
) -> None:
    if board is None:
        word_search = WordSearch(WORDS, WIDTH, HEIGHT)
        word_search.generate_board()
        board = word_search.board

    result = ""
    for row in range(len(board)):
        for col in range(len(board[0])):
            character = "#"
            if (letter := board[row][col]) is not None:
                character = letter
            
            elif add_fake_chars:
                character = chr(randint(97, 122))
            result += f"{character} "
        result += "\n"
    print(result, end="")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    visualise_word_search()
