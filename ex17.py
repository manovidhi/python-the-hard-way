# more files
# writing the python script to copy 1 files to another

# opening the module and checking the OS path
from sys import argv
from os.path import exists

#defining the files at runtime
script, from_file, to_file = argv
print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how? - hard way

in_file = open(from_file)	#opening the from file
indata = in_file.read()		#it is reading the content of in_file.

print( "The input file is %d bytes long" % len(indata)) # telling the size of copied data
print ("Does the output file exist? %r" % exists(to_file)) #checking the to_file existence
print ("Ready, hit RETURN to continue, CTRL-C to abort.")

input()
out_file = open(to_file, 'w')
out_file.write(indata)


print ("Alright, all done.")
out_file.close()
in_file.close()
