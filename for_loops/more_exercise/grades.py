students_count = int(input())

fail_students = 0
good_students = 0
very_good_students = 0
top_student = 0
total_success = 0

for _ in range(1, students_count + 1):
    grade = float(input())
    total_success += grade

    if grade < 3:
        fail_students += 1
    elif grade < 4:
        good_students += 1
    elif grade < 5:
        very_good_students += 1
    else:
        top_student += 1

print(f"Top students: {top_student / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_students / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {good_students / students_count * 100:.2f}%")
print(f"Fail: {fail_students / students_count * 100:.2f}%")
print(f"Average: {total_success / students_count:.2f}")