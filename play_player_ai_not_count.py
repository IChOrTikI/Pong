import random
import tkinter as tk

class PongGame:
    def __init__(self, master, name_player_1='Player 1'):
        self.master = master
        self.name1 = name_player_1

        self.canvas = tk.Canvas(self.master, width=900, height=500, bg='black')

        self.background_image = tk.PhotoImage(file="wallpaper.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        master.iconbitmap('logo.ico')
        master.wm_title('Игра без счёта (сложный уровень компьютера)')

        self.canvas.pack()

        self.paddle_a = self.canvas.create_rectangle(0, 50, 10, 150, fill='blue')
        self.paddle_ai = self.canvas.create_rectangle(892, 50, 902, 150, fill='red')

        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')

        self.score_player_1 = 0
        self.score_player_2 = 0
        self.game_over = False

        self.paddle_a_speed = 0
        self.paddle_b_speed = 0

        self.ball_speed_x = 3
        self.ball_speed_y = 3

        number_ball = random.randint(1, 2)
        if number_ball == 1:
            self.ball_speed_x *= -1
        else:
            self.ball_speed_x *= 1

        self.flag = False

        self.master.bind('<KeyPress-w>', self.start_move_paddle_a_up)
        self.master.bind('<KeyRelease-w>', self.stop_move_paddle_a)
        self.master.bind('<KeyPress-s>', self.start_move_paddle_a_down)
        self.master.bind('<KeyRelease-s>', self.stop_move_paddle_a)

        self.update()

    def write_score(self):
        with open('ScorePlayer.txt', 'a') as file:
            file.write(f"{self.name1}: {self.score_player_1}\n")
            file.write("\n")
        print(self.name1, self.score_player_1)


    def start_move_paddle_a_up(self, event):
        self.paddle_a_speed = -3

    def start_move_paddle_a_down(self, event):
        self.paddle_a_speed = 3

    def stop_move_paddle_a(self, event):
        self.paddle_a_speed = 0

    def update(self):
        self.show_scores()

        self.move_paddles()
        self.move_ball()
        self.move_paddle_ai() 

        if not self.game_over:
            self.master.after(10, self.update)

    def show_scores(self):
        self.canvas.delete("score")
        message_player_1 = f'{self.name1}: {self.score_player_1}'
        message_player_2 = f'Компьютер: {self.score_player_2}'
        self.canvas.create_text(150, 30, text=message_player_1, font=('Arial', 10), fill='white', tag="score")
        self.canvas.create_text(750, 30, text=message_player_2, font=('Arial', 10), fill='white', tag="score")
    
    # def move_paddle_ai(self):
    #     ball_pos = self.canvas.coords(self.ball)
    #     paddle_pos = self.canvas.coords(self.paddle_ai)
    #     if not self.flag:
    #         self.canvas.move(self.paddle_ai, 0, -5)
    #         if paddle_pos[1] == 0 or paddle_pos[1] == 1:
    #             self.flag = True
    #     if self.flag:
    #         self.canvas.move(self.paddle_ai, 0, 5)
    #         if paddle_pos[3] == 500:
    #             self.flag = False
    def move_paddle_ai(self):
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle_ai)

        if ball_pos[2] > 250:
            if ball_pos[1] < paddle_pos[1]:
                self.canvas.move(self.paddle_ai, 0, -2.5)
            elif ball_pos[3] > paddle_pos[3]:
                self.canvas.move(self.paddle_ai, 0, 2.5)





    def move_paddles(self):

        self.ball_speed_x *= 1.00005
        self.ball_speed_y *= 1.00005

        for paddle, speed in [(self.paddle_a, self.paddle_a_speed)]:
            paddle_pos = self.canvas.coords(paddle)
            if speed < 0:
                if paddle_pos[1] + speed >= 0:  
                    self.canvas.move(paddle, 0, speed)
                else:
                    self.canvas.move(paddle, 0, -paddle_pos[1])  
            elif speed > 0: 
                if paddle_pos[3] + speed <= 500:  
                    self.canvas.move(paddle, 0, speed)
                else:
                    self.canvas.move(paddle, 0, 500 - paddle_pos[3])  

    def move_ball(self):

        if self.score_player_1 == 2:
            self.change_paddle_color_level1(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 2:
            self.change_paddle_color_level1(self.paddle_ai, 'player_2_color')
        if self.score_player_1 == 5:
            self.change_paddle_color_level2(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 5:
            self.change_paddle_color_level2(self.paddle_ai, 'player_2_color')
        if self.score_player_1 == 10:
            self.change_paddle_color_level3(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 10:
            self.change_paddle_color_level3(self.paddle_ai, 'player_2_color')
        if self.score_player_1 == 15:
            self.change_paddle_color_level4(self.paddle_a, 'player_1_color')
        if self.score_player_2 == 15:
            self.change_paddle_color_level4(self.paddle_ai, 'player_2_color')

        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        ball_pos = self.canvas.coords(self.ball)

        if ball_pos[1] <= 0 or ball_pos[3] >= 500:
            self.ball_speed_y = -self.ball_speed_y

        if ball_pos[0] <= 0:
            self.score_player_2 += 1
            # self.write_score()
            # self.reset_ball()
            flag = True      #////////
            self.reset_ball(flag) 
        elif ball_pos[2] >= 900:
            self.score_player_1 += 1
            self.write_score()
            # self.reset_ball()
            flag = False               #////////
            self.reset_ball(flag) 

        if self.check_collision(ball_pos, self.paddle_a):
            number = random.randint(1, 5)
            if number == 4:
                self.ball_speed_y = -self.ball_speed_y
            self.ball_speed_x = -self.ball_speed_x
            
        elif self.check_collision(ball_pos, self.paddle_ai):
            self.ball_speed_x = -self.ball_speed_x

    

    def check_collision(self, ball_pos, paddle):
        paddle_pos = self.canvas.coords(paddle)
        return ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1] and \
                ball_pos[1] <= paddle_pos[3]

    def reset_ball(self, flag):
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')
        # self.ball_speed_x = -self.ball_speed_x

        number = random.randint(1,5)
        # print(number)

                                #////////
        self.ball_speed_x = 3
        if flag:
            self.ball_speed_x *= -1
        else:
            self.ball_speed_x *= 1
        self.ball_speed_y = 3
        if (number == 4) or (number == 1):
            self.ball_speed_y *= -1


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

def main(name_player_1='Player 1'):
    root = tk.Tk()
    game = PongGame(root, name_player_1)
    game.update()
    root.mainloop()

if __name__ == "__main__":
    main(name_player_1='Alice')