budget = int(input())
season = input()
count_fishermen = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
else:
    price = 2600

if count_fishermen <= 6:
    price *= 0.90
elif 7 <= count_fishermen <= 11:
    price *= 0.85
else:
    price *= 0.75

if count_fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95

price_diff = budget - price

if price_diff >= 0:
    print(f"Yes! You have {price_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(price_diff):.2f} leva.")