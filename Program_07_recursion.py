# Using recursion create a single list from the nested list.
# For Example: The given list is like [[10, 90, 10, 60], [1, 8, 0, 5]]. 
# Then the output should be like single list with asending data like [0, 1, 5, 8, 10, 10, 60, 90]


def first(number):
	lis = [first(i) if isinstance(i,list) else second.append(i) for i in number]	
firstList=[[10, 90, 10, 60], [1, 8, 0, 5],1] 
second = []
first(firstList)
print(sorted(second))

# for i in number:
	# 	if isinstance(i,list):
	# 		first(i)
	# 	else:
	# 		second.append(i) 



