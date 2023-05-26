budget = float(input())
season = input()

class_type = None
car_type = None
price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    else:
        car_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    else:
        car_type = "Jeep"
        price = budget * 0.80
else:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90

print(f"{class_type}")
print(f"{car_type} - {price:.2f}")

