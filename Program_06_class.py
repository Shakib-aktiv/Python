# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
 # So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Input: capacity = 50
# Output Should be:-
# Total Bus fare is: 5500.0

class vehical:
	def __init__(self,capicity):
		self.capicity = capicity

	def first(self):
		return self.capicity*100

class bus(vehical):
	def findAmount(self):
		totalFare = super().first()
		extraCharge = 0.1*totalFare
		totalAmount = totalFare+ extraCharge
		return totalAmount
capicity = int(input("Enter Capicity..."))

rent = bus(capicity)		
callAFunc = rent.findAmount()
print(callAFunc)