student_name = input()

grade_counter = 0
failed_counter = 0
grades_sum = 0

while True:
    grade = float(input())

    if grade >= 4:
        grades_sum += grade
        grade_counter += 1
        if grade_counter == 12:
            print(f"{student_name} graduated. Average grade: {grades_sum / 12:.2f}")
            break

    else:
        failed_counter += 1
        if failed_counter == 2:
            print(f"{student_name} has been excluded at {grade_counter + 1} grade")
            break