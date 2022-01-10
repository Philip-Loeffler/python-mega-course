# creating a function with an arbitrary amount of arguments
def mean(*args):
    return sum(args) / len(args)


print(mean(1,3,4))

# this is with keyword arguments
# kwargs = keyword arguments
def mean(**kwargs):
    return kwargs

# all arguments must be named
# and you are returned a dictionary

print(mean(a=1, b=2, c=5))