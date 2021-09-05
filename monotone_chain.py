#!/usr/bin/env python3

import random, heapq

def is_left_turn(a, b, c):
    #determines if three points make a left turn
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) >= 0;

def monotone_chain(points):
    points.sort
    hull = [];
    
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


print(monotone_chain([(108, 113),
    (203, 191),
    (247, 136),
    (282, 126),
    (290, 169),
    (324, 147),
    (369, 164),
    (370, 139),
    (386, 101),
    (432, 215),
    (462, 142)]))