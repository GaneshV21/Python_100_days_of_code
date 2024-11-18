from tkinter import *
window=Tk()
window.title("My First GUI Program ")
window.minsize(width=500,height=300)

#Label

# my_label=Label(text="I Am a Label",font=('Arial',24))
# my_label.pack()

# my_label['text']='New Text'
# my_label.config(text="New Text")


#Button:

# def btn_click():
    # my_label.config(text="New Text") # -- when btn clicked the text changes
#     my_label.config(text=input.get()) # -- when btn clicked the text changes to the input box text
#
# my_btn=Button(text="Click Me",command=btn_click) #event for button
# my_btn.pack()

#Entry:

# input = Entry(width=30)
#Already something entered in input box:
# input.insert(END,string="Some text to begin with")
#
# input.pack()
# print(input.get())

#Text

# text=Text(height=5,width=30)
#puts cursor in textbox
# text.focus()
#Add some text to begin with
# text.insert(END,"Example of multi line text entry")
#Gets cuurent value in textbox at line 1,character 0
# print(text.get("1.0",END))
# text.pack()

#spinbox

# def spinbox_used():
#     print(spinbox.get())
#
# spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()


#scale

# def scale_used(value):
#     print(value)
#
# scale=Scale(from_=0,to=100,command=scale_used)
# scale.pack()


#checkbutton
# def check_state():
#     #Pribts 1 if On button checked,otherwise 0
#     print(check_var.get())

#variable to hold on to checked stae ,0 is off, 1 is on.
# check_var=IntVar()
# check=Checkbutton(text="Is On?",command=check_state,variable=check_var)
# check.pack()


#Radio button:
# def radio_used():
#     print(radio_state.get())
# #variable to hold on to which radio button value is checked.
# radio_state=IntVar()
# radio_btn1=Radiobutton(text="Option1",variable=radio_state,value=1,command=radio_used)
# radio_btn2=Radiobutton(text="Option2",variable=radio_state,value=2,command=radio_used)
# radio_btn1.pack()
# radio_btn2.pack()

#listbox:
# def listbox_used(event):
#     #Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox=Listbox(height=4)
# fruits=["Apple",'Pear',"Orange","Banana"]
#
# for item in fruits:
#     listbox.insert(fruits.index(item),item)
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()

#place: and Grid and padding:

#Label
# window.config(padx=100,pady=100)
# my_label1=Label(text="I Am a Label",font=('Arial',20))
# my_label1.pack(side="left")
# my_label1.place(x=0,y=0)
# my_label1.grid(column=0,row=0)


#task in grid:
#Label

# my_label=Label(text="I Am a Label",font=('Arial',24))
# my_label.grid(column=0,row=0)


#Button:
# my_btn=Button(text="Click Me 1")
# my_btn.grid(column=1,row=1)
#
# my_btn1=Button(text="Click Me 2")
# my_btn1.grid(column=2,row=0)
#Entry:

# input = Entry(width=20)
# input.grid(column=3,row=2)



window.mainloop()


