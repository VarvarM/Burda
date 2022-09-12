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


def slot(sp, left_ryad, center_ryad, right_ryad):
    global bet
    global balance
    global speedy
    goto(-160, 260)
    pd()
    color('white')
    fillcolor('white')
    begin_fill()
    for i in range(2):
        fd(600)
        lt(90)
        fd(100)
        lt(90)
    end_fill()
    pu()
    color('black')
    goto(-330, 95)
    pd()
    color('white')
    fillcolor('white')
    begin_fill()
    for i in range(2):
        fd(100)
        lt(90)
        fd(50)
        lt(90)
    end_fill()
    pu()
    color('black')
    goto(-320, 100)
    write(str(int(balance)), font=('aerial', 25, 'normal'))
    goto(-330, -5)
    pd()
    color('white')
    fillcolor('white')
    begin_fill()
    for i in range(2):
        fd(100)
        lt(90)
        fd(50)
        lt(90)
    end_fill()
    pu()
    color('black')
    goto(-320, 0)
    write(str(int(bet)), font=('aerial', 25, 'normal'))
    while int(bet) > int(balance):
        goto(-160, 260)
        write('Не хватает средств', font=('aerial', 40, 'normal'))
        bet = numinput('Ставка',
                       'Выберите ставку автомата:\nПо '
                       'умолчанию ставка 1', 1, 1, int(balance))
        goto(-160, 260)
        pd()
        color('white')
        fillcolor('white')
        begin_fill()
        for i in range(2):
            fd(600)
            lt(90)
            fd(100)
            lt(90)
        end_fill()
        pu()
        color('black')
    speedy = numinput('Скорость',
                      'Выберите скорость автомата:\n1 - самая медленная\n10 - быстрая\n0 - моментальная\nПо '
                              'умолчанию скорость 3', int(speedy), 0, 10)
    balance -= int(bet)
    goto(-330, 95)
    pd()
    color('white')
    fillcolor('white')
    begin_fill()
    for i in range(2):
        fd(100)
        lt(90)
        fd(50)
        lt(90)
    end_fill()
    pu()
    color('black')
    goto(-320, 100)
    write(str(int(balance)), font=('aerial', 25, 'normal'))
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
    while i < count_l or i < count_c or i < count_r:
        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-160, 260)
            write(f'Выигрыш: {str(int(bet)*10)}!', font=('aerial', 50, 'normal'))
            balance += bet * 10
            break

        if i < count_l:
            left_ryad.goto(-140, -200)
            left_ryad.ht()
            left_ryad.goto(-140, 100)
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
        Screen().ontimer(Screen().bye, 1000)


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
goto(240, 160)
write('СПИН', font=('aerial', 40, 'normal'))
goto(-470, 150)
pd()
for i in range(2):
    fd(250)
    rt(90)
    fd(60)
    rt(90)
pu()
goto(-460, 100)
write('Баланс:', font=('aerial', 25, 'normal'))
goto(-470, 50)
pd()
for i in range(2):
    fd(250)
    rt(90)
    fd(60)
    rt(90)
pu()
goto(-460, 0)
write('Ставка:', font=('aerial', 25, 'normal'))

slot(shapes, l_t, c_t, r_t)


def left_mouse_click(x, y):
    if 285 <= x <= 385 and 50 <= y <= 150:
        slot(shapes, l_t, c_t, r_t)
    if -470 <= x <= -220 and -10 <= y <= 50:
        global bet
        global balance
        bet = numinput('Ставка',
                        'Выберите ставку автомата:\nПо '
                        'умолчанию ставка 1', 1, 1, int(balance))


Screen().onclick(left_mouse_click)
listen()
done()
