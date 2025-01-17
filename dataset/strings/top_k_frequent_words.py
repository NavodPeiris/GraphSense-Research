
from collections import Counter
from functools import total_ordering

from data_structures.heap.heap import Heap


@total_ordering
class WordCount:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, WordCount):
            return NotImplemented
        return self.count == other.count

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, WordCount):
            return NotImplemented
        return self.count < other.count


def top_k_frequent_words(words: list[str], k_value: int) -> list[str]:
    heap: Heap[WordCount] = Heap()
    count_by_word = Counter(words)
    heap.build_max_heap(
        [WordCount(word, count) for word, count in count_by_word.items()]
    )
    return [heap.extract_max().word for _ in range(min(k_value, len(count_by_word)))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
