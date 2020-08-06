from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)


# e.insert(0, "Enter your name:")
def button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + int(second_number))
    elif math == "Subtract":
        e.insert(0, f_num - int(second_number))
    elif math == "Multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "Exponential":
        e.insert(0, f_num ** int(second_number))
    elif math == "Divide":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "Subtract"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "Multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_exponential():
    first_number = e.get()
    global f_num
    global math
    math = "Exponential"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "Divide"
    f_num = int(first_number)
    e.delete(0, END)


# define button
Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_Click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_Click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_Click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_Click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_Click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_Click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_Click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_Click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_Click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_Click(0))
Button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
Button_clear = Button(root, text="clear", padx=35, pady=20, command=button_clear)
Button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
Button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
Button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
Button_exponential = Button(root, text="**", padx=40, pady=20, command=button_exponential)
Button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# put button of the screen
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_divide.grid(row=4, column=1)
Button_multiply.grid(row=4, column=2)

Button_clear.grid(row=5, column=0)
Button_subtract.grid(row=5, column=1)
Button_exponential.grid(row=5, column=2)

Button_equal.grid(row=6, column=0)
Button_add.grid(row=6, column=1)

root.mainloop()
