from collections import Counter
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def has_prime_frequency(nums):
    freq = Counter(nums)
    for count in freq.values():
        if is_prime(count):
            return True
    return False