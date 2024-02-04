# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 11.9.1
# Date: 6 November 2023

# passports

file_name = input('Enter the name of the file: ')

passports = open(file_name).read().split('\n\n')

required_information = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid', 'cid']
valid_passports_list = []

valid_passports = 0

for passport in passports:
    check = 0

    for element in required_information:
        if element in passport:
            check += 1

    if check == len(required_information):
        valid_passports += 1
        valid_passports_list.append(passport)

print(f'There are {valid_passports} valid passports')

with open('valid_passports.txt', 'w') as file:
    for valid_passport in valid_passports_list:
        file.write(valid_passport)
        file.write('\n\n')