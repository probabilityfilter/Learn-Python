from graphics import *

def main():
    W = 400
    H = 200
    win = GraphWin("Night Sky", W, H)
    win.setBackground("black")

    ground = Rectangle(Point(0,H-30), Point(W,H))
    ground.setFill("gray")
    ground.draw(win)

    win.getMouse() # pause for click in window
    win.close()

main()
