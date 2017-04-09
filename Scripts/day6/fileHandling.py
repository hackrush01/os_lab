# Writing in file in python
file = open("abc.txt", "w")
file.write("This is test text!\n")
file.close()

# Reading in file in python
file = open("abc.txt", "r")
str = file.read(10)
print ("Read string is(first 10 bytes): ", str)
file.close()
file = open("abc.txt" , "r")
str = file.read()
print ("Complete string is:             ", str)
file.close()

