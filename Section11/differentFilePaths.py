# this will implicity close your file, so it is better to use
# you just need to specify the complete path to the file
# files/blah blah blah
with open("Section11/fruit.txt") as myfile:
    content = myfile.read()
print(content)