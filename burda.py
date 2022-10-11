from turtle import *
from random import *

scr = Screen()
scr.register_shape(name='seven.gif')
scr.register_shape(name='klubnika.gif')
scr.register_shape(name='limon.gif')
scr.register_shape(name='banan.gif')
scr.register_shape(name='bitok.gif')
scr.register_shape(name='crown.gif')
shapes = ['seven.gif']
shapes.append('klubnika.gif')
shapes.append('limon.gif')
shapes.append('banan.gif')
shapes.append('bitok.gif')
shapes.append('crown.gif')
l_t = Turtle()
c_t = Turtle()
r_t = Turtle()
l_t.ht()
c_t.ht()
r_t.ht()
bet = 1
balance = 100
speedy = 3
action = False
auto_spin = 0
streamer = False
count_win = -1
shape_win = 0


def rectangle(x, y, length, width, colorr=''):  # рисование прямоугольника с возможной заливкой
    goto(x, y)
    pd()
    if colorr != '':
        color(colorr)
        fillcolor(colorr)
        begin_fill()
        for i in range(2):
            fd(length)
            lt(90)
            fd(width)
            lt(90)
        end_fill()
        color('black')
    else:
        for i in range(2):
            fd(length)
            lt(90)
            fd(width)
            lt(90)
    pu()


def slot(sp, left_ryad, center_ryad, right_ryad):  # спин
    global bet, balance, speedy, action, auto_spin, streamer, count_win, shape_win
    if int(bet) > int(balance):
        bet = numinput('Ставка',
                       'Выберите ставку автомата:\nПо '
                       'умолчанию ставка 1', 1, 1, int(balance))
        while bet == None:
            bet = numinput('Ставка',
                           'Выберите ставку автомата:\nПо '
                           'умолчанию ставка 1', 1, 1, int(balance))
    action = True
    count_win = -1
    if auto_spin > 0:
        auto_spin -= 1
    rectangle(-330, 95, 100, 50, 'white')  # пишет баланс
    goto(-320, 100)
    write(str(int(balance)), font=('aerial', 25, 'normal'))
    rectangle(-330, -5, 100, 50, 'white')  # пишет ставку
    goto(-320, 0)
    write(str(int(bet)), font=('aerial', 25, 'normal'))
    balance -= int(bet)
    rectangle(-310, -105, 80, 50, 'white')  # пишет скорость
    goto(-280, -100)
    write(str(int(speedy)), font=('aerial', 25, 'normal'))
    rectangle(-330, 95, 100, 50, 'white')  # пишет новый баланс
    goto(-320, 100)
    write(str(int(balance)), font=('aerial', 25, 'normal'))
    rectangle(-160, 260, 600, 100, 'white')

    speed(0)
    turtles = [left_ryad, center_ryad, right_ryad]
    ht()
    goto(-160, 260)
    count_l = randint(1, 10)
    count_c = randint(1, 10)
    count_r = randint(1, 10)
    for t in turtles:
        t.ht()
        t.pu()
        t.speed(speedy)
        t.shape(choice(sp))
    i = 1
    left_ryad.goto(-140, 100)
    left_ryad.st()
    left_ryad.goto(-140, -40)
    center_ryad.goto(0, 100)
    center_ryad.st()
    center_ryad.goto(0, -40)
    right_ryad.goto(140, 100)
    right_ryad.st()
    right_ryad.goto(140, -40)
    if streamer:
        shape_win = choice(sp)
        count_win = min(count_c, count_r, count_l) + 1
        count_l = count_c = count_r = count_win + 1
    while i < count_l or i < count_c or i < count_r:
        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-160, 260)
            write(f'Выигрыш: {str(int(bet) * 10)}!', font=('aerial', 50, 'normal'))
            balance += bet * 10
            break

        if i < count_l:
            left_ryad.goto(-140, -200)
            left_ryad.ht()
            left_ryad.goto(-140, 100)
            if i == count_win and streamer:
                left_ryad.shape(shape_win)
            else:
                left_ryad.shape(choice(sp))
            left_ryad.st()
            left_ryad.goto(-140, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-160, 260)
            write(f'Выигрыш: {str(int(bet) * 10)}!', font=('aerial', 50, 'normal'))
            balance += bet * 10
            break

        if i < count_c:
            center_ryad.goto(0, -200)
            center_ryad.ht()
            center_ryad.goto(0, 100)
            if i == count_win and streamer:
                center_ryad.shape(shape_win)
            else:
                center_ryad.shape(choice(sp))
            center_ryad.st()
            center_ryad.goto(0, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-160, 260)
            write(f'Выигрыш: {str(int(bet) * 10)}!', font=('aerial', 50, 'normal'))
            balance += bet * 10
            break

        if i < count_r:
            right_ryad.goto(140, -200)
            right_ryad.ht()
            right_ryad.goto(140, 100)
            if i == count_win and streamer:
                right_ryad.shape(shape_win)
            else:
                right_ryad.shape(choice(sp))
            right_ryad.st()
            right_ryad.goto(140, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-160, 260)
            write(f'Выигрыш: {str(int(bet) * 10)}!', font=('aerial', 50, 'normal'))
            balance += bet * 10
            break
        i += 1
    if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
        pass
    elif int(balance) != 0:
        write('Проиграл!', font=('aerial', 50, 'normal'))
    else:
        write('Сегодня без завоза!', font=('aerial', 40, 'normal'))
        Screen().ontimer(Screen().bye, 3000)
    if auto_spin == 0:
        action = False
        Screen().listen()
    else:
        slot(shapes, l_t, c_t, r_t)


# рисование аппарата и каркаса для таблиц
ht()
speed(0)
pu()
goto(-210, -250)
pd()
goto(-210, 250)
goto(210, 250)
goto(210, -250)
goto(-210, -250)
pu()
goto(-210, 150)
pd()
goto(210, 150)
goto(70, 150)
goto(70, -250)
goto(-70, -250)
goto(-70, 150)
pu()
goto(210, -150)
pd()
fillcolor('black')
begin_fill()
goto(360, -150)
goto(360, 100)
goto(310, 100)
goto(310, -100)
goto(210, -100)
end_fill()
pu()
goto(335, 50)
pd()
fillcolor('red')
begin_fill()
circle(50)
end_fill()
pu()
goto(-110, 170)
write('БУРДА', font=('aerial', 50, 'normal'))
goto(225, 160)
write('АВТОСПИН', font=('aerial', 30, 'normal'))
rectangle(-470, 90, 250, 60)
goto(-460, 100)
write('Баланс:', font=('aerial', 25, 'normal'))
goto(-320, 100)
write(str(int(balance)), font=('aerial', 25, 'normal'))
rectangle(-470, -10, 250, 60)
goto(-460, 0)
write('Ставка:', font=('aerial', 25, 'normal'))
goto(-320, 0)
write(str(int(bet)), font=('aerial', 25, 'normal'))
rectangle(-470, -110, 250, 60)
goto(-460, -100)
write('Скорость:', font=('aerial', 25, 'normal'))
goto(-280, -100)
write(str(int(speedy)), font=('aerial', 25, 'normal'))
rectangle(220, -240, 130, 80, 'green')
goto(228, -220)
write('ВЫВОЗ', font=('aerial', 25, 'normal'))
Screen().listen()


def left_mouse_click(x, y):  # нажатия мыши: спин, ставка, скорость, вывоз
    global action
    global bet
    global balance
    if 285 <= x <= 385 and 50 <= y <= 150 and not action:
        global auto_spin
        ceil_spins = int(int(balance)/int(bet))
        auto_spin = numinput('Автоспины', 'Введите количество спинов:\n По умалочанию 1', 1, 1, ceil_spins)
        while auto_spin == None:
            auto_spin = numinput('Автоспины', 'Введите количество спинов:\n По умалочанию 1', 1, 1, ceil_spins)
        slot(shapes, l_t, c_t, r_t)
    if -470 <= x <= -220 and -10 <= y <= 50 and not action:
        bet = numinput('Ставка',
                       'Выберите ставку автомата:\nПо '
                       'умолчанию ставка 1', 1, 1, int(balance))
        while bet == None:
            bet = numinput('Ставка',
                           'Выберите ставку автомата:\nПо '
                           'умолчанию ставка 1', 1, 1, int(balance))
        Screen().listen()
    if -470 <= x <= -220 and -110 <= y <= -50 and not action:
        global speedy
        speedy = numinput('Скорость',
                          'Выберите скорость автомата:\n1 - самая медленная\n10 - быстрая\n0 - моментальная\nПо '
                          'умолчанию скорость 3', 3, 0, 10)
        while speedy == None:
            speedy = numinput('Скорость',
                              'Выберите скорость автомата:\n1 - самая медленная\n10 - быстрая\n0 - моментальная\nПо '
                              'умолчанию скорость 3', 3, 0, 10)
        Screen().listen()
    if 220 <= x <= 350 and -240 <= y <= -160 and not action:
        rectangle(-160, 260, 600, 100, 'white')
        percent_win = int((float(balance/100)-1)*100)
        if percent_win > 0:
            percent_win = '+' + str(percent_win)
        goto(-240, 260)
        write(f'Вы вывели {int(balance)}! Это {percent_win}% к депозиту', font=('aerial', 30, 'normal'))
        Screen().ontimer(Screen().bye, 3000)


def space_click():  # спин через пробел
    if not action:
        slot(shapes, l_t, c_t, r_t)


def streamer_mode(): # режим стримера
    global streamer
    if not action:
        if streamer:
            pu()
            rectangle(200, 100, 10, 10, 'red')
            streamer = False
            return 0
        else:
            pu()
            rectangle(200, 100, 10, 10, 'green')
            streamer = True


Screen().onkey(space_click, 'space')
Screen().onkey(streamer_mode, 's')
Screen().onclick(left_mouse_click)
done()
