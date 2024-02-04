# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 4.16
# Date: 09/04/2023


#input
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

if num1>num2 and num1>num3:
    print(f"The largest number is {num1:.1f}")
elif num2>num1 and num2>num3:
    print(f"The largest number is {num2:.1f}")
else:
    print(f"The largest number is {num3:.1f}")
