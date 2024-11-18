from tkinter import *
window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

#label1
label1=Label(text="is equal to",font=('Arial',10))
label1.grid(column=0,row=1)

#label2
label2=Label(text="Miles",font=('Arial',10))
label2.grid(column=2,row=0)

#label3
label3=Label(text="Km",font=('Arial',10))
label3.grid(column=2,row=1)

#label4
label4=Label(text="0",font=('Arial',10))
label4.grid(column=1,row=1)

#Entry
entry=Entry(width=7)
entry.grid(column=1,row=0)

#Button
def btn_click():
    label4.config(text=round(float(entry.get())*1.609))

btn=Button(text="Calculate",command=btn_click)
btn.grid(column=1,row=2)



window.mainloop()
