# from tkinter import *
import tkinter as tk
from InputBox import InputBox
from EnterButton import EnterButton

H = 600 # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
W = 450 # ตัวแปรความกว้าง

class UserInterface:
    sideA = 5
    sideB = 4
    sideC = 3
    inputBox = InputBox()
    enterButton = EnterButton()
    
    # componentList = [inputBox,enterButton,resultDisplay]
    componentList = [inputBox,enterButton]
    enterButton.onClick(sideA,sideB,sideC)
    
    root = tk.Tk()
    def __init__(self):
        from ResultDisplay import ResultDisplay
        resultDisplay = ResultDisplay()
        resultDisplay.drawTri(self.sideA,self.sideB,self.sideC,"right")
        
        self.root.title("Triangle Calculator")
        canvas = tk.Canvas(self.root, height=H, width=W)
        canvas.grid(row=0,column=0)
        
       
       

        # canvas2 = tk.Canvas(self.root, highlightthickness=1, highlightbackground="black", height=H-200,width=W)
        # canvas2.grid(row=0,column=1)
        # canvas2.create_polygon(0, 5, 0, 100, 100, 100)
        
        enterLengthText = tk.Label(self.root, text="Enter the length of sides", font = "Verdana 16 bold")
        enterLengthText.place(x=20, y=30)


        resultText = tk.Label(self.root, text="Result", font = "Verdana 16 bold")
        resultText.place(x=650,y=30)

        side1Text = tk.Label(self.root, text="side1", font = "Verdana 14")
        side1Text.place(x=20,y=110)

        side2Text = tk.Label(self.root, text="side2", font = "Verdana 14")
        side2Text.place(x=20,y=210)

        side3Text = tk.Label(self.root, text="side3", font = "Verdana 14")
        side3Text.place(x=20,y=310)
        
        # point=[250,110,480,200,280,280,250,110]
        # canvas2.create_polygon(point)
        # canvas2.create_rectangle(50, 0, 100, 50, outline='black')
        self.root.mainloop()

    def add(self,component):
        self.componentList.append(component)

    def remove(self,component):
        self.componentList.remove(component)

    def show(self):
        for i in self.componentList:
            if i == InputBox:
                pass
            elif i == EnterButton:
                pass
            elif i == ResultDisplay:
                pass
