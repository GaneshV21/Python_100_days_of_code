logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dict=[]
status=True
while status:
    dic={}
    print("Welcome to the secret auction program")
    name=input("What is your name?\n")
    bid=int(input("What's your bid? $\n"))
    dic["name"]=name
    dic["bid"]=bid
    dict.append(dic)
    others=input("Are there any other bidders? Type 'yes' or 'no'.")
    
    if others=='no':
        status=False
maxi=0
main={}
for i in dict:
    if i['bid']>maxi:
       main=i 
print(f'The winner is {main["name"]} with a bid of ${main["bid"]}')