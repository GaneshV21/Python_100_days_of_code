letter=int(input("How many letters would you like in your password\n"))
symbol=int(input("How many symbols would you like?\n"))
numbers=int(input("How many numbers would you like?\n"))
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
special=['!','#','$','%','&','(',')','*','+']
import random
str1=[]
for i in range (0,letter):
    str1.append(random.choice(alpha))
for i in range (0,symbol):
    str1.append(random.choice(special))
for i in range (0,numbers):
    str1.append(random.choice(num))
random.shuffle(str1)
str2=""
for i in str1:
    str2+=i
print(f"Your password is: {str2}")

