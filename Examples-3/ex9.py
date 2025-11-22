import turtle

def drawFilledRectangle(x,y,w,h,pencolor,fillcolor):
    t=turtle.Turtle()
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.up()
    t.goto(x,y)
    t.begin_fill()
    t.down()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
    t.end_fill()

def drawRectangle2(w,h,pencolor):
    t=turtle.Turtle()
    t.pencolor(pencolor)
    t.up()
    t.goto(0,0)
    t.down()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
def drawDot(x,y,diameter,pencolor):
    t=turtle.Turtle()
    t.pencolor(pencolor)
    t.up()
    t.goto(x,y)
    t.down()
    t.dot(diameter)

drawFilledRectangle(0,0,150,25,"black","red")    
drawFilledRectangle(0,25,150,50,"blue","yellow")
drawFilledRectangle(0,75,150,25,"black","red")
drawDot(75,50,40,"red")
turtle.done()

    
