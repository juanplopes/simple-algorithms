#!/usr/bin/env python3

class KMP:
    def __init__(self, needle):
        self.needle = needle
        self.F = [0] * (len(needle) + 1)
        i, j = 1, 0
        while i < len(needle):
            if needle[i] == needle[j]:
                i += 1
                j += 1
                self.F[i] = j
            elif j == 0:
                i += 1
                self.F[i] = 0
            else:
                j = self.F[j]

    def find_at(self, haystack, start_index = 0):
        i, j = start_index, 0
        n, m = len(haystack), len(self.needle)
    
        while i - j <= n - m:
            while j < m:
                if self.needle[j] != haystack[i]: break
                i += 1
                j += 1
            if j == m: return i - m
            if j == 0: i += 1
            j = self.F[j]

kmp = KMP('abababc')

print(kmp.find_at('ababababababababc'))