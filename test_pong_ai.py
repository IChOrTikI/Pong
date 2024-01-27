import time
import tkinter as tk
import random
from PIL import ImageTk, Image



# Создание главного окна
root = tk.Tk()
root.geometry('900x500')
root.resizable(width=False, height=False)
root.title('Pong')
root.iconbitmap('logo.ico')

root.config(bg='black')



var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()






def open_new_window1():

    # Создание нового окна
    new_window = tk.Toplevel(root)
    # Создание холста в новом окне
    new_window.resizable(width=False, height=False)
    time.sleep(1)
    canvas = tk.Canvas(new_window, width=900, height=500, bg='black')
    root.iconbitmap(new_window,'logo.ico')
    canvas.pack()

    canvas.create_rectangle(240, 60, 280, 110,
                       fill='red')
    canvas.create_text(500, 85, text='- Изначальные цвета ракеток игроков', fill='white', font=('Arial', 15))

    canvas.create_rectangle(190, 60, 230, 110,
                       fill='blue')
    canvas.create_text(525, 160, text='- Выдается за достижение 2 очков ракетки ',fill='white', font=('Arial', 15))

    canvas.create_rectangle(240, 140, 280, 190, outline='green',width=5, fill='orange')
    canvas.create_text(525, 245, fill='white' ,text='- Выдается за достижение 5 очков ракетки ' , font=('Arial', 15))

    canvas.create_rectangle(240, 220, 280, 270, fill='red', outline='black', width=5, dash = (4, 4),)
    canvas.create_text(525, 323,fill='white', text='- Выдается за достижение 10 очков ракетки ', font=('Arial', 15))

    canvas.create_rectangle(240, 300, 280, 350, outline='orange', stipple="gray25", fill='yellow')
    canvas.create_text(525,400 ,fill='white', text='- Выдается за достижение 15 очков ракетки ', font=('Arial', 15))

    canvas.create_rectangle(240, 380, 280, 440, fill='purple', outline='yellow', width=5, dash=(4, 4), stipple="gray25")



def open_new_window_choice_versuin_game():
    # Создание нового окна
    global var1, var2, var3, var4
    new_window_choice = tk.Toplevel(root)
    # Создание холста в новом окне
    new_window_choice.resizable(width=False, height=False)
    canvas_window = tk.Canvas(new_window_choice, width=900, height=500, bg='black')
    canvas_window.pack()
    flag_two_player = tk.Checkbutton(new_window_choice ,variable=var1, text='Два игрока', font=("Arial",20),bg='black',fg='red',activebackground='black',activeforeground='white')
    flag_ai_level1 = tk.Checkbutton(new_window_choice,variable=var2, text='Уровень компьютера лёгкий', font=("Arial",20),bg='black',fg='red',activebackground='black',activeforeground='white')
    flag_ai_level2  = tk.Checkbutton(new_window_choice,variable=var3, text='Уровень компьютера средний', font=("Arial",20),bg='black',fg='red',activebackground='black',activeforeground='white')
    flag_ai_level3 = tk.Checkbutton(new_window_choice ,variable=var4, text='Уровень компьютера сложный', font=("Arial",20),bg='black',fg='red',activebackground='black',activeforeground='white')

    flag_two_player.pack()
    flag_ai_level1.pack()
    flag_ai_level2.pack()
    flag_ai_level3.pack()

    canvas_window.create_window(315, 150, window=flag_two_player, anchor='nw')
    canvas_window.create_window(315, 190, window=flag_ai_level1, anchor='nw')
    canvas_window.create_window(315, 230, window=flag_ai_level2, anchor='nw')
    canvas_window.create_window(315, 270, window=flag_ai_level3, anchor='nw')




def open_new_window():
    digit1 = -2
    digit2 = -2
    new_window = tk.Toplevel(root)
    new_window.resizable(width=False, height=False)
    time.sleep(1)
    canvas = tk.Canvas(new_window, width=900, height=500)
    root.iconbitmap(new_window,'logo.ico')
    canvas.pack()
    path = 'pole_test.png'
    image = Image.open(path)
    image = ImageTk.PhotoImage(image)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    x1 = 450
    y1 = 450
    x2 = x1 + 15
    y2 = y1 + 15
    ball = canvas.create_oval(x1, y1, x2, y2, fill='white',tags="square")
    direction = "up"
    x3 = 30
    y3 = 200
    x4 = x3 + 10
    y4 = y3 + 100
    blue_rectangle = canvas.create_rectangle(x3, y3, x4, y4, fill='blue')
    x5 = 840
    y5 = 200
    x6 = x5 + 10
    y6 = y5 + 100
    red_rectangle = canvas.create_rectangle(x5, y5, x6, y6, fill='red')
    dx = 3
    dy = 3
    label1 = tk.Label(new_window, text=digit1, font=('Arial', '20'),bg="green",fg="white")
    label1.place(x=350, y=0)
    label2 = tk.Label(new_window, text=digit2, font=('Arial', '20'),bg="green",fg="white")
    label2.place(x=550, y=0)

    def change_color_red_rectangel_level1():
        canvas.itemconfig(red_rectangle, fill='orange')
        canvas.itemconfig(red_rectangle, outline='green',width=5)

    def change_color_blue_rectangel_level1():
        canvas.itemconfig(blue_rectangle, fill='orange')
        canvas.itemconfig(blue_rectangle, outline='green',width=5)

    def change_color_red_rectangel_level2():
        canvas.itemconfig(red_rectangle, fill='red')
        canvas.itemconfig(red_rectangle, outline='black', width=5, dash = (4, 4))

    def change_color_blue_rectangel_level2():
        canvas.itemconfig(blue_rectangle, fill='red')
        canvas.itemconfig(blue_rectangle, outline='black', width=5, dash = (4, 4))

    def change_color_red_rectangel_level3():
        canvas.itemconfig(red_rectangle, fill='yellow')
        canvas.itemconfig(red_rectangle, outline='orange', stipple="gray25")

    def change_color_blue_rectangel_level3():
        canvas.itemconfig(blue_rectangle, fill='yellow')
        canvas.itemconfig(blue_rectangle, outline='orange', stipple="gray25")

    def change_color_red_rectangel_level4():
        canvas.itemconfig(red_rectangle, fill='purple')
        canvas.itemconfig(red_rectangle, outline='yellow', width=5, dash=(4, 4), stipple="gray25")

    def change_color_blue_rectangel_level4():
        canvas.itemconfig(blue_rectangle, fill='purple')
        canvas.itemconfig(blue_rectangle, outline='yellow', width=5, dash=(4, 4), stipple="gray25")

    def move_ball():
        nonlocal dx, dy, digit1, digit2
        canvas.lift(ball)
        canvas.lift(ball)
        canvas.lift(ball)
        canvas.lift(ball)
        x1, y1, x2, y2 = canvas.coords(ball)
        if x2 >= canvas.winfo_width():
            dx = -dx
            digit1 = digit1 + 1
            label1.config(text=digit1)
            canvas.move(ball, -450, 0)
        if x1 <= 0:
            dx = -dx
            digit2 = digit2 + 1
            label2.config(text=digit2)
            canvas.move(ball, 450, 0)
        if digit1 == 2:
            change_color_blue_rectangel_level1()
        if digit2 == 2:
            change_color_red_rectangel_level1()
        if digit1 == 5:
            change_color_blue_rectangel_level2()
        if digit2 == 5:
            change_color_red_rectangel_level2()
        if digit1 == 10:
            change_color_blue_rectangel_level3()
        if digit2 == 10:
            change_color_red_rectangel_level3()
        if digit1 == 15:
            change_color_blue_rectangel_level4()
        if digit2 == 15:
            change_color_red_rectangel_level4()
        if y2 >= canvas.winfo_height() or y1 <= 0:
            dy = -dy
        if x2 >= x3 and x1 <= x4 and y2 >= y3 and y1 <= y4:
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            choice = random.randrange(1, 3)
            dx = -dx
            if choice == 2:
                dy = -dy
            else:
                dy = dy
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
        if x2 >= x5 and x1 <= x6 and y2 >= y5 and y1 <= y6:
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            dx = -dx
            choice = random.randrange(1, 3)
            if choice == 2:
                dy = -dy
            else:
                dy = dy
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
            canvas.lift(ball)
        canvas.move(ball, dx, dy)
        new_window.after(10, move_ball)

    def move_blue_rectangle_up(event):
        nonlocal y3, y4
        if y3 > 0:
            canvas.move(blue_rectangle, 0, -5)
            y3 = y3 - 5
            y4 = y4 - 5


    def move_blue_rectangle_down(event):
        nonlocal y3, y4
        if y4 < 500:
            canvas.move(blue_rectangle, 0, 5)
            y3 = y3 + 5
            y4 = y4 + 5

    def move_red_rectangle_up(event):
        nonlocal y5, y6
        if y5 > 0:
            canvas.move(red_rectangle, 0, -5)
            y5 = y5 - 5
            y6 = y6 - 5

    def move_red_rectangle_down(event):
        nonlocal y5, y6
        if y6 < 500:
            canvas.move(red_rectangle, 0, 5)
            y5 = y5 + 5
            y6 = y6 + 5

    if var1.get():
        def move_player():
            canvas.bind_all('<Up>', move_blue_rectangle_up)
            canvas.bind_all('<Down>', move_blue_rectangle_down)
            canvas.bind_all('<Up>', move_blue_rectangle_up)
            canvas.bind_all('<Down>', move_blue_rectangle_down)

            canvas.bind_all('<w>', move_red_rectangle_up)
            canvas.bind_all('<s>', move_red_rectangle_down)
            canvas.bind_all('<W>', move_red_rectangle_up)
            canvas.bind_all('<S>', move_red_rectangle_down)
            canvas.bind_all('<w>', move_red_rectangle_up)
            canvas.bind_all('<s>', move_red_rectangle_down)
            canvas.bind_all('<W>', move_red_rectangle_up)
            canvas.bind_all('<S>', move_red_rectangle_down)

        root.after(0, move_player())

    if var2.get():
        def move_red_rectangle_ai_level1():
            nonlocal y5, y6, direction
            if direction == "up":
                if y5 > 25:
                    canvas.move(red_rectangle, 0, -10)
                    y5 -= 15
                    y6 -= 15
                else:
                    direction = "down"
            else:
                if y6 < 500:
                    canvas.move(red_rectangle, 0, 10)
                    y5 += 15
                    y6 += 15
                else:
                    direction = "up"

            root.after(100, move_red_rectangle_ai_level1)


        direction = "up"


        root.after(100, move_red_rectangle_ai_level1)
        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)
        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)

    if var3.get():
        def move_red_rectangle_ai_level2():
            nonlocal y5, y6, direction

            if direction == "up":
                if y5 > 25:
                    canvas.move(red_rectangle, 0, -10)
                    y5 -= 15
                    y6 -= 15
                else:
                    direction = "down"
            else:
                if y6 < 500:
                    canvas.move(red_rectangle, 0, 10)
                    y5 += 15
                    y6 += 15
                else:
                    direction = "up"

            choice = random.randrange(1, 10)
            if choice == 4:
                if direction == "up":
                    direction = "down"
                elif direction == "down":
                    direction = "up"
            root.after(100, move_red_rectangle_ai_level2)


        direction = "up"


        root.after(100, move_red_rectangle_ai_level2)

        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)
        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)

    if var4.get():
        def move_red_rectangle_ai_level3():
            nonlocal y5, y6, direction
            if direction == "up":
                if y5 > 25:
                    canvas.move(red_rectangle, 0, -85)
                    y5 -= 85
                    y6 -= 85
                else:
                    direction = "down"
            else:
                if y6 < 500:
                    canvas.move(red_rectangle, 0, 85)
                    y5 += 85
                    y6 += 85
                else:
                    direction = "up"
            choice = random.randrange(1, 10)
            if choice == 4:
                if direction == "up":
                    direction = "down"
                elif direction == "down":
                    direction = "up"
            root.after(100, move_red_rectangle_ai_level3)


        direction = "up"


        root.after(100, move_red_rectangle_ai_level3)

        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)
        canvas.bind_all('<Up>', move_blue_rectangle_up)
        canvas.bind_all('<Down>', move_blue_rectangle_down)


    move_ball()
    canvas.create_window(window=ball)
    canvas.create_window(window=red_rectangle)
    canvas.create_window(window=blue_rectangle)
     #### ЕСЛИ ПРОИЗОШЛО СТОЛКНОВЕНИЕ ТО МЯЧЬ СТАВИМ В ВРЕХ



path = 'glav.png'

image = Image.open(path)

image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root,height=500, width=900)
canvas.pack(side="top", fill="both", expand="no")

canvas.create_image(0, 0, anchor="nw", image=image)

# Создаем кнопку и размещяем ее в "окне" ("контейнере") на Canvas
button = tk.Button(root, text='Quit', command=root.quit)


# Создаем текст через create_text, в отличие от Label у него будет прозрачный фон
#anvas.create_text(100, 100, text="Cat", fill="black", font="Verdana 14")

lable = tk.Label(root, text='PONG',font=("Arial", 45),fg='black',width=10,height=1,bg='yellow',borderwidth= 15)
btn1 = tk.Button(root, text='Играть',command=open_new_window,font=("Arial", 25),fg='white',width=10,height=1,bg='black',borderwidth= 15,activebackground='gray',activeforeground='white')
btn2 = tk.Button(root, text='Достижения',command=open_new_window1,font=("Arial", 25),fg='white',width=10,height=1,bg='black',borderwidth= 15,activebackground='gray',activeforeground='white')
btn3 = tk.Button(root, text='Режим игры',command=open_new_window_choice_versuin_game,font=("Arial", 25),fg='white',width=10,height=1,bg='black',borderwidth= 15,activebackground='gray',activeforeground='white')
lable.pack(expand=True, ipadx=10, ipady=10)

btn1.pack(expand=True, ipadx=10, ipady=10)
btn2.pack(expand=True, ipadx=10, ipady=10)
btn3.pack(expand=True, ipadx=10, ipady=10)
canvas.create_window((350, 150), anchor="nw", window=btn1)
canvas.create_window((350, 270), anchor="nw", window=btn2)
canvas.create_window((350, 390), anchor="nw", window=btn3)
canvas.create_window((270, 20), anchor="nw", window=lable)






root.mainloop()