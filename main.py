from turtle import Turtle, Screen
import random
is_race_on = False
turtle_colors = ["red", "blue", "green", "yellow","purple", "orange"]
screen = Screen()
user_bet = screen.textinput(title="Make your Bet", prompt="Enter the color")
screen.setup(width=360, height=400)
y = -100
turtles = []
for colors in turtle_colors:
  t = Turtle(shape="turtle")
  t.penup()
  t.speed(1)
  t.color(colors)
  y += 30
  print(y)
  t.goto(-160, y)
  turtles.append(t)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in turtles:
    if turtle.xcor() > 160:
      is_race_on = False
      winner = turtle.pencolor()
      if user_bet == winner:
        print(f"You've won!! The {winner} turtle won the race")
      else:
        print(f"You've lost!! The {winner} turtle won the race")
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
screen.exitonclick()