excursion_price = float (input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

total_order_toys = puzzles_count + \
                   talking_dolls_count + \
                   teddy_bears_count + \
                   minions_count + \
                   trucks_count

total_order_price = (puzzles_count * PUZZLE_PRICE) + \
                    (talking_dolls_count * TALKING_DOLL_PRICE) + \
                    (teddy_bears_count * TEDDY_BEAR_PRICE) + \
                    (minions_count * MINION_PRICE) + \
                    (trucks_count * TRUCK_PRICE)

if total_order_toys >= 50:
    total_order_price *= 1 - 0.25

total_order_price *= 1 - 0.10

if total_order_price >= excursion_price:
    print(f"Yes! {total_order_price - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - total_order_price:.2f} lv needed.")
