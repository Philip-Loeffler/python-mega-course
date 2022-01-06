def mean(value):
    if type(value) == dict:
        # values is a function that returns the values of the dictionary
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) /len(value)
        
    return the_mean

student_grades = {"marry": 9.1, "sim": 8.8, "john": 7.5}
print(mean(student_grades))