import turtle_etchasketch
import touch_controller

if __name__ == "__main__":
    turt = turtle_etchasketch.MainTurtle()
    touch = touch_controller.TouchController()
    
    def forward_turtle():
        turt.t.forward(10)
    
    touch.button.configure(command=forward_turtle)
    touch.mainloop()
    