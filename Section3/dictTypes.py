
monday_temperatures = [9.1, 8.8, 7.5]
# marry is a key
# 9.1 is the value
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)
# this will return the values of what is in your dictionary. not the key. so it will look like a list
print(student_grades.values())
# this will return just the keys
print(student_grades.keys())