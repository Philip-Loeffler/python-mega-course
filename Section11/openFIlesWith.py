# this will implicity close your file, so it is better to use
with open("Section11/fruit.txt") as myfile:
    content = myfile.read()
print(content)