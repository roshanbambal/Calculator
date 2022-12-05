from tkinter import *
#logic for addition

def addnumber():
    addition = int(text_box1.get()) + int(text_box2.get())
    myText.set(addition)

def subnumber():
    subst = int(text_box1.get()) - int(text_box2.get())
    myText.set(subst)

def mulnumber():
    mul = int(text_box1.get()) * int(text_box2.get())
    myText.set(mul)

def divnumber():
    div = int(text_box1.get()) / int(text_box2.get())
    myText.set(div)

def floordivnumber():
    floordiv = int(text_box1.get()) // int(text_box2.get())
    myText.set(floordiv)

def exponumber():
    expo = int(text_box1.get()) ** int(text_box2.get())
    myText.set(expo)


root=Tk()
root.title("GUI Addition")
root.geometry("500x300")
myText = StringVar()


#Create Label

label_First_number = Label(root, text='Enter Fname :')
label_First_number.grid(row=0, column=0)

label_Second_number = Label(root, text='Enter Lname :')
label_Second_number.grid(row=1, column=0)

label_result=Label(root, text='Result')
label_result.grid(row=2, column=0)

#textbox

text_box1=Entry(root)
text_box1.grid(row=0, column=2)


text_box2=Entry(root)
text_box2.grid(row=1, column=2)

Label(root, text='', textvariable=myText).grid(row=2, column=1)

#submit

add_result = Button(root, text='Addition', command=addnumber)
add_result.grid(row=4, column=0)

add_result = Button(root, text='Subst', command=subnumber)
add_result.grid(row=4, column=1)

add_result = Button(root, text='Multiply', command=mulnumber)
add_result.grid(row=4, column=2)

add_result = Button(root, text='Division', command=divnumber)
add_result.grid(row=5, column=0)

add_result = Button(root, text='FloorDivision', command=floordivnumber)
add_result.grid(row=5, column=1)

add_result = Button(root, text='Expo', command=exponumber)
add_result.grid(row=5, column=2)

mainloop()
