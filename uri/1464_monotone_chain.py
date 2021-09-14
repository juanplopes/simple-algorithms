#!/usr/bin/env python3

def is_left_turn(a, b, c):
    #determines if three points make a left turn
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) > 0;

def monotone_chain(points):
    points.sort()
    hull = []
    
    for point in points:
        while len(hull) >= 2 and is_left_turn(hull[-1], hull[-2], point):
            hull.pop()
        hull.append(point);
    hull.pop();
    
    fixed = len(hull)
    for point in points[::-1]:
        while len(hull) >= fixed + 2 and is_left_turn(hull[-1], hull[-2], point):
            hull.pop()
        hull.append(point)
        
    return hull;

while True:
    N = int(input())
    if N == 0: break

    points = []
    for i in range(N):
        X, Y = map(int, input().split())
        points.append((X, Y))

    layers = 0
    while len(points) > 0:
        hull = monotone_chain(points)
        points = list(set(points) - set(hull))
        layers += 1
    if layers % 2 == 0:
        print('Do not take this onion to the lab!')
    else:
        print('Take this onion to the lab!')

    