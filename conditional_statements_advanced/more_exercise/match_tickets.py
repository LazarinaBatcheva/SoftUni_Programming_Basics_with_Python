budget = float(input())
category = input()
people_count = int(input())

VIP_CATEGORY_TICKET_PRICE = 499.99
NORMAL_CATEGORY_TICKET_PRICE = 249.99

transport_costs = 0

if 1 <= people_count <= 4:
    transport_costs = budget * 0.75
elif 5 <= people_count <= 9:
    transport_costs = budget * 0.60
elif 10 <= people_count <= 24:
    transport_costs = budget * 0.50
elif 25 <= people_count <= 49:
    transport_costs = budget * 0.40
else:
    transport_costs = budget * 0.25

total_costs = 0

if category == "VIP":
    total_costs = people_count * VIP_CATEGORY_TICKET_PRICE + transport_costs
else:
    total_costs = people_count * NORMAL_CATEGORY_TICKET_PRICE + transport_costs

price_diff = budget - total_costs

if price_diff >= 0:
    print(f"Yes! You have {price_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(price_diff):.2f} leva.")