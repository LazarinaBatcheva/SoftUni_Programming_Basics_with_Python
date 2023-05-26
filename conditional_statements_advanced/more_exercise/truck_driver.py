season = input()
km_for_month = float(input())

km_for_season = km_for_month * 4
price_per_km = 0

if km_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    else:
        price_per_km = 1.05
elif 5000 < km_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    else:
        price_per_km = 1.25
elif 10000 < km_for_month <= 20000:
    price_per_km = 1.45

salary = km_for_season * price_per_km * 0.90

print(f"{salary:.2f}")