begin_value_of_first_pair_of_nums = int(input())
begin_value_of_second_pair_of_nums = int(input())
first_pair_difference_between_begin_and_end_value = int(input())
second_pair_difference_between_begin_and_end_value = int(input())

end_value_of_first_pair_of_numbers = \
    begin_value_of_first_pair_of_nums + first_pair_difference_between_begin_and_end_value
end_value_of_second_pair_of_numbers = \
    begin_value_of_second_pair_of_nums + second_pair_difference_between_begin_and_end_value

for num1 in range(begin_value_of_first_pair_of_nums, end_value_of_first_pair_of_numbers + 1):
    for i in range(2, num1 // 2):
        if num1 % i == 0:
            break
    else:
        for num2 in range(begin_value_of_second_pair_of_nums, end_value_of_second_pair_of_numbers + 1):
            for j in range(2, num2 // 2):
                if num2 % j == 0:
                    break
            else:
                print(f"{num1}{num2}")
