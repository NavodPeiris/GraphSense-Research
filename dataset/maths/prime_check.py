
import math
import unittest

import pytest


def is_prime(number: int) -> bool:

    
    if not isinstance(number, int) or not number >= 0:
        raise ValueError("is_prime() only accepts positive integers")

    if 1 < number < 4:
        
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        
        return False

    
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


class Test(unittest.TestCase):
    def test_primes(self):
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        assert is_prime(17)
        assert is_prime(19)
        assert is_prime(23)
        assert is_prime(29)

    def test_not_primes(self):
        with pytest.raises(ValueError):
            is_prime(-19)
        assert not is_prime(0), (
            "Zero doesn't have any positive factors, primes must have exactly two."
        )
        assert not is_prime(1), (
            "One only has 1 positive factor, primes must have exactly two."
        )
        assert not is_prime(2 * 2)
        assert not is_prime(2 * 3)
        assert not is_prime(3 * 3)
        assert not is_prime(3 * 5)
        assert not is_prime(3 * 5 * 7)


if __name__ == "__main__":
    unittest.main()
