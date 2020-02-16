from tkinter import *
import tkinter as tk
from InputBox import InputBox
from EnterButton import EnterButton
from ResultDisplay import ResultDisplay

class UserInterface:
    
    inputBox = InputBox
    enterButton = EnterButton
    resultDisplay = ResultDisplay
    componentList = [inputBox,enterButton,resultDisplay]

    def __init__(self):
        H = 600 # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
        W = 450 # ตัวแปรความกว้าง

        root = tk.Tk()
        root.title("Triangle Calculator")
        canvas = tk.Canvas(root, height=H, width=W)
        canvas.grid(row=0,column=0)
       

        canvas2 = tk.Canvas(root, highlightthickness=1, highlightbackground="black", height=H-200,width=W)
        canvas2.grid(row=0,column=1)
        
        
        enterLengthText = Label(root, text="Enter the length of sides", font = "Verdana 16 bold")
        enterLengthText.place(x=20, y=30)


        resultText = Label(root, text="Result", font = "Verdana 16 bold")
        resultText.place(x=650,y=30)

        side1Text = Label(root, text="side1", font = "Verdana 14")
        side1Text.place(x=20,y=110)

        side2Text = Label(root, text="side2", font = "Verdana 14")
        side2Text.place(x=20,y=210)

        side3Text = Label(root, text="side3", font = "Verdana 14")
        side3Text.place(x=20,y=310)
        
        # point=[250,110,480,200,280,280,250,110]
        # canvas2.create_polygon(point)
        # canvas2.create_rectangle(50, 0, 100, 50, outline='black')
        root.mainloop()

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