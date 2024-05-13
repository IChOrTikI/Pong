import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui
import random
import tkinter as tk
import play_two_player_not_count as game2
import play_two_player_ai_count as game3
import play_two_player_ai_not_count as game4
import play_two_player_ai_count_low as game5
import play_two_player_ai_not_count_low as game6

########################################################################################
# Доделать проект сделать сохранение режима игры
# Сделать имя компьютера по умолчанию
# Сделать паузу при начале игры с отсчетом   л
# Сделать кнопку назад (потому что нажимать на крестик не удобно)
# Написать в раководстве пользвателя что закрытие окон происходит по нажатию кретсика
#######################################################################################


class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()
    switch_window_two_player_with_computer = QtCore.pyqtSignal(str)
    switch_window_two_player = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.text = text
        self.setWindowTitle('Меню')

        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("glav.png")  # Путь к вашему изображению
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        layout = QtWidgets.QGridLayout()

        self.button1 = QtWidgets.QPushButton('Играть')
        self.button1.setFixedWidth(200)
        self.button1.setFixedHeight(50)
        self.button1.clicked.connect(self.chek_choice)


        self.button2 = QtWidgets.QPushButton('Выбор режима игры')
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(50)
        self.button2.clicked.connect(self.login_2)

        self.button3 = QtWidgets.QPushButton('Достижения')
        self.button3.setFixedWidth(200)
        self.button3.setFixedHeight(50)
        self.button3.clicked.connect(self.login)

        layout.addWidget(QtWidgets.QLabel(), 0, 0)
        layout.addWidget(QtWidgets.QLabel(), 1, 0)
        layout.addWidget(self.button1, 2, 0)  
        layout.addWidget(QtWidgets.QLabel(), 3, 0)
        layout.addWidget(self.button2, 4, 0) 
        layout.addWidget(QtWidgets.QLabel(), 5, 0)  
        layout.addWidget(self.button3, 6, 0)

        print()

        self.setLayout(layout)

    def chek_choice(self):
        if self.text != "":
            print(self.text)
            if self.text == 'Игра с компьютером (легкий уровень) с счётом' or self.text == 'Игра с компьютером (легкий уровень) без счёта' or self.text == 'Игра с компьютером (сложный уровень) с счётом' or self.text == 'Игра с компьютером (сложный уровень) без счёта':
                self.switch_window_two_player_with_computer.emit(self.text)
                print('Игра с компьютером')
            elif self.text == 'Игра на два игрока с счётом' or self.text == 'Игра на два игрока без счёта':
                self.switch_window_two_player.emit(self.text)
                print('Игра на два игрока')
        else:
            self.switch_window_3.emit()
            print('Неа')
    
    # def get_choice(self):
    #     print(self.text)

    def login(self):
        self.switch_window.emit()

    def login_2(self):
        self.switch_window_2.emit()
        

class Progress(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Прогресс игроков')
        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("progress.png")  
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        layout = QtWidgets.QGridLayout()

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()

    def closeEvent(self, event):
        self.switch_window.emit()
        event.accept()

class Choice(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    user_input_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.text = ""
        self.setWindowTitle('Выбор режима игры')

        layout = QtWidgets.QVBoxLayout()  

        self.setWindowTitle("Выбор режима игры")
        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("pvpglav.png")  
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        # Добавление RadioButtons
        self.radio_button1 = QtWidgets.QRadioButton('Игра на два игрока с счётом')
        self.radio_button1.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button1, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.radio_button2 = QtWidgets.QRadioButton('Игра на два игрока без счёта')
        self.radio_button2.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button2, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.radio_button3 = QtWidgets.QRadioButton('Игра с компьютером (легкий уровень) с счётом')
        self.radio_button3.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button3, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.radio_button4 = QtWidgets.QRadioButton('Игра с компьютером (легкий уровень) без счёта')
        self.radio_button4.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button4, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.radio_button5 = QtWidgets.QRadioButton('Игра с компьютером (сложный уровень) с счётом')
        self.radio_button5.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button5, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.radio_button6 = QtWidgets.QRadioButton('Игра с компьютером (сложный уровень) без счёта')
        self.radio_button6.setStyleSheet("QRadioButton { background-color : white; }")  # Установка белого фона
        layout.addWidget(self.radio_button6, alignment=QtCore.Qt.AlignCenter)  # Центрирование RadioButton

        self.setLayout(layout)

        # Соединяем сигналы от RadioButtons с методом для обработки выбора
        self.radio_button1.clicked.connect(self.radio_button_clicked)
        self.radio_button2.clicked.connect(self.radio_button_clicked)
        self.radio_button3.clicked.connect(self.radio_button_clicked)
        self.radio_button4.clicked.connect(self.radio_button_clicked)
        self.radio_button5.clicked.connect(self.radio_button_clicked)
        self.radio_button6.clicked.connect(self.radio_button_clicked)

    def radio_button_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.text = sender.text()
            print("Выбран QRadioButton:", sender.text())

    def closeEvent(self, event):
        print(self.text)
        self.switch_window.emit(self.text)
        event.accept()

class ErrorFirst(QtWidgets.QWidget):

    main_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Ошибка')

        self.setWindowTitle("Ошибка")
        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("error.png")  # Путь к вашему изображению
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)
    
    def closeEvent(self, event):
        self.main_window.emit()
        event.accept()
    


class GetUsername_and_computer(QtWidgets.QWidget):

    main_window = QtCore.pyqtSignal()

    def __init__(self, text_choice):
        QtWidgets.QWidget.__init__(self)

        self.choice_player = text_choice

        self.setWindowTitle('Получение имён игроков')

        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("2.png")  # Путь к вашему изображению
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        layout = QtWidgets.QGridLayout()


        # Добавляем надпись

        label = QtWidgets.QLabel('Вы выбрали режим: ' + self.choice_player, self)
        label.move(450, 90)
        label.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

        # Добавляем надпись для первого поля ввода
        label1 = QtWidgets.QLabel("Имя игрока:", self)
        label1.move(50, 80)
        label1.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

        # Добавляем первое поле ввода
        self.input_field1 = QtWidgets.QLineEdit(self)
        self.input_field1.move(150, 80)





        # # Добавляем надпись для второго поля ввода
        # label2 = QtWidgets.QLabel("Обзовите компьютер:", self)
        # label2.move(50, 110)

        # # Добавляем второе поле ввода
        # self.input_field2 = QtWidgets.QLineEdit(self)
        # self.input_field2.move(200, 110)





        # Добавляем кнопку
        self.enter_button = QtWidgets.QPushButton("Ввести данные", self)
        self.enter_button.move(425, 450)

        # Подключаем сигнал нажатия кнопки к функции
        self.enter_button.clicked.connect(self.on_enter_button_clicked)


    def on_enter_button_clicked(self):
        # Добавьте ваш код здесь для обработки введенных данных
        input1_text = self.input_field1.text()


        # input2_text = self.input_field2.text()=============
        # if input1_text != "" and input2_text != "":

        if input1_text != "":
            print("Введенные данные:")
            print("Игрок:", input1_text)


            # print("Компьютер:", input2_text) =============


            # if self.choice_player == 'Игра с компьютером (легкий уровень) с счётом':
            #     self.main_window.emit()
            #     game5.main(input1_text, input2_text)
            # elif self.choice_player == 'Игра с компьютером (легкий уровень) без счёта':
            #     self.main_window.emit()
            #     game6.main(input1_text, input2_text)
            # elif self.choice_player == 'Игра с компьютером (сложный уровень) с счётом':
            #     self.main_window.emit()
            #     game3.main(input1_text, input2_text)
            # elif self.choice_player == 'Игра с компьютером (сложный уровень) без счёта':
            #     self.main_window.emit()
            #     game4.main(input1_text, input2_text)

            if self.choice_player == 'Игра с компьютером (легкий уровень) с счётом':
                self.main_window.emit()
                game5.main(input1_text)
            elif self.choice_player == 'Игра с компьютером (легкий уровень) без счёта':
                self.main_window.emit()
                game6.main(input1_text)
            elif self.choice_player == 'Игра с компьютером (сложный уровень) с счётом':
                self.main_window.emit()
                game3.main(input1_text)
            elif self.choice_player == 'Игра с компьютером (сложный уровень) без счёта':
                self.main_window.emit()
                game4.main(input1_text)

        else:
            message_box = QMessageBox()
            message_box.setText("Введите имена игроков!!!!")
            message_box.setWindowTitle("Ошибка!!!!!")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()
    
    def get_choice(self):
        print(self.choice_player)

    def closeEvent(self, event):
        self.main_window.emit()
        event.accept()

class GetUsername_and_Username(QtWidgets.QWidget):

    main_window = QtCore.pyqtSignal()
    get_name1 = QtCore.pyqtSignal(str, str)

    def __init__(self, text_choice):
        QtWidgets.QWidget.__init__(self)

        self.choice_player = text_choice

        self.setWindowTitle('Получение имён игроков')

        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("1.png")  # Путь к вашему изображению
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        layout = QtWidgets.QGridLayout()

        


        # Добавляем надпись

        label = QtWidgets.QLabel('Вы выбрали режим: ' + self.choice_player, self)
        label.move(450, 90)
        label.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

        # Добавляем надпись для первого поля ввода
        label1 = QtWidgets.QLabel("Имя игрока 1:", self)
        label1.move(50, 80)
        label1.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

        # Добавляем первое поле ввода
        self.input_field1 = QtWidgets.QLineEdit(self)
        self.input_field1.move(150, 80)


        # Добавляем надпись для второго поля ввода
        label2 = QtWidgets.QLabel("Имя игрока 2:", self)
        label2.move(50, 110)
        label2.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

        # Добавляем второе поле ввода
        self.input_field2 = QtWidgets.QLineEdit(self)
        self.input_field2.move(150, 110)
        # Добавляем кнопку
        self.enter_button = QtWidgets.QPushButton("Ввести данные", self)
        self.enter_button.move(425, 450)

        # Подключаем сигнал нажатия кнопки к функции
        self.enter_button.clicked.connect(self.on_enter_button_clicked)


    def on_enter_button_clicked(self):
        input1_text = self.input_field1.text()
        input2_text = self.input_field2.text()
        if input1_text != "" and input2_text != "":
            print("Введенные данные:")
            print("Игрок 1:", input1_text)
            print("Игрок 2:", input2_text)
            if self.choice_player == 'Игра на два игрока без счёта':
                self.get_name1.emit(input1_text, input2_text)
            elif self.choice_player == 'Игра на два игрока с счётом':
                self.main_window.emit()
                game2.main(input1_text, input2_text)
        else:
            message_box = QMessageBox()
            message_box.setText("Введите имена игроков!!!!")
            message_box.setWindowTitle("Ошибка!!!!!")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()

    def get_choice(self):
        print(self.choice_player)

    def closeEvent(self, event):
        self.main_window.emit()
        event.accept()

class Controller:
    def __init__(self):
        pass

    def show_main(self, text=""):
        self.main = MainWindow(text)
        self.main.switch_window.connect(self.show_progress)
        self.main.switch_window_2.connect(self.show_choice)
        self.main.switch_window_3.connect(self.error_window)
        self.main.switch_window_two_player_with_computer.connect(self.get_name_username_and_comp)
        self.main.switch_window_two_player.connect(self.get_name_username_and_username)
        self.main.show()
    
    def get_name_username_and_comp(self, text_choice=""):
        self.get_name_us_co = GetUsername_and_computer(text_choice)
        self.get_name_us_co.main_window.connect(self.show_main)  # Добавляем соединение сигнала switch_window к методу show_main
        self.get_name_us_co.main_window.connect(self.close_comp)
        self.main.close()
        self.get_name_us_co.show()
    
    def close_comp(self):
        self.get_name_us_co.close()

    def close_users(self):
        self.get_name_us_us.close()
    

    def get_name_username_and_username(self, text_choice=""):
        self.get_name_us_us = GetUsername_and_Username(text_choice)
        self.get_name_us_us.main_window.connect(self.show_main)
        self.get_name_us_us.main_window.connect(self.close_users)  # Добавляем соединение сигнала switch_window к методу show_main
        self.get_name_us_us.get_name1.connect(self.game1)
        self.main.close()
        self.get_name_us_us.show()
    
    def show_progress(self):
        self.progress = Progress()
        self.progress.switch_window.connect(self.show_main)  # Добавляем соединение сигнала switch_window к методу show_main
        self.main.close()
        self.progress.show()

    def show_choice(self):
        self.choice = Choice()
        self.choice.switch_window.connect(self.show_main)  # Добавляем соединение сигнала switch_window к методу show_main
        self.main.close()
        self.choice.show()
    
    def error_window(self):
        self.error = ErrorFirst()
        self.error.main_window.connect(self.show_main)  # Добавляем соединение сигнала switch_window к методу show_main
        self.main.close()
        self.error.show()
    
    def game1(self, name1='play1', name2='play2'):
        self.get_name_us_us.close()
        root = tk.Tk()
        root.title("Pong Game")
        width = 900
        height = 500
        x_pos = 500
        y_pos = 300
        # Устанавливаем размеры и позицию окна
        root.geometry(f'{width}x{height}+{x_pos}+{y_pos}')
        game = PongGame(root, name_player_1=name1, name_player_2=name2)
        root.mainloop()
        

class PongGame(QtWidgets.QWidget):


    def __init__(self, master, name_player_1, name_player_2):
        QtWidgets.QWidget.__init__(self)
        self.master = master
        self.name1 = name_player_1
        self.name2 = name_player_2
        
        self.canvas = tk.Canvas(self.master, width=900, height=500, bg='black')
        self.canvas.pack()

        self.paddle_a = self.canvas.create_rectangle(0, 50, 10, 150, fill='white')
        self.paddle_b = self.canvas.create_rectangle(892, 50, 902, 150, fill='white')

        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')

        self.score_player_1 = 0
        self.score_player_2 = 0

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

        self.master.after(10, self.update)

    def show_scores(self):

        self.canvas.delete("score")
        massage_player_1 = self.name1 + ' : ' + str(self.score_player_1)
        massage_player_2 = self.name2 + ' : ' + str(self.score_player_2)
        self.canvas.create_text(150, 30, text=massage_player_1, font=('Arial', 10), fill='white', tag="score")
        self.canvas.create_text(750, 30, text=massage_player_2, font=('Arial', 10), fill='white', tag="score")

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

        if ball_pos[0] <= 0 or ball_pos[2] >= 900:
            self.reset_ball()

    def check_collision(self, ball_pos, paddle):
        paddle_pos = self.canvas.coords(paddle)
        return ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1] and \
            ball_pos[1] <= paddle_pos[3]

    def reset_ball(self):
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')
        self.ball_speed_x = -self.ball_speed_x


class PongGame(QtWidgets.QWidget):


    def __init__(self, master, name_player_1, name_player_2):
        QtWidgets.QWidget.__init__(self)
        self.master = master
        self.name1 = name_player_1
        self.name2 = name_player_2

        self.canvas = tk.Canvas(self.master, width=900, height=500)

        # Добавляем изображение на фон
        self.background_image = tk.PhotoImage(file="wallpaper.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        self.canvas.pack()


        self.paddle_a = self.canvas.create_rectangle(0, 50, 10, 150, fill='white')
        self.paddle_b = self.canvas.create_rectangle(892, 50, 902, 150, fill='white')

        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')

        self.score_player_1 = 0
        self.score_player_2 = 0

        self.paddle_a_speed = 0
        self.paddle_b_speed = 0

        self.ball_speed_x = 5
        self.ball_speed_y = 5

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
        self.paddle_a_speed = -5

    def start_move_paddle_a_down(self, event):
        self.paddle_a_speed = 5

    def start_move_paddle_b_up(self, event):
        self.paddle_b_speed = -5

    def start_move_paddle_b_down(self, event):
        self.paddle_b_speed = 5

    def stop_move_paddle_a(self, event):
        self.paddle_a_speed = 0

    def stop_move_paddle_b(self, event):
        self.paddle_b_speed = 0

    def update(self):
        self.show_scores()
        self.move_paddles()
        self.move_ball()
        self.master.after(10, self.update)

    def show_scores(self):
        self.canvas.delete("score")
        massage_player_1 = self.name1 + ' : ' + str(self.score_player_1)
        massage_player_2 = self.name2 + ' : ' + str(self.score_player_2)
        self.canvas.create_text(150, 30, text=massage_player_1, font=('Arial', 10), fill='white', tag="score")
        self.canvas.create_text(750, 30, text=massage_player_2, font=('Arial', 10), fill='white', tag="score")

    def move_paddles(self):
        for paddle, speed in [(self.paddle_a, self.paddle_a_speed), (self.paddle_b, self.paddle_b_speed)]:
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

        if ball_pos[0] <= 0 or ball_pos[2] >= 900:
            self.reset_ball()

    def check_collision(self, ball_pos, paddle):
        paddle_pos = self.canvas.coords(paddle)
        return ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1] and \
            ball_pos[1] <= paddle_pos[3]

    def reset_ball(self):
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle(445, 245, 465, 265, fill='white')
        self.ball_speed_x = -self.ball_speed_x

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


def maing():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    maing()