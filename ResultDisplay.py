import tkinter as tk
# import UserInterface
# from UserInterface import canvas
# from UserInterface import root


class ResultDisplay:
    # UserInterface.canvas

    def drawTri(self, sideA, sideB, sideC, triType):
        from UserInterface import UserInterface
        canvas2 = tk.Canvas(UserInterface.root, highlightthickness=1,
                            highlightbackground="black", height=400, width=450)
        # print(self.canvas2)
        print(triType)
        canvas2.grid(row=0, column=1)
        canvas2.create_polygon(0, 5, 0, 100, 100, 100)
