season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

night_price = 0
type_of_sport = None

if type_of_group == "girls" or type_of_group == "boys":
    if season == "Winter":
        night_price = 9.60
        if type_of_group == "girls":
            type_of_sport = "Gymnastics"
        else:
            type_of_sport = "Judo"

    elif season == "Spring":
        night_price = 7.20
        if type_of_group == "girls":
            type_of_sport = "Athletics"
        else:
            type_of_sport = "Tennis"

    else:
        night_price = 15
        if type_of_group == "girls":
            type_of_sport = "Volleyball"
        else:
            type_of_sport = "Football"

else:
    if season == "Winter":
        night_price = 10
        type_of_sport = "Ski"
    elif season == "Spring":
        night_price = 9.50
        type_of_sport = "Cycling"
    else:
        night_price = 20
        type_of_sport = "Swimming"

total_price = students_count * night_price * nights_count

if students_count >= 50:
    total_price *= 0.50
elif 20 <= students_count < 50:
    total_price *= 0.85
elif 10 <= students_count < 20:
    total_price *= 0.95

print(f"{type_of_sport} {total_price:.2f} lv.")