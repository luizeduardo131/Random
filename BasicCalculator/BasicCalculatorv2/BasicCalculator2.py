from tkinter import *

root = Tk()
root.title("SimplestCalculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_adds():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equalsit():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))


Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
Button_addon = Button(root, text="+", padx=39, pady=20, command=button_adds)
Button_equals = Button(root, text="=", padx=91, pady=20, command=lambda: button_equalsit())
Button_clears = Button(root, text="Clear", padx=80, pady=20, command=button_clear)

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
Button_clears.grid(row=4, column=1, columnspan=2)
Button_addon.grid(row=5, column=0)
Button_equals.grid(row=5, column=1, columnspan=2)

root.mainloop()
