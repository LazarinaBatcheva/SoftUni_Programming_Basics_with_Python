start_interval_number = int(input())
end_interval_number = int(input())
magic_number = int(input())

combinations_counter = 0
combination_sum = 0
flag = False

for num1 in range(start_interval_number, end_interval_number + 1):
    for num2 in range(start_interval_number, end_interval_number + 1):
        combinations_counter += 1
        combination_sum = num1 + num2

        if combination_sum == magic_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{combinations_counter} ({num1} + {num2} = {combination_sum})")
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
