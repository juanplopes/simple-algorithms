#!/usr/bin/env python3

import random, math

class HyperLogLog:
    def __init__(self, size):
        self.random = random.Random()
        self.data = [0] * size
        self.alphaMM = (0.7213 / (1 + 1.079 / size)) * size * size
        #alphaMM is a magic approximation defined and explained in the paper
        
    def add(self, value):
        self.random.seed(hash(value))
        index = self.random.randint(0, len(self.data) - 1)
        prefix = 64 - math.floor(math.log(self.random.getrandbits(64), 2))
        self.data[index] = max(self.data[index], prefix)
        
    def cardinality(self):
        estimate = self.alphaMM / sum([2 ** -v for v in self.data])
        size = len(self.data)
        if estimate <= 2.5 * size:
            return round(-size * math.log(float(self.data.count(0)) / size))
        else:
            return round(estimate)

hll = HyperLogLog(10000)

for i in range(234567):
    hll.add(i)

print(hll.cardinality())