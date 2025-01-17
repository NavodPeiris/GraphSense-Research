

def score_function(
    source_char: str,
    target_char: str,
    match: int = 1,
    mismatch: int = -1,
    gap: int = -2,
) -> int:
    if "-" in (source_char, target_char):
        return gap
    return match if source_char == target_char else mismatch


def smith_waterman(
    query: str,
    subject: str,
    match: int = 1,
    mismatch: int = -1,
    gap: int = -2,
) -> list[list[int]]:
    
    
    query = query.upper()
    subject = subject.upper()

    
    m = len(query)
    n = len(subject)
    score = [[0] * (n + 1) for _ in range(m + 1)]
    kwargs = {"match": match, "mismatch": mismatch, "gap": gap}

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            match = score[i - 1][j - 1] + score_function(
                query[i - 1], subject[j - 1], **kwargs
            )
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap

            
            score[i][j] = max(0, match, delete, insert)

    return score


def traceback(score: list[list[int]], query: str, subject: str) -> str:
    
    
    query = query.upper()
    subject = subject.upper()
    
    max_value = float("-inf")
    i_max = j_max = 0
    for i, row in enumerate(score):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                i_max, j_max = i, j
    
    i = i_max
    j = j_max
    align1 = ""
    align2 = ""
    gap = score_function("-", "-")
    
    if i == 0 or j == 0:
        return ""
    while i > 0 and j > 0:
        if score[i][j] == score[i - 1][j - 1] + score_function(
            query[i - 1], subject[j - 1]
        ):
            
            align1 = query[i - 1] + align1
            align2 = subject[j - 1] + align2
            i -= 1
            j -= 1
        elif score[i][j] == score[i - 1][j] + gap:
            
            align1 = query[i - 1] + align1
            align2 = f"-{align2}"
            i -= 1
        else:
            
            align1 = f"-{align1}"
            align2 = subject[j - 1] + align2
            j -= 1

    return f"{align1}\n{align2}"


if __name__ == "__main__":
    query = "HEAGAWGHEE"
    subject = "PAWHEAE"

    score = smith_waterman(query, subject, match=1, mismatch=-1, gap=-2)
    print(traceback(score, query, subject))
