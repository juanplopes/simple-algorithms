#!/usr/bin/env python3

def eratosthenes(upper_bound):
    prime = [True] * upper_bound
    for i in range(2, upper_bound):
        if not prime[i]: continue
        yield i
        for j in range(i*i, upper_bound, i):
            prime[j] = False

primes = list(eratosthenes(1000100))
while True:
    try:
        N = int(input())
        factors = set()
        for prime in primes:
            while N % prime == 0:
                factors.add(prime)
                N /= prime
            if N == 1: break
        if N != 1: factors.add(N)

        print(2**len(factors) - len(factors) - 1)
    except EOFError:
        break