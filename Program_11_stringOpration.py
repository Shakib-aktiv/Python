#string Checking .....

givenString= input("Enter String  : ")
firstPartOfString ,*secondPartOfString =givenString
vowels = ['a','e','i','o','u'] 
if firstPartOfString.isalpha():
	firstPart = firstPartOfString.lower()
	if firstPart not in vowels:
		secondPart = "".join(secondPartOfString)
		mainPart = secondPart.replace(" ","")
		
		if mainPart.isalpha():
			print("Congratulations' valid String : ",firstPartOfString+secondPart)
		else:
			print("Wrong string please enter a valid string [a-z][A-Z]....")
	else:
		print("String first letter must not be vowels ... ")
else:
	print("String first letter is not a alphabetic Character...")