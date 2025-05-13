from turtle import*
shape("turtle")
#making house
color("green")
width(7)
forward(200) #start of square
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200) #end of squeare
left(90)
forward(70) #start of door
left(90)
color("red")
forward(100)
right(90)
forward(70)
right(90)
forward(100) #end of door
penup()
left(180)
forward(200)
right(90)
begin_fill()
forward(60) #start of roof
pendown()
color("yellow")
left(135)
forward(160)
left(97)
forward(140) #end of roof
end_fill()
penup()
left(38)
forward(40)
left(90)
forward(25)

pendown()
color("purple")
left(90) #start of window
forward(20)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(40)

penup()
right(90) #start of 2window
forward(90)
pendown()
left(90)
forward(20)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(40)

exitonclick()