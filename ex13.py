# we pass the arguments at the runtime here. we import argument to define it here.

from sys import argv

script, first, second, third = argv 
#print("this is script", argv.script)
print( "The script is called:", script )     # this is what i learnt from hard way
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

age = input("put input your age]")
print("your age is", age)  # i put it to check input and argv difference


#print("this is script", argv[0]) #this is from mihir
#print("this is first", argv[1])
#print("this is 2nd", argv[2])
#print("this is third", argv[3])