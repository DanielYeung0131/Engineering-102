# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 6.16 LAB: Balancing numbers
# Date: 09/18/2023

num = int(input("Enter a value for n: "))

num1 = 0
for i in range(num):
    num1 += i

num2 = num +1
count = 1

i = 2
#while loop
while num1 != num2 and num2 < 10000000000000:
    num2 = num2 + num + i
    i += 1
    count += 1

if num1 == num2:
    print(f'{num} is a balancing number with r={count}')
else:
    print(f'{num} is not a balancing number')