
B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> bytes:
    
    binary_data = "".join(bin(ord(d))[2:].zfill(8) for d in data.decode("utf-8"))
    binary_data = binary_data.ljust(5 * ((len(binary_data) // 5) + 1), "0")
    b32_chunks = map("".join, zip(*[iter(binary_data)] * 5))
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    return bytes(b32_result.ljust(8 * ((len(b32_result) // 8) + 1), "="), "utf-8")


def base32_decode(data: bytes) -> bytes:
    
    binary_chunks = "".join(
        bin(B32_CHARSET.index(_d))[2:].zfill(5)
        for _d in data.decode("utf-8").strip("=")
    )
    binary_data = list(map("".join, zip(*[iter(binary_chunks)] * 8)))
    return bytes("".join([chr(int(_d, 2)) for _d in binary_data]), "utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
