# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 7.26 LAB: Leet speak
# Date: 10/2/2023

#input
words = input("Enter some text: ").split()
list1 ={}
list = []
word=''

for a in words:
    word += a

list1['a'] = 4
list1['e'] = 3
list1['o'] = 0
list1['s'] = 5
list1['t'] = 7



print(f'In leet speak, "{word}" is:')

for i in words:
    list = []
    for j in i:
        if j == 'a':
            list.append(list1[j])
        elif j == 'e':
            list.append(list1[j])
        elif j == 'o':
            list.append(list1[j])
        elif j == 's':
            list.append(list1[j])
        elif j == 't':
            list.append(list1[j])
        else:
            list.append(j)
    for a in list:
        print(a, end='')
    print(" ", end='')