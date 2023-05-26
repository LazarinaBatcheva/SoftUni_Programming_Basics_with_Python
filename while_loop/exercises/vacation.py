needed_money = float(input())
balance = float(input())

spending_counter = 0
days_counter = 0

while True:
    action = input()
    money = float(input())
    days_counter += 1

    if action == "spend":
        spending_counter += 1
        balance = balance - money if balance > money else 0
        if spending_counter == 5:
            print(f"You can't save the money.\n{days_counter}")
            break

    if action == "save":
        spending_counter = 0
        balance += money
        if balance >= needed_money:
            print(f"You saved the money for {days_counter} days.")
            break