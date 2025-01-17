def decimal_to_negative_base_2(num: int) -> int:
    if num == 0:
        return 0
    ans = ""
    while num != 0:
        num, rem = divmod(num, -2)
        if rem < 0:
            rem += 2
            num += 1
        ans = str(rem) + ans
    return int(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
