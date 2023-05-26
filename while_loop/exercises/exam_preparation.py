bad_grades = int(input())

grades_sum = 0
problems_counter = 0
last_problem_name = ""
bad_grades_counter = 0

flag = False

while bad_grades_counter < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        flag = True
        break

    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1

    grades_sum += grade
    problems_counter += 1
    last_problem_name = problem_name

if not flag:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {grades_sum / problems_counter:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {last_problem_name}")