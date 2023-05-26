command = input()
balance = 0

while command != "NoMoreMoney":
    current_sum = float(command)

    if current_sum < 0:
        print(f"Invalid operation!")
        break

    balance += current_sum
    print(f"Increase: {current_sum:.2f}")
    command = input()

print(f"Total: {balance:.2f}")