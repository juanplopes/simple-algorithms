#!/usr/bin/env python3

import collections, functools

def euclid(a, b):
    if b == 0: return (a, 1, 0)
    q = a // b
    gcd, x, y = euclid(b, a - q * b)
    return gcd, y, x - q * y

def product(items):
    answer = 1
    for item in items:
        answer = (answer * item) % 1000000007
    return answer

while True:
    try:
        word = input()

        numerator = product(range(1, len(word)+1))
        denominator = product(product(range(1, x + 1)) 
                    for x in collections.Counter(word).values())
        gcd, denominator_inverse, _ = euclid(denominator, 1000000007)

        print(numerator * denominator_inverse % 1000000007)
    except EOFError:
        break
