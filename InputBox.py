class InputBox:
	def __init__(self, value=""):
		self.value = value

	def isNumber(self):
		try:# num for conditions
			num = float(self.value) 
			if (num >= 0  and num <= 2147483649 and 		
				num <= round(num,12) and len(self.value) < 24):
				return True
			else:
				return False
		except ValueError:
			return False

	def isEmpty(self):
		if self.value == "":
			return True
		else:
			return False

	def getValue(self):
		if self.isNumber():
			num = float(self.value)
			return round(num,12)
		else:
			return False