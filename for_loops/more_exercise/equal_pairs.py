num_of_pairs = int(input())

difference = 0
previous_sum = 0

for num in range(num_of_pairs):
    first_num = int(input())
    second_num = int(input())

    sum_of_pairs = first_num + second_num

    if num == 0:
        previous_sum = sum_of_pairs

    if previous_sum != sum_of_pairs:
        difference = abs(previous_sum - sum_of_pairs)

        previous_sum = sum_of_pairs

if difference == 0:
    print(f'Yes, value={previous_sum}')

else:
    print(f'No, maxdiff={difference}')