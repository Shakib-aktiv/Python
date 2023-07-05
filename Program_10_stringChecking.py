# Write program check if string is a valid identifier or not
# Note: For checking string use search() method of regex module.

import re

givenString = "This is a last Program"
identify = re.search(r'[a-zA-Z]',givenString)

if identify:
	print(givenString,"- yes, String is Valid..")
else:
	print(givenString, "- No , String is not Valid..")