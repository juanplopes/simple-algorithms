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
            self.data[index // 2] = self.data[index] | self.data[index ^ 1]
            index //= 2

    def query(self, left, right):
        value = 0
        left += self.size
        right += self.size
        while left < right:
            if left % 2: 
                value |= self.data[left]
                left += 1
            if right % 2: 
                right -= 1
                value |= self.data[right]
            left //= 2
            right //= 2
        return value

while True:
    try:
        N, Q, M = map(int, input().split())
        T = SegmentTree(N+1)
        for i, monster_type in enumerate(map(int, input().split())):
            T.set(i+1, 1 << monster_type)

        for i in range(Q):
            cmd, a, b = map(int, input().split())
            if cmd == 1:
                print(bin(T.query(a, b+1)).count('1'))
            elif cmd == 2:
                T.set(a, 1 << b)
    except EOFError:
        break