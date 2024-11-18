import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
a=["ramu","somu","kamuu"]

words=random.choice(a)
print(f"Pssst, the solution is {words}")
dash=[]
for i in range(len(words)):
    dash.append("_")
print(dash)
chances=0
while "_" in dash:
    ch=0
    user_choice=input("enter character").lower()
    print(user_choice)
    for i in range(len(dash)):
        if user_choice==words[i]:
            dash[i]=user_choice
        else:
            ch+=1
    if ch==len(dash):
        chances+=1
    str=""
    for i in range(len(dash)):
        str+=dash[i]+" "
    print(str)
    if chances==7:
        print(stages[-(chances)])
        print("You Loss")
        break
    elif chances>0:
        print(stages[-(chances)])


    