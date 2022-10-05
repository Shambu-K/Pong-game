#Classic Pong game by Shambu-K

from logging.config import listen
import turtle
import os

window =  turtle.Screen()
window.title(" PONG Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle User A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle User B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.moveX = 0.06
ball.moveY = 0.06

#Pen for Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Vendana", 24, "normal"))

#Functions
def paddle_a_moveUp():
    y = paddle_a.ycor()
    y+= 40
    paddle_a.sety(y)

def paddle_a_moveDown():
    y = paddle_a.ycor()
    y-= 40
    paddle_a.sety(y)

def paddle_b_moveUp():
    y = paddle_b.ycor()
    y+= 40
    paddle_b.sety(y)

def paddle_b_moveDown():
    y = paddle_b.ycor()
    y-= 40
    paddle_b.sety(y)



#Key Binds
window.listen()
window.onkey(paddle_a_moveUp, "w")
window.onkey(paddle_a_moveDown, "s")
window.onkey(paddle_b_moveUp, "Up")
window.onkey(paddle_b_moveDown, "Down")





#Game loop
while True:
    window.update()

    #Ball Movement
    ball.setx(ball.xcor() + ball.moveX)
    ball.sety(ball.ycor() + ball.moveY)

    #Border Checking
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.moveY*= -1
        os.system("aplay bounce.wav&")


    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.moveY*= -1
        os.system("aplay bounce.wav&")

    
    if(ball.xcor() > 390):
        ball.goto(0,0)
        ball.moveX*= -1
        os.system("aplay beat.wav&")
        score_a+= 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Vendana", 24, "normal"))
        
    
    if(ball.xcor() < -390):
        ball.goto(0,0)
        ball.moveX*= -1
        os.system("aplay beat.wav&")
        score_b+= 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Vendana", 24, "normal"))


    #Paddle and ball bounce/collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.moveX*= -1
        os.system("aplay bounce.wav&")

        


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.moveX*= -1
        os.system("aplay bounce.wav&")

    #result
    if(score_a == 1):
        os.system("aplay victory.wav&")
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player A wins", align = "center", font = ("Comic Sans", 40, "normal"))
        window.exitonclick()

    if(score_b == 1):
        os.system("aplay victory.wav&")
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player B wins", align = "center", font = ("Comic Sans", 40, "normal"))
        window.exitonclick()

    

        



