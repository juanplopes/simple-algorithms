#!/usr/bin/env python3

import random

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (2 * size)

    def set(self, index, value):
        index += self.size  # leaves are on the second half of the array
        self.data[index] = value
        while index > 1:
            self.data[index // 2] = min(self.data[index], self.data[index ^ 1])
            index //= 2

    def query(self, left, right):
        value = float('+inf')
        left += self.size
        right += self.size
        while left < right:
            if left % 2: 
                value = min(value, self.data[left])
                left += 1
            if right % 2: 
                right -= 1
                value = min(value, self.data[right])
            left //= 2
            right //= 2
        return value

tree = SegmentTree(1000)
control = [0] * 1000
for i in range(1000):
    control[i] = random.randint(0, 100000)
    tree.set(i, control[i])

print(tree.query(200, 500))
print(f'Real: {min(control[200:500])}')

print(tree.query(301, 500))
print(f'Real: {min(control[301:500])}')