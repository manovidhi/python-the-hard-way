#reading file from hard way
from sys import argv   	#i am opening package sys and importing 1 list called argv
script , filename = argv # these are place holders only, real argument will be passed
							# on run time
txt = open(filename) 		#txt is the file in which I am opening my text file here
print("here is your %s file" % filename) 
print(txt.read())   #here i am displaying content of my text file.

print("print the file name again")
file_again = input(">")		#inputting the file name at the runtime
txt_again = open(file_again)	#passing the filename at runtime 
print(txt_again.read())   #til now biggest triumph. i got this syntax right by myself