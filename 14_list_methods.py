# list
# List operation - Append, remove, clear all, insert, remove duplicate
numbers = [5,3,1,9, 8, 0]

numbers.append(22)
print(numbers)

numbers.insert(0,100)
print(numbers)

numbers.remove(0)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5,3,1,9, 8, 0]
print (50 in numbers)
print (0 in numbers)
print (numbers.sort()) # prints none
numbers.sort()
print(numbers) # prints numbers in sorted order

numbersBackup = numbers # copy to other list
numbers.append(210)     # Appends to numbersBackup also
print (numbersBackup)
print (numbers)
numbers.append(310)  #Append into list
print(numbersBackup)

print ('before revering', numbers)
numbers.reverse ()
print(numbersBackup)

#remove duplicate in list
numbers = [2,2,2,5,6,88, 2 ]
unique_numbers=[]
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print('number array =', numbers, 'unique numbers are =', unique_numbers)
