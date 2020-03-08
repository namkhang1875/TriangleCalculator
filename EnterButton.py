
import tkinter as tk
from tkinter import *
import ResultDisplay
import TriCalculator


class EnterButton:
    triType = ""

    def onClick(self, sideA, sideB, sideC):
        from ResultDisplay import ResultDisplay
        from TriCalculator import TriCalculator
        from UserInterface import UserInterface
        triCal = TriCalculator()
        resultDisplay = ResultDisplay()

        self.triType = triCal.cal(sideA, sideB, sideC)

        if self.triType is not None:
            resultDisplay.drawTri(sideA, sideB, sideC, self.triType)
        else:
            print(self.triType)
        side1Text = tk.Label(UserInterface.root,
                             text=self.triType, font="Verdana 14")
        side1Text.place(x=675, y=450)
