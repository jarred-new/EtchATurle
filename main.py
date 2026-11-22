import turtle_etchasketch
import touch_controller

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
    
    touch.btn_up.configure(command=forward_turtle)
    touch.btn_down.configure(command=backward_turtle)
    
    touch.btn_left.configure(command=left_turtle)
    touch.btn_right.configure(command=right_turtle)
    
    touch.penlift.configure(command=set_pen)
    
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
    
    touch.mainloop()
    
    
    
    