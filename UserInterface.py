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
    componentList = []
    inputBox1 = ""
    inputBox2 = ""
    inputBox3 = ""
    # componentList = [inputBox,enterButton,resultDisplay]
    # componentList = [inputBox,enterButton]
    # enterButton.onClick(sideA,sideB,sideC)
    # Enterbutton----------------------------------------------
    from EnterButton import EnterButton
    enterButton = EnterButton()
    root = tk.Tk()

    def __init__(self):
        # from ResultDisplay import ResultDisplay  # fix circular import error
        # resultDisplay = ResultDisplay()
        # resultDisplay.drawTri(self.sideA, self.sideB, self.sideC, "right")

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

        self.add("EnterButton")
        self.add("InputBox")
        self.show()
        self.root.mainloop()

    def eventHandler(self):
        # print('Heart')
        self.enterButton.onClick(int(self.inputBox1.get()),
                                 int(self.inputBox2.get()), int(self.inputBox3.get()))

    def add(self, component):
        # from EnterButton import EnterButton
        # enterButton = EnterButton()
        self.componentList.append(component)

    def remove(self, component):
        self.componentList.remove(component)

    def show(self):
        for i in self.componentList:
            if i == "InputBox":
                # pass
                self.inputBox1 = tk.Entry(self.root)
                self.inputBox1.place(x=140, y=115)
                self.inputBox1.insert(0, 0)

                self.inputBox2 = tk.Entry(self.root)
                self.inputBox2.place(x=140, y=215)
                self.inputBox2.insert(0, 0)

                self.inputBox3 = tk.Entry(self.root)
                self.inputBox3.place(x=140, y=315)
                self.inputBox3.insert(0, 0)
            elif i == "EnterButton":
                mButton = tk.Button(self.root, text="Enter", fg="red",
                                    bg="yellow", height=3, width=15)
                mButton.configure(command=self.eventHandler)
                mButton.place(x=150, y=450)
