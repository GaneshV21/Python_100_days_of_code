print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if input1 == 'left':
    input2 = input('You\'ve come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if input2 == 'wait':
        input3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?').lower()
        if input3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif input3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif input3 == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")