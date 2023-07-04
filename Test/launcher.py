from tkinter import *
import time
from PIL import Image, ImageTk, ImageSequence
from BoN import BoN
from HA import HA


# Function to update the canvas with the next frame
def update_frame(frame_index):
    canvas.delete("all")  # Clear the canvas
    canvas.create_image((1200, 211), image=frames[frame_index])
    root.update()

    # Schedule the next frame update after a delay
    root.after(100, lambda: update_frame((frame_index + 1) % len(frames)))

# Function to display GIF frames
def display_gif():
    im = Image.open('Test/Raychem.gif')
    global frames
    frames = []
    for frame in ImageSequence.Iterator(im):
        frames.append(ImageTk.PhotoImage(frame))

    # Start the initial frame update
    update_frame(0)

def main():
    APP_MAP = {"BoN": BoN, "HA": HA}
    
    global root
    root = Tk()
    root.title("Elexant 9300 Launcher")
    root.geometry("1200x411")
    
    global canvas
    canvas = Canvas(root, width=1200, height=311, bg='white')
    canvas.pack(side='bottom')
    root.protocol("WM_DELETE_WINDOW", root.quit)
    # Call the display_gif function
    display_gif()
    root.mainloop()
    


# def main(choice):
#     try:
#         app = APP_MAP[choice]("Launcher")
#         app.launch()
#     except KeyError:
#         print(f"Invalid choice: {choice}")

if __name__ == "__main__":
    main()