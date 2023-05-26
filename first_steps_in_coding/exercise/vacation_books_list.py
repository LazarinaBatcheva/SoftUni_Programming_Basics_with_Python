pages = int(input())
pages_for_one_hour = int(input())
num_of_days_needed_to_read = int(input())

total_pages_for_read = pages // pages_for_one_hour
num_of_hours_to_read_a_day = total_pages_for_read // num_of_days_needed_to_read

print(num_of_hours_to_read_a_day)
