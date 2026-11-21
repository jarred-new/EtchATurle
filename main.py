import turtle_etchasketch
import touch_controller

if __name__ == "__main__":
    turt = turtle_etchasketch.MainTurtle()
    touch = touch_controller.TouchController()
    
    def right_turtle():
        turt.t.right(10)
    
    def left_turtle():
        turt.t.left(10)
    
    def forward_turtle():
        turt.t.forward(10)
    
    def backward_turtle():
        turt.t.backward(10)
    
    touch.btn_up.configure(command=forward_turtle)
    touch.btn_down.configure(command=backward_turtle)
    
    touch.btn_left.configure(command=left_turtle)
    touch.btn_right.configure(command=right_turtle)
    
    touch.mainloop()
    