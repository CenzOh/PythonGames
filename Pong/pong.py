# Pong in Python 3 Beginner
# Vincenzo Mezzio

import turtle  #for graphics, we could also use PyGame but this is simpler.
import os
import winsound # windows equivalent of making sound work

wn = turtle.Screen()
wn.title("Pong by Vincenzo")
wn.bgcolor("black") #background color
wn.setup(width=800, height=800)
wn.tracer(0) #stops window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(-100) #speed of animation
paddle_a.shape("square") #built in shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #def size is 20x20
paddle_a.penup() #no need to draw a line
paddle_a.goto(-350, 0) #0,0 is in the middle


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350, 0) 


# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square") 
ball.color("white")
ball.penup() 
ball.goto(0, 0) 

ball.dx = .15 #delta or change. For some reason ball will randomly speed up
ball.dy = .15 # this helps make the ball move slower. "It's not a bug, it's a feature"


# Pen
pen = turtle.Turtle()
pen.speed(0) #animation speed not movement
pen.color("white")
pen.penup() #dont draw a line
pen.hideturtle() #just see text
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    wn.update() #upddates the screen
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #starts at 0,0. Ball moves by 2 pixels
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay bounce.wav&") #this works for mac.
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC) #windows equivalent
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        
    if ball.xcor() > 390: # goes off right side
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        
    if ball.xcor() < -390: # goes off left side
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


        
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
       ball.setx(340)
       ball.dx *= -1
       winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
       
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
       ball.setx(-340)
       ball.dx *= -1
       winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
