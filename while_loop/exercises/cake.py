all_cake = int(input()) * int(input())
command = input()

pieces_of_cake = 0

while command != "STOP":
    pieces_of_cake += int(command)
    if pieces_of_cake > all_cake:
        print(f"No more cake left! You need {pieces_of_cake - all_cake} pieces more.")
        break
    command = input()

if command == "STOP":
    print(f"{all_cake - pieces_of_cake} pieces are left.")