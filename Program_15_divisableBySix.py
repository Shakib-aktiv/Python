#  program a divisable by 6 all elements return true or false .

userInput = int(input("how may number")) 
firstList =[]
for e  in range(userInput):
	secondInput = int(input('Enter a elements'))
	if secondInput % 6 == 0:
		firstList.append(True)
	else:
		firstList.append(False)	
print(firstList)
print(all(firstList))
