

def is_ip_v4_address_valid(ip: str) -> bool:
    octets = ip.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False

        number = int(octet)
        if len(str(number)) != len(octet):
            return False

        if not 0 <= number <= 255:
            return False

    return True


if __name__ == "__main__":
    ip = input().strip()
    valid_or_invalid = "valid" if is_ip_v4_address_valid(ip) else "invalid"
    print(f"{ip} is a {valid_or_invalid} IPv4 address.")
