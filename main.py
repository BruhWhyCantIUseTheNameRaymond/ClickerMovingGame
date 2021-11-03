# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
box_color = ("lightblue")
box_size = 3
box_shape = ("square")
#-----initialize turtle-----
box = trtl.Turtle()
box.shape(box_shape)
box.shapesize(box_size)
box.fillcolor(box_color)
box.speed(0)
#-----game functions--------
def box_clicked(x,y):
    change_position()
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    box.penup()
    box.hideturtle()
    box.goto(new_xpos,new_ypos)
    box.showturtle()
    box.pendown()

#-----events----------------
box.onclick(box_clicked)
wn = trtl.Screen()
wn.mainloop()