import turtle

screen = turtle.Screen()

# Define coordinates for a 20x20 crosshair with 2px thickness
crosshair_coords = (
    (-1, 10), (1, 10), (1, 1), (10, 1), (10, -1), (1, -1),
    (1, -10), (-1, -10), (-1, -1), (-10, -1), (-10, 1), (-1, 1)
)

# Register and apply the custom shape
screen.register_shape("crosshair", crosshair_coords)

t = turtle.Turtle()
t.shape("crosshair")
t.color("black")

# Test for movement
t.forward(100)

turtle.mainloop()
