# passing 'x' creates a new file and open it for writing
with open("Section11/fruit.txt", "x") as myfile:
    myfile.write("Okra")

# by passing 'a' we can open for writing, and append to the end of the file
with open("Section11/fruit.txt", "a") as myfile:
    myfile.write("Okra")
    
# adding the plus, will open a disk file for updating(reading and writing)
with open("Section11/fruit.txt", "a+") as myfile:
    myfile.write("Okra")
    myfile.seek(0)
    content = myfile.read()

print(content)