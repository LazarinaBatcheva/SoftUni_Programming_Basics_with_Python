command = input()
min_num = float("inf")

while command != "Stop":
    number = int(command)

    if number < min_num:
        min_num = number
    command = input()

print(min_num)