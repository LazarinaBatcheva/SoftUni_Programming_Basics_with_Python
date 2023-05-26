command = input()
max_num = float("-inf")

while command != "Stop":
    number = int(command)

    if number > max_num:
        max_num = number
    command = input()

print(max_num)