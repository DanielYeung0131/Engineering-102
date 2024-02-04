# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: Week 6 Individual Programs (Canvas Lab—List Adventure!) 
# Date: 09/25/2023

import random

inventory = []

challenge_reward = {"Dragon": "Golden Sword of Frodo", "Swamp": "Fetid Lance of Ursula", "Troll": "Stone Bulldozer of Skywalker", "Goblin": "Dagger of Adama", "Dark Forest": "Orb of Granger Danger", "Treasure Chest": "100,000 Doubloons"}

choice = '0'

while not(choice == '6'):
    #menu
    print('')
    print('List Adventure - Inventory Manager')
    print('')
    print("1. Attempt a challenge")
    print('2. Display your inventory')
    print('3. Delete an item from your inventory')
    print('4. Swap items in your inventory')
    print('5. Add a new challenge')
    print('6. Exit the game')
    print('')
    choice = input('Enter your choice: ')

    #if-else statement
    if choice == '1':
        challenge = input(f'Challenges available: {challenge_reward.keys()}. Which one do you want to challenge? ')
        if challenge in challenge_reward:
            ran = random.randint(0,1)
            reward = challenge_reward[challenge]
            if ran == 1:
                append_or_insert = input(f'You won! You get {reward}. Do you want to append the reward item to the end of the inventory list, or insert the reward to a specific position in the inventory list? (type "append" or "insert") ')
                if append_or_insert == "append":
                    inventory.append(reward)
                elif append_or_insert == "insert":
                    index = int(input('Which specific position do you want to put your reward in your inventory list? (enter an index number) '))

                    while index > len(inventory):
                        print('try again.')
                        index = int(input('Which specific position do you want to put your reward in your inventory list? (enter an index number) '))

                    inventory.insert(index, reward)

                challenge_reward.pop(challenge)
            elif ran == 0:
                    print('You lost...')
        else:
            print('Please try again.')

    elif choice == '2':
        all_or_part = input('Do you want to display all or just a specific portion of your inventory list? (type "all" or "part of it") ')
        if all_or_part == "all":
            print(f'inventory: {inventory}')
        elif all_or_part == 'part of it':
            p_start = int(input('Choose a starting index: '))
            p_end = int(input('Choose a ending index: '))
            if p_start > p_end or p_end > len(inventory):
                print('invaild index')
            else:
                print(f'inventory: {inventory[p_start:p_end]}')
        
    elif choice == '3':
        delete_item = input('Which item do you want to delete: ')
        if delete_item in inventory:
            inventory.remove(delete_item)
            print(f'{delete_item} has been removed from your inventory')
        else:
            print(f'{delete_item} is not in your inventory')

    elif choice == '4':
        a = input('Enter the first item you want to swap: ')
        b = input('Enter the second item you want to swap: ')

        if a in inventory and b in inventory:
            c = inventory.index(a)
            d = inventory.index(b)
            inventory.remove(a)
            inventory.insert(c,b)
            inventory.remove(b)
            inventory.insert(d,a)
            print('Done swapping.')
        else:
            print("you don't have items.")

    elif choice == '5':
        prompt_c = input('Enter your challenge: ')
        prompt_r = input('Enter your reward: ')

        challenge_reward.update({prompt_c:prompt_r})

    elif choice == '6':
        print('program done.')

    else:
        print('invaild answer.')

