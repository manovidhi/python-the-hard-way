# Functions and Variables
# The variables in your function are not connected to the variables in your script. 

# defining the function for cheese and cracker counts
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxes of crackers!" % boxes_of_crackers)
	print ("Man that's enough for a party!")
	print ("Get a blanket.\n" )

# calling the function with different argument
print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) 

# calling the function with diff argument and defining the value here
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can do the maths directly here
print ("We can even do math inside too:")
cheese_and_crackers(10 + 200, 5000 + 6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
