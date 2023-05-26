budget = float(input())

num_of_statists = int(input())
price_clothing_for_one_statist = float(input())

decor = budget * 0.10

if num_of_statists > 150:
    price_clothing_for_one_statist *= 1 - 0.10

total_costs = num_of_statists * price_clothing_for_one_statist + decor

if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_costs - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_costs:.2f} leva left.")
