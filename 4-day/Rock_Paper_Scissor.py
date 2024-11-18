import random
rocks = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papers = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lis=[rocks,papers,scissors]
choice=int(input("What do you choose 0 for stone 1 for paper 2 for scisorrs\n"))
if choice>=3 or choice<0:
    print("wrong choice")
else:
    print(lis[choice])
    rand_choice=random.randint(0,2)
    print("cpu chosses\n",lis[rand_choice])
    rock=[1,2]
    paper=[2,0]
    scissor=[0,1]
    if choice==0:
        if rand_choice==rock[0]:
            print("cpu win")
        elif rand_choice==rock[1]:
            print("you win")
        else:
            print("draw")
    elif choice==1:
        if rand_choice==paper[0]:
            print("cpu win")
        elif rand_choice==paper[1]:
            print("you win")
        else:
            print("draw")
    elif choice==2:
        if rand_choice==scissor[0]:
            print("cpu win")
        elif rand_choice==scissor[1]:
            print("you win")
        else:
            print("draw")