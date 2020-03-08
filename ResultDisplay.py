import tkinter as tk
# import UserInterface
# from UserInterface import canvas
# from UserInterface import root
from math import sin, cos
from tkinter import PhotoImage
import numpy as np
import matplotlib.pyplot as plt


class ResultDisplay:
    # UserInterface.canvas

    def drawTri(self, sideA, sideB, sideC, triType):
        from UserInterface import UserInterface
        canvas2 = tk.Canvas(UserInterface.root, highlightthickness=1,
                            highlightbackground="black", height=400, width=550)
        # print(self.canvas2)
        print(triType)

        # my_image = PhotoImage(width=450, height=400)
        # canvas2.create_image(225, 200, image=my_image)
        canvas2.grid(row=0, column=1)

        # canvas2.create_polygon(225, 5, 225, 100, 100, 100)

        # vertices = [(10, sideA), (150, sideB), (350, sideC)]
        # vertices.sort(key=lambda t: t[0])
        # # canvas2.create_line((int)(sin(y * radians) * 225 + 300),
        # #                    (int)(cos(y * radians) * 145 + 170),
        # #                    (int)(sin(x * radians) * 225 + 300),
        # #                    (int)(cos(x * radians) * 145 + 170),
        # #                    fill=color)
        # for x in range(vertices[0][0], vertices[1][0]):
        #     y1 = int((x-vertices[0][0])*(vertices[1][1]-vertices[0]
        #                                  [1])/(vertices[1][0]-vertices[0][0])+vertices[0][1])
        #     y2 = int((x-vertices[0][0])*(vertices[2][1]-vertices[0]
        #                                  [1])/(vertices[2][0]-vertices[0][0])+vertices[0][1])
        #     # print("y1 =", y1)
        #     # print("y2 =", y2)
        #     for y in range(y1, y2):
        #         my_image.put('#000000', (x, y))
        #     my_image.put('#000000', (x, y1))
        #     my_image.put('#000000', (x, y2))
        #     my_image.put('#000000', (x, y1+1))
        #     my_image.put('#000000', (x, y2+1))
        # tk.mainloop()
        # z = np.array([sideA, sideB, sideC])
        # while z[-1] != z.max():
        #     z = z[[2, 0, 1]]  # make sure last entry is largest
        # alpha = np.arccos((sideB**2 + sideC**2 - sideA**2) / (2.*sideB*sideC))
        # beta = np.arccos((-sideB**2 + sideC**2 + sideA**2) / (2.*sideA*sideC))
        # # alpha, beta, _ = calc_angles(*z)
        # x = (sideC*np.tan(beta))/(np.tan(alpha)+np.tan(beta))
        # y = x * np.tan(alpha)
        # # x, y = calc_point(alpha, beta, z[-1])

        # gamma = np.pi-alpha-beta
        # fig, ax = plt.subplots()
        # ax.set_aspect("equal")

        # dreieck = plt.Polygon([(0, 0), (z[-1], 0), (x, y)])
        # ax.add_patch(dreieck)
        # ax.relim()
        # # ax.autoscale_view()
        # plt.show()
        # canvas2.create_polygon((255, 10), (z[-1], 0), (x, y))
        A = (0, 0)
        B = (sideC, 0)
        hc = (2 * (sideA**2*sideB**2 + sideB**2*sideC**2 + sideC**2 *
                   sideA**2) - (sideA**4 + sideB**4 + sideC**4))**0.5 / (2.*sideC)
        dx = (sideB**2 - hc**2)**0.5
        if abs((sideC - dx)**2 + hc**2 - sideA**2) > 0.01:
            dx = -dx  # dx has two solutions
        C = (dx, hc)
        # coords = [int((x + 1) * 35) for x in A+B+C]
        coords = [(x + 1) * 35 for x in A+B+C]
        canvas2.create_polygon(*coords)
