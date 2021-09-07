#!/usr/bin/env python3

import random

class BloomFilter:
    def __init__(self, size, hashes = 7):
        self.random = random.Random()
        self.data = [False] * size
        self.size = size
        self.hashes = hashes
        
    def add(self, item):
        self.random.seed(hash(item))
        for i in range(self.hashes):
            self.data[self.random.randint(0, self.size - 1)] = True

    def contains(self, item):
        self.random.seed(hash(item))
        for i in range(self.hashes):
            if not self.data[self.random.randint(0, self.size - 1)]:
                return False
        return True

bloom = BloomFilter(10000)

for i in range(1000):
    bloom.add(i)

print(sum(1 for i in range(1000) if bloom.contains(i)))
print(sum(1 for i in range(1000, 2000) if bloom.contains(i)))