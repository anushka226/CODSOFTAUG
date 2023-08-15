import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        label = tk.Label(text="TO-DO-LIST",fg="deep pink",bg="NavajoWhite",width=100,height=10,bd=10)
        label.config(font=('Helvatical bold',10))
        label.pack()
        self.tasks = []
        self.load_tasks()

        self.task_listbox = tk.Listbox(root,background="Pink",foreground="Red")
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task,background="coral2",foreground="DodgerBlue4")
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task,background="coral2",foreground="DodgerBlue4")
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task,background="coral2",foreground="DodgerBlue4")
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks,background="coral2",foreground="DodgerBlue4")

        self.add_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.update_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.remove_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.clear_button.pack(padx=10, pady=5, fill=tk.BOTH)

        self.update_task_listbox()

    def load_tasks(self):
        # Load tasks from a file or database
        # For simplicity, using hardcoded tasks
        self.tasks = ["Task 1", "Task 2", "Task 3"]

    def save_tasks(self):
        # Save tasks to a file or database
        pass

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = simpledialog.askstring("Add Task", "Enter a new task:")
        if new_task:
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.save_tasks()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            updated_task = simpledialog.askstring("Update Task", "Edit the task:", initialvalue=self.tasks[selected_task_index])
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
                self.save_tasks()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
            self.save_tasks()

    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()
        self.save_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
