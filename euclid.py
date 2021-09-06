#!/usr/bin/env python3

def euclid(a, b):
    if b == 0: return (a, 1, 0)
    q = a // b
    gcd, x, y = euclid(b, a - q * b)
    return gcd, y, x - q * y

gcd, x, y = euclid(20, 6)
print(f'20*{x} + 6*{y} = {gcd}')
