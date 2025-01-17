from __future__ import annotations

from math import gcd


def pollard_rho(
    num: int,
    seed: int = 2,
    step: int = 1,
    attempts: int = 3,
) -> int | None:
    
    if num < 2:
        raise ValueError("The input value cannot be less than 2")

    
    
    
    
    if num > 2 and num % 2 == 0:
        return 2

    
    
    
    
    
    
    
    
    
    
    def rand_fn(value: int, step: int, modulus: int) -> int:
        return (pow(value, 2) + step) % modulus

    for _ in range(attempts):
        
        tortoise = seed
        hare = seed

        while True:
            
            tortoise = rand_fn(tortoise, step, num)
            hare = rand_fn(hare, step, num)
            hare = rand_fn(hare, step, num)

            
            
            
            
            
            divisor = gcd(hare - tortoise, num)

            if divisor == 1:
                
                continue
            
            elif divisor == num:
                
                break
            else:
                
                return divisor

        
        
        
        
        
        

        
        
        seed = hare

        
        
        
        step += 1

    
    
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        type=int,
        help="The value to find a divisor of",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=3,
        help="The number of attempts before giving up",
    )
    args = parser.parse_args()

    divisor = pollard_rho(args.num, attempts=args.attempts)
    if divisor is None:
        print(f"{args.num} is probably prime")
    else:
        quotient = args.num // divisor
        print(f"{args.num} = {divisor} * {quotient}")
