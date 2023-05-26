months = int(input())

water = 20 * months
internet = 15 * months
electricity_bill = 0

for _ in range(months):
    electricity = float(input())
    electricity_bill += electricity

bills = electricity_bill + water + internet
other_bills = bills + (bills * 0.20)
average = (electricity_bill + water + internet + other_bills) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")