import tkinter as tk
from tkinter import ttk

class TouchController(tk.Tk):

    def __init__(self):
        # Initialize the parent tk.Tk class
        super().__init__()
        
        # Configure the root window using 'self'
        self.title("Etch A Turtle Controller")
        self.geometry("400x300")
        
        # Add widgets
        self.create_widgets()
        
        tk.mainloop()
    
    def create_widgets(self):
        self.label = ttk.Label(self, text="Etch a Turtle")
        self.label.pack(pady=20)
        
        self.button = ttk.Button(self, text="Forward")
        self.button.pack()
    