#!/usr/bin/env python3

class FenwickTree:
    def __init__(self, size):
        self.data = [0] * size 

    def add(self, index, value):
        while index <= len(self.data):
            self.data[index - 1] += value
            index += index & -index

    def query(self, index):
        value = 0
        while index > 0:
            value += self.data[index - 1]
            index -= index & -index
        return value

tree = FenwickTree(20)

for i in range(1, 21):
    tree.add(i, i)

print(tree.query(10)) #sum(tree[1..11])
print(tree.query(20) - tree.query(10)) # sum(tree[11..2])