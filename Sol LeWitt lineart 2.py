from graphics import *
import math

def main(W):
    win = GraphWin("Line Art", W, W)
    win.setBackground("black")
    ratio = 0.25

    drawVLines(win, 0, 0, W, W)
    inset(win, W, ratio)

    win.getMouse() # pause for click in window
    win.close

def drawVLines(windowObj, x1, y1, x2, y2):
    for x in range(x1,x2,10):
        aLine = Line(Point(x,y1), Point(x,y2))
        aLine.setWidth(2)
        aLine.setOutline("white")
        aLine.draw(windowObj)

def drawHLines(windowObj, windowWd, insetPoint):
    cirDia = windowWd-(2*insetPoint)
    for x in range(0,cirDia,10):
        y1 = math.sqrt((((cirDia/2)+1)**2) - ((x-cirDia/2)**2)) + cirDia
        y2 = - math.sqrt((((cirDia/2)+1)**2) - ((x-cirDia/2)**2)) + cirDia
        p1 = Point(y1,x+(cirDia/2))
        p2 = Point(y2,x+(cirDia/2))
        l1 = Line(Point(windowWd-y1,x+(cirDia/2)), p1)
        l2 = Line(Point(windowWd-y2,x+(cirDia/2)), p2)
        l1.setWidth(2)
        l1.setOutline("white")
        l2.setWidth(2)
        l2.setOutline("white")
        l1.draw(windowObj)
        l2.draw(windowObj)

def inset(windowObj, windowWd, r):
    start = int(windowWd * r)
    shape = Oval(Point(start,start), Point(windowWd - start,windowWd - start))
    shape.setFill("black")
    shape.setWidth(2)
    shape.setOutline("white")
    shape.draw(windowObj)
    drawHLines(windowObj, windowWd, start)

windowWidth = input("Enter window size: ")
main(int(windowWidth))