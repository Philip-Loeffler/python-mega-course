myfile = open("Section11/fruit.txt")
print(myfile.read())
myfile.close()
# when you create a file object, a file object is created in ram. and it will remain there till
# the program ends. so it is a good idea close the file when you're finished with the program

