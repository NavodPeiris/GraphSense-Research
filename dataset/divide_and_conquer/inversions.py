

def count_inversions_bf(arr):

    num_inversions = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_inversions += 1

    return num_inversions


def count_inversions_recursive(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    p = arr[0:mid]
    q = arr[mid:]

    a, inversion_p = count_inversions_recursive(p)
    b, inversions_q = count_inversions_recursive(q)
    c, cross_inversions = _count_cross_inversions(a, b)

    num_inversions = inversion_p + inversions_q + cross_inversions
    return c, num_inversions


def _count_cross_inversions(p, q):

    r = []
    i = j = num_inversion = 0
    while i < len(p) and j < len(q):
        if p[i] > q[j]:
            
            
            
            num_inversion += len(p) - i
            r.append(q[j])
            j += 1
        else:
            r.append(p[i])
            i += 1

    if i < len(p):
        r.extend(p[i:])
    else:
        r.extend(q[j:])

    return r, num_inversion


def main():
    arr_1 = [10, 2, 1, 5, 5, 2, 11]

    
    

    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 8

    print("number of inversions = ", num_inversions_bf)

    

    arr_1.sort()
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)

    
    arr_1 = []
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)


if __name__ == "__main__":
    main()
