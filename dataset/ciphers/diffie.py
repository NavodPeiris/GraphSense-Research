from __future__ import annotations


def find_primitive(modulus: int) -> int | None:
    
    for r in range(1, modulus):
        li = []
        for x in range(modulus - 1):
            val = pow(r, x, modulus)
            if val in li:
                break
            li.append(val)
        else:
            return r
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    prime = int(input("Enter a prime number q: "))
    primitive_root = find_primitive(prime)
    if primitive_root is None:
        print(f"Cannot find the primitive for the value: {primitive_root!r}")
    else:
        a_private = int(input("Enter private key of A: "))
        a_public = pow(primitive_root, a_private, prime)
        b_private = int(input("Enter private key of B: "))
        b_public = pow(primitive_root, b_private, prime)

        a_secret = pow(b_public, a_private, prime)
        b_secret = pow(a_public, b_private, prime)

        print("The key value generated by A is: ", a_secret)
        print("The key value generated by B is: ", b_secret)
