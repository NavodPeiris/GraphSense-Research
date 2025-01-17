def edit_distance(source: str, target: str) -> int:
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)

    delta = int(source[-1] != target[-1])  
    return min(
        edit_distance(source[:-1], target[:-1]) + delta,
        edit_distance(source, target[:-1]) + 1,
        edit_distance(source[:-1], target) + 1,
    )


if __name__ == "__main__":
    print(edit_distance("ATCGCTG", "TAGCTAA"))
