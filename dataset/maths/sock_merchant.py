from collections import Counter


def sock_merchant(colors: list[int]) -> int:
    return sum(socks_by_color // 2 for socks_by_color in Counter(colors).values())


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    colors = [int(x) for x in input("Enter socks by color :").rstrip().split()]
    print(f"sock_merchant({colors}) = {sock_merchant(colors)}")
