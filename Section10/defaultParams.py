def area(a, b):
    return a * b

# by adding in the variable, they become keyword arguments
print(area(a=4, b=5))

# normally the arguemnt that you pass in is "positional", but with keyword arguments it does not matter 
# non default arguments follow default arguments

def area2(a, b=6)
    return a * b

# same thing
print(area2(a=5))
print(area2(5))