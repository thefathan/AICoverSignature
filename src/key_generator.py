import random
from typing import Tuple
from util import is_relative_prime

with open('prime_list.txt', 'r') as f:
    primes = list(map(int, f.read().split()))

def get_random_key() -> Tuple[int, int, int]:
    p, q, e = random.choices(primes, k=3)
    totient_n = (p - 1)*(q - 1)

    while not is_relative_prime(totient_n, e):
        p, q, e = random.choices(primes, k=3)

    return p, q, e