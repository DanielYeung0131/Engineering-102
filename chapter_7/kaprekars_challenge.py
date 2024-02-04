# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 7.29
# Date: 27 September 2023

y=1
totalcount = 0
while(y<=9999):
    int1 = y
    listnums = []
    count = 0
    while(int1!=6174):  
        if int1 == 0:
            break
        elif int1>=1000: 
            listnums.append(str(int1))
        elif int1>=100:
            listnums.append('0'+str(int1))
        elif int1>=10:
            listnums.append('00'+str(int1))
        else:
            listnums.append('000'+str(int1))
        split = []
        for char in listnums[count]:
            split.append(int(char))
        split.sort()
        forward = split[:]
        split.reverse()
        backward = split[:]
        num1 = forward[0]*1000+forward[1]*100+forward[2]*10+forward[3]
        num2 = backward[0]*1000+backward[1]*100+backward[2]*10+backward[3]
        int1 = num2-num1
        count+=1
    listnums2 = listnums[:]
    if(int1==6174):
        x = 0
        while(x<len(listnums)):
            listnums2[x] = int(listnums[x])
            #print(listnums2[x], end = " > ")
            x+=1
        #print(6174)
    
    totalcount+=len(listnums)
    y+=1
    #lol
print(f"Kaprekar's routine takes {totalcount} total iterations for all four-digit numbers")