import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
from BoN import BoN
from HA import HA


class AppLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elexant 9300 Launcher")
        self.geometry("1200x411+50+50")

        self.canvas = tk.Canvas(self, width=681, height=240, bg="white")
        self.canvas.pack(side="top", fill="x")

        # Add drop_down menu
        self.menu = tk.StringVar(self)
        self.menu.set("Select App to Launch")
        self.drop = ttk.Combobox(
            self,
            textvariable=self.menu,
            values=["BoN", "HA"],
            font=("Helvetica", 16, "bold"),
        )
        self.drop.pack(pady=20)

        # Add launch button
        button_style = ttk.Style()
        button_style.configure(
            "Launcher_Button.TButton", font=("Helvetica", 16, "bold")
        )
        self.launch_button = ttk.Button(
            self,
            text="Launch App",
            command=self.launch_app,
            width=20,
            style="Launcher_Button.TButton",
        )
        self.launch_button.pack(anchor="n", padx=10)

        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.display_gif()
        
        
    def launch_app(self):
        
        # Create an Error message for invalid selection
        def show_selection_error_dialog():
            messagebox.showerror("Error", "Invalid Selection!")
        
        # Get the selected app name from the dropdown menu
        app_name = self.menu.get()        

        # Create the corresponding app object based on the selected app name
        if app_name == "BoN":
            app = BoN("Launcher")
            app.launch()
            self.quit()
        elif app_name == "HA":
            app = HA("Launcher")
            app.launch()
            self.quit()
        else:
            show_selection_error_dialog()
        

    def display_gif(self):
        # Open the GIF file
        im = Image.open("Test/Raychem.gif")
        self.frames = []

        # Extract each frame from the GIF and convert it to PhotoImage
        for frame in ImageSequence.Iterator(im):
            self.frames.append(ImageTk.PhotoImage(frame))

        # Start displaying the frames
        self.update_frame(0)

    def update_frame(self, frame_index):
        # Clear the canvas
        self.canvas.delete("all")

        # Display the current frame on the canvas
        self.canvas.create_image((600, 120), image=self.frames[frame_index])

        # Update the window
        self.update()

        # Schedule the next frame update after a delay
        self.after(100, lambda: self.update_frame((frame_index + 1) % len(self.frames)))


if __name__ == "__main__":
    # Instantiate the AppLauncher class and start the main event loop
    app_launcher = AppLauncher()
    app_launcher.mainloop()
