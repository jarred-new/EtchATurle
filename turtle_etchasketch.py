import math
import turtle

class MainTurtle(): 
    
    def __init__(self):
        self.screen = turtle.Screen()
        
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
        
        
        
        