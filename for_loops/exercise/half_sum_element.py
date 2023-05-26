n = int(input())

max_num = float("-inf")
sum_of_numbers = 0

for _ in range(0, n):
    number = int(input())
    if number > max_num:
        max_num = number

    sum_of_numbers += number

if max_num == sum_of_numbers - max_num:
    print(f"Yes\nSum = {max_num}")

else:
    print(f"No\nDiff = {abs(max_num - (sum_of_numbers - max_num))}")