import tkinter as tk


class ResultDisplay:

    def drawTri(self, sideA, sideB, sideC, triType):
        from UserInterface import UserInterface
        canvas2 = tk.Canvas(UserInterface.root, highlightthickness=1,
                            highlightbackground="black", height=400, width=550)

        print(triType)
        canvas2.grid(row=0, column=1)

        if sideA > 12 and sideB > 12 and sideC > 12:
            if sideA % 12 == 0:
                sideA += 1
            sideA = sideA % 12

            if sideB % 12 == 0:
                sideB += 1
            sideB = sideB % 12

            if sideC % 12 == 0:
                sideC += 1
            sideC = sideC % 12

        A = (0, 0)
        B = (sideC, 0)
        height = abs((2 * (sideA**2*sideB**2 + sideB**2*sideC**2 + sideC **
                           2 * sideA**2) - (sideA**4 + sideB**4 + sideC**4)))**0.5 / (2.*sideC)
        dx = abs((sideB**2 - height**2))**0.5
        if abs((sideC - dx)**2 + height**2 - sideA**2) > 0.01:
            dx = -dx  # dx has two solutions
        C = (dx, height)
        # coords = [int((x + 1) * 35) for x in A+B+C]
        coords = [(x + 1) * 35 for x in A+B+C]
        # if sideA >= 20 or sideB >= 20 or sideC >=20:
        #     coords = [(x + 1) * 15 for x in A+B+C]
        # else:

        canvas2.create_polygon(*coords)
