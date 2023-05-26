judges = int(input())

grades_counter = 0
total_grades_sum = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    grades_sum = 0

    for _ in range(judges):
        grades_sum += float(input())

    total_grades_sum += grades_sum
    grades_counter += judges

    print(f"{presentation_name} - {grades_sum / judges:.2f}.")

print(f"Student's final assessment is {total_grades_sum / grades_counter:.2f}.")