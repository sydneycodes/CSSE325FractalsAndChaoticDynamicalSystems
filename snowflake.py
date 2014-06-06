#
# Sydney Satchwill
# Chaos Game
# CSSE325 Spring 2014
#
from Tkinter import *
from random import randint
import math
import time

class KochSnowflake(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        self.insertSnowflake()
    
    def initUI(self):
      
        self.parent.title("Koch Snowflake")
        self.pack(fill=BOTH, expand=1)
        
    def insertSnowflake(self):
        canvas = Canvas(self)
        n = randint(5, 10)

        def left():
            return [10, 410, 310, 10]
        def bottom():
            return [10, 410, 610, 410]
        def right():
            return [310, 10, 610, 410]
        
        points = { 1 : left, 2 : bottom, 3 : right,}
        
        def drawSegments(seg):
            slope = 3*math.sqrt(3)
            dx = (seg[2]-seg[0])/4
            print(dx)
            dy = math.sqrt(pow(dx, 2)+pow(0.5*dx, 2))
            print(dy)
            canvas.create_line(seg[0], seg[1], seg[0]+dx, seg[1])
            print(seg[0], seg[1], seg[0]+dx, seg[1])
            canvas.create_line(seg[0]+dx, seg[1], seg[0]+1.5*dx, seg[1]-dy)
            print(seg[0]+dx, seg[1], seg[0]+1.5*dx, seg[1]+dy)
            canvas.create_line(seg[0]+1.5*dx, seg[1]-dy, seg[0]+2*dx, seg[1])
            print(seg[0]+1.5*dx, seg[1]-dy, seg[0]+2+dx, seg[1])
            canvas.create_line(seg[0]+2*dx, seg[1], seg[2], seg[3])
            print(seg[0]+2+dx, seg[1], seg[2], seg[3])

        drawSegments(left())        
        
        canvas.pack(fill=BOTH, expand=1)
           
        
def main():
  
    ksWindow = Tk()
    ksWindow.geometry("620x430+300+300")
    app = KochSnowflake(ksWindow)
    ksWindow.mainloop()  
if __name__ == '__main__':
    main()
