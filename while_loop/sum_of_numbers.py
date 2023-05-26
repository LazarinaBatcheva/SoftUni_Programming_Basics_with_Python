number = int(input())

sum_of_nums = 0

while sum_of_nums < number:
    current_num = int(input())
    sum_of_nums += current_num
    if sum_of_nums >= number:
        print(sum_of_nums)