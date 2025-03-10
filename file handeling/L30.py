#file

#write
file = open ("file.txt", "w")
file.write ("Hello world!")

#read
file = open ("file.txt", "r")
print (file.read())

#add
file = open ("file.txt", "a")
file.write ("\nThis project is made with python.")