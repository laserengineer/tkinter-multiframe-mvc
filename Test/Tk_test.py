import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text = "Hello, Tkinter",
    fg = "white", # set the text color to white
    bg = "black", # set the background color to black
    width = 10, 
    height = 10
)
label.pack()
# label.mainloop()

button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg = "red",
    fg = "yellow"
)

button.pack()
# button.mainloop()



entry = tk.Entry(
    fg = "yellow",
    bg = "blue",
    width = 50
)
entry.pack()
window.mainloop()
"""*.mainloop() tells Python to run Tkinter event loop """