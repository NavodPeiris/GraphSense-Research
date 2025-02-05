







import unittest

from data_structures.suffix_tree.suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "banana"
        self.suffix_tree = SuffixTree(self.text)

    def test_search_existing_patterns(self) -> None:
        patterns = ["ana", "ban", "na"]
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                assert self.suffix_tree.search(pattern), (
                    f"Pattern '{pattern}' should be found."
                )

    def test_search_non_existing_patterns(self) -> None:
        patterns = ["xyz", "apple", "cat"]
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                assert not self.suffix_tree.search(pattern), (
                    f"Pattern '{pattern}' should not be found."
                )

    def test_search_empty_pattern(self) -> None:
        assert self.suffix_tree.search(""), "An empty pattern should be found."

    def test_search_full_text(self) -> None:
        assert self.suffix_tree.search(self.text), (
            "The full text should be found in the suffix tree."
        )

    def test_search_substrings(self) -> None:
        substrings = ["ban", "ana", "a", "na"]
        for substring in substrings:
            with self.subTest(substring=substring):
                assert self.suffix_tree.search(substring), (
                    f"Substring '{substring}' should be found."
                )


if __name__ == "__main__":
    unittest.main()
