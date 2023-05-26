chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY = 2.50

total_price_menu = \
    (chicken_menu * CHICKEN_MENU_PRICE) + \
    (fish_menu * FISH_MENU_PRICE) + \
    (vegetarian_menu * VEGETARIAN_MENU_PRICE)

desert = total_price_menu * 0.20

final_order_price = total_price_menu + desert + DELIVERY

print(final_order_price)
