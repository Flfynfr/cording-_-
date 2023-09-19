import turtle as trtl
#Five Turtles for Pong
#left paddle
Lup = trtl.Turtle()
Lown = trtl.Turtle()
#right paddle
Rup = trtl.Turtle()
Rown = trtl.Turtle()

Rup.up()
Rown.up()
Lup.up()
Lown.up()

v = int(input("turt speed? (higher speed is less accurate)"))

#right go right
Rup.setpos(300,30)
Rown.setpos(300,-30)
Lup.setpos(-300,30)
Lown.setpos(-300,-30)

Rup.down()
Rown.down()
Lup.down()
Lown.down()

Rup.left(-90)
Rown.left(-90)
Lup.right(-90)
Lown.right(-90)

Rup.pensize(10)
Rown.pensize(10)
Lup.pensize(10)
Lown.pensize(10)


while 1 == 1:
    Rup.left(180)
    Rown.left(180)
    Lup.left(180)
    Lown.left(180)

    Rup.pencolor("#000000")
    Lown.pencolor("#000000")
    Lup.pencolor("#FFFFFF")
    Rown.pencolor("#FFFFFF")

    for x in range(100):
        Rup.forward(v)
        Rown.forward(v)
        Lup.forward(v)
        Lown.forward(v)

    Rup.left(180)
    Rown.left(180)
    Lup.left(180)
    Lown.left(180)

    Lup.pencolor("#000000")
    Rown.pencolor("#000000")
    Rup.pencolor("#FFFFFF")
    Lown.pencolor("#FFFFFF")
    
    for x in range(100):
        Rup.forward(v)
        Rown.forward(v)
        Lup.forward(v)
        Lown.forward(v)

wn= trtl.Screen()
wn.exitonclick


