import tkinter as tk

# Initialize Window object
window = tk.Tk()

# Create Label object and pack
greeting = tk.Label(text = "Hello. Tkinter")
greeting.pack()

# Create Entry object and pack 
entry = tk.Entry()
entry.insert(0, "Yang Yu")
entry.pack()


# Create Text Widgets that contain multiple lines of text 

text_box = tk.Text()
test_box.pack()


# Call run window  mainloop 
window.mainloop()