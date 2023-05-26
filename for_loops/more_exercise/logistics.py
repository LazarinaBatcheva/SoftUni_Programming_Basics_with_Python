loads_count = int(input())

van_price_of_ton = 200
truck_price_of_ton = 175
train_price_of_ton = 120

van_tons_cargo = 0
truck_tons_cargo = 0
train_tons_cargo = 0

total_cargo_tonnage = 0
total_price = 0

for cargo in range(1, loads_count + 1):
    cargo_tonnage = int(input())
    total_cargo_tonnage += cargo_tonnage

    if cargo_tonnage < 4:
        total_price += cargo_tonnage * van_price_of_ton
        van_tons_cargo += cargo_tonnage

    elif cargo_tonnage < 12:
        total_price += cargo_tonnage * truck_price_of_ton
        truck_tons_cargo += cargo_tonnage

    else:
        total_price += cargo_tonnage * train_price_of_ton
        train_tons_cargo += cargo_tonnage

    average_price_per_ton = total_price / total_cargo_tonnage

print(f"{average_price_per_ton:.2f}")
print(f"{van_tons_cargo / total_cargo_tonnage * 100:.2f}%")
print(f"{truck_tons_cargo / total_cargo_tonnage * 100:.2f}%")
print(f"{train_tons_cargo / total_cargo_tonnage * 100:.2f}%")