import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
def repeat():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempt=0
    random_number=random.randint(1,100)
    if level == 'easy':
        attempt=10
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        attempt=5
        print(f"You have {attempt} attempts remaining to guess the number.")
    
    def number_guessing_game(user_number):
        if random_number == user_number:
            return "You got it"
        elif random_number>user_number:
            return "Too low."
        else:
            return "Too high."
    
    is_true=True
    a=1
    while is_true and a<=attempt :
        user=int(input("Make a guess: "))
        guess=number_guessing_game(user)
        if guess=="You got it":
            is_true=False
            print(f"You got it the answer is {user}")
        elif a == attempt:
            print("You've run out of guesses, you lose.")
        else:
            print(guess)
            print(f"You have {attempt-a} attempts remaining to guess the number.")
        a+=1
repeat()   

   