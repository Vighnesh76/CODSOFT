import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        self.master.attributes("-fullscreen", True)
        self.master.configure(bg="#F4F4F4")
        self.master.bind("<Escape>", self.exit_fullscreen)

        self.tasks = []
        self.task_entry = tk.Entry(self.master, font=("Helvetica", 16), bg="#FFFFFF", fg="#333333")
        self.task_entry.pack(pady=40)

        self.add_button = tk.Button(self.master, text="Add Task", font=("Helvetica", 14), command=self.add_task,
                                    bg="#81C784", fg="#FFFFFF")
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self.master, font=("Helvetica", 14), bg="#FFFFFF", fg="#333333",
                                       selectbackground="#81C784")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

        self.delete_button = tk.Button(self.master, text="Delete Task", font=("Helvetica", 14), command=self.delete_task,
                                       bg="#E57373", fg="#FFFFFF")
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]

    def load_tasks(self):
        # TODO: 
        self.tasks = ["Task 1", "Task 2", "Task 3"]  
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        # TODO: 
        pass

    def exit_fullscreen(self, event):
        self.master.attributes("-fullscreen", False)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.save_tasks()
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)

    
    app_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
    root.option_add("*Font", app_font)
    root.option_add("*Listbox.Font", app_font)
    root.option_add("*Button.Font", app_font)

    app_icon = tk.PhotoImage(file="trophy.png")  
    root.iconphoto(True, app_icon)

    root.configure(bg="#F4F4F4")

    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
