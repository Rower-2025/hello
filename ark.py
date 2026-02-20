# 导入必要的模块
import turtle  # 用于创建游戏窗口和图形元素
import time    # 用于控制游戏速度
import random  # 用于随机生成砖块颜色
import math    # 用于计算角度和三角函数

# 游戏常量定义
SCREEN_WIDTH = 800      # 游戏窗口宽度
SCREEN_HEIGHT = 600     # 游戏窗口高度
PADDLE_WIDTH = 20       # 玩家板子宽度
PADDLE_HEIGHT = 100     # 玩家板子高度
PADDLE_SPEED = 15       # 玩家板子移动速度
BALL_SIZE = 20          # 球的大小
BALL_SPEED = 4          # 球的初始速度
BRICK_WIDTH = 40        # 砖块宽度
BRICK_HEIGHT = 20        # 砖块高度
BRICK_GAP = 10          # 砖块之间的间隙
MAX_BOUNCE_ANGLE = 60    # 最大反弹角度（度）

# 确保turtle模块正常初始化
print("初始化打砖块游戏...")
print("使用Python版本:", __import__("sys").version)

# 设置游戏窗口
turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # 设置窗口大小
turtle.bgcolor("black")         # 设置背景颜色为黑色
turtle.title("打砖块游戏")      # 设置窗口标题
turtle.tracer(0)                # 关闭自动刷新，提高性能
turtle.update()                 # 手动刷新一次窗口

# 绘制游戏边界
border_pen = turtle.Turtle()     # 创建边界绘制的turtle对象
border_pen.speed(0)              # 设置绘制速度为最快
border_pen.color("white")        # 设置边界颜色为白色
border_pen.penup()               # 抬起画笔，移动时不绘制
border_pen.setposition(-SCREEN_WIDTH//2 + 10, -SCREEN_HEIGHT//2 + 10)  # 设置起始位置
border_pen.pendown()             # 放下画笔，开始绘制
border_pen.pensize(3)            # 设置画笔大小

# 绘制四边形边界
for side in range(4):
    if side % 2 == 0:
        border_pen.forward(SCREEN_WIDTH - 20)  # 绘制水平边
    else:
        border_pen.forward(SCREEN_HEIGHT - 20) # 绘制垂直边
    border_pen.left(90)  # 左转90度

border_pen.hideturtle()  # 隐藏边界绘制的turtle对象

# 初始化分数
score_a = 0  # 玩家得分
score_b = 0  # 未使用，保留用于扩展

# 绘制分数板
scoreboard = turtle.Turtle()     # 创建分数板的turtle对象
scoreboard.speed(0)              # 设置绘制速度为最快
scoreboard.color("white")        # 设置分数板颜色为白色
scoreboard.penup()               # 抬起画笔，移动时不绘制
scoreboard.hideturtle()          # 隐藏分数板的turtle对象
scoreboard.setposition(0, SCREEN_HEIGHT//2 - 40)  # 设置分数板位置
scoreboard.write("分数: 0", align="center", font=("Courier", 24, "normal"))  # 写入初始分数

# 创建玩家板子
paddle_a = turtle.Turtle()       # 创建玩家板子的turtle对象
paddle_a.speed(0)                # 设置绘制速度为最快
paddle_a.shape("square")         # 设置板子形状为正方形
paddle_a.color("white")          # 设置板子颜色为白色
# 调整板子大小
paddle_a.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=PADDLE_WIDTH/20)
paddle_a.penup()                 # 抬起画笔，移动时不绘制
# 设置板子初始位置（左侧）
paddle_a.setposition(-SCREEN_WIDTH//2 + 50, 0)

# 创建砖块数组
bricks = []  # 存储所有砖块的列表
brick_colors = ["red", "yellow"]  # 砖块颜色列表（红色和黄色）

# 计算可以铺满右侧的砖块数量
max_width = SCREEN_WIDTH // 2  # 右侧可用宽度（屏幕宽度的一半）
max_height = SCREEN_HEIGHT - 100  # 右侧可用高度（垂直方向，预留顶部空间）
brick_cols = max_width // (BRICK_WIDTH + BRICK_GAP)  # 计算列数
brick_rows = max_height // (BRICK_HEIGHT + BRICK_GAP)  # 计算行数

# 确保砖块数量不超过框架的一半
max_bricks = (max_width // (BRICK_WIDTH + BRICK_GAP)) * (max_height // (BRICK_HEIGHT + BRICK_GAP)) // 2
brick_cols = min(brick_cols, max_bricks // brick_rows)  # 调整列数，确保不超过最大砖块数

# 确保砖块铺满右侧竖着的一边
# 调整砖块位置，使其靠近右侧边界
start_x = SCREEN_WIDTH // 2 - BRICK_WIDTH - BRICK_GAP  # 起始X坐标

# 创建砖块
for row in range(brick_rows):  # 遍历每一行
    for col in range(brick_cols):  # 遍历每一列
        brick = turtle.Turtle()  # 创建砖块的turtle对象
        brick.speed(0)  # 设置绘制速度为最快
        brick.shape("square")  # 设置砖块形状为正方形
        # 随机选择砖块颜色
        brick.color(random.choice(brick_colors))  # 从颜色列表中随机选择
        # 调整砖块大小
        brick.shapesize(stretch_wid=BRICK_HEIGHT/20, stretch_len=BRICK_WIDTH/20)
        brick.penup()  # 抬起画笔，移动时不绘制
        # 计算砖块位置（右侧，从右向左排列）
        x = start_x - col * (BRICK_WIDTH + BRICK_GAP)  # 计算X坐标
        y = SCREEN_HEIGHT // 2 - 50 - row * (BRICK_HEIGHT + BRICK_GAP)  # 计算Y坐标
        brick.setposition(x, y)  # 设置砖块位置
        bricks.append(brick)  # 将砖块添加到列表中

# 创建球
ball = turtle.Turtle()  # 创建球的turtle对象
ball.speed(0)  # 设置绘制速度为最快
ball.shape("square")  # 设置球的形状为正方形
ball.color("white")  # 设置球的颜色为白色
# 调整球的大小
ball.shapesize(stretch_wid=BALL_SIZE/20, stretch_len=BALL_SIZE/20)
ball.penup()  # 抬起画笔，移动时不绘制
ball.setposition(0, 0)  # 设置球的初始位置（屏幕中心）

# 初始化球的速度
angle = random.uniform(-math.pi/4, math.pi/4)  # 随机生成初始角度（-45度到45度）
ball.dx = BALL_SPEED * math.cos(angle)  # 计算X方向速度分量
ball.dy = BALL_SPEED * math.sin(angle)  # 计算Y方向速度分量

# 玩家板子移动相关变量和函数
paddle_move_up = False  # 上键按下状态
paddle_move_down = False  # 下键按下状态

# 上键按下时调用的函数
def paddle_a_up():
    global paddle_move_up
    paddle_move_up = True  # 设置上键按下状态为True

# 下键按下时调用的函数
def paddle_a_down():
    global paddle_move_down
    paddle_move_down = True  # 设置下键按下状态为True

# 上键释放时调用的函数
def paddle_a_stop_up():
    global paddle_move_up
    paddle_move_up = False  # 设置上键按下状态为False

# 下键释放时调用的函数
def paddle_a_stop_down():
    global paddle_move_down
    paddle_move_down = False  # 设置下键按下状态为False

# 处理板子移动的函数
def update_paddle():
    # 如果上键被按下
    if paddle_move_up:
        y = paddle_a.ycor()  # 获取当前Y坐标
        y += PADDLE_SPEED  # 向上移动
        # 边界检查，防止板子超出屏幕
        if y > SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2:
            y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2
        paddle_a.sety(y)  # 更新板子位置
    
    # 如果下键被按下
    if paddle_move_down:
        y = paddle_a.ycor()  # 获取当前Y坐标
        y -= PADDLE_SPEED  # 向下移动
        # 边界检查，防止板子超出屏幕
        if y < -SCREEN_HEIGHT//2 + PADDLE_HEIGHT//2:
            y = -SCREEN_HEIGHT//2 + PADDLE_HEIGHT//2
        paddle_a.sety(y)  # 更新板子位置

# 移除AI移动逻辑，因为现在使用砖块代替AI

# 键盘绑定
turtle.listen()  # 开始监听键盘事件
turtle.onkeypress(paddle_a_up, "Up")  # 方向键向上（按下）时调用paddle_a_up函数
turtle.onkeypress(paddle_a_down, "Down")  # 方向键向下（按下）时调用paddle_a_down函数
turtle.onkeyrelease(paddle_a_stop_up, "Up")  # 方向键向上（释放）时调用paddle_a_stop_up函数
turtle.onkeyrelease(paddle_a_stop_down, "Down")  # 方向键向下（释放）时调用paddle_a_stop_down函数

# 主游戏循环
try:
    game_over = False  # 游戏结束标志
    while not game_over:  # 游戏主循环
        turtle.update()  # 手动刷新屏幕，提高性能
        
        # 移动球
        ball.setx(ball.xcor() + ball.dx)  # 更新球的X坐标
        ball.sety(ball.ycor() + ball.dy)  # 更新球的Y坐标
        
        # 更新板子位置（支持长按移动）
        update_paddle()  # 调用update_paddle函数更新板子位置
        
        # 移除AI移动，因为现在使用砖块代替AI
        
        # 边界碰撞检测 - 顶部和底部
        if ball.ycor() > SCREEN_HEIGHT//2 - 10:  # 球碰到顶部边界
            ball.sety(SCREEN_HEIGHT//2 - 10)  # 重置球的Y坐标
            ball.dy *= -1  # 反转Y方向速度，实现反弹
        
        if ball.ycor() < -SCREEN_HEIGHT//2 + 10:  # 球碰到底部边界
            ball.sety(-SCREEN_HEIGHT//2 + 10)  # 重置球的Y坐标
            ball.dy *= -1  # 反转Y方向速度，实现反弹
        
        # 边界碰撞检测 - 左侧和右侧
        if ball.xcor() > SCREEN_WIDTH//2 - 10:  # 球碰到右侧边界
            ball.goto(0, 0)  # 重置球的位置到屏幕中心
            ball.dx *= -1  # 反转X方向速度
        
        if ball.xcor() < -SCREEN_WIDTH//2 + 10:  # 球碰到左侧边界（玩家这边）
            # 球触碰玩家这边的边界，游戏结束
            game_over = True  # 设置游戏结束标志
            break  # 跳出游戏主循环
        
        # 球与砖块碰撞检测
        brick_hit = False  # 砖块被击中标志
        for brick in bricks[:]:  # 使用切片创建副本，避免遍历过程中修改列表
            brick_x = brick.xcor()  # 获取砖块的X坐标
            brick_y = brick.ycor()  # 获取砖块的Y坐标
            
            # 检查球是否与砖块碰撞
            if (brick_x - BRICK_WIDTH/2 < ball.xcor() < brick_x + BRICK_WIDTH/2) and \
               (brick_y - BRICK_HEIGHT/2 < ball.ycor() < brick_y + BRICK_HEIGHT/2):
                # 反射式反弹
                # 计算碰撞点相对于砖块中心的位置
                collision_x = ball.xcor() - brick_x  # 碰撞点X方向偏移
                collision_y = ball.ycor() - brick_y  # 碰撞点Y方向偏移
                
                # 计算碰撞的法向量，确定碰撞类型
                if abs(collision_x) > abs(collision_y):
                    # 水平碰撞（球从左右两侧击中砖块）
                    ball.dx *= -1  # 反转X方向速度
                else:
                    # 垂直碰撞（球从上下两侧击中砖块）
                    ball.dy *= -1  # 反转Y方向速度
                
                # 确保球向左侧反弹（朝向玩家）
                if ball.dx > 0:
                    ball.dx *= -1  # 如果球向右移动，则反转方向
                
                # 根据砖块颜色得分
                brick_color = brick.color()[0]  # 获取砖块颜色
                if brick_color == "red":
                    score_a += 1  # 红色砖块得1分
                elif brick_color == "yellow":
                    score_a += 2  # 黄色砖块得2分
                
                # 更新分数板
                scoreboard.clear()  # 清除旧分数
                scoreboard.write(f"分数: {score_a}", align="center", font=("Courier", 24, "normal"))  # 写入新分数
                
                # 移除被击中的砖块
                brick.hideturtle()  # 隐藏砖块
                bricks.remove(brick)  # 从列表中移除砖块
                brick_hit = True  # 设置砖块被击中标志
                break  # 跳出循环，处理下一个球的位置
        
        # 左侧板子（玩家）碰撞检测 - 反射式反弹
        paddle_x = paddle_a.xcor()  # 获取板子的X坐标
        paddle_y = paddle_a.ycor()  # 获取板子的Y坐标
        ball_x = ball.xcor()        # 获取球的X坐标
        ball_y = ball.ycor()        # 获取球的Y坐标
        
        # 检查球是否与板子碰撞
        if (ball_x < paddle_x + PADDLE_WIDTH/2 and ball_x > paddle_x - PADDLE_WIDTH/2) and \
           (ball_y < paddle_y + PADDLE_HEIGHT/2 and ball_y > paddle_y - PADDLE_HEIGHT/2):
            ball.setx(paddle_x + PADDLE_WIDTH/2)  # 重置球的X坐标，避免卡在板子内
            
            # 反射式反弹
            # 计算碰撞点相对于板子中心的位置（归一化到-1到1之间）
            relative_intersect_y = (ball_y - paddle_y) / (PADDLE_HEIGHT/2)
            
            # 计算反弹角度（范围：-MAX_BOUNCE_ANGLE度到MAX_BOUNCE_ANGLE度）
            bounce_angle = relative_intersect_y * MAX_BOUNCE_ANGLE
            
            # 计算新的速度方向
            angle_rad = math.radians(bounce_angle)  # 将角度转换为弧度
            speed = math.sqrt(ball.dx**2 + ball.dy**2)  # 计算球的当前速度大小
            ball.dx = speed * math.cos(angle_rad)  # 计算新的X方向速度分量
            ball.dy = speed * math.sin(angle_rad)  # 计算新的Y方向速度分量
        
        # 小延迟，使游戏速度适中
        time.sleep(0.01)  # 控制游戏帧率，避免速度过快
    
    # 游戏结束，显示结算信息
    if game_over:
        # 隐藏球和板子
        ball.hideturtle()      # 隐藏球
        paddle_a.hideturtle()  # 隐藏板子
        
        # 隐藏所有剩余的砖块
        for brick in bricks:
            brick.hideturtle()  # 隐藏每一个剩余的砖块
        
        # 显示游戏结束和最终得分
        game_over_text = turtle.Turtle()  # 创建游戏结束文本的turtle对象
        game_over_text.speed(0)           # 设置绘制速度为最快
        game_over_text.color("white")     # 设置文本颜色为白色
        game_over_text.penup()            # 抬起画笔，移动时不绘制
        game_over_text.hideturtle()       # 隐藏文本的turtle对象
        game_over_text.setposition(0, 0)   # 设置文本位置
        game_over_text.write(f"游戏结束！\n最终得分: {score_a}", align="center", font=("Courier", 36, "normal"))  # 写入游戏结束信息和最终得分
        
        # 显示操作说明
        instruction_text = turtle.Turtle()  # 创建操作说明文本的turtle对象
        instruction_text.speed(0)           # 设置绘制速度为最快
        instruction_text.color("white")     # 设置文本颜色为白色
        instruction_text.penup()            # 抬起画笔，移动时不绘制
        instruction_text.hideturtle()       # 隐藏文本的turtle对象
        instruction_text.setposition(0, -100)  # 设置文本位置
        instruction_text.write("操作说明:\n长按方向键↑↓移动板子\n红色砖块得1分，黄色砖块得2分", align="center", font=("Courier", 16, "normal"))  # 写入操作说明
        
        # 等待用户点击关闭
        turtle.done()  # 进入turtle主循环，等待用户交互

except turtle.Terminator:
    # 处理窗口关闭时的异常
    pass  # 静默处理异常，避免程序崩溃