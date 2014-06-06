# Sydney Satchwill
# Project 3 - Fractional Brownian Motion Simulator
# CSSE325 Spring 2014
#

from Tkinter import *
from random import randint
from math import *

Randnum = randint(1, 10)
Nrand = 4
Arand = randint(5, 100)
GaussAdd = 3
GaussFac = 8

class FrequencyChart(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()

        self.interpolatedFM1D()
    
    def initUI(self):
      
        self.parent.title("Brownian Motion")
        self.pack(fill=BOTH, expand=1)

    

    def interpolatedFM1D(self):

        canvas = Canvas(self)
        canvas.pack(fill =BOTH, expand=1)

        def InitGauss():
            global Nrand
            Nrand = 4
            global GaussAdd
            GaussAdd = sqrt(3.0*(float)(Nrand))
            global GaussFac
            GaussFac = 2.0 * (float)(GaussAdd) / ((float)(Nrand) * (float)(Arand))
        

        def Gauss():
            global Nrand
            global Randnum
            global GaussFac
            global GaussAdd
            sum = 0.0
            for i in range(1, Nrand+1):
                sum = sum + (float) (Randnum)
            return (GaussFac * sum - GaussAdd)

        

        sigma = 1.0
        H = 0.8
        r = 0.2
        N = 100

        x = []
        for i in range(N):
            x.append(0)
        x[0] = 0
        x[1] = sigma*Gauss()
        print sigma*Gauss()
        y = []
        for i in range(N):
            y.append(0)
        sizex = 2
        T = 1.0
        t = 0.0

        #loop through array

        while sizex < N:

            #set up new resolution of mt points
            
            sizey = (int) (sizex / 0.2)
            if sizey == sizex:
                sizey = sizex + 1
            if sizey > N:
                sizey = N
            t = (1.0 / ((float)(sizey) - 1.0))
            
            #interpolate new points from old points

            y[0] = x[0]
            y[sizey-1] = x[sizex-1]
            for i in range(1, sizey-1):
                index = (int) ((float)(i) * t / (float)(T))
                h = i*t - index
                y[i] = (1-h)*x[index]+h*x[index+1]

            #compute the standard deviation for offsets

            delta = sqrt(0.5)*pow(t, H)*sigma*sqrt(1.0-pow(t/T, 2-2*H))

            #do displacement at all positions

            for i in range(0, sizey):
                x[i] = y[i] + delta*Gauss()

            sizex = sizey

            T = 1.0/((float)(sizex) - 1.0)

            for i in range(N):
                canvas.create_line(x[i]*8, y[i]*8, x[i]*8+1, y[i]*8+1)
                print x[i], y[i]
                
            
        

def main():

    bmWindow = Tk()
    bmWindow.geometry("500x500")
    app = FrequencyChart(bmWindow)
    bmWindow.mainloop()  

if __name__ == '__main__':
    main()  
