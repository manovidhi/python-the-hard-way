# making decisions

# There would be 2 doors. rest would be wall.

print('which door do you prefer; Door number 1 or Door number 2')
door = input('> ')

# A bear would be guarding the door1
if door == "1":
	print( "There's a giant bear here eating a cheese cake. What do you do?")
	print ("1. Take the cake.")
	print ("2. Scream at the bear." )
	
	bear = input('> ') 

	if bear == "1":
		print ("The bear eats your face off. Good job!")

	elif bear == "2":
		print ("The bear eats your legs off. Good job!")
	else:
		print ("Well, scaring %s is probably better. Bear runs away." % bear )


elif door == "2":
	print ("AB will eat your head")
	print("1. Run from AB")
	print("2. fight with AB")
	
	AB = input('>')
	
	if AB == "1":
		print ("AB will play with you. Good job!")

	elif AB == "2":
		print ("AB will cycle with you. Good job!")
	else:
		print ("Well, AB will beat you up." % AB )


else:
	print("You will be eaten by a lion")