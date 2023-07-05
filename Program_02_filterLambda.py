# Write program for filter even numbers from a list using lambda function with filter().
# numbers = [22,35,98,32,41,7]
# O/P: [22, 98, 32]

firstList  = [22,35,98,32,41,7]
output = filter(lambda number :number%2==0 ,firstList)
print(list(output))