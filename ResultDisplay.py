import tkinter as tk
# import UserInterface
# from UserInterface import canvas
# from UserInterface import root
from UserInterface import UserInterface


class ResultDisplay:
    # UserInterface.canvas

    canvas2 = tk.Canvas(UserInterface.root, highlightthickness=1,
                        highlightbackground="black", height=400, width=450)

    def drawTri(self, sideA, sideB, sideC, triType):
        # print(self.canvas2)
        print(triType)
        self.canvas2.grid(row=0, column=1)
        self.canvas2.create_polygon(0, 5, 0, 100, 100, 100)
