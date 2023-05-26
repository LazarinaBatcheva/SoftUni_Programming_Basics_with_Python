type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCIS_PRICE = 3
GLADIOLI_PRICE = 2.50

costs = 0

if type_of_flowers == "Roses":
    costs = flowers_count * ROSE_PRICE
    if flowers_count > 80:
        costs *= 0.90

elif type_of_flowers == "Dahlias":
    costs = flowers_count * DAHLIA_PRICE
    if flowers_count > 90:
        costs *= 0.85

elif type_of_flowers == "Tulips":
    costs = flowers_count * TULIP_PRICE
    if flowers_count > 80:
        costs *= 0.85

elif type_of_flowers == "Narcissus":
    costs = flowers_count * NARCIS_PRICE
    if flowers_count < 120:
        costs *= 1.15

elif type_of_flowers == "Gladiolus":
    costs = flowers_count * GLADIOLI_PRICE
    if flowers_count < 80:
        costs *= 1.20

price_diff = budget - costs

if price_diff >= 0:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {price_diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(price_diff):.2f} leva more.")