from tkinter import *
from tkinter import ttk

root = Tk()  # Create root window
root.title("Button Widget")  # title of the GUI window


#
def volumeUp():
    """output message to terminal to tell that the button is working"""
    print("Volume Increase +1")


def volumeDown():
    """output message to terminal to tell that the button is working"""
    print("Volume Increase - 1")


# use Button and Label widgets to create a simple TV remote
def turnOnTV():
    """callback method used for turn_on button"""
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(root)
    window.title("TV")
    image = PhotoImage(file="Test\giphy.gif")

    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()


# use Button and Label widgets to create a simple TV remote
# select image for on button
on_button_photo = PhotoImage(file="Test\BoN.png")
photo = on_button_photo.subsample(1, 1)
turn_on = ttk.Button(root, image=photo, command=turnOnTV)
turn_on.pack()


# turn_on = Button(root, text="ON", command=turnOnTV)
# turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()


root.mainloop()
