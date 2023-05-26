num1 = int(input())
num2 = int(input())
magic_number = int(input())

combinations_counter = 0

for x in range(num1, num2 + 1):
    for y in range(num1, num2 + 1):
        result = x + y
        combinations_counter += 1
        if result == magic_number:
            print(f"Combination N:{combinations_counter} ({x} + {y} = {magic_number})")
            exit()
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")