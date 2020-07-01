# loops

the_count = [1,2,3,4,5]
fruits = ['apple','orange','pear','mango']
change = [1,'penny', 2, 'quarter',3, 'half']

# using for loop as counter

for number in the_count:
	print("The number in the count is %d" %number)

for fruit in fruits:
	print("AB eats %s fruits" %fruit)
	
	
for chillar in change:
	print("I had %r change only" %chillar)	
	
# we can build list also

# create an empty list
elements = []

# then use range function to do 0 to 5 counts
for i in range(0,6):
	print("adding %d to the list" %i)
	elements.append(i)
	
# now checking the populated list

for i in elements:
	print("elements are %d." %i)
	

# checking for study drills
metals = range(0,6)
for i in metals:
	print("metals are %d." %i)
	
# making 2D lists
heera = range(0,3,6)	