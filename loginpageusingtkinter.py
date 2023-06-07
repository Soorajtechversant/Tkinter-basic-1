import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        # Code to navigate to the second page
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create login button
login_button = tk.Button(window, text="Login", command=validate_login)
login_button.pack()

# Run the main window's event loop
window.mainloop()