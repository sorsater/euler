import math
import time
import sys
from IPython.display import clear_output

def is_prime(n):
    # If divisible by two, no prime
    if ((n % 2 == 0 and n > 2) or n < 2):
        return False
    
    # Only check odd numbers, no need to check longer than sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def proper_divisor(n):
    divisors = set() 
    divisors.add(1) # Always include 1 and start at 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def sum_of_divisors(n):
    return sum(proper_divisor(n))

def prime_factors(n):
    res = []  
    # All modulo 2s added
    while n % 2 == 0: 
        res.append(2)
        n = n / 2
        
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0: 
            res.append(i) 
            n = n / i 

    # Remainder is also prime
    if n > 2:
        res.append(int(n))
    return res

class Progress():
    """
    Inspired by this blogpost:
    https://www.mikulskibartosz.name/how-to-display-a-progress-bar-in-jupyter-notebook/

    Modified to include execution time and convert to class.
    """

    def __init__(self, include_time=True, show_bar=True):
        self.start = time.time()
        self.bar_length = 30
        self.include_time = include_time
        self.show_bar = show_bar

    def tick(self, progress=1, msg=None):
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
        if progress < 0:
            progress = 0
        if progress >= 1:
            progress = 1

        block = int(round(self.bar_length * progress))
        non_block = self.bar_length - block

        clear_output(wait = True)
        text = ''
        
        if self.show_bar:
            text += 'Progress: [{0}] {1:.2f}%'.format( '#' * block + '-' * non_block, progress * 100)

        if self.include_time:
            text += ' {:.1f} seconds'.format(time.time() - self.start)
        if msg:
            text += ' {}'.format(msg)
        print(text)