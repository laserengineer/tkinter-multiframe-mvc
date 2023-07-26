import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_error_dialog():
    messagebox.showerror("Error", "An error has occurred!")

root = tk.Tk()
root.title("Error Dialog Example")

error_button = ttk.Button(root, text="Show Error", command=show_error_dialog)
error_button.pack(pady=20)

root.mainloop()
