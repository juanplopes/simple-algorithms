#!/usr/bin/env python3

def eratosthenes(upper_bound):
    prime = [True] * upper_bound
    for i in range(2, upper_bound):
        if not prime[i]: continue
        yield i
        for j in range(i*i, upper_bound, i):
            prime[j] = False

print(list(eratosthenes(100)))