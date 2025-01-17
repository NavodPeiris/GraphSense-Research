

def get_check_digit(barcode: int) -> int:
    barcode //= 10  
    checker = False
    s = 0

    
    while barcode != 0:
        mult = 1 if checker else 3
        s += mult * (barcode % 10)
        barcode //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def is_valid(barcode: int) -> bool:
    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10


def get_barcode(barcode: str) -> int:
    if str(barcode).isalpha():
        msg = f"Barcode '{barcode}' has alphabetic characters."
        raise ValueError(msg)
    elif int(barcode) < 0:
        raise ValueError("The entered barcode has a negative value. Try again.")
    else:
        return int(barcode)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    barcode = get_barcode(input("Barcode: ").strip())

    if is_valid(barcode):
        print(f"'{barcode}' is a valid barcode.")
    else:
        print(f"'{barcode}' is NOT a valid barcode.")
