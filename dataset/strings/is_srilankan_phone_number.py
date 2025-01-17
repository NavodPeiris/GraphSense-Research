import re


def is_sri_lankan_phone_number(phone: str) -> bool:

    pattern = re.compile(r"^(?:0|94|\+94|0{2}94)7(0|1|2|4|5|6|7|8)(-| |)\d{7}$")

    return bool(re.search(pattern, phone))


if __name__ == "__main__":
    phone = "0094702343221"

    print(is_sri_lankan_phone_number(phone))
