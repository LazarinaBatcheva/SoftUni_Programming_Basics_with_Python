control_number = int(input())

control_value_counter = 0
password = list()

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if a < b and c > d and a * b + c * d == control_number:
                    print(f"{a}{b}{c}{d}", end=" ")
                    password.append(f"{a}{b}{c}{d}")
                    control_value_counter += 1
print()
if control_value_counter >= 4:
    print(f"Password: {password[3]}")
else:
    print("No!")