# Pong Game
import turtle as t

# Board
board = t.Screen()
board.title("Pong by Pat and Rik")
board.bgcolor("gray")
board.setup(width=1000, height=600)
board.tracer(0)

# Left Block
lb = t.Turtle()
lb.speed(0)
lb.shape(name="square")
lb.color("black")
lb.resizemode("user")
lb.shapesize(stretch_wid=5, stretch_len=1)
lb.penup()
lb.goto(-490, 0)

# Right Block
rb = t.Turtle()
rb.shape(name="square")
rb.resizemode("user")
rb.color("black")
rb.shapesize(stretch_wid=5, stretch_len=1)
rb.penup()
rb.goto(480, 0)

# Ball
ball = t.Turtle()
ball.shape(name="circle")
ball.color("white")
ball.penup()
ball.dx = 2
ball.dy = 2

# Scoreboard
score1 = 0
score2 = 0

pen = t.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player1:"+str(score1)+"  Player2:"+str(score2), align= "center", font=("Courier", 24, "normal"))

# Movement methods
def resetball():
  ball.setposition(0,0)
    
def rup():
  y= rb.ycor()
  y+=30
  rb.sety(y)

def rdow():
  y= rb.ycor()
  y-=30
  rb.sety(y)

def lup():
  y= lb.ycor()
  y+=30
  lb.sety(y)

def ldow():
  y= lb.ycor()
  y-=30
  lb.sety(y)


# Key Bindings
board.listen()
board.onkeypress(lup, "w")
board.onkeypress(ldow, "s")
board.onkeypress(rup, "Up")
board.onkeypress(rdow, "Down")
board.onkeypress(resetball, "f")

# Gameplay algorithm
while True:
  board.update()

  xe = ball.xcor() + ball.dx
  ye = ball.ycor() + ball.dy
  ball.setposition(xe, ye)

  if ball.ycor() > 390:
    ball.sety(390)
    ball.dy*=-1

  if ball.ycor() < -390:
    ball.sety(-390)
    ball.dy*=-1

  if ball.xcor() > 490:
    ball.setx(490)
    ball.dx*=-1
    score1+=1
    pen.clear()
    pen.write("Player1:"+str(score1)+"  Player2:"+str(score2), align= "center", font=("Courier", 24, "normal"))
                

  if ball.xcor() < -490:
    ball.setx(-490)
    ball.dx*=-1
    score2+=1
    pen.clear()
    pen.write("Player1:"+str(score1)+"  Player2:"+str(score2), align= "center", font=("Courier", 24, "normal"))



  if ball.xcor()> 460 and ball.xcor()< 490 and (ball.ycor() < rb.ycor()+50 and ball.ycor()> rb.ycor()-50):
    ball.dx*=-1
            

  if ball.xcor()< -460 and ball.xcor()> -490 and (ball.ycor()< lb.ycor()+ 50 and ball.ycor()> lb.ycor()-50):
    ball.dx*=-1