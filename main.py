import turtle
#import winsound

abi = turtle.Screen()
abi.title("BALL AND PADDLE by @Rosary")
abi.bgcolor("#C39BD3")
abi.setup(width=800, height=600)
abi.tracer(0)


# score
score = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("#2980B9")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(-350, -250)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
#pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("courier", 24, "bold"))

# Function


def paddle_move_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


def paddle_move_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


# key
abi.listen()
abi.onkeypress(paddle_move_right, "Right")
abi.onkeypress(paddle_move_left, "Left")

# Loop
while True:
    abi.update()

    # ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score -= 10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("courier", 24, "bold"))


    # Paddle and ball
    if(ball.ycor() < -240) and (ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 40) and (ball.xcor() > paddle.xcor() - 40):
        ball.sety(-240)
        ball.dy *= -1
        score += 10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("courier", 24, "bold"))
        #winsound.PlaySound("sound.mp3", winsound.SND_ASYNC)

    if score > 50:
        paddle.shapesize(stretch_len=4.5, stretch_wid=1)

    if score > 100:
        paddle.shapesize(stretch_len=4, stretch_wid=1)

    if score < -50:
        exit()