# Count the number of occurance of the character in the string.
# Take user input for the string and character.

enterString = input("Enter a String : ")
enterCharacter = input("Enter a Character : ")
count=0

for character in enterString:
	if character== enterCharacter:
		count+=1
print(f'character  {enterCharacter} is occous in {enterString}. Total {count}')