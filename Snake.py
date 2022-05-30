
from tkinter import font
import turtle
import time
import random

retraso = 0.1
score = 0
high_score = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Snake")

snake = turtle.Turtle()
snake.speed(3)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
snake.color("green")

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.speed(0)

body = []

text = turtle.Turtle()
text.speed(0)
text.color("black")
text.penup()
text.hideturtle()
text.goto(0,-260)
text.write("Score: 0\tHigh Score: 0",align="center",font=("verdana",24,"normal"))



def arriba():
    snake.direction = "up"
def abajo():
    snake.direction = "down"
def izq():
    snake.direction = "left"
def dcha():
    snake.direction = "right"
def movimiento():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(dcha,"Right")
s.onkeypress(izq,"Left")


while True:
    s.update()

    if snake.xcor() > 300 or snake.ycor() < -300 or snake.xcor() < -300 or snake.ycor() > 300:
        time.sleep(1)
        for i in body:
          i.clear()
          i.hideturtle()
        snake.home()
        snake.direction = "stop"
        body.clear()
        score = 0
        text.clear()
        text.write("Score: {}\tHigh Score: {}".format(score,high_score),align="center",font=("verdana",24,"normal"))

    if snake.distance(food) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        newfood = turtle.Turtle()
        newfood.shape("square")
        newfood.color("green")
        newfood.penup()
        newfood.goto(0,0)
        newfood.speed(0)
        body.append(newfood)

        score += 10
        if score > high_score:
            high_score = score
            text.clear()
            text.write("Score: {}\tHigh Score: {}".format(score,high_score),align="center",font=("verdana",24,"normal"))

  
    total = len(body)
    for i in range(total-1,0,-1):
      x = body[i-1].xcor()
      y = body[i-1].ycor()
      body[i].goto(x,y)
 
    if total > 0:
     x = snake.xcor()
     y = snake.ycor()
     body [0].goto(x,y)

    movimiento()

    for i in body:
        if i.distance(snake) < 20:
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            snake.direction = "stop"
            score = 0
            text.clear()
            text.write("Score: {}\tHigh Score: {}".format(score,high_score),align="center",font=("verdana",24,"normal"))


    time.sleep(retraso)


turtle.done()