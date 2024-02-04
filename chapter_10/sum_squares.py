# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 9.16.1
# Date: 10/22/2023

from time import time

def list_nums(n):
    for a in range(0, int(n**0.5) + 1):
        for b in range(a, int(n**0.5) + 1):
            for c in range(b, int(n**0.5) + 1):
                d_squared = n - (a**2 + b**2 + c**2)
                if d_squared >= 0:
                    d = int(d_squared**0.5)
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]
    return []

'''
def count_sets(n):
    a = list_nums(n)
    b = 0
    for i in a:
        if i != 0:
            b += 1
    if i == 1:
        return 4
    return 16
'''


def count_sets(n):
    unique_sets = set()

    for a in range(int(n**0.5) + 1):
        for b in range(a, int(n**0.5) + 1):
            for c in range(b, int(n**0.5) + 1):
                d_squared = n - (a**2 + b**2 + c**2)
                if d_squared >= 0:
                    d = int(d_squared**0.5)
                    if a**2 + b**2 + c**2 + d**2 == n:
                        unique_set = tuple(sorted([a, b, c, d]))
                        unique_sets.add(unique_set)

    return len(unique_sets)



# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(25)) # run function
t2 = time() # get end time
print(count_sets(25))
print(f"This took {t2-t1} seconds") # print result
