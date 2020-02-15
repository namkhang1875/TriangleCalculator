from tkinter import *
import tkinter as tk
from InputBox import InputBox
from EnterButton import EnterButton
from ResultDisplay import ResultDisplay

class UserInterface:
    def __init__(self):
        H = 500 # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
        W = 800 # ตัวแปรความกว้าง

        root = tk.Tk()

        canvas = tk.Canvas(root, height=H, width=W)
        canvas.pack()
        frame = tk.Frame(root, bg='#80c1ff', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
        root.mainloop()

    def add(self):
        pass

    def remove(self):
        pass

    def show(self):
        pass