needed_sum = int(input())

pay_in_cash_counter = 0
pay_with_credit_card = 0
cash_payments_sum = 0
credit_card_payments_sum = 0
total_sum = 0
item_counter = 0

while total_sum < needed_sum:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break

    else:
        item_price = int(command)
        item_counter += 1
        if item_counter % 2 != 0 and 0 < item_price <= 100:
            pay_in_cash_counter += 1
            cash_payments_sum += item_price
            print("Product sold!")

        elif item_counter % 2 == 0 and item_price > 10:
            pay_with_credit_card += 1
            credit_card_payments_sum += item_price
            print("Product sold!")

        else:
            print("Error in transaction!")

    total_sum = cash_payments_sum + credit_card_payments_sum

if total_sum >= needed_sum:
    print(f"Average CS: {cash_payments_sum / pay_in_cash_counter:.2f}")
    print(f"Average CC: {credit_card_payments_sum / pay_with_credit_card:.2f}")