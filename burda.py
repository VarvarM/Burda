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


def slot(sp, left_ryad, center_ryad, right_ryad):
    speedy = textinput(title='Скорость',
                       prompt='Выберите скорость автомата:\n1 - самая медленная\n10 - быстрая\n0 - моментальная\nПо '
                              'умолчанию скорость 3')
    speed(0)
    ht()
    goto(-120, 260)
    pd()
    color('white')
    fillcolor('white')
    begin_fill()
    for i in range(2):
        fd(400)
        lt(90)
        fd(200)
        lt(90)
    end_fill()
    pu()
    color('black')
    count_l = randint(1, 10)
    count_c = randint(1, 10)
    count_r = randint(1, 10)
    left_ryad.ht()
    left_ryad.pu()
    left_ryad.speed(int(speedy))
    center_ryad.ht()
    center_ryad.pu()
    center_ryad.speed(int(speedy))
    right_ryad.ht()
    right_ryad.pu()
    right_ryad.speed(int(speedy))
    i = 1
    left_ryad.goto(-140, 100)
    left_ryad.shape(choice(sp))
    left_ryad.st()
    left_ryad.goto(-140, -40)

    center_ryad.goto(0, 100)
    center_ryad.shape(choice(sp))
    center_ryad.st()
    center_ryad.goto(0, -40)

    right_ryad.goto(140, 100)
    right_ryad.shape(choice(sp))
    right_ryad.st()
    right_ryad.goto(140, -40)
    while i < count_l or i < count_c or i < count_r:
        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-110, 270)
            write('ВЫВОЗ!', font='aerial, 50')
            break

        if i < count_l:
            left_ryad.goto(-140, -200)
            left_ryad.ht()
            left_ryad.goto(-140, 100)
            left_ryad.shape(choice(sp))
            left_ryad.st()
            left_ryad.goto(-140, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-110, 270)
            write('Вывоз!', font='aerial, 50')
            break

        if i < count_c:
            center_ryad.goto(0, -200)
            center_ryad.ht()
            center_ryad.goto(0, 100)
            center_ryad.shape(choice(sp))
            center_ryad.st()
            center_ryad.goto(0, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-110, 270)
            write('Вывоз!', font='aerial, 50')
            break

        if i < count_r:
            right_ryad.goto(140, -200)
            right_ryad.ht()
            right_ryad.goto(140, 100)
            right_ryad.shape(choice(sp))
            right_ryad.st()
            right_ryad.goto(140, -40)

        if left_ryad.shape() == center_ryad.shape() == right_ryad.shape():
            goto(-110, 270)
            write('Вывоз!', font='aerial, 50')
            break
        i += 1


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
ht()
write('БУРДА', font='aerial, 50')
goto(240, 160)
write('ДОДЕП', font='aerial, 40')

slot(shapes, l_t, c_t, r_t)


def left_mouse_click(x, y):
    if 285 <= x <= 385 and 50 <= y <= 150:
        slot(shapes, l_t, c_t, r_t)


Screen().onclick(left_mouse_click)
listen()

done()
