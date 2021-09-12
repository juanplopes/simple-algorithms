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

T = int(input())
for test in range(T):
    N, C = map(int, input().split(' '))
    T1 = FenwickTree(N)
    T2 = FenwickTree(N)

    for i in range(C):
        command = list(map(int, input().split(' ')))
        if command[0] == 0:
            A, B, V = command[1:]
            T1.add(A, V)     
            T1.add(B+1, -V)    

            T2.add(A, (A-1)*V)  
            T2.add(B+1, -B*V) 
        elif command[0] == 1:
            A, B = command[1:]
            print((T1.query(B)*B - T2.query(B)) - (T1.query(A-1)*(A-1) - T2.query(A-1)))                     
        