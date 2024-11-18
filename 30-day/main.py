#FileNotFound
# try:
#     file=open("data.txt")
#     dic={"key":"value"}
#     print(dic['keey'])
# except FileNotFoundError: #-- specify error in except
#    file=open('data.txt','w')
#    file.write("something")
# except KeyError as error: #-- specify what error in except
#     print(f"{error} is not there key error")
# else: #-- try succeed else run
#     content=file.read()
#     print(content)
# finally: # -- always run
#     file.close()
#     print("File was closed")


# raise :
# height=float(input("Height : "))
# weight=int(input("Weight : "))
#
# if height>3:
#     raise ValueError("Human weight should not be over 3 meters")
# bmi=weight/height **2
# print(bmi)



# ---- Nato_Phonetic Project -----

# import pandas
#
# data=pandas.read_csv("./nato_phonetic_alphabet.csv")
# data_dict={row['letter']:row['code'] for (index,row) in data.iterrows() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# def generate_pheonic():
#     try:
#         user_choice=input("Enter a word: ")
#         new_list=[data_dict[letter.upper()] for letter in user_choice]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_pheonic()
#     else:
#         print(new_list)
# generate_pheonic()

# --- Password Manager ----



from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    letter= random.randint(8,10)
    symbol= random.randint(2,4)
    numbers= random.randint(2,4)
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num=['0','1','2','3','4','5','6','7','8','9']
    special=['!','#','$','%','&','(',')','*','+']
    import random
    str1=[random.choice(alpha) for _ in range(letter)]
    str2=[random.choice(num) for _ in range(numbers)]
    str3=[random.choice(special) for _ in range(symbol)]
    str1.extend(str2)
    str1.extend(str3)
    random.shuffle(str1)
    str2="".join(str1)
    passw.delete(0, END)
    passw.insert(0,str2)
    pyperclip.copy(str2)




# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website=web.get()
    emails= email.get()
    password=passw.get()
    new_data={
        website:{
            "email":emails,
            "password":password
        }
    }
    if len(website) <1 or len(password)<1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        # with open('data1.json', mode="r") as data:
            #write json data:
            # json.dump(new_data,data,indent=4) # indent--- for json indented

            #Read json data:
            # data_file=json.load(data)
            # print(data_file)

            #update json data:
        #     data_file1=json.load(data)
        #     data_file1.update(new_data)
        # with open('data1.json','w') as data:
            #saving updated data
            # json.dump(data_file1,data,indent=4)
            # web.delete(0,END)
            # passw.delete(0,END)


        #using exception handling
        try:
            with open('data.json','r') as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            #updating old data with newdata
            data.update(new_data)
            with open('data.json','w') as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            web.delete(0,END)
            passw.delete(0,END)

#----------------------------- FIND PASSWORD -------------------------- #
def find_password():
    key_value = web.get()
    try:
        with open('data.json') as data_file3:
            dataf=json.load(data_file3)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if dataf[key_value]:
            messagebox.showinfo(message=f"email:{dataf[key_value]['email']}\nPassword:{dataf[key_value]['password']}")
        else:
            messagebox.showinfo(message=f"No details for the {key_value} exists")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.config(padx=50,pady=50)
window.title("Password Manager")

canvas=Canvas(width=200,height=200)
image=PhotoImage(file='./logo.png')
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

#labels:
website=Label(text="Website:")
website.grid(row=1,column=0)

email_username=Label(text="Email/Username:")
email_username.grid(row=2,column=0)

password=Label(text="Password:")
password.grid(row=3,column=0)

#entry:
web=Entry(width=21)
web.grid(row=1,column=1)
web.focus()

email=Entry(width=35)
email.grid(row=2,column=1,columnspan=2)
email.insert(0,string="123@gmail.com")

passw=Entry(width=21)
passw.grid(row=3,column=1)

#button:
gen_password=Button(text="Generate Password",command=password_generator)
gen_password.grid(row=3,column=2)

add=Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

search=Button(text="Search",width=15,command=find_password)
search.grid(row=1,column=2)


window.mainloop()