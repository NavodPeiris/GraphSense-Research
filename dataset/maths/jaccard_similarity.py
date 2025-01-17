

def jaccard_similarity(
    set_a: set[str] | list[str] | tuple[str],
    set_b: set[str] | list[str] | tuple[str],
    alternative_union=False,
):

    if isinstance(set_a, set) and isinstance(set_b, set):
        intersection_length = len(set_a.intersection(set_b))

        if alternative_union:
            union_length = len(set_a) + len(set_b)
        else:
            union_length = len(set_a.union(set_b))

        return intersection_length / union_length

    elif isinstance(set_a, (list, tuple)) and isinstance(set_b, (list, tuple)):
        intersection = [element for element in set_a if element in set_b]

        if alternative_union:
            return len(intersection) / (len(set_a) + len(set_b))
        else:
            
            union = list(set_a) + [element for element in set_b if element not in set_a]
            return len(intersection) / len(union)
    raise ValueError(
        "Set a and b must either both be sets or be either a list or a tuple."
    )


if __name__ == "__main__":
    set_a = {"a", "b", "c", "d", "e"}
    set_b = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similarity(set_a, set_b))
