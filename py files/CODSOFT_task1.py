#!/usr/bin/env python
# coding: utf-8

# In[18]:


import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return f"{self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)

    def get_tasks(self):
        return [str(task) for task in self.tasks]

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            if new_description:
                self.tasks[index].description = new_description
    



class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")
        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(self)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)


    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.todo_list.add_task(task_description)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.get_tasks():
            self.task_listbox.insert(tk.END, task)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_description = self.task_entry.get()
            if new_description:
                self.todo_list.update_task(selected_index[0], new_description)
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task description cannot be empty.")
        else:
            messagebox.showwarning("Warning", "No task selected.")


if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()


# In[ ]:





# In[ ]:




