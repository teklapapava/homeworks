from turtle import*


#we want to paint a house 
#step 1: draw a square
#speed(60)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of the square

#draw a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door

# drawing a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing a window

color("purple")
penup()
goto(0, 70)
pendown()
left(120)
color("brown")
begin_fill()
forward(30)
left(90)
forward(50)
left(90)
forward(30)
end_fill()

penup()
goto(200, 70)
pendown()
begin_fill()
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()

#end of windows



exitonclick()