from graphics import *

def main(circleCount):
    W = 400
    H = 400
    win = GraphWin("My Circle", W, H)
    win.setBackground("white")
    circleRadius = int(W/(2*circleCount))

    for x in range(circleRadius, W, circleRadius*2):
        for y in range(circleRadius, H, circleRadius*2):
            c = Circle(Point(x,y), circleRadius)
            colorGrad = getColor(x,y,400)
            c.setFill(color_rgb(colorGrad[0],colorGrad[1],colorGrad[2]))
            c.draw(win)

    win.getMouse() # pause for click in window
    win.close()

def getColor(px,py,winSize):
    c1 = (0,0,0)
    c2 = (255,255,255)
    R = int(((c2[0]-c1[0])*px/winSize)+c1[0])
    G = int(((c2[1]-c1[1])*px/winSize)+c1[1])
    B = int(((c2[2]-c1[2])*px/winSize)+c1[2])
    return R,G,B


x = input("How many circles do you want? ") 
main(int(x))