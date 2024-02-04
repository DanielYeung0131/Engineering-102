# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 8.10
# Date: 10/18/2023


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