from turtle import Turtle,Screen
game_on=True
window=Screen()
window.setup(1000,800)
window.bgcolor("black")
window.title("Tutle Race")
colors=["red","green","blue"]
while game_on:
 color=window.textinput("Guess the winner","Type a color: Red,Blue or Green?")
 if color:
  color=color.lower()


 if color in colors:
  sam=Turtle()
  sam.shape("turtle")
  sam.penup()
  sam.color("green")
  sam.goto(-400,0)

  tom=Turtle()
  tom.shape("turtle")
  tom.penup()
  tom.color("blue")
  tom.goto(-400,300)

  turbo=Turtle()
  turbo.shape("turtle")
  turbo.penup()
  turbo.color("red")
  turbo.goto(-400,-300)


  def race(turtle):
   import random
   turtle.speed("fast")
   for _ in range(1):
    turtle.forward(random.randint(1,10))
  while sam.xcor()<380 or tom.xcor()<380 or turbo.xcor()<380:
   race(sam)
   race(tom)
   race(turbo)
  if sam.xcor()>tom.xcor() and sam.xcor()>turbo.xcor():
   wining_color="green"
  elif tom.xcor()>sam.xcor() and tom.xcor()>turbo.xcor():
   wining_color="blue"
  else:
   wining_color="red"
  if color==wining_color:
    window.clear()
    window.bgcolor("black")
    message=Turtle()
    message.color("white")
    message.hideturtle()
    message.write("You win !",font=("arial",30,'bold'),align="center")
    window.exitonclick()
  else:
     window.clear()
     window.bgcolor("black")
     message=Turtle()
     message.color("white")
     message.hideturtle()
     message.write("You lose !",font=("arial",30,'bold'),align="center")
     window.exitonclick()
