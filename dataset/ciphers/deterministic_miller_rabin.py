

def miller_rabin(n: int, allow_probable: bool = False) -> bool:
    
    if n == 2:
        return True
    if not n % 2 or n < 2:
        return False
    if n > 5 and n % 10 not in (1, 3, 7, 9):  
        return False
    if n > 3_317_044_064_679_887_385_961_981 and not allow_probable:
        raise ValueError(
            "Warning: upper bound of deterministic test is exceeded. "
            "Pass allow_probable=True to allow probabilistic test. "
            "A return value of True indicates a probable prime."
        )
    
    bounds = [
        2_047,
        1_373_653,
        25_326_001,
        3_215_031_751,
        2_152_302_898_747,
        3_474_749_660_383,
        341_550_071_728_321,
        1,
        3_825_123_056_546_413_051,
        1,
        1,
        318_665_857_834_031_151_167_461,
        3_317_044_064_679_887_385_961_981,
    ]

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for idx, _p in enumerate(bounds, 1):
        if n < _p:
            
            plist = primes[:idx]
            break
    d, s = n - 1, 0
    
    while d % 2 == 0:
        d //= 2
        s += 1
    for prime in plist:
        pr = False
        for r in range(s):
            m = pow(prime, d * 2**r, n)
            
            if (r == 0 and m == 1) or ((m + 1) % n == 0):
                pr = True
                
                break
        if pr:
            continue
        
        return False
    return True


def test_miller_rabin() -> None:
    
    assert not miller_rabin(561)
    assert miller_rabin(563)
    

    assert not miller_rabin(838_201)
    assert miller_rabin(838_207)
    

    assert not miller_rabin(17_316_001)
    assert miller_rabin(17_316_017)
    

    assert not miller_rabin(3_078_386_641)
    assert miller_rabin(3_078_386_653)
    

    assert not miller_rabin(1_713_045_574_801)
    assert miller_rabin(1_713_045_574_819)
    

    assert not miller_rabin(2_779_799_728_307)
    assert miller_rabin(2_779_799_728_327)
    

    assert not miller_rabin(113_850_023_909_441)
    assert miller_rabin(113_850_023_909_527)
    

    assert not miller_rabin(1_275_041_018_848_804_351)
    assert miller_rabin(1_275_041_018_848_804_391)
    

    assert not miller_rabin(79_666_464_458_507_787_791_867)
    assert miller_rabin(79_666_464_458_507_787_791_951)
    
    assert not miller_rabin(552_840_677_446_647_897_660_333)
    assert miller_rabin(552_840_677_446_647_897_660_359)
    


if __name__ == "__main__":
    test_miller_rabin()
