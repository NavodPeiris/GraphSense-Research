

from dataclasses import dataclass

__version__ = "0.1"
__author__ = "Lucia Harcekova"


@dataclass
class Token:
    

    offset: int
    length: int
    indicator: str

    def __repr__(self) -> str:
        
        return f"({self.offset}, {self.length}, {self.indicator})"


class LZ77Compressor:
    

    def __init__(self, window_size: int = 13, lookahead_buffer_size: int = 6) -> None:
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size
        self.search_buffer_size = self.window_size - self.lookahead_buffer_size

    def compress(self, text: str) -> list[Token]:
        

        output = []
        search_buffer = ""

        
        while text:
            
            token = self._find_encoding_token(text, search_buffer)

            
            search_buffer += text[: token.length + 1]
            if len(search_buffer) > self.search_buffer_size:
                search_buffer = search_buffer[-self.search_buffer_size :]

            
            text = text[token.length + 1 :]

            
            output.append(token)

        return output

    def decompress(self, tokens: list[Token]) -> str:
        

        output = ""

        for token in tokens:
            for _ in range(token.length):
                output += output[-token.offset]
            output += token.indicator

        return output

    def _find_encoding_token(self, text: str, search_buffer: str) -> Token:
        

        if not text:
            raise ValueError("We need some text to work with.")

        
        length, offset = 0, 0

        if not search_buffer:
            return Token(offset, length, text[length])

        for i, character in enumerate(search_buffer):
            found_offset = len(search_buffer) - i
            if character == text[0]:
                found_length = self._match_length_from_index(text, search_buffer, 0, i)
                
                if found_length >= length:
                    offset, length = found_offset, found_length

        return Token(offset, length, text[length])

    def _match_length_from_index(
        self, text: str, window: str, text_index: int, window_index: int
    ) -> int:
        
        if not text or text[text_index] != window[window_index]:
            return 0
        return 1 + self._match_length_from_index(
            text, window + text[text_index], text_index + 1, window_index + 1
        )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    lz77_compressor = LZ77Compressor(window_size=13, lookahead_buffer_size=6)

   
    TEXT = "cabracadabrarrarrad"
    compressed_text = lz77_compressor.compress(TEXT)
    print(lz77_compressor.compress("ababcbababaa"))
    decompressed_text = lz77_compressor.decompress(compressed_text)
    assert decompressed_text == TEXT, "The LZ77 algorithm returned the invalid result."
