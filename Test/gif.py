from tkinter import *
import time
from PIL import Image, ImageTk, ImageSequence

root = Tk()
root.title("Elexant 9300 Launcher")
root.geometry("1200x411")

canvas = Canvas(root, width=1200, height=311, bg='white')
canvas.pack(side='bottom')

# Function to display GIF frames
def display_gif():
    im = Image.open('Test/Raychem.gif')
    frames = []
    for frame in ImageSequence.Iterator(im):
        frames.append(ImageTk.PhotoImage(frame))

    # Function to update the canvas with the next frame
    def update_frame(frame_index):
        canvas.delete("all")  # Clear the canvas
        canvas.create_image((1200, 211), image=frames[frame_index])
        root.update()

        # Schedule the next frame update after a delay
        root.after(100, lambda: update_frame((frame_index + 1) % len(frames)))

    # Start the initial frame update
    update_frame(0)

# Call the display_gif function
display_gif()

root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()