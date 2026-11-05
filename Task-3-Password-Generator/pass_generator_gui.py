import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Warning", "Minimum length is 4!")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


# Copy password
def copy_password():
    password = password_entry.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied successfully!")
    else:
        messagebox.showwarning("Warning", "Generate a password first!")


# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x550")
window.config(bg="#151525")
window.resizable(False, False)

# Heading
title = tk.Label(
    window,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 22, "bold"),
    bg="#151525",
    fg="#A78BFA"
)
title.pack(pady=35)

subtitle = tk.Label(
    window,
    text="Create strong passwords in seconds",
    font=("Arial", 11),
    bg="#151525",
    fg="white"
)
subtitle.pack(pady=5)

# Password length
length_label = tk.Label(
    window,
    text="Enter Password Length",
    font=("Arial", 12, "bold"),
    bg="#151525",
    fg="white"
)
length_label.pack(pady=20)

length_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center",
    width=15,
    bg="#292940",
    fg="white",
    insertbackground="white"
)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Generate button
generate_button = tk.Button(
    window,
    text="GENERATE PASSWORD",
    font=("Arial", 12, "bold"),
    bg="#8B5CF6",
    fg="white",
    activebackground="#7C3AED",
    width=23,
    command=generate_password
)
generate_button.pack(pady=25)

# Password display
password_label = tk.Label(
    window,
    text="Your Generated Password",
    font=("Arial", 12),
    bg="#151525",
    fg="white"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    window,
    font=("Arial", 13),
    justify="center",
    width=30,
    bg="#292940",
    fg="#A78BFA",
    insertbackground="white"
)
password_entry.pack(pady=10)

# Copy button
copy_button = tk.Button(
    window,
    text="COPY PASSWORD",
    font=("Arial", 11, "bold"),
    bg="#14B8A6",
    fg="white",
    width=20,
    command=copy_password
)
copy_button.pack(pady=20)

# Footer
footer = tk.Label(
    window,
    text="SECURE  •  RANDOM  •  SIMPLE",
    font=("Arial", 10, "bold"),
    bg="#151525",
    fg="#A78BFA"
)
footer.pack(pady=25)

window.mainloop()
