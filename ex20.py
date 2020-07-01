# function and files
# how functions and ﬁles can work together to make useful stuff

# here we are defining the functions for print all, rewind and print line by line
from sys import argv
script, input_file = argv

def print_all(f):
	print (f.read())
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print(line_count, f.readline())
	
	
# Now calling functions 
current_file = open(input_file)

print("Print the whole file here: \n")
print_all(current_file)   		#calling the function

print("Rewind just like we do in cassettes")
rewind(current_file)

print("Now print 3 lines line by line")
current_line = 1						#initialization the line number 1
print_a_line(current_line, current_file)

current_line += 1
#current_line = current_line + 1			# line number 2
print_a_line(current_line, current_file)

current_line = current_line + 1			#line number 3
print_a_line(current_line, current_file)

		