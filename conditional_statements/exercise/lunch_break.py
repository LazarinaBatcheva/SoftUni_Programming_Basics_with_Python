from math import ceil

series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

total_time = lunch_time + rest_time + episode_time
time_left = break_time - total_time

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")
