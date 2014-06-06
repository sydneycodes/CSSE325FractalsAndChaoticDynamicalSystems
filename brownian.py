# Sydney Satchwill
# Homework 5 - Brownian Motion Simulator
# CSSE325 Spring 2014
#

from Tkinter import *
from random import randint
from math import *

class FrequencyChart(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()

        self.displayFrequencies()
    
    def initUI(self):
      
        self.parent.title("Brownian Motion")
        self.pack(fill=BOTH, expand=1)

    def displayFrequencies(self):

        minVal = 0
        maxVal = 0
        msd = 0

        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        freqList = {}

        data = self.brownianMotion()

        for i in range(10000):
            if data[i]<minVal:
                minVal = data[i]
            elif data[i]>maxVal:
                maxVal = data[i]
            if data[i] in freqList:
                freqList[data[i]] = freqList[data[i]] + 1
            else:
                freqList[data[i]] = 1

        scaleFactor = int(450 / min(abs(minVal), abs(maxVal)))
                
        for key, value in freqList.iteritems():
            if key < 0:
                lineColor = "blue"
            elif key > 0:
                lineColor = "red"
            else:
                lineColor = "black"

            msd = msd + pow(key, 2)
            
            canvas.create_line(key+450+key*scaleFactor, 600, key+450+key*scaleFactor, 600-value, width=scaleFactor, fill=lineColor)


        rangeLabel = Label(canvas, text=("Range: %d, %d" % (minVal, maxVal)))
        rangeLabel.pack()

        print sqrt(msd)

    def brownianMotion(self):

        displacementList = []

        for i in range(10000):
            displacement = 0
            for j in range(300):
                if randint(0, 1) == 0:
                    displacement = displacement + 1
                else:
                    displacement = displacement - 1
                
            displacementList.append(displacement)

        return displacementList

        
        

def main():

    bmWindow = Tk()
    bmWindow.geometry("900x700")
    app = FrequencyChart(bmWindow)
    bmWindow.mainloop()  

if __name__ == '__main__':
    main()  
