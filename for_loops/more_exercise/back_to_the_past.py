heritage_money = float(input())
year_to_live_up_to = int(input())

money_left = heritage_money
starting_year = 18
spend_money_for_year = 12_000

for year in range(1800, year_to_live_up_to + 1):

    if year % 2 == 0:
        money_left = money_left - spend_money_for_year
        starting_year += 1

    else:
        money_left = money_left - (spend_money_for_year + (starting_year * 50))
        starting_year += 1

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")

else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")