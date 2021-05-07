#TODO Add "Continue" option
#TODO Fix algorithm after crash of turtles
#TODO Add custom images for turtle
#TODO Add option to shoot from one turtle to another
#TODO Customize seconds counter
#TODO Add AI (versus comp)
import turtle
import time
from constants import *


class TurtleParent(turtle.Turtle):
    def __init__(self, pos_x=0, pos_y=0, t_shape="turtle", t_color="red"):
        super(TurtleParent, self).__init__()
        self.penup()
        self.goto(pos_x, pos_y)
        self.shape(t_shape)
        self.color(t_color)
        self.chaser = False
        self.time_left = TIME_DURATION

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_SPEED_RUN)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_SPEED_RUN)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_SPEED_RUN)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_SPEED_RUN)

    def move_forward_fast(self):
        self.forward(MOVE_SPEED_CHASE)

    def move_backward_fast(self):
        self.backward(MOVE_SPEED_CHASE*3)

    def turn_left(self):
        self.left(TURN_SPEED)

    def turn_right(self):
        self.right(TURN_SPEED)


# Game Starts here
screen = turtle.Screen()
screen.listen()
turtle_tom = TurtleParent(pos_x=-60, pos_y=-60, t_color="grey")
turtle_tom.chaser = True
turtle_jerry = TurtleParent(pos_x=60, pos_y=60, t_color="purple")
turtle_tuffy = TurtleParent(pos_x=-100, pos_y=230, t_color="black")
turtle_yes = TurtleParent(pos_x=-30, pos_y=-150, t_color="green")
turtle_no = TurtleParent(pos_x=30, pos_y=-150, t_color="red")
turtle_tuffy.hideturtle()
turtle_yes.hideturtle()
turtle_no.hideturtle()
turtle_yes.shape("circle")
turtle_no.shape("circle")

def print_coordinates(x, y):
    print((x, y))

screen.onclick(print_coordinates, btn=1)

def key_define(chaser):
    if chaser == turtle_tom:
        # Tom
        screen.onkey(key="w", fun=turtle_tom.move_up)
        screen.onkey(key="a", fun=turtle_tom.move_left)
        screen.onkey(key="d", fun=turtle_tom.move_right)
        screen.onkey(key="s", fun=turtle_tom.move_down)
        # Jerry
        screen.onkeypress(key="i", fun=turtle_jerry.move_forward_fast)
        screen.onkeypress(key="k", fun=turtle_jerry.move_backward_fast)
        screen.onkeypress(key="j", fun=turtle_jerry.turn_left)
        screen.onkeypress(key="l", fun=turtle_jerry.turn_right)
    else:
        # Jerry
        screen.onkey(key="w", fun=turtle_jerry.move_up)
        screen.onkey(key="a", fun=turtle_jerry.move_left)
        screen.onkey(key="d", fun=turtle_jerry.move_right)
        screen.onkey(key="s", fun=turtle_jerry.move_down)
        # Tom
        screen.onkeypress(key="i", fun=turtle_tom.move_forward_fast)
        screen.onkeypress(key="k", fun=turtle_tom.move_backward_fast)
        screen.onkeypress(key="j", fun=turtle_tom.turn_left)
        screen.onkeypress(key="l", fun=turtle_tom.turn_right)

def turtle_distance(x, y):
    if turtle_yes.distance(x, y) < turtle_no.distance(x, y) and turtle_yes.distance(x, y) < 15:
        turtle_tom.time_left = TIME_DURATION
        turtle_jerry.time_left = TIME_DURATION

def catch_turtle():
    if turtle_tom.distance(turtle_jerry) < 20:
        print("Switch places!")
        turtle_tom.left(90)
        turtle_jerry.left(-90)
        turtle_tom.move_backward_fast()
        turtle_jerry.move_backward_fast()
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
pre_game = True


def pre_game_ends():
    global pre_game
    pre_game = False

screen.onkey(key='space', fun=pre_game_ends)

while pre_game:
    time.sleep(TIME_REFRESH)

    turtle_tuffy.write(f"{RULE_LINE}")

turtle_tuffy.clear()
for time_start in range(5, 0, -1):
    turtle_tuffy.write(f"{time_start}")
    time.sleep(1)
    turtle_tuffy.clear()
game_continues = True
big_game_continues = True
while big_game_continues:

    while game_continues:
        catch_turtle()
        time.sleep(TIME_REFRESH)
        if turtle_tom.chaser:
            turtle_tom.time_left -= TIME_REFRESH
        if turtle_jerry.chaser:
            turtle_jerry.time_left -= TIME_REFRESH
        if turtle_tom.time_left < 0 or turtle_jerry.time_left < 0:
            break
        turtle_tuffy.clear()
        turtle_tuffy.write(f"Jerry = {round(turtle_jerry.time_left, 1)}, Tom = {round(turtle_tom.time_left, 1)}")
        screen.update()
    turtle_tuffy.clear()
    if turtle_tom.time_left > turtle_jerry.time_left:
        turtle_tuffy.write(
            f"Jerry={round(turtle_jerry.time_left, 1)}, Tom={round(turtle_tom.time_left, 1)} \nTom wins!")
    else:
        turtle_tuffy.write(
            f"Jerry={round(turtle_jerry.time_left, 1)}, Tom={round(turtle_tom.time_left, 1)} \nJerry wins!")

    turtle_tuffy.goto(x=-100, y=-130)
    turtle_tuffy.write(f"Would you like to start a new game?\n")
    turtle_yes.showturtle()
    turtle_no.showturtle()
    screen.update()

    answer = input("Would you like to start a new game? \n")
    if answer == "yes":
        turtle_tom.time_left = TIME_DURATION
        turtle_jerry.time_left = TIME_DURATION
    else:
        big_game_continues = False
        exit(15)


screen.mainloop()
