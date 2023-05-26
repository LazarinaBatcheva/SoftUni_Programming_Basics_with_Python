while True:
    destination = input()

    if destination == "End":
        break

    min_budget = float(input())
    saved_money = 0

    while min_budget > saved_money:
        saved_money += float(input())

    print(f"Going to {destination}!")