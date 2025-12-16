import turtle
import time
import os
import sys
import time as t
import random as r
import winsound
def startto():
    python = sys.executable
    os.execl(python, python, *sys.argv)
# 设置屏幕
wn = turtle.Screen()
wn.title("打砖块游戏")
wn.bgcolor("black")
wn.setup(width=1600, height=800)
wn.tracer(0)

# 挡板
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# 球
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.5
ball.dy = -3.5

# 砖块
bricks = []
colors = ["red", "orange", "yellow", "green", "blue","purple","white"]
for i in range(7):
    for j in range(20):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-700 + j * 70, 200 - i * 30)
        bricks.append(brick)
# 分数
life=10
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-120,260)
pen.write("生命: 10", align="center", font=("Courier", 24, "normal"))
pen.goto(120, 260)
pen.write("分数: 0", align="center", font=("Courier", 24, "normal"))

# 移动挡板
def paddle_right():
    x = paddle.xcor()
    if x < 780:
        x += 60
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -780:
        x -= 60
    paddle.setx(x)

# 键盘绑定
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# 主游戏循环
while True:
    if brick==[]:
        pen.write("YOU WIN")
        break
    wn.update()
    
    # 移动球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # 边界检查
    if ball.xcor() > 770:
        ball.setx(750)
        ball.dx *= -1
    
    if ball.xcor() < -770:
        ball.setx(-750)
        ball.dx *= -1
    
    if ball.ycor() > 400:
        ball.sety(380)
        ball.dy *= -1
    
    if ball.ycor() < -450:
        ball.goto(0, 0)
        ball.dy +=10
        ball.dy +=-10
        pen.clear()
        life-=1
        pen.goto(-120, 260)
        pen.write("生命: {}".format(life), align="center", font=("Courier", 24, "normal"))
        pen.goto(120, 260)
        pen.write("分数: {}".format(score), align="center", font=("Courier", 24, "normal"))

        if life==0:
            pen.clear()
            pen.goto(350,0)
            pen.write("GAME OVER",align="right",font=("Courier", 100, "bold"))
            t.sleep(3)
            startto()            
    # 挡板碰撞
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 100 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1
    
    # 砖块碰撞
    for brick in bricks[:]:
        if (ball.ycor() > brick.ycor() - 22 and ball.ycor() < brick.ycor() + 22) and (ball.xcor() > brick.xcor() - 35 and ball.xcor() < brick.xcor() + 35):
            brick.goto(1000, 1000)  # 移出屏幕
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            pen.clear()
            pen.goto(120, 260)
            pen.write("分数: {}".format(score), align="center", font=("Courier", 24, "normal"))
            pen.goto(-120, 260)
            pen.write("生命: {}".format(life), align="center", font=("Courier", 24, "normal"))
    time.sleep(0.01)
