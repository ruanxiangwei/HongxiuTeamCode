import turtle
turtle.setup(600,400)
turtle.penup()
turtle.goto(-180,-80)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('black')
turtle.seth(-20)
turtle.circle(500,40)
turtle.seth(110)
turtle.circle(182,140)
turtle.seth(150)
for i in range(4):
    turtle.circle(-35,143)
    turtle.circle(19,110)
turtle.circle(-35,135)
turtle.left(5)
turtle.circle(19,100)
turtle.circle(-26.5,150)

turtle.penup()
turtle.goto(-149,-9)
turtle.pendown()
turtle.seth(-40)
turtle.fd(5)

turtle.penup()
turtle.goto(-83,52)
turtle.pendown()
turtle.seth(-67)
turtle.fd(20)

turtle.penup()
turtle.goto(2,70)
turtle.pendown()
turtle.seth(-97)
turtle.fd(24)

turtle.penup()
turtle.goto(83,42)
turtle.pendown()
turtle.seth(-120)
turtle.fd(15)

turtle.penup()
turtle.goto(145,-24)
turtle.pendown()
turtle.seth(-155)
turtle.fd(5)

turtle.penup()
turtle.pensize(12)
turtle.goto(-45,-20)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.goto(40,-20)
turtle.pendown()
turtle.dot()

turtle.penup()
turtle.pensize(5)
turtle.goto(-25,-50)
turtle.seth(5)
turtle.pendown()
turtle.fd(47)

turtle.penup()
turtle.goto(-25,-50)
turtle.seth(-85)
turtle.pendown()
turtle.circle(25,175)

turtle.penup()
turtle.pensize(20)
turtle.pencolor('pink')
turtle.goto(-60,-50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.goto(58,-49)
turtle.pendown()
turtle.dot()

turtle.penup()
turtle.goto(-200,300)
turtle.done()