# function which can return something

def add(a,b,c):
	print("adding %d and %d and %d" % (a, b, c))
	return (a + b + c)
	
def Subtract(a,b):
	print("Substracting %d and %d" % (a, b))
	return (a - b)	
	
def multi(a,b):
	print("multiplying %d and %d" % (a, b))
	return (a * b)

def div(a,b):
	print("dividing %d and %d" % (a, b))
	return (a / b)

# passing the value to the function		
print("Print age of these people")	
age = add(12,30,40)
ht = Subtract(160,130)
wt = multi(70, 32)
ip = div(110, 54)

# you are passing the value not the function so use age, Ht etc not add, subtract etc
print("Age:", age ,"Height:", ht, "Weight: ", wt, "IQ:",ip	)

# bonus puzzle
print("Here is the puzzle")
what = add(55550,age, Subtract(ht, multi(wt, div(ip, 2))))
print("that become ", what, "can we do it by hand")

