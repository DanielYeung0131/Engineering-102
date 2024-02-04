# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: Week 7 Team Programs (Canvas Lab—Your Stony Past (aka Go Game)) 
# Date: 2 October 2023



board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']] 


def display():#Function to display the board
    n = 1
    print('    A   B   C   D   E   F   G   H   I')
    for num in board:
        p=0
        print(n, end = '   ')
        n+=1
        for i in num:
            if(p<len(num)-1):
                print(i, end = '   ')
                p+=1
            else:
                print(i)



def white_turn():#White's Turn
    place = input('White Stone Turn: Enter where you want to put your stone (Ex. "1,A" where 1 is the row and A is the column): ')#Takes the input for row and column
    if place == 'stop':
        return place
    place = place.split(',')
    place[1] = int(ord(place[1]))-65#Converts from letter to number
    place[0] = int(place[0]) - 1#Takes one of number for index
    if place[1] not in range(9) or place[0] not in range(9):#Makes sure the place is not out of bounds
        print("That is not a valid place, try again?")#Friendly message
        white_turn()#runs function again
    elif board[place[0]][place[1]] == chr(9679) or board[place[0]][place[1]] == chr(9675):#Runs if there is a stone already in place
        print("That is not a valid place, try again?")#Friendly message
        white_turn()#runs function again
    elif board[place[0]][place[1]] != chr(9679) and board[place[0]][place[1]] != chr(9675):#Makes sure the board place is empty
        board[place[0]][place[1]] = chr(9679)#Places Stone        



def black_turn():#Black's Turn
    place = input('Black Stone Turn: Enter where you want to put your stone (Ex. "1,A" where 1 is the row and A is the column): ')#Takes the input for row and column
    if place == 'stop':
        return place
    place = place.split(',')
    place[1] = int(ord(place[1]))-65#Converts from letter to number
    place[0] = int(place[0]) - 1#Takes one of number for index
    if place[1] not in range(9) or place[0] not in range(9):#Makes sure the place is not out of bounds
        print("That is not a valid place, try again?")#Friendly message
        black_turn()#runs function again
    elif board[place[0]][place[1]] == chr(9679) or board[place[0]][place[1]] == chr(9675):#Runs if there is a stone already in place
        print("That is not a valid place, try again?")#Friendly message
        black_turn()#runs function again
    elif board[place[0]][place[1]] != chr(9679) and board[place[0]][place[1]] != chr(9675):#Makes sure the board place is empty
        board[place[0]][place[1]] = chr(9675)#Places Stone
        


print("1.The board is empty at the onset of the game (unless players agree to place a handicap).\n2. Black makes the first move, after which White and Black alternate.\n3. A move consists of placing one stone of one's own color on an empty intersection on the board.\n4. A player may pass their turn at any time.\n5. A stone or solidly connected group of stones of one color is captured and removed from the board when all the intersections directly adjacent to it are occupied by the enemy. (Capture of the enemy takes precedence over self-capture.)\n6. No stone may be played so as to recreate a former board position.\n7. Two consecutive passes end the game.\n8. A player's area consists of all the points the player has either occupied or surrounded.\n9. The player with more area wins. ")#Prints Rules
count = 0
print("")
display()
print("")
place = ''
while place != 'stop':
    if count%2 == 0:#Black goes on even turns and first
        place = black_turn()
        count += 1
        print('')
        display()
    else:#White goes on odd turns
        place = white_turn()
        count += 1
        print('')
        display()
    print('')


print('Game finished.')