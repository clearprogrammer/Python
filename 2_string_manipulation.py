# strings
#Single quote, double quote, print specific part  

stringForManipulation = "New Movie of Donald's"

print (stringForManipulation [:5])
print (stringForManipulation [:])
print (stringForManipulation [0:1])
print (stringForManipulation [1:-1])
print (stringForManipulation[0])
print (stringForManipulation[-1])

stringReduced1 = stringForManipulation [2:]
print (stringReduced1)

stringReduced2 = stringForManipulation [3:10]
print(stringReduced2)

stringReduced3 = stringForManipulation [2:30]
print (stringReduced3)
