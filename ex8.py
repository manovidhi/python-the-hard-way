formatter = "%r %r %r %r"
print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, True, False))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
"agnipath agneepath ageepath", 
"ho ghane ho bade",
	"1 patra chhanv bhi maang mat maang mat",
	"maang ma't"))
	
while True:
	for i in ["/","-","|","\\","|"]: print ("%s\r" % i),