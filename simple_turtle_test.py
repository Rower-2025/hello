import turtle
import time

print("启动turtle测试...")

# 创建一个简单的turtle窗口
turtle.setup(400, 300)
turtle.title("Turtle测试")
turtle.bgcolor("lightblue")

# 绘制一个简单的图形
t = turtle.Turtle()
t.color("red")
t.pensize(3)
t.speed(1)

print("绘制正方形...")
for i in range(4):
    t.forward(100)
    t.left(90)
    time.sleep(0.5)

print("绘制完成，点击窗口关闭...")

# 等待用户点击关闭
turtle.done()