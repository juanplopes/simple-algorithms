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


def note(note):
    index = (ord(note[0]) - ord('A')) * 2
    if index > 8: index -= 2
    elif index > 2: index -= 1
    if '#' in note[1:]: index += 1
    elif 'b' in note[1:]: index -= 1
    return index % 12

while True:
    M, T = map(int, input().split())
    if M == 0 and T == 0: break

    haystack = list(map(note, input().split()))
    haystack = [(b-a)%12 for a, b in zip(haystack, haystack[1:])]

    needle = list(map(note, input().split()))
    needle = [(b-a)%12 for a, b in zip(needle, needle[1:])]

    kmp = KMP(needle)

    print('S' if kmp.find_at(haystack) is not None else 'N')