class TriCalculator:
    def __init__(self):
        print("hello")

    def cal(self, sideA, sideB, sideC):

    # some input is 0
        if sideA == 0:
            print("error sideA")
        elif sideB == 0:
            print("error sideB")
        elif sideC == 0:
            print("error sideC")
        else:
            a = pow(sideA, 2)
            b = pow(sideB, 2)
            c = pow(sideC, 2)
            # all input is equal
            if sideA == sideB and sideA == sideC:
                return "right triangle"
            # 2-input is equal
            elif sideA == sideB or sideA == sideC or sideB == sideC:
                return "right triangle"
            else:
                # a is the most
                if a > b and a > c and a == b + c:
                    return "right triangle"
                # b is the most
                elif b > a and b > c and b == a + c:
                    return "right triangle"
                # c is the most
                elif c > a and c > b and c == a + b:
                    return "right triangle"
                # all input are not equal
                else:
                    return "right triangle"
# t = TriCalculator()
# t.cal(5,4,3)