number = int(input())
current_number_sum = 0

for num in range(number):
    current_number = int(input())
    current_number_sum += current_number

print(f"{current_number_sum / number:.2f}")