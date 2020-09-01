class Vehicle:
	def __init__(self,regno,color):
		self.color =  color
		self.regno = regno

class Car(Vehicle):

	def __init__(self,regno,color):
		Vehicle.__init__(regno,color)

	def getType(self):
		return "Car"
