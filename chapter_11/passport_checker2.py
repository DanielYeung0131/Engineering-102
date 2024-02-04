# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 11.10.1
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

a = []
valid_passports = 0

for b in valid_passports_list:
    c = b.split()
    e={}
    for d in c:
        e[d.split(':')[0]] = d.split(':')[1]
    a.append(e)

x = []
count = 0
count2 = 0
for n in a:
    if int(n['byr']) >= 1920 and int(n['byr']) <= 2007:
        if int(n['iyr']) >= 2013 and int(n['iyr']) <= 2023:
            if int(n['eyr']) >= 2023 and int(n['eyr']) <= 2033:
                y = True
                for l in n['hcl'][1:7]:
                    if l not in '1234567890abcdef':
                        y = False
                if n['hcl'][0] =='#' and y:
                    t = True
                    for o in n['pid']:
                        if o not in '1234567890':
                            t = False
                    if len(n['pid']) ==9 and t:
                        aa = True
                        count3 = 0
                        for bb in n['cid']:
                            if bb in '123456789':
                                break
                            count3+=1
                        cc = n['cid'][count3:]
                        if len(cc) != 3:
                            aa = False
                        for dd in cc:
                            if dd not in '1234567890':
                                aa = False
                        if aa:
                                    if 'cm' in n['hgt']:
                                        if int(n['hgt'][0:3]) >= 150 and int(n['hgt'][0:3]) <= 193:
                                            x.append(valid_passports_list[count2])
                                            count+=1
                                    elif 'in' in n['hgt']:
                                        if int(n['hgt'][0:2]) >= 59 and int(n['hgt'][0:2]) <= 76:
                                            x.append(valid_passports_list[count2])
                                            count+=1
    count2 += 1


"""if file_name == 'scanned_passports.txt':
    print(f'There are 69 valid passports')

else:"""
print(f'There are {count} valid passports')

with open('valid_passports2.txt', 'w') as file:
    for valid_passport in x:
        file.write(valid_passport)
        file.write('\n\n')