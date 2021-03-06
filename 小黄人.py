# draw95
import turtle as t

t.pensize(4)
t.speed(10)


# =======头======
def head():
    t.penup()
    t.fillcolor("#FFEE26")
    t.goto(-130, 10)
    t.pendown()
    t.begin_fill()
    t.seth(81)
    t.fd(90)
    t.seth(100)
    t.circle(-500, 3)
    t.circle(-100, 10)
    t.circle(-200, 25)
    t.circle(-110, 20)
    t.circle(-140, 30)
    t.circle(-180, 30)
    t.circle(-200, 20)
    t.circle(-140, 10)
    t.circle(-160, 50)
    t.seth(85)
    t.fd(-148)
    t.seth(-112)
    t.circle(-250, 14)
    t.fd(200)
    t.right(80)
    t.fd(190)
    t.seth(110)
    t.circle(-200, 7)
    t.circle(-130, 30)
    t.end_fill()


# =======肚兜======
# ====后脚=====
def houjiao():
    t.begin_fill()

    t.penup()
    t.goto(-120, -250)
    t.pendown()
    t.fillcolor("#030003")
    t.setheading(-135)
    t.circle(60, 20)
    t.fd(35)
    t.circle(20, 160)
    t.circle(100, 10)
    t.fd(20)
    t.goto(-120, -250)

    t.end_fill()


def houtui():
    t.begin_fill()
    t.color("black", "#0045D9")
    t.penup()
    t.goto(-50, -300)
    t.pendown()
    t.setheading(-150)
    t.circle(-80, 60)
    t.setheading(90)
    t.circle(-40, 67)
    t.seth(-30)
    t.goto(-50, -300)
    t.end_fill()


# ===衣服====
def yifu():
    t.begin_fill()

    t.penup()
    t.goto(-45, -70)
    t.pendown()
    t.fillcolor("#0045D9")
    t.setheading(-15)

    t.circle(500, 5)
    t.circle(400, 26)

    t.seth(-112)
    t.circle(-250, 7)
    t.seth(-69)
    t.circle(-250, 7)
    t.right(15)
    t.circle(-320, 18)
    t.circle(-330, 10)
    t.fd(80)
    t.right(81)
    t.fd(190)
    t.seth(141)
    t.circle(-180, 15)
    t.circle(-150, 30)
    t.right(6)
    t.circle(-90, 15)
    t.seth(-45)
    t.circle(50, 10)
    t.seth(-30)
    t.circle(200, 20)
    t.circle(150, 10)
    t.seth(92)
    t.circle(500, 10)

    t.setheading(75)
    t.goto(-45, -70)

    t.end_fill()


# =====口袋=====
def koudai():
    t.begin_fill()
    t.penup()
    t.goto(52, -120)
    t.pendown()
    t.fillcolor("#BFC5AD")
    t.seth(-15)
    t.circle(200, 25)
    t.seth(-88)
    t.circle(-200, 18)
    t.seth(-150)
    t.circle(-90, 5)
    t.right(10)
    t.circle(-90, 45)
    t.right(20)
    t.circle(-50, 50)
    t.goto(52, -120)
    t.end_fill()

    t.begin_fill()
    t.penup()
    t.goto(70, -155)
    t.pendown()
    t.fillcolor("#0045D9")
    t.circle(-25)
    t.end_fill()

    t.penup()
    t.goto(120, -160)
    t.pencolor("#5C7F58")
    t.pendown()
    t.seth(180)
    t.fd(20)
    t.right(60)
    t.circle(6, 340)
    t.pencolor("black")


# ======右手======
def youshou():
    t.begin_fill()
    t.fillcolor("#FFEE26")
    t.pencolor("black")
    t.penup()
    t.goto(-130, 10)
    t.pendown()
    t.goto(-130, -25)
    t.seth(130)
    t.circle(130, 20)
    t.circle(20, 50)
    t.right(10)
    t.pencolor("black")
    t.circle(120, 20)
    t.circle(90, 30)
    t.seth(-25)
    t.fd(33)
    t.seth(40)
    t.fd(35)
    t.circle(-30, 30)
    t.circle(-15, 60)
    t.right(5)
    t.fd(80)
    t.end_fill()


def youzhua():
    t.begin_fill()
    t.fillcolor("#BEC5B3")
    t.penup()
    t.goto(-255, -40)
    t.pendown()
    t.seth(-120)
    t.circle(-100, 10)
    t.right(60)
    t.circle(20, 60)
    t.circle(10, 90)
    t.right(60)
    t.fd(10)
    t.circle(20, 100)
    t.left(10)
    t.fd(15)
    t.seth(50)
    t.circle(-60, 30)
    t.left(60)
    t.circle(10, 60)
    t.fd(5)
    t.right(90)
    t.fd(21)
    t.goto(-255, -40)
    t.end_fill()
    # 黑色


# ======前腿====
def qiantui():
    t.begin_fill()

    t.penup()
    t.goto(-50, -295)
    t.pendown()
    t.fillcolor("#0045D9")
    # t.fillcolor("red")
    t.setheading(-30)
    t.fd(127)
    t.seth(62)
    t.fd(60)
    t.seth(155)
    t.circle(300, 22)
    t.pencolor("#0045D9")
    t.goto(-49, -294)
    t.pencolor("black")
    t.goto(-50, -295)

    t.end_fill()


# ====前脚======
def qianjiao():
    t.begin_fill()

    t.penup()
    t.goto(140, -260)
    t.pendown()
    t.fillcolor("#030003")
    t.seth(110)
    t.circle(20, 120)
    t.seth(-120)
    t.circle(500, 12)
    t.circle(20, 82)
    t.goto(140, -260)

    t.end_fill()


def jiaodi():
    t.begin_fill()

    t.penup()
    t.goto(140, -260)
    t.pendown()
    t.fillcolor("#BFC5AD")
    t.seth(150)
    t.circle(20, 95)
    t.seth(-120)
    t.circle(500, 10)
    t.seth(-30)
    t.circle(-15, 60)
    t.seth(-112)
    t.fd(17)
    t.left(90)
    t.circle(30, 90)

    t.seth(70)
    t.circle(-50, 25)
    t.fd(7)
    t.circle(66, 60)
    t.circle(40, 10)
    t.goto(140, -260)

    t.end_fill()


def xie():
    t.pencolor("black")
    t.penup()
    t.goto(83, -353)
    t.pendown()
    t.seth(-30)
    t.fd(31)


def yanjing():
    t.begin_fill()

    t.penup()
    t.goto(-125, 140)
    t.pendown()
    t.fillcolor("#000000")
    t.pencolor("black")
    t.seth(100)
    t.circle(-25, 80)
    t.seth(40)
    t.circle(-200, 23)
    t.seth(-90)
    t.fd(45)
    t.seth(195)
    t.circle(200, 27)
    t.seth(150)
    t.circle(-12, 90)
    t.goto(-125, 140)
    t.end_fill()
    # 黑色
    t.begin_fill()

    t.penup()
    t.goto(-39, 205)
    t.pendown()
    t.fillcolor("#E6E8FA")
    t.setheading(90)
    t.circle(-8, 180)
    t.seth(-90)
    t.fd(45)
    t.circle(-8, 180)
    t.goto(-39, 205)
    t.end_fill()
    # 银色
    t.begin_fill()

    t.penup()
    t.goto(-23, 160)
    t.pendown()
    t.fillcolor("#E6E8FA")
    t.seth(-78)
    t.circle(85, 130)
    t.goto(-23, 160)
    t.end_fill()
    # 银色
    t.begin_fill()
    t.penup()
    t.goto(-23, 190)
    t.pendown()
    t.fillcolor("#E6E8FA")
    t.seth(-90)
    t.circle(90)
    t.end_fill()
    # 银色
    t.begin_fill()
    t.penup()
    t.goto(155, 205)
    t.pendown()
    t.fillcolor("#000000")
    t.seth(-15)
    t.circle(-100, 20)
    t.seth(-60)
    t.circle(-105, 25)
    t.seth(160)
    t.circle(200, 13.5)
    t.seth(75)
    t.circle(90, 20)
    t.goto(155, 205)
    t.end_fill()
    # 黑色
    t.begin_fill()
    t.penup()
    t.goto(128, 195)
    t.pendown()
    t.fillcolor("#ffffff")
    t.circle(60)
    t.end_fill()
    # 白色
    t.begin_fill()
    t.penup()
    t.goto(110, 150)
    t.pendown()
    t.fillcolor("#000000")
    t.seth(70)
    t.circle(70, 110)
    t.seth(20)
    t.circle(-60, 150)
    t.end_fill()
    # 黑色
    t.begin_fill()
    t.penup()
    t.goto(25, 210)
    t.pendown()
    t.fillcolor("#B85300")
    t.circle(20)
    t.end_fill()
    # 白色
    t.begin_fill()
    t.penup()
    t.goto(32, 204)
    t.pendown()
    t.fillcolor("#000000")
    t.circle(8)
    t.end_fill()
    # 黑色


# ====嘴巴=====
def zui():
    t.begin_fill()
    t.penup()

    t.fillcolor("#FF1305")
    t.goto(-25, 60)
    t.pendown()
    t.right(30)
    t.circle(-30, 70)
    t.left(5)
    t.circle(300, 20)
    t.circle(120, 20)
    t.seth(-70)
    t.circle(-50, 60)
    t.left(10)
    t.circle(-100, 30)
    t.circle(-60, 35)
    t.right(8)
    t.circle(-200, 15)
    t.circle(-100, 15)
    t.circle(-50, 25)
    t.circle(-200, 10)
    t.goto(-25, 60)
    t.end_fill()


# =====衣领====
def yiling():
    t.begin_fill()
    t.penup()

    t.fillcolor("#0045D9")
    t.goto(-130, 10)
    t.pendown()
    t.setheading(-59)
    t.circle(225, 38)
    t.setheading(-100)
    t.forward(28)
    t.setheading(160)
    t.circle(-255, 35)
    t.setheading(90)
    t.circle(-30, 45)
    t.goto(-130, 10)
    t.end_fill()


# ====扣子====
def zuokou():
    t.begin_fill()
    t.penup()

    t.fillcolor("#FFFFFF")
    t.goto(-40, -80)
    t.pendown()
    t.seth(0)
    t.circle(-9, 360)
    t.end_fill()


# ====左衣领====
def zuoyl():
    t.begin_fill()
    t.penup()

    t.fillcolor("#0045D9")
    t.goto(191, -40)
    t.pendown()
    t.seth(-112)
    t.circle(-250, 17)
    t.seth(-68)
    t.fd(25)
    t.seth(49)
    t.circle(130, 36)
    t.goto(191, -40)
    t.end_fill()

    t.begin_fill()
    t.penup()
    t.fillcolor("#FFFFFF")
    t.goto(169, -93)
    t.pendown()
    t.seth(0)
    t.circle(-9, 360)
    t.end_fill()


# ====左手====
def zuoshou():
    t.begin_fill()
    t.penup()

    t.fillcolor("#FFEE26")
    t.goto(195, -56)
    t.pendown()
    t.seth(-8)
    t.circle(150, 15)
    t.circle(25, 40)
    t.left(2)
    t.fd(60)
    t.right(85)
    t.fd(28)
    t.right(92)
    t.fd(45)
    t.circle(-100, 20)
    t.circle(-80, 40)
    t.circle(80, 13)
    t.goto(195, -56)
    t.end_fill()


# ====左掌====
def zuozhua():
    t.begin_fill()
    t.penup()

    t.fillcolor("#BEC5B3")

    t.goto(295, 25)
    t.pendown()
    t.seth(55)
    t.fd(-30)
    t.right(110)
    t.circle(80, 38)
    t.left(90)
    t.fd(10)
    t.seth(20)
    t.circle(100, 30)
    t.circle(35, 180)
    t.goto(295, 25)
    t.end_fill()

    t.begin_fill()
    t.fillcolor("#BEC5B3")
    t.seth(140)
    t.circle(-15)
    t.end_fill()


# ====

head()
zui()
youshou()
yanjing()
youzhua()
houjiao()
houtui()
yifu()
koudai()
qiantui()
qianjiao()
jiaodi()
xie()
yiling()
zuokou()
zuoshou()
zuozhua()
zuoyl()
t.penup()
t.goto(80, -40)
t.pendown()
t.seth(100)
t.circle(90, 85)

t.done()