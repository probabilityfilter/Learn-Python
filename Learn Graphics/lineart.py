from graphics import *

def main(W):
    win = GraphWin("Line Art", W, W)
    win.setBackground("black")
    ratio = 0.25

    drawLines(win, "v", 0, 0, W, W)
    inset(win, W, ratio)

    win.getMouse() # pause for click in window
    win.close

def drawLines(windowObj, orientation, x1, y1, x2, y2):
        for x in range(x1,x2,10):
            if orientation == "v":
                aLine = Line(Point(x,y1), Point(x,y2))
            else:
                aLine = Line(Point(x1,x), Point(x2,x))
            aLine.setWidth(2)
            aLine.setOutline("white")
            aLine.draw(windowObj)

def inset(windowObj, windowWd, r):
    start = int(windowWd * r)
    square = Rectangle(Point(start,start), Point(windowWd - start,windowWd - start))
    square.setFill("black")
    square.setWidth(2)
    square.setOutline("white")
    square.draw(windowObj)
    drawLines(windowObj, "h", start, start, windowWd - start, windowWd - start)

windowWidth = input("Enter window size: ")
main(int(windowWidth))