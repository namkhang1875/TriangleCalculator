
import tkinter as tk
from tkinter import *
import ResultDisplay
import TriCalculator

class EnterButton:
    
    def __init__(self):
        pass

    def onClick(self):
        cal(self, sideA, sideB, sideC)
        drawTri(self,sideA,sideB,sideC,triType)