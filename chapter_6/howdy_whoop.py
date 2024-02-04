# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 6.13 LAB: Howdy Whoop
# Date: 09/18/2023

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))

#for-loop
for i in range(1,101):
    if i % num1 == 0 and i % num2 == 0:
        print("Howdy Whoop")
    elif i % num1 == 0:
        print("Howdy")
    elif i % num2 == 0:
        print("Whoop")
    else:
        print(i)