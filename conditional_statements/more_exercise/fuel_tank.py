fuel_type = input()        # Diesel, Gasoline, Gas
liters_fuel_in_tank = float(input())

if fuel_type in ["Diesel", "Gasoline", "Gas"] and liters_fuel_in_tank < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type in ["Diesel", "Gasoline", "Gas"] and liters_fuel_in_tank >= 25:
    print(f"You have enough {fuel_type.lower()}.")
else:
    print("Invalid fuel!")