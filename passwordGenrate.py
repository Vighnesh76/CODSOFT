import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_label.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the length.")


window = tk.Tk()
window.title("Password Generator")
window.attributes("-fullscreen", True)


background_image = tk.PhotoImage(file="background_image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


length_label = tk.Label(window, text="Length:", font=("Arial", 20, "bold"), fg="#FFFFFF", bg="#000000")
length_label.pack(pady=10)

length_entry = tk.Entry(window, font=("Arial", 16))
length_entry.pack()

generate_button = tk.Button(window, text="Generate", command=generate_button_clicked, font=("Arial", 16, "bold"), bg="#FF6B6B")
generate_button.pack(pady=10)

password_label = tk.Label(window, text="", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#000000")
password_label.pack(pady=10)


window.mainloop()
