w_length_m = float(input())
h_width_m = float(input())

#one_work_place = 70 / 100
#corridor_cm = 100
#podium_cm = 160 / 120
#podium_and_door = -3 places

w_hall_cm = w_length_m * 100
h_hall_cm = h_width_m * 100
real_h_cm = h_hall_cm - 100
num_of_rows_by_w = w_hall_cm // 120
num_of_desks = real_h_cm // 70

num_of_places = num_of_rows_by_w * num_of_desks - 3

print(num_of_places)