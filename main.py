import turtle_etchasketch
import touch_controller

from tkinter import messagebox
from tkinter import colorchooser

ispen = 0

if __name__ == "__main__":
    # Declare and Construct Windows
    turt = turtle_etchasketch.MainTurtle()
    touch = touch_controller.TouchController()
    
    # Print the turtle details here...
    def print_movement():
        angle = turt.t.heading()
        pos = turt.t.pos()
        touch.footer.config(text=f"Angle: {angle}; Position (x,y): {pos}")
    
    # Movement
    def right_turtle():
        turt.t.right(10)
        print_movement()
    
    def left_turtle():
        turt.t.left(10)
        print_movement()
    
    def forward_turtle():
        turt.t.forward(10)
        print_movement()
    
    def backward_turtle():
        turt.t.backward(10)
        print_movement()
        
    def set_pen():
        global ispen
        ispen += 1
        
        if ispen == 1:
            turt.t.penup()
            touch.penlift.config(text="Pen Up")
        elif ispen == 2:
            ispen = 0
            turt.t.pendown()
            touch.penlift.config(text="Pen Down")
    
    def clear_turtle():
        turt.t.penup()
        touch.penlift.config(text="Pen Up", state="disabled")
        
        print_movement()
        
        turt.t.clear()
        turt.t.home()
        
        turt.t.pendown()
        touch.penlift.config(text="Pen Down", state="normal")
        
        print_movement()
        
    def set_turtle_from_dialog():
        valid_choices = ["crosshair", "arrow", "turtle", "circle", "square", "triangle", "classic"]
        user_choice = turt.screen.textinput(
            title="Choose Shape",
            prompt="Enter a shape (crosshair, arrow, turtle, circle, square, triangle, classic):"
        )
        
        if user_choice:
            cleaned_choice = user_choice.lower()
            if cleaned_choice in valid_choices:
                turt.t.shape(cleaned_choice)
            else:
                messagebox.showerror("Error", "Invalid Shape Selected!", parent=touch)
                
    def set_turtle_color():
        rgb, hexc = colorchooser.askcolor(title="Change Turtle Color", parent=touch)
        if hexc:
            turt.t.color(hexc)
            
    def set_turtle_bg_color():
        rgb, hexc = colorchooser.askcolor(title="Change Background Color", parent=touch)
        if hexc:
            turt.screen.bgcolor(hexc)

    def set_turtle_visibility():
        if turt.t.isvisible():
            turt.t.hideturtle()
            touch.hideTurtle.config(text="Show Turtle")
        else:
            turt.t.showturtle()
            touch.hideTurtle.config(text="Hide Turtle")
    
    touch.btn_up.configure(command=forward_turtle)
    touch.btn_down.configure(command=backward_turtle)
    
    touch.btn_left.configure(command=left_turtle)
    touch.btn_right.configure(command=right_turtle)
    
    touch.penlift.configure(command=set_pen)
    
    touch.shakeClear.configure(command=clear_turtle)
    
    #touch.turtlePick.configure(command=set_turtle_from_dialog)
    
    #touch.colorPick.configure(command=set_turtle_color)
    
    touch.hideTurtle.configure(command=set_turtle_visibility)
    
    touch.bind('w', lambda event: touch.btn_up.invoke())
    touch.bind('W', lambda event: touch.btn_up.invoke())
    touch.bind('s', lambda event: touch.btn_down.invoke())
    touch.bind('S', lambda event: touch.btn_down.invoke())
    touch.bind('a', lambda event: touch.btn_left.invoke())
    touch.bind('A', lambda event: touch.btn_left.invoke())
    touch.bind('d', lambda event: touch.btn_right.invoke())
    touch.bind('D', lambda event: touch.btn_right.invoke())
    
    touch.bind('p', lambda event: touch.penlift.invoke())
    touch.bind('P', lambda event: touch.penlift.invoke())
    
    touch.bind('c', lambda event: touch.shakeClear.invoke())
    touch.bind('C', lambda event: touch.shakeClear.invoke())

    touch.bind('t', lambda event: set_turtle_from_dialog())
    touch.bind('T', lambda event: set_turtle_from_dialog())

    touch.bind('o', lambda event: set_turtle_color())
    touch.bind('O', lambda event: set_turtle_color())
    
    touch.bind('b', lambda event: set_turtle_bg_color())
    touch.bind('B', lambda event: set_turtle_bg_color())
    
    touch.bind('h', lambda event: touch.hideTurtle.invoke())
    touch.bind('H', lambda event: touch.hideTurtle.invoke())
    
    # fileMenu
    touch.fileMenu.add_command(label="Take Picture")
    touch.fileMenu.add_separator()
    touch.fileMenu.add_command(label="Exit")
    
    # turtleMenu
    touch.turtleMenu.add_command(label="Change Turtle Shape", command=set_turtle_from_dialog)
    touch.turtleMenu.add_command(label="Change Turtle Color", command=set_turtle_color)
    touch.turtleMenu.add_command(label="Change BG Color", command=set_turtle_bg_color)
    touch.turtleMenu.add_separator()
    touch.turtleMenu.add_command(label="Shake the Device!", command=clear_turtle)
    
    touch.mainMenu.add_cascade(label="File", menu=touch.fileMenu)
    touch.mainMenu.add_cascade(label="Turtle", menu=touch.turtleMenu)
    
    touch.mainloop()
    
    
    
    