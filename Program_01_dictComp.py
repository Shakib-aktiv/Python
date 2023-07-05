# Creating a new dictionary with only pairs where the key is any alphabet after "d" alphabet
# (ex. e,f,g,h,i, etc..) and value is larger than 2 (Using Dictionary comprehension)
# d = {'a':1,'e':2,'c':3, 'd':5, 'j':8}
# O/p: {'j': 8}
# i will check later vyou are comment 
dictionary =  {'a':1,'e':4,'c':3, 'd':5, 'j':1, 'h':12}

wlistofKeys  = list(dictionary.keys()) 
listofKeys =sorted(wlistofKeys)
dIndex= listofKeys.index('d')
for i in range(dIndex+1,len(dictionary)):
	if dictionary[listofKeys[i]]>2:
		print({f'{listofKeys[i]}':dictionary[listofKeys[i]]})	 


