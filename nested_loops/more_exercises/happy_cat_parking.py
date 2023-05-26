days = int(input())
hours = int(input())

price = 0

for day in range(1, days + 1):
    price_for_day = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_for_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price_for_day += 1.25
        else:
            price_for_day += 1

    print(f"Day: {day} - {price_for_day:.2f} leva")
    price += price_for_day

total_price = days * price

print(f"Total: {price:.2f} leva")