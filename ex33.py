# while loop

i = 0
number = []

while i <= 20:
	print("At the top i is %d." %i)
	number.append(i)
	
	i = i+1
	print("numbers now:" , number)
	print("at the bottom i is %d." %i)
	
print("The Number: ")

for num in number:
	print(num)