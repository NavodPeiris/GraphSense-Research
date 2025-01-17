def calculate_pi(limit: int) -> str:
    
    q = 1
    r = 0
    t = 1
    k = 1
    n = 3
    m = 3

    decimal = limit
    counter = 0

    result = ""

    
    
    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            result += str(n)
            if counter == 0:
                result += "."

            if decimal == counter:
                break

            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * m
            nn = (q * (7 * k) + 2 + (r * m)) // (t * m)
            q *= k
            t *= m
            m += 2
            k += 1
            n = nn
            r = nr
    return result


def main() -> None:
    print(f"{calculate_pi(50) = }")
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
