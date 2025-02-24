a = {1, 2, 3, 3.14, "D", "E", "F"}
b = {3, 4, 5, 3.14, "A", "B", "C"}

print ("\n")

print (a)
print (b)

print ("\n")

print (a.union(b))
print (a.intersection(b))
print (a.difference(b))
print (b.difference(a))
print (a.symmetric_difference(b))

a.add (0)
b.remove (3)

print ("\n")

print (a)
print (b)

print ("\n")

if 3.14 in a:
    print ("3.14 is present in a")
else:
    print ("3.14 is not present in a")

if 3 in b:
    print ("3 is present in b")
else:
    print ("3 is not present in b")

print ("\n")

print ("A =", end=" | ")
for x in a:
    print (x, end=" | ")

print ()

print ("B =", end=" | ")
for x in b:
    print (x, end=" | ")

print ("\n")