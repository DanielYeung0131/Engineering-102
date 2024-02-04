# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 7.25 LAB: Pig latin
# Date: 10/2/2023

#input
word = input('Enter word(s) to convert to Pig Latin: ').split()
latin = ''
list = []
count = 0
words=''

for b in word:
    words += b

print(f'In Pig Latin, "{words}" is:', end=' ')
for i in word:
    if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'y':
        count = 0
        list = []
        while count < len(i):
            list.append(i[count])
            count+=1            
        list.append('yay')
        for a in list:
            print(a, end='')
    elif ((i[0] == 't' or i[0] == 'w') and i[1] == 'h') or (i[1] == 'r') or (i[0] == 'b' and i[1] == 'l'):
        count = 0
        list = []
        while count < len(i)-2:
            list.append(i[count+2])
            count+=1            
        list.append(i[0])
        list.append(i[1])
        list.append('ay')
        for a in list:
            print(a, end='')
    else:
        count = 0
        list = []
        while count < len(i)-1:
            list.append(i[count+1])
            count+=1            
        list.append(i[0])
        list.append('ay')
        for a in list:
            print(a, end='')
    print(" ", end ='')