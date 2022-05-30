import turtle
import random

s = turtle.Screen()
s.title("Turtle Race")
s.bgcolor("grey")

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.hideturtle()
t2.hideturtle()

t1.shape("turtle")
t1.color("green","green")
t1.shapesize(2,2,2)
t1.pensize(3)

t2.shape("turtle")
t2.color("blue","blue")
t2.shapesize(2,2,2)
t2.pensize(3)

t1.penup()
t1.goto(200,200)
t1.pendown()
t1.circle(35)

t2.penup()
t2.goto(200,-200)
t2.pendown()
t2.circle(35)

t1.penup()
t2.penup()
t1.goto(-250,225)
t2.goto(-250,-170)

t1.showturtle()
t2.showturtle()

dado = [1,2,3,4,5,6,0]

for i in range(20):
    if t1.pos() >= (200,200):
     print("Jugador1 Gana!")
     break
    elif t2.pos() >= (200,-200):
     print("Jugador2 Gana!")
     break
    else:
        turno1 = input("Jugador1 presione ENTER para continuar")
        turno1 = random.choice(dado)
        print("tu numero es;",turno1,"\nAvanzas: ",turno1*20)
        t1.pendown()
        t1.forward(turno1*20)

        turno2 = input("Jugador2 presione ENTER para continuar")
        turno2 = random.choice(dado)
        print("tu numero es;",turno2,"\nAvanzas: ",turno2*20)
        t2.pendown()
        t2.forward(20*turno2)


turtle.done()

