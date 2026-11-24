import os
import tkinter as tk
import turtle

class MainTurtle(): 
    
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.base_dir, "assets", "EtchASketch-01.png")
        
        self.screen = turtle.Screen()
        self.icon = tk.PhotoImage(file=self.icon_path)

        self.screen.getcanvas().winfo_toplevel().iconphoto(True, self.icon)
        
        self.screen.title("Etch A Turtle")

        # Define coordinates for a 20x20 crosshair with 2px thickness
        self.crosshair_coords = (
            (-1, 10), (1, 10), (1, 1), (10, 1), (10, -1), (1, -1),
            (1, -10), (-1, -10), (-1, -1), (-10, -1), (-10, 1), (-1, 1)
        )
        
        # Register and apply the custom shape
        self.screen.register_shape("crosshair", self.crosshair_coords)
        
        self.t = turtle.Turtle()
        self.t.shape("crosshair")
        self.t.color("black")
        
        # Intro Movement
        self.t.penup()
        self.t.forward(10)
        self.t.forward(-10)
        self.t.pendown()
        
        
        
        