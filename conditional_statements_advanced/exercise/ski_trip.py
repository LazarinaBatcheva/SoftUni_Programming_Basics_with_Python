days = int(input())
room = input()
evaluation = input()

ROOM_FOR_ONE_PERSON_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

nights = days - 1

room_for_one_person_prise = nights * ROOM_FOR_ONE_PERSON_PRICE
apartment_price = nights * APARTMENT_PRICE
president_apartment_price = nights * PRESIDENT_APARTMENT_PRICE

total_price = 0

if room == "room for one person":
    total_price = room_for_one_person_prise
elif room == "apartment":
    if days < 10:
        total_price = apartment_price * 0.70
    elif 10 <= days <= 15:
        total_price = apartment_price * 0.65
    else:
        total_price = apartment_price * 0.50
elif room == "president apartment":
    if days < 10:
        total_price = president_apartment_price * 0.90
    elif 10 <= days <= 15:
        total_price = president_apartment_price * 0.85
    else:
        total_price = president_apartment_price * 0.80

if evaluation == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

print(f"{total_price:.2f}")