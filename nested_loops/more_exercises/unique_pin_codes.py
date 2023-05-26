first_number = int(input())
second_number = int(input())
third_number = int(input())

for num1 in range(1, first_number + 1):
    for num2 in range(1, second_number + 1):
        for num3 in range(1, third_number + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and str(num2) in "2357":
                print(f"{num1} {num2} {num3}")