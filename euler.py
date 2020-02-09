import math

def is_prime(n):
    # If divisible by two, no prime
    if n % 2 == 0 and n > 2:
        return False
    
    # Only check odd numbers, no need to check longer than sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True