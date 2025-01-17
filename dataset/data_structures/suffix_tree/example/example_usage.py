







from data_structures.suffix_tree.suffix_tree import SuffixTree


def main() -> None:
    text = "monkey banana"
    suffix_tree = SuffixTree(text)

    patterns = ["ana", "ban", "na", "xyz", "mon"]
    for pattern in patterns:
        found = suffix_tree.search(pattern)
        print(f"Pattern '{pattern}' found: {found}")


if __name__ == "__main__":
    main()
