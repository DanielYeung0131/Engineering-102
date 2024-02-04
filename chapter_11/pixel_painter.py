# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 11.12 LAB: Pixel painter
# Date: 11/6/2023

#function
def convert_to_pixel_art(filename, character):
    try:
        with open(filename, 'r') as file:
            output_filename = filename.replace('.csv', '.txt')
            with open(output_filename, 'w') as output_file:
                for line in file:
                    line = line.strip().split(',')
                    line = [int(x) for x in line]
                    for i in range(len(line)):
                        if i % 2 == 0:
                            output_file.write(' ' * line[i])
                        else:
                            output_file.write(character * line[i])
                    output_file.write('\n')

        print(f'{output_filename} created!')
    except FileNotFoundError:
        print('File not found. Please check the filename.')

if __name__ == '__main__':
    filename = input('Enter the filename: ')
    character = input('Enter a character: ')
    convert_to_pixel_art(filename, character)