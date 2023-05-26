years_old = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_of_toys = 0
money = 10 - 1
saved_money = 0

for age in range(1, years_old + 1):
    if age % 2 != 0:
        money_of_toys += toy_price
    else:
        if age == 2:
            saved_money = money
        else:
            money = money + 10
            saved_money += money

total_money = saved_money + money_of_toys

diff = total_money - washing_machine_price

if diff >= 0:
    print(f"Yes! {diff:.2f}")

else:
    print(f"No! {abs(diff):.2f}")