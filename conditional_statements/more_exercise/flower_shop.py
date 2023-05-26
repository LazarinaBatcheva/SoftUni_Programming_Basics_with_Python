from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())

present_price = float(input())

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.5
CACTI_PRICE = 8

order_value = (magnolias * MAGNOLIAS_PRICE) + \
              (hyacinths * HYACINTHS_PRICE) + \
              (roses * ROSES_PRICE) + \
              (cacti * CACTI_PRICE)

taxes = order_value * 0.05
total_amount = order_value - taxes

difference_between_value = present_price - total_amount

if difference_between_value > 0:
    print(f"She will have to borrow {ceil(difference_between_value)} leva.")
else:
    print(f"She is left with {floor(abs(difference_between_value))} leva.")
