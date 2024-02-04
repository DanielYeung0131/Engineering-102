# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 10.15 LAB: Guessing game
# Date: 10/30/2023


def check(guess):
    while True:
        try:
            guess = int(guess)
            break
        except:
            guess = input('Bad input! Try again: ')
            guess = check(guess)
    return guess

#match
def match():
    guess = input('What is your guess? ')
    guess = check(guess)
    count = 1
    while guess != 27:
        while True:
            try:
                if guess > 27:
                    print('Too high!')
                    count += 1
                else:
                    print("Too low!")
                    count += 1
                break
            except:
                guess = input('Bad input! Try again: ')
                guess = check(guess)
            
        guess = input('What is your guess? ')
        guess = check(guess)

    return count





#main
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
count = match()
print(f'You guessed it! It took you {count} guesses.')
