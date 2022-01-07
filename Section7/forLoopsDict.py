student_grades = {"marry": 9.1, "sim": 8.8, "john": 7.5}

# this will print out your items in a tuple
for grades in student_grades.items():
    print(grades)

# this will print out your items keys

for grades in student_grades.keys():
    print(grades)


# this will print out your items values

for grades in student_grades.values():
    print(grades)


# dict loop with string formatting
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))