from tkinter import *
from tkinter import messagebox
import pyperclip

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
    print(len(website),len(password))
    if len(website) <1 or len(password)<1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        msg = messagebox.askokcancel(title="Website", message=f"These are the detailed entered: \nEmail:{emails} "
                                                     f"\nPassword:{password} \n Is is ok to save")
        if msg:
            with open('./data.txt',mode="a") as data:
                data.write(f"{website} | {emails} | {password}\n")
            web.delete(0,END)
            passw.delete(0,END)

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
web=Entry(width=35)
web.grid(row=1,column=1,columnspan=2)
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


window.mainloop()