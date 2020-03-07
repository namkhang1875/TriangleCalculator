# from tkinter import *
import tkinter as tk
from InputBox import InputBox


H = 600  # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
W = 450  # ตัวแปรความกว้าง


class UserInterface:
    sideA = 0
    sideB = 0
    sideC = 0
    inputBox = InputBox()

    # componentList = [inputBox,enterButton,resultDisplay]
    # componentList = [inputBox,enterButton]
    # enterButton.onClick(sideA,sideB,sideC)

    root = tk.Tk()

    def __init__(self):
        from ResultDisplay import ResultDisplay  # fix circular import error
        resultDisplay = ResultDisplay()
        resultDisplay.drawTri(self.sideA, self.sideB, self.sideC, "right")

        self.root.title("Triangle Calculator")
        canvas = tk.Canvas(self.root, height=H, width=W)
        canvas.grid(row=0, column=0)

        enterLengthText = tk.Label(
            self.root, text="Enter the length of sides", font="Verdana 16 bold")
        enterLengthText.place(x=20, y=30)

        resultText = tk.Label(self.root, text="Result", font="Verdana 16 bold")
        resultText.place(x=650, y=30)

        side1Text = tk.Label(self.root, text="side1", font="Verdana 14")
        side1Text.place(x=20, y=110)

        side2Text = tk.Label(self.root, text="side2", font="Verdana 14")
        side2Text.place(x=20, y=210)

        side3Text = tk.Label(self.root, text="side3", font="Verdana 14")
        side3Text.place(x=20, y=310)

        # point=[250,110,480,200,280,280,250,110]
        # canvas2.create_polygon(point)
        # canvas2.create_rectangle(50, 0, 100, 50, outline='black')

        # InputBox----------------------------------------------
        inputBox1 = tk.Entry(self.root)
        inputBox1.place(x=140, y=115)
        inputBox1.insert(0, 0)

        inputBox2 = tk.Entry(self.root)
        inputBox2.place(x=140, y=215)
        inputBox2.insert(0, 0)

        inputBox3 = tk.Entry(self.root)
        inputBox3.place(x=140, y=315)
        inputBox3.insert(0, 0)

        # self.sideA = inputBox1.get()
        # self.sideB = inputBox2.get()
        # self.sideC = inputBox3.get()

        # Enterbutton----------------------------------------------
        from EnterButton import EnterButton
        enterButton = EnterButton()
        mButton = tk.Button(self.root, text="Enter", fg="red", bg="yellow", height=3, width=15,
                            command=enterButton.onClick(int(inputBox1.get()), int(inputBox2.get()), int(inputBox3.get())))
        # mButton = tk.Button(self.root, text="Enter", fg="red", bg="yellow", height=3, width=15,
        #                     command=enterButton.onClick(self.sideA, self.sideB, self.sideC))
        # mButton = tk.Button(self.root, text="Enter", fg="red", bg="yellow", height=3, width=15,
        #                     command=enterButton.onClick(5, 4, 3))
        mButton.place(x=150, y=450)

        self.root.mainloop()

    def add(self, component):
        from EnterButton import EnterButton
        enterButton = EnterButton()
        self.componentList.append(component)

    def remove(self, component):
        self.componentList.remove(component)

    def show(self):
        for i in self.componentList:
            if i == InputBox:
                pass
            elif i == EnterButton:
                pass
            elif i == ResultDisplay:
                pass
