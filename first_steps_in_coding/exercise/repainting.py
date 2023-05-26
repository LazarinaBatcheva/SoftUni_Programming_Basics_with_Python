nylon = int(input())
paint = int(input())
diluent = int(input())
hours_for_work = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
DILUENT_PRICE = 5
BAGS = 0.40

nylon += 2
paint += paint * 0.10

total_costs_for_materials = \
    (nylon * NYLON_PRICE) + \
    (paint * PAINT_PRICE) + \
    (diluent * DILUENT_PRICE) + \
    BAGS

total_price_for_work = hours_for_work * (total_costs_for_materials * 0.30)

print(total_costs_for_materials + total_price_for_work)
