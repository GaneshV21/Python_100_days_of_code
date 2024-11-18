import requests
print("Welcome to Ganesh's Flight Club.")
print("We find the best flight deals and email you.")
f_name=input("What is your first name?\n").title()
l_name=input("What is your last name?\n").title()
email1=input("What is your email?\n")
email2=input("Type your email again.\n")

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

api_endpoint=api_endpoint
parameter={
    "sheet2":{
        "firstName":f_name,
        "lastName":l_name,
        "email":email1
    }
}
token2=token2
headers={
    "Authorization": token
}

response=requests.post(api_endpoint,json=parameter,headers=headers)
print(response.text)