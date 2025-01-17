
from __future__ import annotations


def generate_all_permutations(sequence: list[int | str]) -> None:
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
) -> None:
    
    if index == len(sequence):
        print(current_sequence)
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False



sequence: list[int | str] = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence_2: list[int | str] = ["A", "B", "C"]
generate_all_permutations(sequence_2)
