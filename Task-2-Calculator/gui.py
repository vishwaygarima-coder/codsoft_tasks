import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("My Calculator")
root.geometry("380x620")
root.resizable(False, False)
root.configure(bg="#151515")

# Variables
display = tk.StringVar(value="0")
first_number = None
operator = None
new_number = True


# Number Button Function
def press(value):
    global new_number

    current = display.get()

    if value == ".":
        if new_number:
            display.set("0.")
            new_number = False
        elif "." not in current:
            display.set(current + ".")
        return

    if new_number or current == "0":
        display.set(value)
        new_number = False
    else:
        display.set(current + value)


# Operator Function
def choose_operator(op):
    global first_number, operator, new_number

    try:
        first_number = float(display.get())
        operator = op
        new_number = True
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


# Clear Function
def clear():
    global first_number, operator, new_number

    display.set("0")
    first_number = None
    operator = None
    new_number = True


# Backspace Function
def backspace():
    global new_number

    if new_number:
        return

    current = display.get()

    if len(current) > 1:
        display.set(current[:-1])
    else:
        display.set("0")
        new_number = True


# Calculation Function
def calculate():
    global first_number, operator, new_number

    if operator is None:
        return

    try:
        second_number = float(display.get())

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero!"
                )
                clear()
                return

            result = first_number / second_number

        # Save calculation in history
        expression = (
            f"{first_number:g} {operator} "
            f"{second_number:g} = {result:g}"
        )

        history_box.insert(0, expression)

        # Display result
        display.set(str(result))

        first_number = None
        operator = None
        new_number = True

    except ValueError:
        messagebox.showerror("Error", "Invalid input")


# Clear History Function
def clear_history():
    history_box.delete(0, tk.END)


# Heading
heading = tk.Label(
    root,
    text="MY CALCULATOR",
    font=("Arial", 21, "bold"),
    bg="#151515",
    fg="#FFFFFF"
)
heading.pack(pady=18)


# Display Screen
screen = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 27, "bold"),
    bg="#252525",
    fg="#FFFFFF",
    justify="right",
    bd=0,
    state="readonly",
    readonlybackground="#252525"
)
screen.pack(fill="x", padx=20, ipady=18, pady=12)


# History Heading
history_title = tk.Label(
    root,
    text="CALCULATION HISTORY",
    font=("Arial", 10, "bold"),
    bg="#151515",
    fg="#AAAAAA"
)
history_title.pack(pady=(8, 2))


# History Display
history_box = tk.Listbox(
    root,
    height=3,
    font=("Arial", 11),
    bg="#252525",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    selectbackground="#176B50"
)
history_box.pack(fill="x", padx=20, pady=5)


# Clear History Button
clear_history_btn = tk.Button(
    root,
    text="Clear History",
    font=("Arial", 9),
    bg="#333333",
    fg="white",
    bd=0,
    cursor="hand2",
    command=clear_history
)
clear_history_btn.pack(pady=5)


# Button Frame
button_frame = tk.Frame(
    root,
    bg="#151515"
)
button_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=8
)


# Button Creation Function
def create_button(
    text, row, col, command,
    color="#292929",
    colspan=1,
    rowspan=1
):

    btn = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=command
    )

    btn.grid(
        row=row,
        column=col,
        columnspan=colspan,
        rowspan=rowspan,
        sticky="nsew",
        padx=5,
        pady=5
    )


# Calculator Buttons
buttons = [
    ("C", 0, 0, clear, "#A83232"),
    ("⌫", 0, 1, backspace, "#444444"),
    ("÷", 0, 2, lambda: choose_operator("/"), "#176B50"),
    ("×", 0, 3, lambda: choose_operator("*"), "#176B50"),

    ("7", 1, 0, lambda: press("7"), "#292929"),
    ("8", 1, 1, lambda: press("8"), "#292929"),
    ("9", 1, 2, lambda: press("9"), "#292929"),
    ("−", 1, 3, lambda: choose_operator("-"), "#176B50"),

    ("4", 2, 0, lambda: press("4"), "#292929"),
    ("5", 2, 1, lambda: press("5"), "#292929"),
    ("6", 2, 2, lambda: press("6"), "#292929"),
    ("+", 2, 3, lambda: choose_operator("+"), "#176B50"),

    ("1", 3, 0, lambda: press("1"), "#292929"),
    ("2", 3, 1, lambda: press("2"), "#292929"),
    ("3", 3, 2, lambda: press("3"), "#292929"),
    ("=", 3, 3, calculate, "#23865F"),

    ("0", 4, 0, lambda: press("0"), "#292929"),
    (".", 4, 2, lambda: press("."), "#292929")
]


# Display Buttons
for text, row, col, command, color in buttons:

    if text == "0":
        create_button(
            text, row, col, command,
            color, colspan=2
        )

    elif text == "=":
        create_button(
            text, row, col, command,
            color, rowspan=2
        )

    else:
        create_button(
            text, row, col, command, color
        )


# Grid Configuration
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# Run Application
root.mainloop()
