# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 4.18
# Date: 09/10/2023

day = int(input("Please enter a positive value for day: "))

gadgets = 0

#if-else
if day < 0:
    print("You entered an invalid number!")
elif day >= 0 and day < 11:
    gadgets = 10
    total = day * gadgets
    print(f'The sum total number of gadgets produced on day {day} is {total}')
elif day >= 11 and day < 51:
    gadgets = 10
    total = 10 * gadgets
    total += sum(range(11, day+1))
    print(f'The sum total number of gadgets produced on day {day} is {total}')
elif day >= 51 and day < 101:
    gadgets = 10
    total = 10 * gadgets
    total += sum(range(11, 51)) #1320
    a = (day - 50)*50
    total += a
    print(f'The sum total number of gadgets produced on day {day} is {total}')
elif day >= 101:
    gadgets = 10
    total = 10 * gadgets
    total += sum(range(11, 51)) #1320
    a = 50 *50
    total += a
    print(f'The sum total number of gadgets produced on day {day} is {total}')