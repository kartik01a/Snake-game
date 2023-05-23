import os
import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game By Kartik")
wn.bgcolor("green")
wn.setup(width=600,height=600)

wn.tracer(0)

head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = ("stop")

food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

body = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0    Highscore: 0" , align = "center", font = ("courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up, "8")
wn.onkeypress(go_down, "2")
wn.onkeypress(go_left, "4")
wn.onkeypress(go_right, "6")

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for rest_body in body:
            rest_body.goto(1000,1000)

        body.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}    Highscore: {}".format(score, high_score) , align = "center", font = ("courier", 24, "normal"))
    

    if head.distance(food)<20:
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
        food.goto(x,y)
        
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        body.append(new_body)
    
        delay -= 0.001
        score += 10

        if score>high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}    Highscore: {}".format(score, high_score) , align = "center", font = ("courier", 24, "normal"))

    for index in range(len(body)-1, 0 ,-1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x,y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()

    for rest_body in body:
        if rest_body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for rest_body in body:
                rest_body.goto(1000,1000)

            body.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}    Highscore: {}".format(score, high_score) , align = "center", font = ("courier", 24, "normal"))
    
    time.sleep(delay)

wn.mainloop()