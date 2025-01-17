

class RadixNode:
    def __init__(self, prefix: str = "", is_leaf: bool = False) -> None:
        
        self.nodes: dict[str, RadixNode] = {}

        
        self.is_leaf = is_leaf

        self.prefix = prefix

    def match(self, word: str) -> tuple[str, str, str]:
        x = 0
        for q, w in zip(self.prefix, word):
            if q != w:
                break

            x += 1

        return self.prefix[:x], self.prefix[x:], word[x:]

    def insert_many(self, words: list[str]) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        
        
        if self.prefix == word and not self.is_leaf:
            self.is_leaf = True

        
        
        
        elif word[0] not in self.nodes:
            self.nodes[word[0]] = RadixNode(prefix=word, is_leaf=True)

        else:
            incoming_node = self.nodes[word[0]]
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )

            
            
            if remaining_prefix == "":
                self.nodes[matching_string[0]].insert(remaining_word)

            
            
            
            else:
                incoming_node.prefix = remaining_prefix

                aux_node = self.nodes[matching_string[0]]
                self.nodes[matching_string[0]] = RadixNode(matching_string, False)
                self.nodes[matching_string[0]].nodes[remaining_prefix[0]] = aux_node

                if remaining_word == "":
                    self.nodes[matching_string[0]].is_leaf = True
                else:
                    self.nodes[matching_string[0]].insert(remaining_word)

    def find(self, word: str) -> bool:
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )
            
            if remaining_prefix != "":
                return False
            
            elif remaining_word == "":
                return incoming_node.is_leaf
            
            else:
                return incoming_node.find(remaining_word)

    def delete(self, word: str) -> bool:
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )
            
            if remaining_prefix != "":
                return False
            
            elif remaining_word != "":
                return incoming_node.delete(remaining_word)
            
            elif not incoming_node.is_leaf:
                return False
            else:
                
                if len(incoming_node.nodes) == 0:
                    del self.nodes[word[0]]
                    
                    if len(self.nodes) == 1 and not self.is_leaf:
                        merging_node = next(iter(self.nodes.values()))
                        self.is_leaf = merging_node.is_leaf
                        self.prefix += merging_node.prefix
                        self.nodes = merging_node.nodes
                
                elif len(incoming_node.nodes) > 1:
                    incoming_node.is_leaf = False
                
                else:
                    merging_node = next(iter(incoming_node.nodes.values()))
                    incoming_node.is_leaf = merging_node.is_leaf
                    incoming_node.prefix += merging_node.prefix
                    incoming_node.nodes = merging_node.nodes

                return True

    def print_tree(self, height: int = 0) -> None:
        if self.prefix != "":
            print("-" * height, self.prefix, "  (leaf)" if self.is_leaf else "")

        for value in self.nodes.values():
            value.print_tree(height + 1)


def test_trie() -> bool:
    words = "banana bananas bandana band apple all beast".split()
    root = RadixNode()
    root.insert_many(words)

    assert all(root.find(word) for word in words)
    assert not root.find("bandanas")
    assert not root.find("apps")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")

    return True


def pytests() -> None:
    assert test_trie()


def main() -> None:
    root = RadixNode()
    words = "banana bananas bandanas bandana band apple all beast".split()
    root.insert_many(words)

    print("Words:", words)
    print("Tree:")
    root.print_tree()


if __name__ == "__main__":
    main()
