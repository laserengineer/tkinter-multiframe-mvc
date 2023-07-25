import tkinter as tk
from tkinter import ttk

root = tk.Tk()

button_style = ttk.Style()
button_style.configure("Launcher_Button.TButton", font=("Helvetica", 20, "bold"))

launch_button = ttk.Button(
    root,
    text="Launch App",
    command=root.quit,
    width=20,
    style="Launcher_Button.TButton",
)
launch_button.pack(anchor="n", padx=10)

root.mainloop()
