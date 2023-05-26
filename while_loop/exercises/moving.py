total_space = int(input()) * int(input()) * int(input())
command = input()

boxes = 0

while command != "Done":
    boxes += int(command)
    if boxes > total_space:
        print(f"No more free space! You need {boxes - total_space} Cubic meters more.")
        break
    command = input()

if command == "Done":
    print(f"{total_space - boxes} Cubic meters left.")