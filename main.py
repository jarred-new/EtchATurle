import turtle_etchasketch
import touch_controller

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
    
    touch.btn_up.configure(command=forward_turtle)
    touch.btn_down.configure(command=backward_turtle)
    
    touch.btn_left.configure(command=left_turtle)
    touch.btn_right.configure(command=right_turtle)
    
    touch.mainloop()
    