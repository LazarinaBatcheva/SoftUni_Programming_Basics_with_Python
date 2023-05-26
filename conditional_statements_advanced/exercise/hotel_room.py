month = input()
nights = int(input())

studio_price_for_night = 0
apartment_price_for_night = 0

if month == "May" or month == "October":
    studio_price_for_night = 50
    apartment_price_for_night = 65
    if 7 < nights < 14:
        studio_price_for_night *= 0.95
    elif nights > 14:
        studio_price_for_night *= 0.70
        apartment_price_for_night *= 0.90
elif month == "June" or month == "September":
    studio_price_for_night = 75.20
    apartment_price_for_night = 68.70
    if nights > 14:
        studio_price_for_night *= 0.80
        apartment_price_for_night *= 0.90
else:
    studio_price_for_night = 76
    apartment_price_for_night = 77
    if nights > 14:
        apartment_price_for_night *= 0.90

studio_price = nights * studio_price_for_night
apartment_price = nights * apartment_price_for_night

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")