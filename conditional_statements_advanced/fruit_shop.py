fruit = input()
day_of_week = input()
quantity = float(input())

price = ""

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = f"{quantity * 2.50:.2f}"
    elif fruit == "apple":
        price = f"{quantity * 1.20:.2f}"
    elif fruit == "orange":
        price = f"{quantity * 0.85:.2f}"
    elif fruit == "grapefruit":
        price = f"{quantity * 1.45:.2f}"
    elif fruit == "kiwi":
        price = f"{quantity * 2.70:.2f}"
    elif fruit == "pineapple":
        price = f"{quantity * 5.50:.2f}"
    elif fruit == "grapes":
        price = f"{quantity * 3.85:.2f}"
    else:
        price = "error"

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = f"{quantity * 2.70:.2f}"
    elif fruit == "apple":
        price = f"{quantity * 1.25:.2f}"
    elif fruit == "orange":
        price = f"{quantity * 0.90:.2f}"
    elif fruit == "grapefruit":
        price = f"{quantity * 1.60:.2f}"
    elif fruit == "kiwi":
        price = f"{quantity * 3.00:.2f}"
    elif fruit == "pineapple":
        price = f"{quantity * 5.60:.2f}"
    elif fruit == "grapes":
        price = f"{quantity * 4.20:.2f}"
    else:
        price = "error"

else:
    price = "error"

print(price)
