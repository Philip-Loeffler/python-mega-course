myfile = open("Section11/fruit.txt")
print(myfile.read())

# doing the read method will only print out once
# by adding it into a variable you can print it out multiple times
content = myfile.read()
print(content)
print(content)