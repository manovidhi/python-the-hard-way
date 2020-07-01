# this is auxillary prog to check the knowledge of function calling

# define the function
def ABs_friend(count, gift):
	print("AB's friends are %r in numbers and they need %r return gift" % (count, gift))
	print("AB's party is grand and best in the world")
	print("AB is best in the world \n \n" )

# calling the function
print("printing AB's friend's number directly")
ABs_friend(13, 26)

# calling the function indirect way by defining variables in the program
print("printing AB's friend's number and return gift as variable in prog")
No_of_friend = 50
return_gift = 100
ABs_friend(No_of_friend, return_gift)

#calculating the friend number and return gift
print("printing by calculating directly here")
No_of_friend = 5+10+6
return_gift = 2 * (5+10+6)
ABs_friend(No_of_friend, return_gift)

# calculating by mixing the variable and numbers
print("printing by calculating with variables and number here")
No_of_friend = 5+10+6
return_gift = 3 * No_of_friend
ABs_friend(No_of_friend, return_gift)

# asking for user to provide the input at runtime
print("Ab will provide the number of friends and return gift as he wishes")
No_of_friend = input("No of Friends you want to invite")
return_gift = input("How many reurn gift total for them")
ABs_friend(No_of_friend, return_gift)


# do it in 10 more type to call function