# Pong Class
import turtle as t

class pong:
  # Pat
  def left_block(self):
    lb = t.Turtle()
    lb.speed(0)
    lb.shape("square")
    lb.color("black")
    lb.shapesize(stretch_wid=4, stretch_len=2)
    lb.penup()
    lb.goto(-400, 0)

  #Rik
  #def right_block(self):

  #Pat
  #def ball(self):
  
  #Pat
  def board(self):
    board = t.Screen()
    board.title("Pong by Pat and Rik")
    board.bgcolor("gray")
    board.setup(width=1000, height=600)
    board.update()

  def play(self):
    while True:
        self.board()
        self.left_block()

pong = pong()
pong.play()