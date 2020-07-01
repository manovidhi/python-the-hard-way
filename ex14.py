# this is for prompting and passing
from sys import argv   #always remember sys is a module imported and argv is a list
script, user_name = argv # here is just a placehoder. we have to pass argument in CLI
prompt = '>'  # this is something new 

print("Hello %r, this is %s script." % (user_name, script))
print("I like to recite poems")
print("Do you like me %s" % user_name)
likes = input(prompt)
print("where do you live %s?" %user_name )
lives = input(prompt)
print( "What kind of computer do you have?")
computer = input(prompt)

print( """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

age = float(input("whats your age buddy"))
print("age", age)



