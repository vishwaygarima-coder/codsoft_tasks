import json
import os

FILE = "tasks.json"
tasks = []

#load saved tasks
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        tasks = json.load(f)
        
#show all tasks 
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(i, task["title"],"-", status)
            
#Add task
def add_task():
    title = input("Enter task:")
    tasks.append({"title": title,"done": False})
    save_tasks()
    print("Task added!")
    
#Complete task
def complete_task():
    show_tasks()
    n = int(input("Enter task number:"))
    
    if 1<=n <= len(tasks):
        tasks[n - 1]["done"] = True
        save_tasks()
        print("Task completed!")
    else:
        print("Invalid task number.")
        
#Delete task
def delete_task():
    show_tasks()
    n = int(input("Enter task number:"))
    if 1<=n <=len(tasks):
        tasks.pop(n - 1)
        save_tasks()
        print(" Task deleted!")
    else:
        print("Invalid task number ")
        
#Save tasks
def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)
        
#Main menu
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!!")
        break
    else:
        print("Invalid choice.")
