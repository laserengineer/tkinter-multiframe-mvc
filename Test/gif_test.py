from tkinter import *
import time
from PIL import Image, ImageTk, ImageSequence

root = Tk()
root.title("Elexant 9300 Launcher")
root.geometry("1200x611")

canvas = Canvas(root, width=1200, height=311, bg='white')

canvas.pack(side = 'bottom')

# Function to display GIF frames
def display_gif(canvas):
    while True:
        im = Image.open('Test\Raychem.gif')
        iter = ImageSequence.Iterator(im)
        for frame in iter:
            pic = ImageTk.PhotoImage(frame)
            canvas.create_image((1200, 211), image=pic)
            time.sleep(0.1)
            root.update_idletasks()
            root.update()

# Bind the display_gif function to the canvas
# canvas.bind("<Enter>", lambda event: display_gif(canvas))

display_gif(canvas)
root.mainloop()