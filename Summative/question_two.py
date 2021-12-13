""" Function to find for the next multiple of five of a given number"""
def find_next_multiple(number):
    multiple = 0

    j = 1
    while True:
        if (number + j) % 5 == 0:
            multiple = number + j 
            return multiple
        else:
            j += 1

""" Function to round the students' grades based of conditions:
    1. if grade is less than 38, then do not round it
    2. if grade is greater or equal to 38:
        a. if the grade and the its next multiple difference 
        is less than 3 then round it to its next multiple of five
        b. else, do not round it
"""
def gradingStudents(n, grades):
    new_grades = []

    for i in range(n):
        if grades[i] < 38:
            new_grades.append(grades[i])
        elif grades[i] >= 38:
            mult = find_next_multiple(grades[i])
            if (mult - grades[i] < 3):
                new_grades.append(mult)
            else:
                new_grades.append(grades[i])    

    return new_grades

print(gradingStudents(4, [73, 67, 38, 33]))
print(gradingStudents(3, [84, 29, 57]))
print(gradingStudents(10, [34, 75, 22, 82, 93, 95, 48, 50, 47, 86]))

