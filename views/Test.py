import tkinter as tk

BUTTON_WIDTH = 10


class MainWindowView:
    def __init__(self):
        # Defie the root window
        self.root = tk.Tk()
        self.root.title("Elexant 9300 Test System Application")
        self.root.geometry("500x500")
        self.root.minsize(width=500, height=500)

        # Define main menu bar
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Define secondary menus and add them to main menu
        self.secondary_menu_file = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="File", menu=self.secondary_menu_file)
        self.secondary_menu_settings = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(
            label="Settings", menu=self.secondary_menu_settings)

        # Define items for secondary_menu_file and link them to corresponding commands
        self.secondary_menu_file.add_command(
            label="Clear Message", command=self.cmd_clear_message)
        self.secondary_menu_file.add_separator()
        self.secondary_menu_file.add_command(
            label="Exit", command=self.cmd_exit)

        #
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=0)
        self.button_frame.columnconfigure(1, weight=0)
        self.button_frame.columnconfigure(2, weight=0)
        self.button_refresh = tk.Button(
            self.button_frame, width=BUTTON_WIDTH, text="Refresh")
        self.button_refresh.grid(row=0, column=0, sticky=tk.E)
        self.button_start = tk.Button(
            self.button_frame, width=BUTTON_WIDTH, text="Start")
        self.button_start.grid(row=0, column=1, sticky=tk.E)
        self.button_stop = tk.Button(
            self.button_frame, width=BUTTON_WIDTH, text="Stop")
        self.button_stop.grid(row=0, column=2, sticky=tk.E)
        self.button_frame.pack(anchor=tk.E)

        # Add status output textbox at the bottom of the window
        self.status_output = tk.Text(self.root, height=10)
        self.status_output.pack(fill="both", side="bottom")
        # self.status_output.configure(state="disabled")

        # Start the UI's main loop
        self.root.mainloop()

    # cmd_clear_message

    def cmd_clear_message(self):
        print("cmd_clear_message method called")
        self.status_output.delete("1.0", tk.END)

    # cmd_exit

    def cmd_exit(self):
        print("cmd_exit method called")
        self.root.quit()


my_GUI = MainWindowView()

