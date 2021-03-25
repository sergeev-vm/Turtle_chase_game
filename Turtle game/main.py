# TODO: 2 turtles, different colour, same shape, one turtle runs away and it moved up and downward, left and right,
# TODO: second turtle turns left and right with faster speed and chases the fist one.
# TODO: turtles swap and than chaser becomes runner and vice versa
# TODO: calculate seconds how turtles run and chase
import turtle
import time
from constants import *

class TurtleParent(turtle.Turtle):
    def __init__(self, posx=0, posy=0, tshape="turtle", tcolor="red"):
        super(TurtleParent, self).__init__()
        self.penup()
        self.goto(posx, posy)
        self.shape(tshape)
        self.color(tcolor)
        self.chaser = False
        self.timeleft = TIME_DURATION
    def moveup(self):
        self.setheading(90)
        self.forward(MOVE_SPEED_RUN)
    def moveleft(self):
        self.setheading(180)
        self.forward(MOVE_SPEED_RUN)
    def moveright(self):
        self.setheading(0)
        self.forward(MOVE_SPEED_RUN)
    def movedown(self):
        self.setheading(270)
        self.forward(MOVE_SPEED_RUN)
    def moveforwardfast(self):
        self.forward(MOVE_SPEED_CHASE)
    def movebackwardfast(self):
        self.backward(MOVE_SPEED_CHASE*3)
    def turnleft(self):
        self.left(TURN_SPEED)
    def turnright(self):
        self.right(TURN_SPEED)

# Game Starts here
screen = turtle.Screen()
screen.listen()
turtle_tom = TurtleParent(posx=-60, posy=-60, tcolor="grey")
turtle_tom.chaser = True
turtle_jerry = TurtleParent(posx=60, posy=60, tcolor="purple")
turtle_tuffy = TurtleParent(posx=-100, posy=230, tcolor="black")
turtle_tuffy.hideturtle()

def key_define(chaser):
    if chaser == turtle_tom:
        # Tom
        screen.onkey(key="w", fun=turtle_tom.moveup)
        screen.onkey(key="a", fun=turtle_tom.moveleft)
        screen.onkey(key="d", fun=turtle_tom.moveright)
        screen.onkey(key="s", fun=turtle_tom.movedown)
        # Jerry
        screen.onkeypress(key="i", fun=turtle_jerry.moveforwardfast)
        screen.onkeypress(key="k", fun=turtle_jerry.movebackwardfast)
        screen.onkeypress(key="j", fun=turtle_jerry.turnleft)
        screen.onkeypress(key="l", fun=turtle_jerry.turnright)
    else:
        # Jerry
        screen.onkey(key="w", fun=turtle_jerry.moveup)
        screen.onkey(key="a", fun=turtle_jerry.moveleft)
        screen.onkey(key="d", fun=turtle_jerry.moveright)
        screen.onkey(key="s", fun=turtle_jerry.movedown)
        # Tom
        screen.onkeypress(key="i", fun=turtle_tom.moveforwardfast)
        screen.onkeypress(key="k", fun=turtle_tom.movebackwardfast)
        screen.onkeypress(key="j", fun=turtle_tom.turnleft)
        screen.onkeypress(key="l", fun=turtle_tom.turnright)

def catch_turtle():
    if turtle_tom.distance(turtle_jerry) < 20:
        print("Switch places!")
        turtle_tom.left(90)
        turtle_jerry.left(-90)
        turtle_tom.movebackwardfast()
        turtle_jerry.movebackwardfast()
        if turtle_tom.chaser:
            turtle_tom.chaser = False
            turtle_jerry.chaser = True
            key_define(turtle_jerry)
        else:
            turtle_tom.chaser = True
            turtle_jerry.chaser = False
            key_define(turtle_tom)

key_define(turtle_tom)
screen.tracer(0)
game_continues = True
while game_continues:
    catch_turtle()
    time.sleep(TIME_REFRESH)
    if turtle_tom.chaser:
        turtle_tom.timeleft -= TIME_REFRESH
    if turtle_jerry.chaser:
        turtle_jerry.timeleft -= TIME_REFRESH
    if turtle_tom.timeleft < 0 or turtle_jerry.timeleft < 0:
        break
    turtle_tuffy.clear()
    turtle_tuffy.write(f"Jerry = {round(turtle_jerry.timeleft,1)}, Tom = {round(turtle_tom.timeleft,1)}")
    screen.update()
turtle_tuffy.clear()
if turtle_tom.timeleft > turtle_jerry.timeleft:
    turtle_tuffy.write(f"Jerry={round(turtle_jerry.timeleft, 1)}, Tom={round(turtle_tom.timeleft, 1)} \nTom wins!")
else:
    turtle_tuffy.write(f"Jerry={round(turtle_jerry.timeleft, 1)}, Tom={round(turtle_tom.timeleft, 1)} \nJerry wins!")
screen.mainloop()