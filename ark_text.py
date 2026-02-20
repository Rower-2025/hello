import time
import os

# 文本版Pong游戏 - 人机对战

class PongGame:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.player_y = self.height // 2
        self.ai_y = self.height // 2
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = 1
        self.ball_dy = 1
        self.player_score = 0
        self.ai_score = 0
        self.paddle_height = 3
    
    def clear_screen(self):
        # 清除屏幕
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw(self):
        self.clear_screen()
        
        # 绘制顶部边界
        print('┌' + '─' * self.width + '┐')
        
        # 绘制游戏区域
        for y in range(self.height):
            line = '│'
            for x in range(self.width):
                # 绘制玩家 paddle
                if x == 1 and abs(y - self.player_y) <= self.paddle_height // 2:
                    line += '█'
                # 绘制AI paddle
                elif x == self.width - 2 and abs(y - self.ai_y) <= self.paddle_height // 2:
                    line += '█'
                # 绘制球
                elif x == self.ball_x and y == self.ball_y:
                    line += '●'
                else:
                    line += ' '
            line += '│'
            print(line)
        
        # 绘制底部边界
        print('└' + '─' * self.width + '┘')
        
        # 显示分数
        print(f'玩家: {self.player_score}  AI: {self.ai_score}')
        print('控制: W(上) S(下) Q(退出)')
    
    def move_player(self, key):
        if key == 'w' and self.player_y > self.paddle_height // 2:
            self.player_y -= 1
        elif key == 's' and self.player_y < self.height - 1 - self.paddle_height // 2:
            self.player_y += 1
    
    def move_ai(self):
        # 简单的AI逻辑
        if self.ball_y > self.ai_y + self.paddle_height // 2 and self.ai_y < self.height - 1 - self.paddle_height // 2:
            self.ai_y += 1
        elif self.ball_y < self.ai_y - self.paddle_height // 2 and self.ai_y > self.paddle_height // 2:
            self.ai_y -= 1
    
    def move_ball(self):
        # 移动球
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy
        
        # 边界碰撞检测 - 顶部和底部
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1
        
        # 边界碰撞检测 - 左侧和右侧
        if self.ball_x <= 0:
            # AI得分
            self.ai_score += 1
            self.reset_ball()
        elif self.ball_x >= self.width - 1:
            # 玩家得分
            self.player_score += 1
            self.reset_ball()
        
        # 球与paddle碰撞检测
        # 玩家 paddle
        if self.ball_x == 2 and abs(self.ball_y - self.player_y) <= self.paddle_height // 2:
            self.ball_dx *= -1
        # AI paddle
        elif self.ball_x == self.width - 3 and abs(self.ball_y - self.ai_y) <= self.paddle_height // 2:
            self.ball_dx *= -1
    
    def reset_ball(self):
        # 重置球的位置
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = 1 if self.ball_dx < 0 else -1
        self.ball_dy = 1 if self.ball_dy < 0 else -1
    
    def get_key(self):
        # 简单的键盘输入处理
        try:
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8').lower()
            return None
        except ImportError:
            # 在非Windows系统上使用备用方案
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                return ch.lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    def run(self):
        print('文本版Pong游戏 - 人机对战')
        print('按W键向上移动，S键向下移动，Q键退出')
        print('游戏即将开始...')
        time.sleep(1)
        
        while True:
            # 绘制游戏画面
            self.draw()
            
            # 获取键盘输入
            key = self.get_key()
            if key == 'q':
                break
            elif key in ['w', 's']:
                self.move_player(key)
            
            # AI移动
            self.move_ai()
            
            # 移动球
            self.move_ball()
            
            # 控制游戏速度
            time.sleep(0.1)
        
        print('游戏结束！')
        print(f'最终得分: 玩家 {self.player_score} - {self.ai_score} AI')

if __name__ == '__main__':
    game = PongGame()
    game.run()