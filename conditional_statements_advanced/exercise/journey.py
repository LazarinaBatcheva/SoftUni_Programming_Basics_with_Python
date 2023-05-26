budget = float(input())
season = input()

costs = 0
destination = None
type_of_trip = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_trip = "Camp"
        costs = budget * 0.30
    else:
        type_of_trip = "Hotel"
        costs = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_trip = "Camp"
        costs = budget * 0.40
    else:
        type_of_trip = "Hotel"
        costs = budget * 0.80

else:
    destination = "Europe"
    type_of_trip = "Hotel"
    costs = budget * 0.90


print(f"Somewhere in {destination}")
print(f"{type_of_trip} - {costs:.2f}")