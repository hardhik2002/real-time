from turtle import *
hideturtle()
bgcolor("black")
color("red")
begin_fill()
fillcolor("red")
left(140)
forward(180)
circle(-90, 200)
setheading(60)
circle(-90, 200)
forward(180)
end_fill()
penup()
goto(0,-100)
pendown()

color("red")
style=("Arial",30,"italic")
write("I Love you",font=style,align="center")
done()
