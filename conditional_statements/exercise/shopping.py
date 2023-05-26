budget = float(input())

graphics_count = int(input())
processors_count = int(input())
ram_count = int(input())

GRAPHIC_PRICE = 250
PROCESSOR_PRICE = graphics_count * GRAPHIC_PRICE * 0.35
RAM_PRICE = graphics_count * GRAPHIC_PRICE * 0.10

total_price = (graphics_count * GRAPHIC_PRICE) + \
              (processors_count * PROCESSOR_PRICE) + \
              (ram_count * RAM_PRICE)

if graphics_count > processors_count:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
