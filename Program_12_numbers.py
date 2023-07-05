# number Program ....

expectationList = []
userGivenList = []
userInput = int(input("how many numbers  (Ex - 1 ) : "))
for i in range(userInput):
	elementsEnterInlist = int(input("Enter a number (Ex. Between [1000-9999]...)  : "))
	if len(str(elementsEnterInlist))==4:
		userGivenList.append(int(elementsEnterInlist))
	else:
		exit("wrong value, next time enter a 4 digit number ...")

for number in userGivenList:
	if number%8==0 or number%5==0:
		convertStringFirstString= str(number)
		convertIntFirstInt= int(convertStringFirstString[3])
		convertStringSecondCondition=str(int(number/100)) 
		convertIntSecondInt= int(convertStringSecondCondition[1])
		if convertIntSecondInt%2!=0 and convertIntFirstInt%2==0:
			expectationList.append(number)


print(expectationList)			