import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, fg="Orange Red1")


root = tk.Tk()
root.title("Task list")
root.configure(background="DarkBlue")

text1 = tk.Label(root, text="ENTER YOUR TASK", bg="DarkBlue", fg="lime green")
text1.pack(pady=10)

task_entry = tk.Entry(root, width=33, bg="DodgerBlue4", fg="snow1")
task_entry.pack(pady=15)

add_task_button = tk.Button(root, text="Add Task", fg="snow1", bg="navy", command=add_task)
add_task_button.pack(pady=2)

delete_button = tk.Button(root, text="Delete Task", fg="snow1", bg="navy", command=delete_task)
delete_button.pack(pady=2)

mark_button = tk.Button(root, text="Mark Running Task", fg="snow1", bg="navy", command=mark_task)
mark_button.pack(pady=2)

text2 = tk.Label(root, text="TASK LIST", bg="DarkBlue", fg="lime green")
text2.pack(pady=6)

task_listBox = tk.Listbox(root, height=10, width=100, bg="DodgerBlue4", fg="snow1")
task_listBox.pack(pady=10)

root.mainloop()