# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 4.13 LAB: Make change
# Date: 09/06/2023

from math import *
#how much they paid
paid = float(input("How much did you pay? "))

#how much they cost
cost = float(input("How much did it cost? "))

change = paid - cost

print(f"You received ${change:.2f} in change. That is...")

quarter = int(change // 0.25)
change -= quarter *0.25

if quarter>1 :
    print(quarter, "quarters")
elif quarter == 1:
    print(quarter, "quarter")

dime = int(change // 0.1)
change -= dime*0.1
if dime>1 :
    print(dime, "dimes")
elif dime == 1:
    print(dime, "dime")


nickel = int(change // 0.05)
change -= nickel*0.05
if nickel>1 :
    print(nickel, "nickels")
elif nickel == 1:
    print(nickel, "nickel")
    
penny = int(round(change / 0.01))
if penny>1:
    print(penny, "pennies")
elif penny == 1:
    print(penny, "penny")