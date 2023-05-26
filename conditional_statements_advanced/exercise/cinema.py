screening_type = input()
num_of_rows, num_of_columns = int(input()), int(input())

hall = num_of_rows * num_of_columns
price = 0

if screening_type == "Premiere":
    price = hall * 12
elif screening_type == "Normal":
    price = hall * 7.50
else:
    price = hall * 5.00
print(f"{price:.2f} leva")