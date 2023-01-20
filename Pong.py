# Pong Game
# Authors: Pat and Rik
#  Turtle allows to create simple graphics
#  Allows to create simple games
import turtle as t

class pong:
  def start(self):
    def button(x, y):
      if 0 < x < 91 and 0 > y > -91:
        t.clearscreen()
        self.play()

    # Screen
    screen = t.Screen()
    screen.title("Pong Game")
    screen.bgcolor("gray")
    screen.setup(width=1000, height=600)
    screen.tracer(0)

    # Start button
    pen = t.Turtle()
    pen.speed(0)

    pen.forward(90)
    pen.left(90)

    pen.penup()
    pen.goto(8, -46)
    pen.write("Start", font=("Courier", 24, "normal" ))

    t.onscreenclick(button, 1)
    t.listen()
    t.done()

  def play(self):
    # Board
    # -Creates game board w/ specific characteristics
    board = t.Screen()
    board.title("Pong by Pat and Rik")
    board.bgcolor("gray")
    board.setup(width=800, height=600)
    board.tracer(0)

    # Left Block
    # -Creates left block
    lb = t.Turtle()
    lb.speed(0)
    lb.shape(name="square")
    lb.color("black")
    lb.resizemode("user")
    lb.shapesize(stretch_wid=5, stretch_len=1)
    lb.penup()
    lb.goto(-350, 0)

    # Right Block
    # -Creates right block
    rb = t.Turtle()
    rb.speed(0)
    rb.shape(name="square")
    rb.resizemode("user")
    rb.color("black")
    rb.shapesize(stretch_wid=5, stretch_len=1)
    rb.penup()
    rb.goto(350, 0)

    # Ball
    # -Creates ball object
    ball = t.Turtle()
    ball.shape(name="circle")
    ball.color("blue")
    ball.penup()
    ball.dx = 2
    ball.dy = 2

    # Scoreboard
    # -Creates the score tracker
    score1 = 0
    score2 = 0

    pen = t.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Player 1:" + str(score1) + "  Player2:" + str(score2), align= "center", font = ("Comic Sans", 24, "normal"))
    
    # Movement methods
    # Resets ball into initial position
    def resetball():
      ball.setposition(0,0)
    
    # Method to move up for right block
    def rup():
      y = rb.ycor()
      y += 30
      rb.sety(y)

    # Method to move down for left block
    def rdow():
      y = rb.ycor()
      y -= 30
      rb.sety(y)

    # Method to move up for left block
    def lup( ):
      y= lb.ycor()
      y += 30
      lb.sety(y)

    # Method to move down for left block
    def ldow():
      y = lb.ycor()
      y -= 30
      lb.sety(y)

    # Key Bindings
    # Left Block Controls: w - up, s - down
    # Right Block Controls: up arrow - up, down arrow - down
    board.listen()
    board.onkeypress(lup, "w")
    board.onkeypress(ldow, "s")
    board.onkeypress(rup, "Up")
    board.onkeypress(rdow, "Down")
    board.onkeypress(resetball, "f")

    # Gameplay algorithm
    while True:
      # Updates screen w/ each iteration of loop
      board.update()

      ball.setx(ball.xcor() + ball.dx)
      ball.sety(ball.ycor() + ball.dy)
      # Top Border
      if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

      # Bottom border
      elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
      
      # Right border
      if ball.xcor() > 390:
        resetball()
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player1:"+str(score1)+"  Player2:"+str(score2), align= "center", font=("Courier", 24, "normal"))
                
      # Left border
      elif ball.xcor() < -390:
        resetball()
        ball.dx *=- 1
        score2 += 1
        pen.clear()
        pen.write("Player 1:" + str(score1)+ "  Player 2:" + str(score2), align= "center", font=("Courier", 24, "normal"))
      
      # Collisions
      if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rb.ycor() + 40 and ball.ycor() > rb.ycor() - 40):
        ball.setx(340)
        ball.dx*=-1
            

      if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< lb.ycor() + 40 and ball.ycor() > lb.ycor() - 40):
        ball.setx(-340)
        ball.dx*=-1
  
def main():
  game = pong()
  game.start()

if __name__ == "__main__":
  main()