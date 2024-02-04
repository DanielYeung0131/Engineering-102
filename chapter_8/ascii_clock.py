# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 8.10
# Date: 18 October 2023


#function for switching between either 12 hours type or 24 hours type.
def clock12_24(time_list):
    a = time_list[:]
    if clock_type == '12':
            if list(time)[1] != ':':
                b = int(list(time)[0] + list(time)[1])
                if b >= 12 and time2[0] != '0':
                    if b > 12:
                        del a[0]
                        del a[0]
                        d = list(str(b-12))
                        d.reverse()
                        for i in d:
                            e = number_to_ascii[i]
                            if preferred_type != '':
                                for number in e:
                                    temp = ''
                                    for character in number:
                                        if character == ' ':
                                            temp += ' '
                                        else:
                                            temp += preferred_type
                                    e[e.index(number)] = temp
                            a.insert(0,e)
                        a.append(number_to_ascii['P'])
                        a.append(number_to_ascii['M'])
                    else:
                        a.append(number_to_ascii['P'])
                        a.append(number_to_ascii['M'])
                else:
                    a.append(number_to_ascii['A'])
                    a.append(number_to_ascii['M'])
            else:
                a.append(number_to_ascii['A'])
                a.append(number_to_ascii['M'])
    return a




time = input('Enter the time: ')
time2 = time
if time[0] == '0':
    time = '12' + time[1:]

clock_type = input('Choose the clock type (12 or 24): ')
preferred_type = input('Enter your preferred character: ')
while preferred_type not in 'abcdeghkmnopqrsuvwxyz@$&*=':
    preferred_type = input("Character not permitted! Try again: ")


print('')

if time[0] == '0':
    time = time[1:]
    print(time)


numbers = '0123456789'
time_list = []
number_to_ascii = {'0': ['000 ','0 0 ','0 0 ','0 0 ','000 '], 
                   '1': [' 1  ','11  ', ' 1  ', ' 1  ', '111 '],
                   '2': ['222 ','  2 ','222 ','2   ','222 '],
                   '3': ['333 ','  3 ','333 ','  3 ','333 '],
                   '4': ['4 4 ','4 4 ','444 ','  4 ','  4 '],
                   '5': ['555 ','5   ', '555 ','  5 ','555 '],
                   '6': ['666 ','6   ','666 ','6 6 ','666 '],
                   '7': ['777 ','  7 ','  7 ','  7 ','  7 '],
                   '8': ['888 ','8 8 ','888 ','8 8 ','888 '],
                   '9': ['999 ','9 9 ','999 ','  9 ','999 '],
                   'A': [' A  ','A A ','AAA ','A A ','A A '],
                   'M': ['M   M','MM MM','M M M','M   M','M   M'],
                   'P': ['PPP ','P P ','PPP ','P   ','P   ']
                   }

for character in time:
    if character in numbers:
        time_list.append(number_to_ascii[character])   

if preferred_type != '':
    for element in time_list:
        for number in element:
            temp = ''

            for character in number:
                if character == ' ':
                    temp += ' '
                else:
                    temp += preferred_type

            time_list[time_list.index(element)][element.index(number)] = temp

if len(time_list) == 3:
    time_list.insert(1, ['  ', ': ','  ',': ','  '])
    time_list = clock12_24(time_list)


elif len(time_list) == 4:
    time_list.insert(2, ['  ', ': ','  ',': ','  '])
    time_list = clock12_24(time_list)

if clock_type == '24':
    for i in range(5):
        time_list[len(time_list)-1][i] = time_list[len(time_list)-1][i][0:3]


for i in range(5):
    for j in range(len(time_list)):
        print(time_list[j][i], end='')
    print()

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
