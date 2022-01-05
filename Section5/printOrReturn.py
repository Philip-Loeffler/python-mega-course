# if there is no return statement, your function will return none
# python will go line by line in your code, and will return a print if you have it in the function
# but at the end, if it does not see a return statement, it will return none

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1,4,5]))

mymean = mean([0, 3, 4])
print(mymean + 10)