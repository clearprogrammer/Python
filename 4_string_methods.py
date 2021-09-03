stringManipulation = '.. Python is easy language. Has various built in support  '

print (len(stringManipulation))
print(stringManipulation.upper())
print(stringManipulation.lower())
print(stringManipulation.find('t'))
print(stringManipulation.lstrip()) 
print (stringManipulation) #without strip
print(stringManipulation.lstrip("..e")) # not clear. If string starts with space then it doesn't work
#print(stringManipulation.isupper())


print (stringManipulation.replace('P', 'A'))
print ('python' in stringManipulation)

