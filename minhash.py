#!/usr/bin/env python3

import random, heapq

def minhash(k, elements):
    return heapq.nsmallest(k, map(hash, elements))

def minhash_compare(k, hash1, hash2):
    union = heapq.nsmallest(k, set(hash1).union(hash2))
    intersection = set(union).intersection(hash1).intersection(hash2)
    return len(intersection)/float(k)

A = [str(random.randint(0, 20000)) for _ in range(10000)]
B = [str(random.randint(0, 20000)) for _ in range(10000)]

hash1 = minhash(512, A)
hash2 = minhash(512, B)
print(minhash_compare(512, hash1, hash2))
print('Real:', len(set(A).intersection(B))/float(len(set(A).union(B))))