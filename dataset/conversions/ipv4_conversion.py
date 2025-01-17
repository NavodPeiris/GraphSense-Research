

def ipv4_to_decimal(ipv4_address: str) -> int:
    
    octets = [int(octet) for octet in ipv4_address.split(".")]
    if len(octets) != 4:
        raise ValueError("Invalid IPv4 address format")

    decimal_ipv4 = 0
    for octet in octets:
        if not 0 <= octet <= 255:
            raise ValueError(f"Invalid IPv4 octet {octet}")  
        decimal_ipv4 = (decimal_ipv4 << 8) + int(octet)

    return decimal_ipv4


def alt_ipv4_to_decimal(ipv4_address: str) -> int:
    
    return int("0x" + "".join(f"{int(i):02x}" for i in ipv4_address.split(".")), 16)


def decimal_to_ipv4(decimal_ipv4: int) -> str:
    

    if not (0 <= decimal_ipv4 <= 4294967295):
        raise ValueError("Invalid decimal IPv4 address")

    ip_parts = []
    for _ in range(4):
        ip_parts.append(str(decimal_ipv4 & 255))
        decimal_ipv4 >>= 8

    return ".".join(reversed(ip_parts))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
