import turtle

# 简单的turtle测试
print("测试turtle模块...")

turtle.setup(width=400, height=300)
turtle.bgcolor("white")
turtle.title("Turtle测试")

# 绘制一个简单的图形
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

print("测试完成，请关闭窗口")

turtle.done()