#tuples
details = ("Sebbe", 11)
details2 = "Sebbe", 11
print (type(details))
print (type(details2))

#packing
address = (7, "Water Street", "Landmark Bridge", "Zaandam", "Netherlands", "77071")
for x in address:
    print (x, end = " ")

#unpacking
houseNo, street, landmark, city, country, pincode = address
print ()
print ("House number: ", houseNo)

#nesting
nestedTuple = ("Sebbe", [1, 2, 3], (7, 8, 9), 9.8)
print (nestedTuple[1][2])
print (nestedTuple[0][1])

#slicing
slicedTuple = ("a", "b", "c", "e", "f", "g")
#slice "c" to end
print (slicedTuple[2:])
#slice begin to "c"
print (slicedTuple[:3])
#slice "b" to "f"
print (slicedTuple[1:5])
#slice every other "c" to "f" 
print (slicedTuple[1:5:2])
#slice end to begin
print (slicedTuple[::-1])
#slice every other "f" to "a"
print (slicedTuple[-2:-7:-2])