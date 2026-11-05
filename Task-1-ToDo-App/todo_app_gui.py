import tkinter as tk
from tkinter import messagebox
import json
import os

# COLORS
BG = "#111318"
CARD = "#1C2029"
ACCENT = "#8B7CF6"
WHITE = "#F5F5F7"
GREY = "#969BA8"
GREEN = "#75C69B"

FILE = "tasks.json"

# LOAD TASKS
def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)

            if isinstance(data, list):
                return [
                    x if isinstance(x, dict)
                    else {"task": str(x), "completed": False}
                    for x in data
                ]
        except (ValueError, OSError):
            pass
    return []

tasks = load_tasks()

# SAVE TASKS
def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ADD TASK
def add_task():
    value = entry.get().strip()

    if not value:
        messagebox.showwarning("Reminder", "Please enter a task!")
        return

    tasks.append({"task": value, "completed": False})
    entry.delete(0, tk.END)
    save_tasks()
    display_tasks()

# COMPLETE TASK
def complete_task(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    display_tasks()

# DELETE TASK
def delete_task(index):
    tasks.pop(index)
    save_tasks()
    display_tasks()

# MAIN WINDOW
root = tk.Tk()
root.title("FocusFlow | Task Manager")
root.geometry("760x720")
root.configure(bg=BG)
root.resizable(False, False)

# HEADER
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=45, pady=30)

tk.Label(
    header, text="FOCUSFLOW",
    font=("Arial", 12, "bold"),
    bg=BG, fg=ACCENT
).pack(anchor="w")

tk.Label(
    header, text="Stay focused. Get things done.",
    font=("Arial", 25, "bold"),
    bg=BG, fg=WHITE
).pack(anchor="w", pady=(15, 5))

tk.Label(
    header, text="Your personal productivity space.",
    font=("Arial", 11),
    bg=BG, fg=GREY
).pack(anchor="w")

# PROGRESS CARD
progress_card = tk.Frame(root, bg=CARD, padx=20, pady=18)
progress_card.pack(fill="x", padx=45, pady=10)

progress_title = tk.Label(
    progress_card, text="DAILY PROGRESS",
    font=("Arial", 10, "bold"),
    bg=CARD, fg=GREY
)
progress_title.pack(anchor="w")

progress_text = tk.Label(
    progress_card, text="0 / 0 completed",
    font=("Arial", 17, "bold"),
    bg=CARD, fg=WHITE
)
progress_text.pack(anchor="w", pady=8)

# INPUT AREA
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill="x", padx=45, pady=20)

entry = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg=CARD, fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)
entry.pack(side="left", fill="x", expand=True, ipady=13, padx=(0, 12))

add_button = tk.Button(
    input_frame,
    text="+  ADD TASK",
    command=add_task,
    bg=ACCENT, fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat", padx=20, pady=12,
    cursor="hand2"
)
add_button.pack(side="right")

entry.bind("<Return>", lambda event: add_task())

# TASK HEADING
task_heading = tk.Label(
    root, text="YOUR TASKS",
    font=("Arial", 12, "bold"),
    bg=BG, fg=WHITE
)
task_heading.pack(anchor="w", padx=50, pady=10)

# TASK LIST
task_frame = tk.Frame(root, bg=BG)
task_frame.pack(fill="both", expand=True, padx=45)

def display_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("completed", False))

    progress_text.config(
        text=f"{completed} / {total} completed"
    )

    if not tasks:
        tk.Label(
            task_frame,
            text="No tasks yet. Add your first task!",
            bg=BG, fg=GREY,
            font=("Arial", 12)
        ).pack(pady=30)

    for i, item in enumerate(tasks):
        row = tk.Frame(task_frame, bg=CARD, padx=15, pady=12)
        row.pack(fill="x", pady=5)

        var = tk.BooleanVar(value=item.get("completed", False))

        tk.Checkbutton(
            row,
            variable=var,
            command=lambda n=i: complete_task(n),
            bg=CARD, fg=GREEN,
            selectcolor=CARD,
            activebackground=CARD,
            relief="flat"
        ).pack(side="left")

        tk.Label(
            row,
            text=item["task"],
            bg=CARD,
            fg=GREEN if item.get("completed", False) else WHITE,
            font=("Arial", 11)
        ).pack(side="left", padx=10)

        tk.Button(
            row,
            text="DELETE",
            command=lambda n=i: delete_task(n),
            bg=CARD, fg="#F08080",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(side="right")

# FOOTER
tk.Label(
    root,
    text="BUILT WITH PYTHON  •  JSON  •  OS",
    font=("Arial", 8),
    bg=BG, fg=GREY
).pack(pady=18)

display_tasks()
root.mainloop()
