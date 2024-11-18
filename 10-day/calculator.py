# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation={"+":add,"-":subtract,"*":multiply,"/":divide}
def calc():
    print(logo)
    num1=float(input("What's the first number?: "))
    for i in operation:
        print(i)
    
    option=(input("Pick an operation from the line above: "))
    num2=float(input("What's the next number?: "))
    
    answer=operation[option](num1,num2)
    print(f"{num1} {option} {num2} = {answer}")
    
    status=True
    while status:
        choice=(input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new  "))
        if choice=="n":
            status=False
            calc()
        else:
            option=(input("Pick an operation: "))
            num3=float(input("What's the next number?: "))
            exist=answer
            answer=operation[option](answer,num3)
            print(f"{exist} {option} {num3} = {answer}")

calc()