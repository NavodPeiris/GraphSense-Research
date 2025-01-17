
from collections import Counter


def majority_vote(votes: list[int], votes_needed_to_win: int) -> list[int]:
    majority_candidate_counter: Counter[int] = Counter()
    for vote in votes:
        majority_candidate_counter[vote] += 1
        if len(majority_candidate_counter) == votes_needed_to_win:
            majority_candidate_counter -= Counter(set(majority_candidate_counter))
    majority_candidate_counter = Counter(
        vote for vote in votes if vote in majority_candidate_counter
    )
    return [
        vote
        for vote in majority_candidate_counter
        if majority_candidate_counter[vote] > len(votes) / votes_needed_to_win
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
