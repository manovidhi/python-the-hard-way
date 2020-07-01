#Names, Variables, Code, Functions 18apr2020
#Functions do three things:
# 1.	They name pieces of code the way variables name strings and numbers.
# 2.	They take arguments the way your scripts take argv.
# 3.	Using #1 and #2, they let you make your own “mini-scripts” or “tiny commands.”



# defining the function method 1
def print_2(*argv):
	arg1, arg2 = argv
	print("argument1, %r, argument2, %r" % (arg1, arg2))
	
#method 2 of defing function
def print_2_again(arg1, arg2):
	print("Name is %r, Surname is %r" % (arg1, arg2))
	
# running for just 1 argument
def print_1(arg):
	print("Address is %r" % arg)
	
# defining the function with 0 argument
def print_0():
	print("Print none")	
	
# calling the function
print_2("Amit", "Sinha")	
print_2_again("AMit", "Sinha")
print_1("Noida")
print_0()


