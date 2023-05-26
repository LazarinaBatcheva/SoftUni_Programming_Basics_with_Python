from math import ceil, floor

num_of_days = int(input())
pets_food_kg = int(input())

dog_food_for_one_day_kg = float(input())
cat_food_for_one_day_kg = float(input())
turtle_food_for_one_day_gr = float(input())

turtle_food_for_one_day_kg = turtle_food_for_one_day_gr / 1000

total_food_for_day = dog_food_for_one_day_kg + \
                     cat_food_for_one_day_kg + \
                     turtle_food_for_one_day_kg

total_food = num_of_days * total_food_for_day

difference_between_amount_of_food = pets_food_kg - total_food

if pets_food_kg >= total_food:
    print(f"{floor(difference_between_amount_of_food)} kilos of food left.")
else:
    print(f"{ceil(abs(difference_between_amount_of_food))} more kilos of food are needed.")
