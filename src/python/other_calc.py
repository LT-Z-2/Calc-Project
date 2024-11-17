from tkinter import *
from math import sqrt, pow

root = Tk()
root.title("Advanced Calculator")

e = Entry(root, width=50, borderwidth=5, fg="teal")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functionality
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

def button_clear():
    e.delete(0, END)

def button_operation(op):
    global first_num
    global operation
    first_num = float(e.get())
    operation = op
    e.delete(0, END)

def button_equal():
    second_num = float(e.get())
    e.delete(0, END)

    if operation == "+":
        e.insert(0, first_num + second_num)
    elif operation == "-":
        e.insert(0, first_num - second_num)
    elif operation == "*":
        e.insert(0, first_num * second_num)
    elif operation == "/":
        if second_num != 0:
            e.insert(0, first_num / second_num)
        else:
            e.insert(0, "Error (Divide by 0)")
    elif operation == "^":
        e.insert(0, pow(first_num, second_num))
    elif operation == "sqrt":
        e.insert(0, sqrt(first_num))

def button_sqrt():
    global first_num
    global operation
    first_num = float(e.get())
    operation = "sqrt"
    button_equal()

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operation("+"))
button_sub = Button(root, text="-", padx=39, pady=20, command=lambda: button_operation("-"))
button_mult = Button(root, text="*", padx=39, pady=20, command=lambda: button_operation("*"))
button_div = Button(root, text="/", padx=39, pady=20, command=lambda: button_operation("/"))
button_pow = Button(root, text="^", padx=39, pady=20, command=lambda: button_operation("^"))
button_sqrt = Button(root, text="√", padx=39, pady=20, command=button_sqrt)

button_clear = Button(root, text="CLEAR", padx=79, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)

# Place buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_pow.grid(row=4, column=1)
button_sqrt.grid(row=4, column=2)

button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)

root.mainloop()