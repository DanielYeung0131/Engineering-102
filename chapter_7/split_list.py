# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 7.27 LAB: Split list
# Date: 10/2/2023

#input

num = input('Enter numbers: ').split(' ')

x = 0
for i in num:
    num[x] = int(num[x])
    x += 1

n1 = 0
n2 = 0

list1 = []
list2 = num[:]
sum = 0

for j in range(len(num)):
    n1 = 0
    n2 = 0
    for number in num[0:j+1]:
        n1 += number
    for number in num[j+1:len(num)]:
        n2 += number
    list1.append(num[j])
    del list2[0]
    if n1 == n2:
        print(f'Left: {list1}')
        print(f'Right: {list2}')
        print(f'Both sum to {n1}')
        break
else:
    print('Cannot split evenly')
    