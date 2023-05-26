length_in_cm, width_in_cm, height_in_cm = int(input()), int(input()), int(input())
percent = float(input()) / 100

volume_of_the_fish_tank_in_cubic_cm = length_in_cm * width_in_cm * height_in_cm
volume_in_litres = volume_of_the_fish_tank_in_cubic_cm * 0.001

needed_litres = volume_in_litres * (1-percent)

print(needed_litres)
