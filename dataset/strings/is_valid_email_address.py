
import string

email_tests: tuple[tuple[str, bool], ...] = (
    ("simple@example.com", True),
    ("very.common@example.com", True),
    ("disposable.style.email.with+symbol@example.com", True),
    ("other-email-with-hyphen@and.subdomains.example.com", True),
    ("fully-qualified-domain@example.com", True),
    ("user.name+tag+sorting@example.com", True),
    ("x@example.com", True),
    ("example-indeed@strange-example.com", True),
    ("test/test@test.com", True),
    (
        "123456789012345678901234567890123456789012345678901234567890123@example.com",
        True,
    ),
    ("admin@mailserver1", True),
    ("example@s.example", True),
    ("Abc.example.com", False),
    ("A@b@c@example.com", False),
    ("abc@example..com", False),
    ("a(c)d,e:f;g<h>i[j\\k]l@example.com", False),
    (
        "12345678901234567890123456789012345678901234567890123456789012345@example.com",
        False,
    ),
    ("i.like.underscores@but_its_not_allowed_in_this_part", False),
    ("", False),
)



MAX_LOCAL_PART_OCTETS = 64
MAX_DOMAIN_OCTETS = 255


def is_valid_email_address(email: str) -> bool:

    
    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")
    
    if len(local_part) > MAX_LOCAL_PART_OCTETS or len(domain) > MAX_DOMAIN_OCTETS:
        return False

    
    if any(
        char not in string.ascii_letters + string.digits + ".(!#$%&'*+-/=?^_`{|}~)"
        for char in local_part
    ):
        return False

    
    if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
        return False

    
    if any(char not in string.ascii_letters + string.digits + ".-" for char in domain):
        return False

    
    if domain.startswith("-") or domain.endswith("."):
        return False

    
    return not (domain.startswith(".") or domain.endswith(".") or ".." in domain)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for email, valid in email_tests:
        is_valid = is_valid_email_address(email)
        assert is_valid == valid, f"{email} is {is_valid}"
        print(f"Email address {email} is {'not ' if not is_valid else ''}valid")
