import tkinter as tk

class TouchController(tk.Tk):

    def __init__(self):
        # Initialize the parent tk.Tk class
        super().__init__()
        
        # Configure the root window using 'self'
        self.title("Etch A Turtle Controller")
        self.geometry("400x467")
        self.config(bg="red")
        
        # Add widgets
        self.create_widgets()
    
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
        
        self.penlift = tk.Button(self, text="Pen Down", **self.btn_style_auto)
        self.penlift.pack(expand=True, pady=5)
        
        self.shakeClear = tk.Button(self, text="SHAKE!", **self.btn_style_auto)
        self.shakeClear.pack(expand=True, pady=5)
        
        self.btn_up.grid(row=0, column=1, padx=2, pady=2)
        self.btn_left.grid(row=1, column=0, padx=2, pady=2)
        self.btn_right.grid(row=1, column=2, padx=2, pady=2)
        self.btn_down.grid(row=2, column=1, padx=2, pady=2)
        
        self.footer = tk.Label(self, 
            text="Welcome to Etch A Turtle!", 
            **self.footer_style
        )
        self.footer.pack(anchor="sw", padx=5, pady=5)
        
        
        
        
        
        
        
    