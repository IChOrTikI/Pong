import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

import random
import threading
import tkinter as tk
import play_two_player_not_count as game_1
import play_two_player_count as game2
import play_player_ai_count as game3
import play_player_ai_not_count as game4
import play_player_ai_count_low as game5
import play_player_ai_not_count_low as game6


thread_game = threading.Thread(name="First")

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

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("glav.png")  # Путь к изображению
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        self.label = QtWidgets.QLabel("Пинг-понг", self)
        self.label.setGeometry(290, 0, 550, 125)
        self.label.setFont(QFont('Arial', 45))

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

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

        self.setWindowTitle('Прогресс игроков')
        self.setGeometry(500, 300, 900, 500)
        self.setFixedSize(900, 500)

        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("progress.png")  
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)


        # Создаём надписи для квадратов
        self.label_0= QtWidgets.QLabel(" -Изначальные цвета ракеток игроков", self)
        self.label_0.setGeometry(302, 15, 550, 125)
        self.label_0.setFont(QFont('Arial', 13))
        self.label_0.setStyleSheet("color: white")


        self.label_1 = QtWidgets.QLabel(" - Выдается за достижение 2 очков ракетки", self)
        self.label_1.setGeometry(302, 100, 550, 125)
        self.label_1.setFont(QFont('Arial', 13))
        self.label_1.setStyleSheet("color: white")


        self.label_2 = QtWidgets.QLabel(" -Выдается за достижение 5 очков ракетки", self)
        self.label_2.setGeometry(302, 185, 550, 125)
        self.label_2.setFont(QFont('Arial', 13))
        self.label_2.setStyleSheet("color: white")


        self.label_3 = QtWidgets.QLabel(" -Выдается за достижение 10 очков ракетки", self)
        self.label_3.setGeometry(302, (185 + 85), 550, 125)
        self.label_3.setFont(QFont('Arial', 13))
        self.label_3.setStyleSheet("color: white")

        self.label_4 = QtWidgets.QLabel(" -Выдается за достижение 14 очков ракетки", self)
        self.label_4.setGeometry(302, (185 + 85 + 85), 550, 125)
        self.label_4.setFont(QFont('Arial', 13))
        self.label_4.setStyleSheet("color: white")




        # Создаём квадраты
        self.square_blue = QtWidgets.QLabel(self)
        self.square_blue.setGeometry(245, 50, 45, 55)
        self.square_blue.setStyleSheet("background-color: blue; border: 1px solid black;")

        self.square_red = QtWidgets.QLabel(self)
        self.square_red.setGeometry(195, 50, 45, 55)
        self.square_red.setStyleSheet("background-color: red; border: 1px solid black;")

        self.square_level1 = QtWidgets.QLabel(self)
        self.square_level1.setGeometry(244, 135, 45, 55)
        self.square_level1.setStyleSheet("background-color: orange; border: 5px solid green;")

        # self.square_level2 = QtWidgets.QLabel(self)
        # self.square_level2.setGeometry(244, (135 + 85), 45, 55)
        # self.square_level2.setStyleSheet("background-color: red; border : 3px dashed black;")
        # layout = QtWidgets.QGridLayout()

        # self.square_level2 = QtWidgets.QLabel(self)
        # self.square_level2.setGeometry(244, (135 + 85 + 85), 45, 55)
        # self.square_level2.setStyleSheet("background-color: red; border : 3px dashed orange;")
       
        layout = QtWidgets.QGridLayout()

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()

    def closeEvent(self, event):
        self.switch_window.emit()
        event.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black,  3, Qt.DotLine))
        painter.drawRect(244, (135 + 85), 45, 55)

        painter1 = QPainter(self)
        painter1.setBrush(QBrush(Qt.yellow, Qt.Dense5Pattern))
        painter1.setPen(QPen(QColor(255, 165, 0), 3, Qt.DotLine))
        painter1.drawRect(244, (135 + 85 + 85), 45, 55)

        painter2 = QPainter(self)
        painter2.setBrush(QBrush(QColor(0,0,51), Qt.Dense5Pattern))
        painter2.setPen(QPen(Qt.yellow, 3, Qt.DotLine))
        painter2.drawRect(244, (135 + 85 + 85 + 85), 45, 55)

        

class Choice(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    user_input_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.text = ""
        self.setWindowTitle('Выбор режима игры')

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

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

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

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

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

        self.choice_player = text_choice
        
       
        self.setWindowTitle('Получение имени игрока')

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

        # Добавляем кнопку
        self.enter_button = QtWidgets.QPushButton("Ввести данные", self)
        self.enter_button.move(425, 450)

        # Подключаем сигнал нажатия кнопки к функции
        self.enter_button.clicked.connect(self.on_enter_button_clicked)


    def on_enter_button_clicked(self):

        input1_text = self.input_field1.text()
        global thread_game
        print(thread_game.name)

        if input1_text != "":
            print("Введенные данные:")
            print("Игрок:", input1_text)

            if (self.choice_player == 'Игра с компьютером (легкий уровень) с счётом')  and (thread_game.is_alive() == False) :
                self.main_window.emit()
                thread_game = threading.Thread(name="second", target=game5.main, args= (input1_text, ))
                thread_game.start()
            elif (self.choice_player == 'Игра с компьютером (легкий уровень) без счёта') and (thread_game.is_alive() == False):
                self.main_window.emit()
                thread_game = threading.Thread(name="second", target=game6.main, args= (input1_text, ))
                thread_game.start()
            elif (self.choice_player == 'Игра с компьютером (сложный уровень) с счётом') and (thread_game.is_alive() == False):
                self.main_window.emit()
                thread_game = threading.Thread(name="second", target=game3.main, args= (input1_text, ))
                thread_game.start()
            elif (self.choice_player == 'Игра с компьютером (сложный уровень) без счёта') and (thread_game.is_alive() == False):
                self.main_window.emit()
                thread_game = threading.Thread(name="second", target=game4.main, args= (input1_text, ))
                thread_game.start()
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

        self.setWindowIcon(QtGui.QIcon('logo.ico'))

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
        global thread_game
        input1_text = self.input_field1.text()
        input2_text = self.input_field2.text()
        if input1_text != "" and input2_text != "":
            print("Введенные данные:")
            print("Игрок 1:", input1_text)
            print("Игрок 2:", input2_text)
            if (self.choice_player == 'Игра на два игрока без счёта') and (thread_game.is_alive() == False):
                # self.get_name1.emit(input1_text, input2_text)
 
                self.main_window.emit()
                thread_game = threading.Thread(name="second", target=game_1.main, args= (input1_text, input2_text,))
                thread_game.start()
            elif (self.choice_player == 'Игра на два игрока с счётом') and (thread_game.is_alive() == False):
                self.main_window.emit()
                # game2.main(input1_text, input2_text)
                thread_game = threading.Thread(name="second", target=game2.main, args= (input1_text, input2_text,))
                thread_game.start()
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

def maing():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
        maing()
        