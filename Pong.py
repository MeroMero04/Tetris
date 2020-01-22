import turtle  # variable and import setup
import random

wn = turtle.Screen()
point_pl1 = 0
point_pl2 = 0
style_boi = ('Helvetica ', 12, 'normal')
# global break_var
break_var = True
wn.register_shape("rectangle", ((-2, 65), (-2, -65), (2, -65), (2, 65)))
wn.register_shape('circle_small', ((3, -2), (2, -3), (-2, -3), (-3, -2), (-3, 2), (-2, 3), (2, 3), (3, 2)))
wn.register_shape("rectangle_large", ((-4, 130), (-4, -120), (4, -130), (4, 130)))
colors = ["red", "white", "blue", "#4FBF4B", "#E429CD", "# FBF410"]

# area setup
wn.bgcolor('white')
pl1 = turtle.Turtle()
pl2 = turtle.Turtle()
pl1.up()
ball = turtle.Turtle()
pl1.color('white')
pl2.color("white")
pl1.color(random.choice(colors))
pl1.pensize(2)
pl1.speed(-1)
ball.up()
pl1.left(90)
pl1.fd(285)
pl1.right(90)
pl1.backward(315)
pl1.down()

for itr in range(2):
    pl1.fd(630)
    pl1.right(90)
    pl1.fd(570)
    pl1.right(90)
pl1.up()
pl1.color('white')
pl1.setpos(0, 0)
ball.shape('circle_small')
pl1.up()
pl2.up()
pl1.speed(-1)
pl2.speed(-1)
pl1.shape("rectangle")
pl2.shape("rectangle")
pl1.fd(-300)
pl1.setheading(90)
pl2.fd(300)
pl2.setheading(90)
wn.bgcolor('black')
bl_lst = [0, 180]
ball.right(random.choice(bl_lst))
pl1.color('white')
ball.color('white')
ball.speed(2)
ball.right(360)
ball.speed(-1)
speed = 6

# functions

while break_var:

    ball.fd(speed)


    def check():
        # global break_var
        if point_pl1 == 3:
            print("player 1 wins")
            # break_var = False
        if point_pl2 == 3:
            print('player 2 wins')
            # break_var = False


    def reset():
        pl1.setpos(-300, 0)
        pl2.setpos(300, 0)
        ball.setheading(0)
        ball.setpos(0, 0)


    def timer():
        ball.speed(2)
        ball.right(360)
        ball.speed(-1)
        ball.right(random.choice(bl_lst))


    def hard_reset():
        point_pl1 = 0
        point_pl2 = 0
        pl1.setpos(-300, 0)
        pl2.setpos(300, 0)
        ball.setheading(0)
        ball.setpos(0, 0)
        ball.speed(2)
        ball.right(360)
        ball.speed(-1)
        ball.right(random.choice(bl_lst))


    def up1():
        if pl1.pos()[1] < 205:
            pl1.setheading(90)
            pl1.fd(20)


    def down1():
        if pl1.pos()[1] > -205:
            pl1.setheading(270)
            pl1.fd(20)


    def up2():
        if pl2.pos()[1] < 205:
            pl2.setheading(90)
            pl2.fd(20)


    def down2():
        if pl2.pos()[1] > -205:
            pl2.setheading(270)
            pl2.fd(20)


    def r():
        pl1.shape(rectangle_large)


    if ball.pos()[1] > (pl2.pos()[1] - 65) and ball.pos()[1] < (pl2.pos()[1] + 65) and ball.pos()[0] > 295:
        ball.setheading(random.randrange(120, 240))
        ball.fd(5)
        speed = random.randrange(6, 11)

    if ball.pos()[1] > (pl1.pos()[1] - 65) and ball.pos()[1] < (pl1.pos()[1] + 65) and ball.pos()[0] < -295:
        ball.setheading(180 - abs(random.randrange(120, 240)))
        ball.fd(5)
        speed = random.randrange(6, 11)

    if ball.pos()[1] > 283:
        if ball.heading() >= 90 and ball.heading() < 180:
            ball.right(2 * (ball.heading() - 180) + 0)
        elif ball.heading() < 90 and ball.heading() > 0:
            ball.right(2 * (ball.heading() - 180) + 0)

    if ball.pos()[1] < -283:
        if ball.heading() < 360 and ball.heading() >= 270:
            ball.right(2 * (ball.heading() - 180) + 0)
        elif ball.heading() < 270 and ball.heading() > 180:
            ball.right(2 * (ball.heading() - 180) + 0)

    if ball.pos()[0] > 313:
        wn.update()
        point_pl1 += 1
        check()
        ball.setpos(0, 320)
        ball.clear()
        ball.write((str(point_pl1) + "               -               " + str(point_pl2)), font=style_boi,
                   align='center')
        reset()

    if ball.pos()[0] < -313:
        wn.update()
        point_pl2 += 1
        check()
        ball.setpos(0, 320)
        ball.clear()
        ball.write((str(point_pl1) + "               -               " + str(point_pl2)), font=style_boi,
                   align='center')
        reset()
        timer()

    # listen and loop commands
    wn.onkey(up1, "w")
    wn.onkey(down1, "s")
    wn.onkey(up2, "Up")
    wn.onkey(down2, "Down")
    wn.onkey(r, "r")

    wn.listen()
    wn.mainloop()