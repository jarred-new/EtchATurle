import os
import tkinter as tk

class TouchController(tk.Tk):

    def __init__(self):
        # Initialize the parent tk.Tk class
        super().__init__()
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.base_dir, "assets", "EtchASketch-01.png")
        
        # Configure the root window using 'self'
        self.title("Etch A Turtle Controller")
        self.geometry("400x467")
        self.config(bg="red")
        self.appicon = tk.PhotoImage(file=self.icon_path, master=self)
        self.iconphoto(True, self.appicon)
        
        # Add widgets
        self.create_widgets()
        self.create_menu()
    
    def create_widgets(self):
        self.header_style = {"background": "red", "foreground": "yellow", "font": ("Arial", 24, "bold")}
        self.footer_style = {"background": "red", "foreground": "yellow", "font": ("Arial", 12)}
        
        self.header = tk.Label(self, text="Etch a Turtle", **self.header_style)
        self.header.pack(pady=20)
        
        self.dpad_frame = tk.Frame(self)
        self.dpad_frame.pack(expand=True)
        
        self.btn_style = {"width": 5, "height": 2, "font": ("Arial", 12, "bold")}
        self.btn_style_auto = {"height": 2, "font": ("Arial", 12, "bold")}

        # 2. Place the 4 buttons using a 3x3 grid layout
        self.btn_up = tk.Button(self.dpad_frame, text="▲", **self.btn_style)
        self.btn_left = tk.Button(self.dpad_frame, text="◄", **self.btn_style)
        self.btn_right = tk.Button(self.dpad_frame, text="►", **self.btn_style)
        self.btn_down = tk.Button(self.dpad_frame, text="▼", **self.btn_style)

        self.tools = tk.Frame(self)
        self.tools.pack(expand=True, pady=10)
        
        self.penlift = tk.Button(self.tools, text="Pen Down", **self.btn_style_auto)
        self.penlift.grid(row=0, column=0, padx=2, pady=2)

        self.hideTurtle = tk.Button(self.tools, text="Hide Turtle", **self.btn_style_auto)
        self.hideTurtle.grid(row=0, column=1, padx=2, pady=2)
        
        self.turtlePick = tk.Button(self.tools, text="Set Turtle", **self.btn_style_auto)
        self.turtlePick.grid(row=1, column=0, padx=2, pady=2)
        
        self.colorPick = tk.Button(self.tools, text="Set Color", **self.btn_style_auto)
        self.colorPick.grid(row=1, column=1, padx=2, pady=2)

        self.shakeClear = tk.Button(self, text="SHAKE!", **self.btn_style_auto)
        self.shakeClear.pack(expand=True, pady=10)
        
        self.btn_up.grid(row=0, column=1, padx=2, pady=2)
        self.btn_left.grid(row=1, column=0, padx=2, pady=2)
        self.btn_right.grid(row=1, column=2, padx=2, pady=2)
        self.btn_down.grid(row=2, column=1, padx=2, pady=2)
        
        self.footer = tk.Label(self, 
            text="Welcome to Etch A Turtle!", 
            **self.footer_style
        )
        self.footer.pack(anchor="sw", padx=5, pady=5)
        
    def create_menu(self):
        self.mainMenu = tk.Menu(self)
        self.config(menu=self.mainMenu)
        
        self.fileMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.turtleMenu = tk.Menu(self.mainMenu, tearoff=0)
        # Creating or putting it on the menu is at the end of the main.py file
        
        
    