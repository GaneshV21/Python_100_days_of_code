import turtle
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
reset=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global reset,reps
    window.after_cancel(reset)
    reps=0
    canvas.itemconfig(timer,text="00:00")
    label.config(text="Timer",fg=GREEN)
    label_tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    if reps == 7:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="BREAK", fg=RED)
        reset_time()
    elif reps%2==0:
        count_down(WORK_MIN*60)
        label.config(text="WORK",fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="BREAK", fg=PINK)

    reps+=1




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reset
    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if(count>0):
       reset = window.after(1000,count_down,count-1)
    else:
        if reps!=7:
            start_time()
            if reps % 2 == 0:
                val=int((reps/2))*"✅"
                label_tick.config(text=f"{val}")








# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='./tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

label=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

label_tick=Label(fg=GREEN,bg=YELLOW)
label_tick.grid(column=1,row=3)

btn_start=Button(text="Start",highlightthickness=0,command=start_time)
btn_start.grid(column=0,row=2,)

btn_reset=Button(text="Reset",highlightthickness=0,command=reset_time)
btn_reset.grid(column=2,row=2)


window.mainloop()


