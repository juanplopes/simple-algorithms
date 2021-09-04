#!/usr/bin/env python3

import functools

def knapsack(target_price, items):
    @functools.lru_cache(maxsize = None)
    def inner(price, index):
        if price == 0: return [()] #single valid solution with no items
        if index < 0 or price < 0: return []  #no valid solution
        return inner(price, index - 1) + [
            other + (items[index],) 
            for other in inner(price - items[index][1], index - 1)
        ]

    return inner(target_price, len(items) - 1)


solutions = knapsack(4394, [
    ('Yo yo', 122),
    ('Doll', 275),
    ('Duckie', 185),
    ('Tractor', 597),
    ('Airplane', 647),
    ('Ball', 216),
    ('Racecar', 713),
    ('Dog', 457),
    ('Jump Rope', 146),
    ('Car', 518),
    ('Elephant', 316),
    ('Bear', 489),
    ('Xylophone', 711),
    ('Tank', 645),
    ('Checkers', 477),
    ('Boat', 804),
    ('Train', 671),
    ('Jacks', 231),
    ('Truck', 621),
    ('Whistle', 98),
    ('Pinwheel', 87),
])

for solution in solutions:
    print(sum(price for _, price in solution), solution)
    
print(len(solutions))