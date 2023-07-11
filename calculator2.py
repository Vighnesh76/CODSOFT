from tkinter import *


root = Tk()
root.title("Calculator")
root.attributes('-fullscreen', True)


root.configure(bg='#212121')


entry = Entry(root, font=('Arial', 40), bd=0, relief=FLAT, bg='#212121', fg='white', justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))


def button_clear():
    entry.delete(0, END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for button in button_list:
    text, row, column = button
    btn = Button(root, text=text, font=('Arial', 30, 'bold'), bd=0, relief=RAISED, bg='#ff6f00', fg='white',
                 command=lambda text=text: button_click(text))
    btn.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')


clear_btn = Button(root, text='C', font=('Arial', 30, 'bold'), bd=0, relief=RAISED, bg='#d50000', fg='white',
                   command=button_clear)
clear_btn.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')


equal_btn = Button(root, text='=', font=('Arial', 30, 'bold'), bd=0, relief=RAISED, bg='#64dd17', fg='white',
                   command=button_equal)
equal_btn.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')


rows = 6
columns = 4
for row in range(rows):
    root.grid_rowconfigure(row, weight=1)
for column in range(columns):
    root.grid_columnconfigure(column, weight=1)


root.mainloop()
