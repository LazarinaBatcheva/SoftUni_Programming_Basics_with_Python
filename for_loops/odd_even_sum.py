number = int(input())

odd_sum = 0
even_sum = 0

for num in range(1, number + 1):
    current_num = int(input())
    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if odd_sum == even_sum:
    print(f"Yes\nSum = {odd_sum}")

else:
    diff = abs(odd_sum - even_sum)
    print(f"No\nDiff = {diff}")