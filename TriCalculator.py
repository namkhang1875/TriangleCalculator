class TriCalculator:
    def cal(self, sideA, sideB, sideC):
    	a = pow(sideA,2)
    	b = pow(sideB,2)
    	c = pow(sideC,2)
    	if sideA == sideB and sideA == sideC:
    		print("equilateral triangle")
    	elif sideA == sideB or sideA == sideC or sideB == sideC:
    		print("isosceles triangle")
    	else: 
    		if a > b and a > c and a == b + c: #a ค่ามากสุด
    			print("right triangle sideA is the most")
    		elif b > a and b > c and b == a + c: #b ค่ามากสุด
    			print("right triangle sideB is the most")
    		elif c > a and c > b and c == a + b: #c ค่ามากสุด
    			print("right triangle sideC is the most")
    		else:
    			print("scalene")

t = TriCalculator()
t.cal(5,4,3)