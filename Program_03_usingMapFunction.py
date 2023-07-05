# Write program for convert temperatures from Celsius to Fahrenheit using lambda function with map().
# numbers = [22,30,15,28]
# O/P: [71.6, 86.0, 59.0, 82.4]

firstList = [22,30,15,28]
output = map(lambda x:x*(9/5)+32,firstList)
print(list(output))