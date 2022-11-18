student_marks = 'alex', 80, 'bob', 65, 'cook', 90
grade_boundaries = {'A': 90, 'B': 80, 'C': 60}
result = []

for index in range(len(student_marks)):
    if index % 2 == 0:
        result.append(student_marks[index])
    else:
        for grade in grade_boundaries.keys():
            if student_marks[index] >= grade_boundaries[grade]:
                result.append(grade)
                break
              
result = tuple(result)
print(result)