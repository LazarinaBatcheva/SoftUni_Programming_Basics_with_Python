pens_packs = int(input())
markers_pack = int(input())
liters_of_detergent = int(input())
discount = int(input()) / 100

PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGENT_PRICE = 1.20

price_of_materials = \
    (pens_packs * PENS_PRICE) + \
    (markers_pack * MARKERS_PRICE) + \
    (liters_of_detergent * DETERGENT_PRICE)

total_price = price_of_materials - (price_of_materials * discount)

print(total_price)
