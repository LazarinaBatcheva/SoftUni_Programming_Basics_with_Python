from math import ceil, floor

square_meters_of_vineyard = int(input())
grapes_per_square_meter = float(input())
liters_wine_needed = int(input())
workers_count = int(input())

KG_GRAPES_FOR_LITER_WINE = 2.5

total_grapes = square_meters_of_vineyard * grapes_per_square_meter
harvest_for_wine = total_grapes * 0.40
total_wine = harvest_for_wine / KG_GRAPES_FOR_LITER_WINE

difference_between_liters_wine = floor(abs(total_wine - liters_wine_needed))

if total_wine < liters_wine_needed:
    print(f"It will be a tough winter! More {difference_between_liters_wine} liters wine needed.")
else:
    wine_for_one_worker = ceil(difference_between_liters_wine / workers_count)
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{difference_between_liters_wine} liters left -> {wine_for_one_worker} liters per person.")
