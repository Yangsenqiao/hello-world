import turtle 
turtle.screensize(400,300,"yellow")
R=150
turtle.pensize(3)
turtle.pencolor('black')
turtle.speed(10)
TJT_color={1:'white',-1:'black'}
corlor_list=[1,-1]
for c in corlor_list:
    turtle.fillcolor(TJT_color.get(c))
    turtle.begin_fill()
    turtle.circle(R/2,180)
    turtle.circle(R,180)
    turtle.circle(R/2,-180)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,R/3*c)
    turtle.pendown()
    turtle.fillcolor(TJT_color.get(-c))
    turtle.begin_fill()
    turtle.circle(-R/6,360)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
