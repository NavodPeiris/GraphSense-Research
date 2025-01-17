







from data_structures.suffix_tree.suffix_tree_node import SuffixTreeNode


class SuffixTree:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.root: SuffixTreeNode = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self) -> None:
        text = self.text
        n = len(text)
        for i in range(n):
            suffix = text[i:]
            self._add_suffix(suffix, i)

    def _add_suffix(self, suffix: str, index: int) -> None:
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
        node.is_end_of_string = True
        node.start = index
        node.end = index + len(suffix) - 1

    def search(self, pattern: str) -> bool:
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
