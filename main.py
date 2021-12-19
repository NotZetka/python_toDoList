import tkinter
import tkinter.messagebox
import pickle

def addTask():
    # getting task as string
    task = entryTask.get()
    if task != "":
        tasksList.insert(tkinter.END, task)
        # clearing textbox
        entryTask.delete(0, tkinter.END)
        # saving task
        save_tasks()
    else:
        # warning box
        tkinter.messagebox.showwarning(title="Uwaga!", message="Nie wpisano zadania!")

def load_tasks():
    tasks = pickle.load(open("tasks.dat", "rb"))
    tasksList.delete(0, tkinter.END)
    for task in tasks:
        tasksList.insert(tkinter.END, task)

def save_tasks():
    tasks = tasksList.get(0, tasksList.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def delete_task():
    try:
        task_index = tasksList.curselection()[0]
        tasksList.delete(task_index)
        save_tasks()
    except:
        tkinter.messagebox.showwarning(title="Uwaga!", message="Nie wybrano zadania do usunięcia")

# gui

# creating window
root = tkinter.Tk()
root.title('ToDoList')

# making a frame for list and scrollbar
tasksWindow = tkinter.Frame(root)
tasksWindow.pack()

# list
tasksList = tkinter.Listbox(tasksWindow, height=10, width=40)
tasksList.pack(side=tkinter.LEFT)

# scrollbar
scrollbar = tkinter.Scrollbar(tasksWindow)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# this makes scrollbar also work not just mouse scroll
tasksList.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasksList.yview)

# textbox for entering tasks
entryTask = tkinter.Entry(root, width=40)
entryTask.pack()

# addbutton
button_add_task = tkinter.Button(root, text="Add task", width=38, command=addTask)
button_add_task.pack()

# delete button
button_delete_task = tkinter.Button(root, text="Delete task", width=38, command=delete_task)
button_delete_task.pack()



# initial functions
save_tasks()
load_tasks()
# it stop's window from closing
root.mainloop()

