import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
window=Tk()
data={}
try:
    file=pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    file1=pandas.read_csv('./data/french_words.csv')
    data=file1.to_dict(orient="records")
else:
    data=file.to_dict(orient="records")

current_card={}
# -------------------------------- Functions -------------------------
def next_card():
    global data
    canvas.itemconfig(old_image,image=front_image)
    global current_card,flip_time
    window.after_cancel(flip_time)
    current_card=random.choice(data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=f"{current_card['French']}",fill="black")
    flip_time=window.after(3000,answer_card)


def is_known():
    data.remove(current_card)
    new=pandas.DataFrame(data)
    new.to_csv('./data/words_to_learn.csv',index=False)
    next_card()
def answer_card():
    canvas.itemconfig(old_image, image=back_image)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=f"{current_card['English']}",fill="white")


flip_time=window.after(3000,answer_card)


# ----------------------------------- UI ------------------------------


window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_image=PhotoImage(file='./images/card_front.png')
back_image=PhotoImage(file='./images/card_back.png')

old_image=canvas.create_image(400,263,image=front_image)

card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,'italic'))
card_word=canvas.create_text(400,263,text="Word",font=("Ariel",60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

right=PhotoImage(file="./images/right.png")
right_image=Button(image=right,highlightthickness=0,command=is_known)
right_image.grid(row=1,column=1)
wrong=PhotoImage(file='./images/wrong.png')
wrong_image=Button(image=wrong,highlightthickness=0,command=next_card)
wrong_image.grid(row=1,column=0)

next_card()









window.mainloop()