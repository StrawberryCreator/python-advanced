#set

#covert list to set
list1 = [1, 2, 3, "sebbe", 1.5]
set1 = set(list1)

print (set1)

#set doesn't have index | set1[2]

#check for value
if 1.5 in set1:
    print ("1.5 is present")
else:
    print ("1.5 is not present")

if 3.14 in set1:
    print ("3.14 is present")
else:
    print ("3.14 is not present")

#add value
set1.add ("Bob")
set1.add (4)
set1.add (3.14)

print (set1)

#remove value
set1.remove ("Bob")

print (set1)

#set operations
a = {1, 2, 3, "a", "b", "c", 3.14}
b = {3, 4, 5, "x", "y", "z", 3.14}

#union | all the values from A and B but only add duplicates values once
print (a.union(b))
print (a|b)

#intersection | all the values that are duplicate
print (a.intersection(b))
print (a&b)

#difference | all values that are only in set A (if a is infront of '.difference')
print (a.difference(b))
print (a-b)
print (b.difference(a))
print (b-a)

#symmetric difference | all values that are only in one set for both A and B (or diffrence for both joined together)
print (a.symmetric_difference(b))
print (a^b)

#supersets/subsets
c = {2, 3}
d = {4, 3, 2, 1}
#subset | if all of the values in C are in D (if S is infront of '.issubset')
print (c.issubset(d))
#superset | if D contains every value C contains (if D is infront of '.issuperset')
print (d.issuperset(c))