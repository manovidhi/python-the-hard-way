

name = "Amit Sinha"
age = 40 #real age
height = 160 # in cm
weight = 170 # in kg
eyes = "black"
color = "brown"

print("lets talk about %r." % name)
print("he is %s inch tall." % ( round(height/2.54, 2)))
print("He is %r kg heavy." % weight)
print("Ohh, He is too heavy")
print("He is got %r eyes and %r color." % (eyes, color))
print("If I add %r, %r, and %r i will get %d" % (height, weight, age, height + weight + age))