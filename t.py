import turtle
import time

t5 = turtle.Turtle()
t5.hideturtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


t5.color("#188f36", "black")
t5.pensize(5)
t5.begin_fill()
l = [t1, t2, t3, t4]
for i in range(4):
    l[i].hideturtle()
    l[i].getscreen().bgcolor("#2c2e2d")
    l[i].color("#188f36")
    l[i].speed(0)
    l[i].pensize(5)

t1.penup()
t1.goto((0,200))
t1.pendown()
t3.penup()
t3.goto((0,-200))
t3.pendown()
t4.penup()
t4.goto((200,0))
t4.pendown()
t2.penup()
t2.goto((-200,0))
t2.pendown()
c = 0
d = 0
r = 0
while True:
    for x in range(4):
        for h in range(4):
            l[h].forward(50)
            l[h].right(90)
    for o in range(4):
        l[o].right(45)
    c+=1
    if c>=8:
        for x in range(4):
            l[x].color("#188f36")
        t1.penup()
        t1.setposition(100.00, 100.00)
        t1.pendown()
        t2.penup()
        t2.setposition(-100.00, 100.00)
        t2.pendown()
        t3.penup()
        t3.setposition(-100.00, -100.00)
        t3.pendown()
        t4.penup()
        t4.setposition(100.00, -100.00)
        t4.pendown()
        c = 0
        d +=1
        if d >=2:
            t1.penup()
            t1.setposition(0, 0)
            t1.pendown()
        r+=1
        if r>=3:
            break

t5.penup()
t5.setposition(0, 300)
t5.pendown()
t5.right(45)
for i in range(4):
    t5.forward(425)
    t5.right(90)
t5.end_fill()
turtle.done()