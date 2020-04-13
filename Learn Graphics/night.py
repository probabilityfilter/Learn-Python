from graphics import *

def main():
    W = 800
    H = 400
    win = GraphWin("Night Sky", W, H)
    win.setBackground("black")

    gndHt = H - 30
    ground = Rectangle(Point(0,gndHt), Point(W,H))
    ground.setFill("gray")
    ground.draw(win)

    clickPoint = win.getMouse()
    while clickPoint.getY() < gndHt:
        drawStar(win, clickPoint)
        clickPoint = win.getMouse()

    clickPtMoon = win.getMouse()
    drawMoon(win, clickPtMoon)

    win.getMouse() # pause for click in window
    win.close()

def drawStar(sky, starLoc):
    #star = Circle(Point, 10)
    x = starLoc.getX()
    y = starLoc.getY()
    star = Polygon(Point(x-10,y), Point(x-3,y-3), Point(x,y-10), Point(x+3,y-3), Point(x+10,y), Point(x+3,y+3), Point(x,y+10), Point(x-3,y+3))
    star.setFill("white")
    star.draw(sky)

def drawMoon(sky, moonLoc):
    r = 20
    moon = Circle(moonLoc, r)
    moon.setFill("white")
    moon.draw(sky)
    moonCover = Circle(Point(moonLoc.getX()-(r*2), moonLoc.getY()), r)
    moonCover.setFill("black")
    moonCover.draw(sky)

    sky.getMouse()
    for i in range(0,4*r):
        moonCover.move(1,0)
        update(15)

main()
