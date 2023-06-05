from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")
root.iconbitmap("cal.ico")
root.geometry("559x574")
root.resizable(1, 1)
root.configure(bg="#0a0a0a")

# Variable to store the operator and the first number
operator = ""

# Create an Entry widget for the calculator display
e = Entry(root, font=("arial", 24), bg="#0a0a0a", fg="white")
e.place(x=0, y=30, width=553, height=40)


# Function to handle button clicks for numbers
def button1_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Function to clear the calculator display
def button_clear():
    e.delete(0, END)


# Function to handle the addition operation
def button_add():
    first_number = e.get()
    global f_num
    global operator
    operator = "+"
    f_num = int(first_number)
    e.delete(0, END)


# Function to handle the subtraction operation
def button_difference():
    first_number = e.get()
    global f_num
    global operator
    operator = "-"
    f_num = int(first_number)
    e.delete(0, END)


# Function to handle the division operation
def divide():
    first_number = e.get()
    global f_num
    global operator
    operator = "/"
    f_num = int(first_number)
    e.delete(0, END)


# Function to handle the multiplication operation
def button_multiply():
    first_number = e.get()
    global f_num
    global operator
    operator = "*"
    f_num = int(first_number)
    e.delete(0, END)


# Function to handle the percentage operation
def percentage():
    first_number = e.get()
    global f_num
    global operator
    operator = "%"
    f_num = int(first_number)
    e.delete(0, END)


# Function to handle the equal operation
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if operator == "+":
        e.insert(0, f_num + int(second_number))
    elif operator == "-":
        e.insert(0, f_num - int(second_number))
    elif operator == "/":
        e.insert(0, f_num / int(second_number))
    elif operator == "*":
        e.insert(0, f_num * int(second_number))
    elif operator == "%":
        e.insert(0, f_num % int(second_number))


# Create button widgets for various operations




button_clear1=Button(root,font=("arial", 12),text="C",padx=53,pady=20,bd=1,fg="#fff",bg="#a3a09d",command=button_clear)
button_clear1.place(x=10,y=100)
button_divide1=Button(root,font=("arial", 12),text="/",padx=53,pady=20,fg="#fff",bg="#a3a09d",command=divide)
button_divide1.place(x=150,y=100)
button_percentage1=Button(root,font=("arial", 12),text="%",padx=53,pady=20,fg="#fff",bg="#a3a09d",command=percentage)
button_percentage1.place(x=290,y=100)
button_multiply1=Button(root,font=("arial", 13),text="*",padx=53,pady=20,fg="#fff",bg="#FE9037",command=button_multiply)
button_multiply1.place(x=430,y=100)

button7=Button(root,font=("arial", 12),width=5,height=1,text="7",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(7))
button7.place(x=10,y=200)
button8=Button(root,font=("arial", 12),width=5,height=1,text="8",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(8))
button8.place(x=150,y=200)
button9=Button(root,font=("arial", 12),width=5,height=1,text="9",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(9))
button9.place(x=290,y=200)
button_difference1=Button(root,font=("arial", 12),width=5,height=1,text="-",padx=40,pady=20,fg="#fff",bg="#FE9037",command=button_difference)
button_difference1.place(x=430,y=200)

button4=Button(root,font=("arial", 12),width=5,height=1,text="4",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(4))
button4.place(x=10,y=300)
button5=Button(root,font=("arial", 12),width=5,height=1,text="5",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(5))
button5.place(x=150,y=300)
button6=Button(root,font=("arial", 12),width=5,height=1,text="6",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(6))
button6.place(x=290,y=300)
button_add1=Button(root,font=("arial", 12),width=5,height=1,text="+",padx=39,pady=20,fg="#fff",bg="#FE9037",command=button_add)
button_add1.place(x=430,y=300)

button1=Button(root,font=("arial", 12),width=5,height=1,text="1",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(1))
button1.place(x=10,y=400)
button2=Button(root,font=("arial", 12),width=5,height=1,text="2",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(2))
button2.place(x=150,y=400)
button3=Button(root,font=("arial", 12),width=5,height=1,text="3",padx=40,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(3))
button3.place(x=290,y=400)
button0=Button(root,font=("arial", 12),width=11,height=1,text="0",padx=80,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click(0))
button0.place(x=10,y=500)

buttonpoint=Button(root,font=("arial", 12),text=".",padx=58,pady=20,fg="#fff",bg="#45403c",command=lambda:button1_click("."))
buttonpoint.place(x=290,y=500)
button_equal1=Button(root,font=("arial", 12),text="=",padx=53,pady=70,fg="#fff",bg="#FE9037",command=button_equal)
button_equal1.place(x=430,y=400)



root.mainloop()
