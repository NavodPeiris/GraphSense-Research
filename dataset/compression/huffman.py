from __future__ import annotations

import sys


class Letter:
    def __init__(self, letter: str, freq: int):
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right


def parse_file(file_path: str) -> list[Letter]:
    
    chars: dict[str, int] = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    return sorted((Letter(c, f) for c, f in chars.items()), key=lambda x: x.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    
    response: list[Letter | TreeNode] = list(letters)
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters


def huffman(file_path: str) -> None:
    
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(letters[c], end=" ")
    print()


if __name__ == "__main__":
    
    huffman(sys.argv[1])
