fuel_type = input()
fuel_amount = float(input())
club_card = input()

fuel_price = 0

# GASOLINE_PRICE = 2.22     - 0.18
# DIESEL_PRICE = 2.33       - 0.12
# GAS_PRICE = 0.93          - 0.08

if fuel_type == "Gasoline":
    fuel_price = 2.22
    if club_card == "Yes":
        fuel_price = 2.22 - 0.18
elif fuel_type == "Diesel":
    fuel_price = 2.33
    if club_card == "Yes":
        fuel_price = 2.33 - 0.12
elif fuel_type == "Gas":
    fuel_price = 0.93
    if club_card == "Yes":
        fuel_price = 0.93 - 0.08

total_price = fuel_price * fuel_amount

if 20 <= fuel_amount <= 25:
    total_price *= 0.92
elif fuel_amount > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")
