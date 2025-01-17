

def greatest_common_divisor(a: int, b: int) -> int:
    return abs(b) if a == 0 else greatest_common_divisor(b % a, a)


def gcd_by_iterative(x: int, y: int) -> int:
    while y:  
        x, y = y, x % y
    return abs(x)


def main():
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(
            f"greatest_common_divisor({num_1}, {num_2}) = "
            f"{greatest_common_divisor(num_1, num_2)}"
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")


if __name__ == "__main__":
    main()
