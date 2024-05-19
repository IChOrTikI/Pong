import random
import tkinter as tk
import sys

class PongGame:
    def __init__(self, master, name_player_1='Player 1', name_player_2='Player 2'):
        self.master = master
        self.name1 = name_player_1
        self.name2 = name_player_2
        
        self.canvas = tk.Canvas(self.master, width=900, height=500)

        # Добавляем изображение на фон
        self.background_image = tk.PhotoImage(file="wallpaper.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        self.canvas.pack()

        self.paddle_a = self.canvas.create_rectangle(0, 50, 10, 150, fill='blue')
        self.paddle_b = self.canvas.create_rectangle(892, 50, 902, 150, fill='red')

        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')

        self.score_player_1 = 0
        self.score_player_2 = 0
        self.game_over = False

        self.paddle_a_speed = 0
        self.paddle_b_speed = 0

        self.ball_speed_x = 3
        self.ball_speed_y = 3

        self.master.bind('<KeyPress-w>', self.start_move_paddle_a_up)
        self.master.bind('<KeyRelease-w>', self.stop_move_paddle_a)
        self.master.bind('<KeyPress-s>', self.start_move_paddle_a_down)
        self.master.bind('<KeyRelease-s>', self.stop_move_paddle_a)
        self.master.bind('<Up>', self.start_move_paddle_b_up)
        self.master.bind('<Down>', self.start_move_paddle_b_down)
        self.master.bind('<KeyRelease-Up>', self.stop_move_paddle_b)
        self.master.bind('<KeyRelease-Down>', self.stop_move_paddle_b)

        self.update()

    def start_move_paddle_a_up(self, event):
        self.paddle_a_speed = -3

    def start_move_paddle_a_down(self, event):
        self.paddle_a_speed = 3

    def start_move_paddle_b_up(self, event):
        self.paddle_b_speed = -3

    def start_move_paddle_b_down(self, event):
        self.paddle_b_speed = 3

    def stop_move_paddle_a(self, event):
        self.paddle_a_speed = 0

    def stop_move_paddle_b(self, event):
        self.paddle_b_speed = 0

    def update(self):
        self.show_scores()

        self.move_paddles()
        self.move_ball()

        if not self.game_over:
            self.master.after(10, self.update)

    def show_scores(self):
        self.canvas.delete("score")
        message_player_1 = f'{self.name1}: {self.score_player_1}'
        message_player_2 = f'{self.name2}: {self.score_player_2}'
        self.canvas.create_text(150, 30, text=message_player_1, font=('Arial', 10), fill='white', tag="score")
        self.canvas.create_text(750, 30, text=message_player_2, font=('Arial', 10), fill='white', tag="score")

    def move_paddles(self):
        for paddle, speed in [(self.paddle_a, self.paddle_a_speed), (self.paddle_b, self.paddle_b_speed)]:
            paddle_pos = self.canvas.coords(paddle)
            if speed < 0:  # Moving up
                if paddle_pos[1] + speed >= 0:  # Check if moving won't go beyond top boundary
                    self.canvas.move(paddle, 0, speed)
                else:
                    self.canvas.move(paddle, 0, -paddle_pos[1])  # Stop at the top boundary
            elif speed > 0:  # Moving down
                if paddle_pos[3] + speed <= 500:  # Check if moving won't go beyond bottom boundary
                    self.canvas.move(paddle, 0, speed)
                else:
                    self.canvas.move(paddle, 0, 500 - paddle_pos[3])  # Stop at the bottom boundary

    def move_ball(self):

        if self.score_player_1 == 2:
            self.change_paddle_color_level1(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 2:
            self.change_paddle_color_level1(self.paddle_b, 'player_2_color')
        if self.score_player_1 == 5:
            self.change_paddle_color_level2(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 5:
            self.change_paddle_color_level2(self.paddle_b, 'player_2_color')
        if self.score_player_1 == 10:
            self.change_paddle_color_level3(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 10:
            self.change_paddle_color_level3(self.paddle_b, 'player_2_color')
        if self.score_player_1 == 14:
            self.change_paddle_color_level4(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 14:
            self.change_paddle_color_level4(self.paddle_b, 'player_2_color')

        if not self.game_over:
            if self.score_player_1 >= 15:
                self.game_over = True
                self.display_winner(self.name1)
            elif self.score_player_2 >= 15:
                self.game_over = True
                self.display_winner(self.name2)

        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        ball_pos = self.canvas.coords(self.ball)

        if ball_pos[1] <= 0 or ball_pos[3] >= 500:
            self.ball_speed_y = -self.ball_speed_y

        if ball_pos[0] <= 0:
            self.score_player_2 += 1
            self.reset_ball()
        elif ball_pos[2] >= 900:
            self.score_player_1 += 1
            self.reset_ball()

        if self.check_collision(ball_pos, self.paddle_a) or self.check_collision(ball_pos, self.paddle_b):
            number = random.randint(1, 5)
            if number == 4:
                self.ball_speed_y = -self.ball_speed_y
            self.ball_speed_x = -self.ball_speed_x

    def check_collision(self, ball_pos, paddle):
        paddle_pos = self.canvas.coords(paddle)
        return ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1] and \
                ball_pos[1] <= paddle_pos[3]

    def reset_ball(self):
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')
        self.ball_speed_x = -self.ball_speed_x

    def display_winner(self, winner_name):
        winner_label = tk.Label(self.master, text=f'{winner_name} ПОБЕДИЛ!!!!!')
        winner_label.pack()
        self.master.after(3000, self.master.destroy)
    
    def change_paddle_color_level1(self, paddle, color):
        if color == 'player_1_color':
            self.canvas.itemconfig(paddle, outline='green', width=2, fill='orange')
        elif color == 'player_2_color':
            self.canvas.itemconfig(paddle, outline='green', width=2, fill='orange')
    
    def change_paddle_color_level2(self, paddle, color):
        if color == 'player_1_color':
            self.canvas.itemconfig(paddle, fill='red', outline='black', width=5, dash = (4, 4))
        elif color == 'player_2_color':
            self.canvas.itemconfig(paddle, fill='red', outline='black', width=5, dash = (4, 4))
    
    def change_paddle_color_level3(self, paddle, color):
        if color == 'player_1_color':
            self.canvas.itemconfig(paddle, outline='orange', stipple="gray25", fill='yellow')
        elif color == 'player_2_color':
            self.canvas.itemconfig(paddle, outline='orange', stipple="gray25", fill='yellow')
    
    def change_paddle_color_level4(self, paddle, color):
        if color == 'player_1_color':
            self.canvas.itemconfig(paddle, fill='purple', outline='yellow', width=5, dash=(4, 4), stipple="gray25")
        elif color == 'player_2_color':
            self.canvas.itemconfig(paddle, fill='purple', outline='yellow', width=5, dash=(4, 4), stipple="gray25")

def main(name_player_1='Player 1', name_player_2='Player 2'):
    root = tk.Tk()
    game = PongGame(root, name_player_1, name_player_2)
    
    game.update()
    root.mainloop()

if __name__ == "__main__":
    main(name_player_1='Alice', name_player_2='Bob')