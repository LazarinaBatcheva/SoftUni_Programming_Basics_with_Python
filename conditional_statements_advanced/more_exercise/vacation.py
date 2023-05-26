budget = float(input())
season = input()

location = None
accommodation = None
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60
else:
    accommodation = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {accommodation} - {price:.2f}")