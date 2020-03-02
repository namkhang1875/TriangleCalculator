class EnterButton:
    def onClick(self,sideA, sideB, sideC):
        from ResultDisplay import ResultDisplay
        from TriCalculator import TriCalculator     
        triCal = TriCalculator()
        resultDisplay = ResultDisplay()
        triType = triCal.cal(sideA, sideB, sideC)
        if triType is not None:
            resultDisplay.drawTri(sideA, sideB, sideC, triType)
        else:
            print(triType)