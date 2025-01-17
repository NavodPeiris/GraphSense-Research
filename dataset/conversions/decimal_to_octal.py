

import math


def decimal_to_octal(num: int) -> str:
    
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.floor(math.pow(10, counter)))
        counter += 1
        num = math.floor(num / 8)  
        
    return f"0o{int(octal)}"


def main() -> None:
    print("\n2 in octal is:")
    print(decimal_to_octal(2))  
    print("\n8 in octal is:")
    print(decimal_to_octal(8))  
    print("\n65 in octal is:")
    print(decimal_to_octal(65))  
    print("\n216 in octal is:")
    print(decimal_to_octal(216))  
    print("\n512 in octal is:")
    print(decimal_to_octal(512))  
    print("\n")


if __name__ == "__main__":
    main()
