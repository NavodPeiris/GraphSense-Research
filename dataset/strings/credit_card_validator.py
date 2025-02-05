

def validate_initial_digits(credit_card_number: str) -> bool:
    return credit_card_number.startswith(("34", "35", "37", "4", "5", "6"))


def luhn_validation(credit_card_number: str) -> bool:
    cc_number = credit_card_number
    total = 0
    half_len = len(cc_number) - 2
    for i in range(half_len, -1, -2):
        
        digit = int(cc_number[i])
        digit *= 2
        
        
        
        
        if digit > 9:
            digit %= 10
            digit += 1
        cc_number = cc_number[:i] + str(digit) + cc_number[i + 1 :]
        total += digit

    
    for i in range(len(cc_number) - 1, -1, -2):
        total += int(cc_number[i])

    return total % 10 == 0


def validate_credit_card_number(credit_card_number: str) -> bool:
    error_message = f"{credit_card_number} is an invalid credit card number because"
    if not credit_card_number.isdigit():
        print(f"{error_message} it has nonnumerical characters.")
        return False

    if not 13 <= len(credit_card_number) <= 16:
        print(f"{error_message} of its length.")
        return False

    if not validate_initial_digits(credit_card_number):
        print(f"{error_message} of its first two digits.")
        return False

    if not luhn_validation(credit_card_number):
        print(f"{error_message} it fails the Luhn check.")
        return False

    print(f"{credit_card_number} is a valid credit card number.")
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    validate_credit_card_number("4111111111111111")
    validate_credit_card_number("32323")
