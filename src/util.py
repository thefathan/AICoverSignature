from typing import Tuple
import os

def is_relative_prime(a: int, b: int) -> bool:
    while b:
        a, b = b, a % b
    
    return a == 1

def is_prime(n: int) -> bool:
    try:
        if (n == 1):
            return False
        i = 2
        while (i*i <= n):
            if (n % i ==0):
                return False
            i += 1
        return True
    except:
        return False

def write_key_file(key: Tuple[int, int], file_name: str) -> None:
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as f:
        f.write(','.join(map(str, key)))

def read_key_file(file_name: str) -> Tuple[int, int]:
    with open(file_name, 'r') as f:
        return tuple(map(int, f.read().split(',')))